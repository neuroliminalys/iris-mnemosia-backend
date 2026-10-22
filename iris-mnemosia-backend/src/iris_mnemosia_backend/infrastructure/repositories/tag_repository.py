import logging
from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iris_mnemosia_backend.core.models.entities.tag_entity import TagEntity

logger = logging.getLogger(__name__)


class TagRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def select_by_id(self, target_id: UUID) -> TagEntity | None:
        return self.session.get(TagEntity, target_id)

    def select_all(self) -> Sequence[TagEntity]:
        return self.session.scalars(select(TagEntity)).all()

    def insert(self, data: TagEntity) -> TagEntity:
        self.session.add(data)
        # Flushing so the database generated values are hydrated and
        # Pydantic model_validate wouldn't fail for missing database generated values
        self.session.flush()
        return data

    def delete(self, target_id: UUID) -> bool:
        found = self.session.get(TagEntity, target_id)
        if found:
            self.session.delete(found)
            return True
        return False
