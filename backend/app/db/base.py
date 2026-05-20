from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,     # Reconnect on stale connections (hosting compartido)
    pool_recycle=300,       # Recycle connections every 5 min
    pool_size=5,
    max_overflow=10,
    echo=settings.DEBUG,    # Log SQL queries in DEBUG mode
)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass
