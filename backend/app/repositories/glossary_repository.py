from sqlalchemy.orm import Session

from app.models.glossary import GlossaryEntry, GlossaryType
from app.repositories.base_repository import BaseRepository


class GlossaryRepository(BaseRepository[GlossaryEntry]):
    def __init__(self, db: Session) -> None:
        super().__init__(GlossaryEntry, db)

    def get_by_type(self, glossary_type: GlossaryType) -> list[GlossaryEntry]:
        return (
            self._db.query(GlossaryEntry)
            .filter(GlossaryEntry.type == glossary_type)
            .order_by(GlossaryEntry.order_index, GlossaryEntry.term)
            .all()
        )

    def get_all_ordered(self) -> list[GlossaryEntry]:
        return (
            self._db.query(GlossaryEntry)
            .order_by(GlossaryEntry.type, GlossaryEntry.order_index, GlossaryEntry.term)
            .all()
        )
