import typing
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.sql.schema import ForeignKey

from iris_mnemosia_backend.core.config.database import DatabaseModel

if typing.TYPE_CHECKING:
    from iris_mnemosia_backend.core.models.resources_entity import ResourceEntity
    from iris_mnemosia_backend.core.models.tag_entity import TagEntity

class ResourceTagsAssociation(DatabaseModel):
    __tablename__ = "resources_tags_association"

    resource_id: Mapped[UUID] = mapped_column(ForeignKey("resources.id"), primary_key=True)
    resource: Mapped["ResourceEntity"] = relationship(back_populates="tag_association")

    tag_id: Mapped[UUID] = mapped_column(ForeignKey("tags.id"), primary_key=True)
    tag: Mapped["TagEntity"] = relationship(back_populates="resource_association")
