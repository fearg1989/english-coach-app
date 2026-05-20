from fastapi import APIRouter, Depends, Query

from app.api.deps import get_lesson_service
from app.schemas.lesson import LessonDetailResponse, LessonResponse
from app.services.lesson_service import LessonService

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get(
    "/level/{level_id}",
    response_model=list[LessonResponse],
    summary="List lessons for a level",
)
def list_lessons_by_level(
    level_id: int,
    lesson_type: str | None = Query(
        default=None,
        description="Filter by type: 'grammar' or 'phonetics'",
        alias="type",
    ),
    category: str | None = Query(
        default=None,
        description="Filter by category: 'verb_tenses', 'phrasal_verbs', 'prepositions', or 'irregular_verbs'",
    ),
    service: LessonService = Depends(get_lesson_service),
) -> list[LessonResponse]:
    """Returns all published lessons for the given level, optionally filtered by type or category."""
    if category:
        return service.get_lessons_by_level_and_category(level_id, category)
    if lesson_type:
        return service.get_lessons_by_level_and_type(level_id, lesson_type)
    return service.get_lessons_by_level(level_id)


@router.get(
    "/category/{category}",
    response_model=list[LessonResponse],
    summary="List lessons by specialized category",
)
def list_lessons_by_category(
    category: str,
    service: LessonService = Depends(get_lesson_service),
) -> list[LessonResponse]:
    """Returns published lessons for the requested specialized category."""
    return service.get_lessons_by_category(category)


@router.get(
    "/{lesson_id}",
    response_model=LessonDetailResponse,
    summary="Get lesson with examples and exercises",
)
def get_lesson_detail(
    lesson_id: int,
    service: LessonService = Depends(get_lesson_service),
) -> LessonDetailResponse:
    """Returns a lesson with its full content: examples (phrase + IPA) and exercises."""
    return service.get_lesson_detail(lesson_id)
