from uuid import UUID

from pydantic import BaseModel


class userInput(BaseModel):
    name: str

class userOutput(BaseModel):
    id: UUID
    name: str