from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.lesson import Lesson, LessonCategory, LessonType
from app.repositories.lesson_repository import LessonRepository
from app.schemas.lesson import LessonCreate


class LessonService:
    """
    Encapsulates all business logic related to lessons.
    Depends on LessonRepository (Dependency Inversion Principle).
    """

    def __init__(self, db: Session) -> None:
        self._repo = LessonRepository(db)

    def get_lessons_by_level(self, level_id: int) -> list[Lesson]:
        return self._repo.get_by_level(level_id)

    def get_lessons_by_level_and_type(
        self, level_id: int, lesson_type: str
    ) -> list[Lesson]:
        try:
            parsed_type = LessonType(lesson_type)
        except ValueError:
            valid = [t.value for t in LessonType]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid lesson type '{lesson_type}'. Valid values: {valid}",
            )
        return self._repo.get_by_level_and_type(level_id, parsed_type)

    def get_lessons_by_level_and_category(
        self, level_id: int, category: str
    ) -> list[Lesson]:
        try:
            parsed_category = LessonCategory(category)
        except ValueError:
            valid = [c.value for c in LessonCategory]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid lesson category '{category}'. Valid values: {valid}",
            )
        return self._repo.get_by_level_and_category(level_id, parsed_category)

    def get_lessons_by_category(self, category: str) -> list[Lesson]:
        try:
            parsed_category = LessonCategory(category)
        except ValueError:
            valid = [c.value for c in LessonCategory]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid lesson category '{category}'. Valid values: {valid}",
            )
        return self._repo.get_by_category(parsed_category)

    def get_lesson_detail(self, lesson_id: int) -> Lesson:
        lesson = self._repo.get_with_details(lesson_id)
        if lesson is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lesson with id={lesson_id} not found.",
            )
        return lesson

    def create_lesson(self, payload: LessonCreate) -> Lesson:
        return self._repo.create(Lesson(**payload.model_dump()))
