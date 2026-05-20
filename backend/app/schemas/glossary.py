from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.glossary import GlossaryType


class GlossaryEntryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    type: GlossaryType
    term: str
    meaning: str
    form_past: str | None
    form_participle: str | None
    order_index: int
    created_at: datetime
    updated_at: datetime
