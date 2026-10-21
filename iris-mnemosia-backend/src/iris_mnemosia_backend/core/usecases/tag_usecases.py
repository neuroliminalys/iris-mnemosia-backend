import logging
from uuid import UUID

from sqlalchemy.exc import IntegrityError

from iris_mnemosia_backend.application.dto.tag_dto import TagInput
from iris_mnemosia_backend.application.services.tag_service import TagService
from iris_mnemosia_backend.core.exceptions.tag.invalid_tag_name import (
    InvalidTagName,
)
from iris_mnemosia_backend.core.exceptions.tag.tag_already_exists import (
    TagAlreadyExists,
)
from iris_mnemosia_backend.core.exceptions.tag.tag_not_found import TagNotFound

logger = logging.getLogger(__name__)


class TagUsecases:
    service: TagService

    def __init__(self, service: TagService) -> None:
        self.service = service

    def create(self, data: TagInput) -> dict | None:
        try:
            if data.name.strip():
                resp = self.service.create(data)
                return resp.model_dump(mode="json")
            raise InvalidTagName()
        except IntegrityError as e:
            # The second word of the casted error is the constraint name
            if str(e).strip().split(" ")[1] == "UNIQUE":
                raise TagAlreadyExists()

    def read_all(self) -> list[dict]:
        categories = self.service.read_all()
        return [category.model_dump(mode="json") for category in categories]

    def read_by_id(self, target_id: UUID) -> dict | None:
        resp = self.service.read_by_id(target_id)
        if resp:
            return resp.model_dump(mode="json")
        raise TagNotFound()

    def update(self, target_id: UUID, data: TagInput) -> dict | None:
        try:
            resp = self.service.update(target_id, data)
            if resp:
                return resp.model_dump(mode="json")
            raise TagNotFound()
        except Exception as e:
            logger.exception(str(e))
            raise

    def delete(self, target_id: UUID) -> None:
        resp = self.service.delete(target_id)
        if resp == False:
            raise TagNotFound()
