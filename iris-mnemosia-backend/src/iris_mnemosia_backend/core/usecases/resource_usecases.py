import logging
from uuid import UUID

from sqlalchemy.exc import IntegrityError

from iris_mnemosia_backend.application.dto.resource_dto import ResourceInput
from iris_mnemosia_backend.application.services.resource_service import ResourceService
from iris_mnemosia_backend.core.exceptions.resources.invalid_resource_name import (
    InvalidResourceName,
)
from iris_mnemosia_backend.core.exceptions.resources.resource_already_exists import (
    ResourceAlreadyExists,
)
from iris_mnemosia_backend.core.exceptions.resources.resource_not_found import (
    ResourceNotFound,
)

logger = logging.getLogger(__name__)


class ResourcesUsecases:
    service: ResourceService

    def __init__(self, service: ResourceService) -> None:
        logger.info(f"New instance of {__name__} (USECASES-{id(self)}) linked to SERVICE-{id(service)}")
        self.service = service

    def create(self, data: ResourceInput) -> dict | None:
        try:
            if data.title.strip():
                resp = self.service.create(data)
                return resp.model_dump(mode="json")
            raise InvalidResourceName()
        except IntegrityError as e:
            # The second word of the casted error is the constraint name
            if str(e).strip().split(" ")[1] == "UNIQUE":
                raise ResourceAlreadyExists()

    def read_all(self) -> list[dict]:
        categories = self.service.read_all()
        return [category.model_dump(mode="json") for category in categories]

    def read_by_id(self, target_id: UUID) -> dict | None:
        resp = self.service.read_by_id(target_id)
        if resp:
            return resp.model_dump(mode="json")
        raise ResourceNotFound()

    def update(self, target_id: UUID, data: ResourceInput) -> dict | None:
        try:
            resp = self.service.update(target_id, data)
            if resp:
                return resp.model_dump(mode="json")
            raise ResourceNotFound()
        except Exception as e:
            logger.exception(str(e))
            raise

    def delete(self, target_id: UUID) -> None:
        resp = self.service.delete(target_id)
        if resp == False:
            raise ResourceNotFound()
