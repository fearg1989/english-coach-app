import logging
import anyio
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

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
        transcribed_text = await anyio.to_thread.run_sync(
            audio_service.transcribe_audio, file_bytes
        )
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
        "accuracy_score": accuracy_score
    }
