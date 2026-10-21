from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryInput(BaseModel):
    name: str

class CategoryOutput(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)
