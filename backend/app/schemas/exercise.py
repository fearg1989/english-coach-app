from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.exercise import ExerciseType


class ExerciseBase(BaseModel):
    type: ExerciseType
    question: str
    correct_answer: str
    options: dict[str, str] | None = None
    order_index: int = 0


class ExerciseCreate(ExerciseBase):
    lesson_id: int


class ExerciseResponse(ExerciseBase):
    id: int
    lesson_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
