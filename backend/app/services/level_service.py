from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.level import Level
from app.repositories.level_repository import LevelRepository
from app.schemas.level import LevelCreate


class LevelService:
    """
    Encapsulates all business logic related to CEFR levels.
    Depends on LevelRepository for data access (Dependency Inversion Principle).
    """

    def __init__(self, db: Session) -> None:
        self._repo = LevelRepository(db)

    def get_all_levels(self) -> list[Level]:
        return self._repo.get_all_ordered()

    def get_level_by_id(self, level_id: int) -> Level:
        level = self._repo.get_by_id(level_id)
        if level is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Level with id={level_id} not found.",
            )
        return level

    def get_level_by_code(self, code: str) -> Level:
        level = self._repo.get_by_code(code.upper())
        if level is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Level '{code.upper()}' not found.",
            )
        return level

    def create_level(self, payload: LevelCreate) -> Level:
        existing = self._repo.get_by_code(payload.code)
        if existing is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Level with code '{payload.code}' already exists.",
            )
        return self._repo.create(Level(**payload.model_dump()))
