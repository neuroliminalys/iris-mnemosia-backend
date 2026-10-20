import logging
from uuid import UUID

from fastapi._compat.v2 import ValidationError

from iris_mnemosia_backend.application.dto.resource_dto import (
    ResourceInput,
    ResourceOutput,
)
from iris_mnemosia_backend.core.models import ResourceEntity
from iris_mnemosia_backend.infrastructure.repositories.resource_repository import (
    ResourceRepository,
)

logger = logging.getLogger(__name__)


class ResourceService:
    repository: ResourceRepository

    def __init__(self, repository: ResourceRepository) -> None:
        logger.info(
            f"New instance of {__name__} with SERVICE-{id(self)} and REPOSITORY-{id(repository)}"
        )
        self.repository = repository

    def read_by_id(self, target_id: UUID) -> ResourceOutput | None:
        logger.info(f"SERVICE-{id(self)} : Read by {target_id}")
        found = self.repository.select_by_id(target_id)
        if found:
            return ResourceOutput.model_validate(found)
        return None

    def read_all(self) -> list[ResourceOutput]:
        logger.info(f"SERVICE-{id(self)} : Read all")
        resources = self.repository.select_all()
        return [ResourceOutput.model_validate(resource) for resource in resources]

    def create(self, data: ResourceInput) -> ResourceOutput:
        logger.info(f"SERVICE-{id(self)} : Create request")
        # ** is used to unpack the the dictonary (instead of doing : title=example.title, etc)
        resource = self.repository.insert(ResourceEntity(**data.model_dump()))
        return ResourceOutput.model_validate(resource)

    def update(self, target_id: UUID, updated: ResourceInput) -> ResourceOutput | None:
        logger.info(f"SERVICE-{id(self)} : Update {target_id}")
        found = self.repository.select_by_id(target_id)
        if found:
            for attr, value in updated.model_dump():
                setattr(found, attr, value)

            self.repository.session.flush()
            return ResourceOutput.model_validate(found)
        return None

    def delete(self, target_id: UUID) -> bool:
        logger.info(f"SERVICE-{id(self)} : Delete {target_id}")
        return self.repository.delete(target_id)
