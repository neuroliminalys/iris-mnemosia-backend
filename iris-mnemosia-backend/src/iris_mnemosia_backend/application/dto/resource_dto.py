from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ResourceInput(BaseModel):
    title: str
    description: str | None = None
    content: str

class ResourceOutput(BaseModel):
    id: UUID
    title: str
    description: str
    content: str
    created_at: datetime
    updated_at: datetime
