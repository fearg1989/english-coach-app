from sqlalchemy.orm import Session

from app.models.level import Level
from app.repositories.base_repository import BaseRepository


class LevelRepository(BaseRepository[Level]):
    def __init__(self, db: Session) -> None:
        super().__init__(Level, db)

    def get_by_code(self, code: str) -> Level | None:
        return self._db.query(Level).filter(Level.code == code).first()

    def get_all_ordered(self) -> list[Level]:
        return self._db.query(Level).order_by(Level.order_index).all()
