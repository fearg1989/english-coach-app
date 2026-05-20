from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ExampleBase(BaseModel):
    phrase: str
    translation: str
    ipa_notation: str | None = None
    sentence_type: str | None = None
    audio_url: str | None = None  # Phase 2: populated by TTS service
    order_index: int = 0


class ExampleCreate(ExampleBase):
    lesson_id: int


class ExampleResponse(ExampleBase):
    id: int
    lesson_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
