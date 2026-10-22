import logging
from uuid import UUID

from sqlalchemy.exc import IntegrityError

from iris_mnemosia_backend.application.dto.category_dto import (
    CategoryInput,
)
from iris_mnemosia_backend.application.services.category_service import CategoryService
from iris_mnemosia_backend.core.exceptions.category.category_already_exists import (
    CategoryAlreadyExists,
)
from iris_mnemosia_backend.core.exceptions.category.category_not_found import (
    CategoryNotFound,
)
from iris_mnemosia_backend.core.exceptions.category.invalid_category_name import (
    InvalidCategoryName,
)

logger = logging.getLogger(__name__)


class CategoryUsecases:
    service: CategoryService

    def __init__(self, service: CategoryService) -> None:
        self.service = service

    def create(self, data: CategoryInput) -> dict | None:
        try:
            if data.name.strip():
                resp = self.service.create(data)
                return resp.model_dump(mode="json")
            raise InvalidCategoryName()
        except IntegrityError as e:
            # The second word of the casted error is the constraint name
            if str(e).strip().split(" ")[1] == "UNIQUE":
                raise CategoryAlreadyExists()

    def read_all(self) -> list[dict]:
        categories = self.service.read_all()
        return [category.model_dump(mode="json") for category in categories]

    def read_by_id(self, target_id: UUID) -> dict | None:
        resp = self.service.read_by_id(target_id)
        if resp:
            return resp.model_dump(mode="json")
        raise CategoryNotFound()

    def update(self, target_id: UUID, data: CategoryInput) -> dict | None:
        try:
            resp = self.service.update(target_id, data)
            if resp:
                return resp.model_dump(mode="json")
            raise CategoryNotFound()
        except Exception as e:
            logger.exception(str(e))
            raise

    def delete(self, id: UUID) -> None:
        resp = self.service.delete(id)
        if resp == False:
            raise CategoryNotFound()
