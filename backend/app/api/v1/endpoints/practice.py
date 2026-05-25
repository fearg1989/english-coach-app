from fastapi import APIRouter, Depends

from app.api.deps import get_practice_service
from app.schemas.practice import PracticeGenerateRequest, PracticeSessionResponseSchema
from app.services.practice_service import PracticeService

router = APIRouter(prefix="/practice", tags=["Practice"])


@router.post("/generate", response_model=PracticeSessionResponseSchema)
async def generate_practice_session(
    payload: PracticeGenerateRequest,
    service: PracticeService = Depends(get_practice_service),
) -> dict:
    """
    Generates a dynamic, context-aware 5-question practice session
    based on the lesson's grammar context and the user's custom theme.
    """
    return await service.generate_practice_session(
        lesson_id=payload.lesson_id, theme=payload.theme
    )
