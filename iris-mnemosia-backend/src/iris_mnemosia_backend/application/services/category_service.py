from uuid import UUID

from iris_mnemosia_backend.application.dto.category_dto import (
    CategoryInput,
    CategoryOutput,
)
from iris_mnemosia_backend.core.models.categories import Category
from iris_mnemosia_backend.infrastructure.repositories.categories_repository import (
    CategoryRepository,
)


class CategoryService:
    repository: CategoryRepository

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def read_by_id(self, id: UUID) -> CategoryOutput | None:
        searched = self.repository.select_by_id(id)
        if searched:
            return CategoryOutput.model_validate(searched)
        return None

    def read_all(self) -> list[CategoryOutput]:
        categories = self.repository.select_all()
        all = []
        for category in categories:
            all.append(CategoryOutput.model_validate(category))
        return all

    def create(self, newCategory: CategoryInput) -> CategoryOutput:
        # ** is used to unpack the the dictonary (instead of doing : title=example.title, etc)
        category = self.repository.insert(Category(**newCategory.model_dump()))
        return CategoryOutput.model_validate(category)

    def update(self, updatedCategory: CategoryOutput) -> CategoryOutput | None:
        searched = self.repository.select_by_id(updatedCategory.id)
        if searched:
            searched.name = updatedCategory.name
            return CategoryOutput.model_validate(searched)
        return None

    def delete(self, id: UUID) -> bool:
        return self.repository.delete(id)
