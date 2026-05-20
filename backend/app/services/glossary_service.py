from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.glossary import GlossaryEntry, GlossaryType
from app.repositories.glossary_repository import GlossaryRepository


class GlossaryService:
    def __init__(self, db: Session) -> None:
        self._repo = GlossaryRepository(db)

    def get_entries(self, glossary_type: str | None = None) -> list[GlossaryEntry]:
        if glossary_type is None:
            return self._repo.get_all_ordered()

        try:
            gtype = GlossaryType(glossary_type)
        except ValueError:
            valid = [t.value for t in GlossaryType]
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid glossary type '{glossary_type}'. Valid values: {valid}",
            )

        return self._repo.get_by_type(gtype)
