from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.lesson import Lesson


class Level(Base):
    """
    Represents a CEFR proficiency level (A1 → C2).
    One Level has many Lessons.
    """

    __tablename__ = "levels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(
        String(10), unique=True, nullable=False, index=True
    )  # e.g. "A1", "B2"
    name: Mapped[str] = mapped_column(String(100), nullable=False)  # e.g. "Beginner"
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # ─── Relationships ───────────────────────────────────────────────────────
    lessons: Mapped[list[Lesson]] = relationship(
        "Lesson", back_populates="level", cascade="all, delete-orphan"
    )
