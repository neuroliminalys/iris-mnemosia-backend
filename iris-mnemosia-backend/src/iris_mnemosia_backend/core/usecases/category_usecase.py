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

    def create(self, newCategory: CategoryInput) -> dict | None:
        try:
            if newCategory.name.strip():
                resp = self.service.create(newCategory)
                return resp.model_dump(mode="json")
            raise InvalidCategoryName()
        except IntegrityError as e:
            # The second word of the casted error is the constraint name
            if str(e).strip().split(" ")[1] == "UNIQUE":
                raise CategoryAlreadyExists()

    def read_all(self) -> list[dict]:
        categories = self.service.read_all()
        return [category.model_dump(mode="json") for category in categories]

    def read_by_id(self, id: UUID) -> dict | None:
        resp = self.service.read_by_id(id)
        if resp:
            return resp.model_dump(mode="json")
        raise CategoryNotFound()

    def update(self, id: UUID, updatedCategory: CategoryInput) -> dict | None:
        try:
            resp = self.service.update(id, updatedCategory)
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
