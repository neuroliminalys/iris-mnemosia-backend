import logging
from uuid import UUID

from iris_mnemosia_backend.application.dto.tag_dto import TagInput, TagOutput
from iris_mnemosia_backend.core.models.entities.tag_entity import TagEntity
from iris_mnemosia_backend.infrastructure.repositories.tag_repository import (
    TagRepository,
)

logger = logging.getLogger(__name__)


class TagService:
    repository: TagRepository

    def __init__(self, repository: TagRepository) -> None:
        self.repository = repository

    def read_by_id(self, target_id: UUID) -> TagOutput | None:
        found = self.repository.select_by_id(target_id)
        if found:
            return TagOutput.model_validate(found)
        return None

    def read_all(self) -> list[TagOutput]:
        resources = self.repository.select_all()
        return [TagOutput.model_validate(resource) for resource in resources]

    def create(self, data: TagInput) -> TagOutput:
        # ** is used to unpack the the dictonary (instead of doing : title=example.title, etc)
        resource = self.repository.insert(TagEntity(**data.model_dump()))
        return TagOutput.model_validate(resource)

    def update(self, target_id: UUID, updated: TagInput) -> TagOutput | None:
        found = self.repository.select_by_id(target_id)
        if found:
            for attr, value in updated.model_dump():
                setattr(found, attr, value)

            self.repository.session.flush()
            return TagOutput.model_validate(found)
        return None

    def delete(self, target_id: UUID) -> bool:
        return self.repository.delete(target_id)
