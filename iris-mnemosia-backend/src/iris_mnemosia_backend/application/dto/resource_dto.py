from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic.config import ConfigDict


class ResourceInput(BaseModel):
    title: str
    description: str | None = None
    content: str
    category_id: UUID | None = None

class ResourceOutput(BaseModel):
    id: UUID
    title: str
    description: str
    content: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
