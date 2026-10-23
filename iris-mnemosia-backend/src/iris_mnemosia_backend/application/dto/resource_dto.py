from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic.fields import Field

from iris_mnemosia_backend.application.dto.category_dto import CategoryOutput
from iris_mnemosia_backend.application.dto.tag_dto import TagOutput


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
    category: CategoryOutput | None = Field(
        default=None, exclude_if=lambda value: value is None
    )
    tag_association: list[TagOutput] = Field(
        default_factory=list[TagOutput], exclude_if=lambda value: len(value) == 0
    )

    model_config = ConfigDict(from_attributes=True)
