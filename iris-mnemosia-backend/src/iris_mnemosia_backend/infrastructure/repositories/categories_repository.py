from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iris_mnemosia_backend.core.models.categories import Category


class CategoryRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def select_by_id(self, id: UUID) -> Category | None:
        return self.session.get(Category, id)

    def select_all(self) -> Sequence[Category]:
        return self.session.scalars(select(Category)).all()

    def insert(self, newCategory: Category) -> Category:
        self.session.add(newCategory)
        # Flushing so the operation is instantly done and
        # Pydantic model_validate wouldn't fail for missing database generated values
        self.session.flush()
        return newCategory

    # def update(self, updatedCategory: Category) -> Category | None:
    #     category = self.session.get(Category, updatedCategory.id)
    #     if category:
    #         category.name = updatedCategory.name
    #     return category

    def delete(self, id: UUID) -> bool:
        category = self.session.get(Category, id)
        if category:
            self.session.delete(category)
            return True
        return False
