from __future__ import annotations

import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.lesson import Lesson


class SentenceType(str, enum.Enum):
    AFFIRMATIVE   = "affirmative"
    NEGATIVE      = "negative"
    INTERROGATIVE = "interrogative"


class Example(Base):
    """
    A sample English sentence attached to a Lesson.
    Contains the phrase, Spanish translation, IPA notation, and
    a nullable audio_url reserved for Phase 2 (TTS integration).
    """

    __tablename__ = "examples"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lesson_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("lessons.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    phrase: Mapped[str] = mapped_column(String(500), nullable=False)
    translation: Mapped[str] = mapped_column(String(500), nullable=False)
    ipa_notation: Mapped[str | None] = mapped_column(String(500), nullable=True)
    sentence_type: Mapped[SentenceType | None] = mapped_column(
        Enum(SentenceType, values_callable=lambda obj: [e.value for e in obj]),
        nullable=True,
    )

    # ── Phase 2: Will be populated by OpenAI TTS or Web Speech API ──────────
    audio_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # ─── Relationships ───────────────────────────────────────────────────────
    lesson: Mapped[Lesson] = relationship("Lesson", back_populates="examples")
