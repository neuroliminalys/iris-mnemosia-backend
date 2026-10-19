import typing
from uuid import UUID, uuid7

from sqlalchemy.orm import Mapped, mapped_column, relationship

from iris_mnemosia_backend.core.config.database import DatabaseModel

if typing.TYPE_CHECKING:
    from iris_mnemosia_backend.core.models.associations.resource_tags_association import (
        ResourceTagsAssociation,
    )


class TagEntity(DatabaseModel):
    __tablename__ = "tags"
    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    resource_association: Mapped[list["ResourceTagsAssociation"]] = relationship(
        back_populates="tag"
    )
