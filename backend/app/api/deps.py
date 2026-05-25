from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.glossary_service import GlossaryService
from app.services.lesson_service import LessonService
from app.services.level_service import LevelService
from app.services.practice_service import PracticeService
from fastapi import Depends


def get_level_service(db: Session = Depends(get_db)) -> LevelService:
    return LevelService(db)


def get_lesson_service(db: Session = Depends(get_db)) -> LessonService:
    return LessonService(db)


def get_glossary_service(db: Session = Depends(get_db)) -> GlossaryService:
    return GlossaryService(db)


def get_practice_service(db: Session = Depends(get_db)) -> PracticeService:
    return PracticeService(db)
