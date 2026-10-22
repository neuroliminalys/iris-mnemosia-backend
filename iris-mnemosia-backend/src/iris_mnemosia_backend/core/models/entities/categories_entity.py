import typing
from uuid import UUID, uuid7

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from iris_mnemosia_backend.core.config.database import DatabaseModel

if typing.TYPE_CHECKING:
    from iris_mnemosia_backend.core.models.entities.resources_entity import (
        ResourceEntity,
    )


class CategoryEntity(DatabaseModel):
    __tablename__ = "categories"
    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, default=uuid7, nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    resources: Mapped[list["ResourceEntity"]] = relationship(back_populates="category")
