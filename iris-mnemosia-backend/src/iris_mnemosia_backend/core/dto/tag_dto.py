from uuid import UUID

from pydantic import BaseModel


class tagInput(BaseModel):
    name: str

class tagOutput(BaseModel):
    id: UUID
    name: str