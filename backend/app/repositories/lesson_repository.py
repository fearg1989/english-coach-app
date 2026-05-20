from sqlalchemy.orm import Session, joinedload

from app.models.lesson import Lesson, LessonCategory, LessonType
from app.repositories.base_repository import BaseRepository


class LessonRepository(BaseRepository[Lesson]):
    def __init__(self, db: Session) -> None:
        super().__init__(Lesson, db)

    def get_by_level(self, level_id: int) -> list[Lesson]:
        return (
            self._db.query(Lesson)
            .filter(Lesson.level_id == level_id, Lesson.is_published.is_(True))
            .order_by(Lesson.order_index)
            .all()
        )

    def get_with_details(self, lesson_id: int) -> Lesson | None:
        """Eagerly loads examples and exercises to avoid N+1 queries."""
        return (
            self._db.query(Lesson)
            .options(
                joinedload(Lesson.examples),
                joinedload(Lesson.exercises),
            )
            .filter(Lesson.id == lesson_id)
            .first()
        )

    def get_by_level_and_type(
        self, level_id: int, lesson_type: LessonType
    ) -> list[Lesson]:
        return (
            self._db.query(Lesson)
            .filter(
                Lesson.level_id == level_id,
                Lesson.type == lesson_type,
                Lesson.is_published.is_(True),
            )
            .order_by(Lesson.order_index)
            .all()
        )

    def get_by_level_and_category(
        self, level_id: int, category: LessonCategory,
    ) -> list[Lesson]:
        return (
            self._db.query(Lesson)
            .filter(
                Lesson.level_id == level_id,
                Lesson.category == category,
                Lesson.is_published.is_(True),
            )
            .order_by(Lesson.order_index)
            .all()
        )

    def get_by_category(self, category: LessonCategory) -> list[Lesson]:
        return (
            self._db.query(Lesson)
            .filter(Lesson.category == category, Lesson.is_published.is_(True))
            .order_by(Lesson.order_index)
            .all()
        )
