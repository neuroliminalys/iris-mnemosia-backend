import logging
from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iris_mnemosia_backend.core.models.tag_entity import TagEntity

logger = logging.getLogger(__name__)


class TagRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session
        logger.debug(f"New instance of {__name__} with id {id(self)} and session {id(session)}")

    def select_by_id(self, target_id: UUID) -> TagEntity | None:
        logger.debug(f"REPOSITORY-{id(self)} : Select by {target_id} (SESSION-{id(self.session)})")
        return self.session.get(TagEntity, target_id)

    def select_all(self) -> Sequence[TagEntity]:
        logger.debug(f"REPOSITORY-{id(self)} : Select all (SESSION-{id(self.session)})")
        return self.session.scalars(select(TagEntity)).all()

    def insert(self, data: TagEntity) -> TagEntity:
        logger.debug(f"REPOSITORY-{id(self)} : Insert (SESSION-{id(self.session)})")
        self.session.add(data)
        # Flushing so the database generated values are hydrated and
        # Pydantic model_validate wouldn't fail for missing database generated values
        self.session.flush()
        return data

    def delete(self, target_id: UUID) -> bool:
        logger.debug(f"REPOSITORY-{id(self)} : Deleting {target_id} (SESSION-{id(self.session)})")
        found = self.session.get(TagEntity, target_id)
        if found:
            self.session.delete(found)
            return True
        return False
