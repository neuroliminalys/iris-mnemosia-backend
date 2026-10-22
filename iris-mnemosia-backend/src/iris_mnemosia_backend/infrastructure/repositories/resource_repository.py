import logging
from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iris_mnemosia_backend.core.models.entities.resources_entity import (
    ResourceEntity,
)

logger = logging.getLogger(__name__)


class ResourceRepository:
    __tablename__ = "resources"
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def select_by_id(self, target_id: UUID) -> ResourceEntity | None:
        return self.session.get(ResourceEntity, target_id)

    def select_all(self) -> Sequence[ResourceEntity]:
        return self.session.scalars(select(ResourceEntity)).all()

    def insert(self, data: ResourceEntity) -> ResourceEntity:
        self.session.add(data)
        # Flushing so the database generated values are hydrated and
        # Pydantic model_validate wouldn't fail for missing database generated values
        self.session.flush()
        return data

    def delete(self, target_id: UUID) -> bool:
        found = self.session.get(ResourceEntity, target_id)
        if found:
            self.session.delete(found)
            return True
        return False
