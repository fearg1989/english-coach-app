from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class LevelBase(BaseModel):
    code: str
    name: str
    description: str | None = None
    order_index: int = 0

    @field_validator("code")
    @classmethod
    def uppercase_code(cls, v: str) -> str:
        return v.upper()


class LevelCreate(LevelBase):
    pass


class LevelUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    order_index: int | None = None


class LevelResponse(LevelBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
