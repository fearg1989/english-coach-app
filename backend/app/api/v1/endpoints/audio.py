import logging
import json
import anyio
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status, WebSocket, WebSocketDisconnect

from app.services.audio_service import audio_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/audio", tags=["Audio"])

@router.post("/evaluate-pronunciation")
async def evaluate_pronunciation(
    file: UploadFile = File(...),
    target_text: str = Form(...)
):
    """
    Evaluates pronunciation by:
    1. Transcribing the uploaded browser audio blob using Whisper.
    2. Calculating a normalized similarity score against the target text.
    
    This endpoint executes the heavy transcription and accuracy scoring steps
    in a thread pool to prevent blocking FastAPI's main async event loop.
    """
    logger.info(f"Received audio evaluation request. Target text: '{target_text}'")

    if not target_text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Target text cannot be empty."
        )

    # Read uploaded file bytes asynchronously
    try:
        file_bytes = await file.read()
    except Exception as err:
        logger.error(f"Failed to read audio file upload: {err}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not read uploaded audio file."
        )

    if not file_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded audio file is empty."
        )

    # Offload synchronous, CPU-intensive audio decoding and model inference to a thread pool
    try:
        transcription_result = await anyio.to_thread.run_sync(
            audio_service.transcribe_audio, file_bytes
        )
        transcribed_text = transcription_result["transcribed_text"]
        words_list = transcription_result["words"]
        
        # Perform word alignment to capture mispronunciations and confidence details
        word_feedback = audio_service.align_words(target_text, words_list)
        
        accuracy_score = await anyio.to_thread.run_sync(
            audio_service.calculate_accuracy, transcribed_text, target_text
        )
    except ValueError as val_err:
        logger.warning(f"Audio processing validation error: {val_err}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(val_err)
        )
    except Exception as exc:
        logger.exception("Unexpected error during pronunciation evaluation process")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during speech-to-text evaluation."
        )

    logger.info(f"Evaluation complete. Score: {accuracy_score}")
    return {
        "transcribed_text": transcribed_text,
        "accuracy_score": accuracy_score,
        "words": word_feedback
    }


@router.websocket("/stream-evaluation")
async def stream_evaluation(websocket: WebSocket, target_text: str):
    """
    WebSocket endpoint for real-time speech evaluation.
    Receives binary audio WebM chunks from the browser every second, normalizes it,
    runs fast interim Speech-to-Text, and pushes the text back.
    Upon receiving the {"event": "stop"} text message, performs deep, accent-tuned final
    transcription, SequenceMatcher word alignment, and pronunciation evaluation.
    """
    await websocket.accept()
    logger.info(f"WebSocket connection accepted for streaming. Target text: '{target_text}'")

    audio_buffer = bytearray()
    try:
        while True:
            # Wait for data from the client
            message = await websocket.receive()
            
            # Process binary data chunks
            if "bytes" in message:
                binary_chunk = message["bytes"]
                if binary_chunk:
                    audio_buffer.extend(binary_chunk)
                    
                    # Run quick interim transcription on current accumulated audio buffer
                    interim_text = await anyio.to_thread.run_sync(
                        audio_service.transcribe_audio_interim, bytes(audio_buffer)
                    )
                    
                    # Send interim transcript back to client
                    await websocket.send_json({
                        "type": "interim",
                        "text": interim_text
                    })
            
            # Process control text messages
            elif "text" in message:
                data = json.loads(message["text"])
                event = data.get("event")
                
                if event == "stop":
                    logger.info("Received stop event from client. Processing final evaluation...")
                    
                    if not audio_buffer:
                        await websocket.send_json({
                            "type": "error",
                            "detail": "No audio was received during the session."
                        })
                        break
                        
                    # Execute full final evaluation (accent-tuned)
                    transcription_result = await anyio.to_thread.run_sync(
                        audio_service.transcribe_audio, bytes(audio_buffer)
                    )
                    transcribed_text = transcription_result["transcribed_text"]
                    words_list = transcription_result["words"]
                    
                    # Align target words and compute similarity matching
                    word_feedback = audio_service.align_words(target_text, words_list)
                    accuracy_score = await anyio.to_thread.run_sync(
                        audio_service.calculate_accuracy, transcribed_text, target_text
                    )
                    
                    # Push final structured assessment
                    await websocket.send_json({
                        "type": "final",
                        "transcribed_text": transcribed_text,
                        "accuracy_score": accuracy_score,
                        "words": word_feedback
                    })
                    logger.info(f"Final streaming evaluation complete. Score: {accuracy_score}")
                    break
                    
    except WebSocketDisconnect:
        logger.info("Streaming WebSocket disconnected by client")
    except Exception as err:
        logger.exception("Unexpected error inside WebSocket stream-evaluation")
        try:
            await websocket.send_json({
                "type": "error",
                "detail": "Internal server error during speech streaming."
            })
        except Exception:
            pass
    finally:
        try:
            await websocket.close()
        except Exception:
            pass
