from __future__ import annotations

import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class GlossaryType(str, enum.Enum):
    PHRASAL_VERB = "phrasal_verb"
    IRREGULAR_VERB = "irregular_verb"


class GlossaryEntry(Base):
    """
    A single entry in the quick-reference glossary.
    - PHRASAL_VERB entries store term + meaning only.
    - IRREGULAR_VERB entries also store form_past and form_participle.
    """

    __tablename__ = "glossary_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[GlossaryType] = mapped_column(
        Enum(GlossaryType), nullable=False, index=True
    )
    term: Mapped[str] = mapped_column(String(100), nullable=False)
    meaning: Mapped[str] = mapped_column(String(300), nullable=False)
    form_past: Mapped[str | None] = mapped_column(String(100), nullable=True)
    form_participle: Mapped[str | None] = mapped_column(String(100), nullable=True)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
