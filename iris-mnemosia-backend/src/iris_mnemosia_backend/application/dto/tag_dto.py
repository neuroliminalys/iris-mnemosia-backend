from uuid import UUID

from pydantic import BaseModel


class TagInput(BaseModel):
    name: str

class TagOutput(BaseModel):
    id: UUID
    name: str
