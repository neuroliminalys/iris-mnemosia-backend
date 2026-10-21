from uuid import UUID

from pydantic import BaseModel


class UserInput(BaseModel):
    name: str

class UserOutput(BaseModel):
    id: UUID
    name: str
