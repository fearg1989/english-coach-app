# Re-export all models so that Base.metadata.create_all() and Alembic
# can discover every table in a single import.
from app.models.example import Example, SentenceType  # noqa: F401
from app.models.exercise import Exercise, ExerciseType  # noqa: F401
from app.models.glossary import GlossaryEntry, GlossaryType  # noqa: F401
from app.models.lesson import Lesson, LessonType, LessonCategory  # noqa: F401
from app.models.level import Level  # noqa: F401

__all__ = [
    "Level",
    "Lesson",
    "LessonType",
    "LessonCategory",
    "Example",
    "SentenceType",
    "Exercise",
    "ExerciseType",
    "GlossaryEntry",
    "GlossaryType",
]
