from __future__ import annotations

import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.example import Example
    from app.models.exercise import Exercise
    from app.models.level import Level


class LessonType(str, enum.Enum):
    GRAMMAR = "grammar"
    PHONETICS = "phonetics"


class LessonCategory(str, enum.Enum):
    VERB_TENSES      = "verb_tenses"
    MODAL_VERBS      = "modal_verbs"
    PHRASAL_VERBS    = "phrasal_verbs"
    PREPOSITIONS     = "prepositions"
    IRREGULAR_VERBS  = "irregular_verbs"
    GENERAL_GRAMMAR  = "general_grammar"
    PHONETICS        = "phonetics"
    VERB_PATTERNS    = "verb_patterns"
    CONDITIONALS     = "conditionals"
    PASSIVE_VOICE    = "passive_voice"
    REPORTED_SPEECH  = "reported_speech"
    CONNECTORS       = "connectors"
    COLLOCATIONS     = "collocations"


class Lesson(Base):
    """
    A single lesson belonging to a Level.
    Type determines whether it focuses on grammar or phonetics.
    One Lesson has many Examples and Exercises.
    """

    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("levels.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    type: Mapped[LessonType] = mapped_column(Enum(LessonType), nullable=False)
    category: Mapped[LessonCategory] = mapped_column(
        Enum(LessonCategory, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False, default=LessonCategory.VERB_TENSES, index=True,
    )
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # ─── Relationships ───────────────────────────────────────────────────────
    level: Mapped[Level] = relationship("Level", back_populates="lessons")
    examples: Mapped[list[Example]] = relationship(
        "Example", back_populates="lesson", cascade="all, delete-orphan"
    )
    exercises: Mapped[list[Exercise]] = relationship(
        "Exercise", back_populates="lesson", cascade="all, delete-orphan"
    )
