from fastapi import APIRouter, Depends, Query

from app.api.deps import get_glossary_service
from app.schemas.glossary import GlossaryEntryResponse
from app.services.glossary_service import GlossaryService

router = APIRouter(prefix="/glossary", tags=["Glossary"])


@router.get(
    "/",
    response_model=list[GlossaryEntryResponse],
    summary="List glossary entries",
)
def list_glossary_entries(
    type: str | None = Query(
        default=None,
        description="Filter by type: 'phrasal_verb' or 'irregular_verb'",
    ),
    service: GlossaryService = Depends(get_glossary_service),
) -> list[GlossaryEntryResponse]:
    """Returns all glossary entries, optionally filtered by type."""
    return service.get_entries(type)
