import typing
from datetime import datetime, timezone
from uuid import UUID, uuid7

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import ForeignKey

from iris_mnemosia_backend.core.config.database import DatabaseModel

if typing.TYPE_CHECKING:
    from iris_mnemosia_backend.core.models.associations.resource_tags_association import (
        ResourceTagsAssociation,
    )
    from iris_mnemosia_backend.core.models.categories_entity import CategoryEntity


class ResourceEntity(DatabaseModel):
    __tablename__ = "resources"
    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, unique=True, nullable=False
    )
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        # Choose between Python or ORM to set DB create time
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    category_id: Mapped[UUID | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    category: Mapped["CategoryEntity | None"] = relationship(back_populates="resources")

    tag_association: Mapped[list["ResourceTagsAssociation"]] = relationship(
        back_populates="resource"
    )
