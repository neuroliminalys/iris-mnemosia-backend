from uuid import UUID

from pydantic import BaseModel
from pydantic.config import ConfigDict


class TagInput(BaseModel):
    name: str

class TagOutput(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)
