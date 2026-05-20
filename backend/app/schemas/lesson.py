from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.lesson import LessonCategory, LessonType
from app.schemas.example import ExampleResponse
from app.schemas.exercise import ExerciseResponse


class LessonBase(BaseModel):
    title: str
    type: LessonType
    category: LessonCategory
    description: str | None = None
    order_index: int = 0
    is_published: bool = False


class LessonCreate(LessonBase):
    level_id: int


class LessonUpdate(BaseModel):
    title: str | None = None
    type: LessonType | None = None
    description: str | None = None
    order_index: int | None = None
    is_published: bool | None = None


class LessonResponse(LessonBase):
    id: int
    level_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LessonDetailResponse(LessonResponse):
    """Full lesson payload including examples and exercises."""

    examples: list[ExampleResponse] = []
    exercises: list[ExerciseResponse] = []
