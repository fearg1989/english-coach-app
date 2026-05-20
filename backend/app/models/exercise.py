from __future__ import annotations

import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, JSON, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.lesson import Lesson


class ExerciseType(str, enum.Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_BLANK = "fill_blank"
    PRONUNCIATION = "pronunciation"  # Phase 4: Azure Speech + GPT-4o-mini validation


class Exercise(Base):
    """
    A practice exercise attached to a Lesson.
    - multiple_choice: options stored as JSON dict {a: ..., b: ..., c: ...}
    - fill_blank:      options is null, student types the answer
    - pronunciation:   Phase 4 — audio recorded via MediaRecorder and
                       validated by Whisper + Azure Speech Services
    """

    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("lessons.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    type: Mapped[ExerciseType] = mapped_column(Enum(ExerciseType), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    correct_answer: Mapped[str] = mapped_column(Text, nullable=False)

    # JSON dict for multiple_choice: {"a": "option1", "b": "option2", ...}
    options: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # ─── Relationships ───────────────────────────────────────────────────────
    lesson: Mapped[Lesson] = relationship("Lesson", back_populates="exercises")
