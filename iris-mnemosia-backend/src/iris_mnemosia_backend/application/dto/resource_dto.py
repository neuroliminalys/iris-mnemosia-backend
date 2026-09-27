from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class resourceInput(BaseModel):
    title: str
    description: str
    content: str

class resourceOutput(BaseModel):
    id: UUID
    title: str
    description: str
    content: str
    created_at: datetime
    updated_at: datetime