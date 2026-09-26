from uuid import UUID

from pydantic import BaseModel


class categoryInput(BaseModel):
    name: str

class categoryOutput(BaseModel):
    id: UUID
    name: str