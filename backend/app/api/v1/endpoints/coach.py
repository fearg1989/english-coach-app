from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.services.ai_coach_service import AICoachService

router = APIRouter()

class CoachFeedbackRequest(BaseModel):
    target_phrase: str
    user_transcription: str
    score: float

@router.post("/feedback")
async def get_coach_feedback(request: CoachFeedbackRequest):
    """
    Get AI Coach feedback as a Server-Sent Events (SSE) stream.
    """
    coach_service = AICoachService()
    
    return StreamingResponse(
        coach_service.generate_feedback_stream(
            target_phrase=request.target_phrase,
            user_transcription=request.user_transcription,
            score=request.score
        ),
        media_type="text/event-stream"
    )
