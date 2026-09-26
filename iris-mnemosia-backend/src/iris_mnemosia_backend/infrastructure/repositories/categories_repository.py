from uuid import UUID

from iris_mnemosia_backend.core.models.categories import Category
from sqlalchemy import select
from sqlalchemy.orm import Session


class CategoryRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def select_by_id(self, id: UUID) -> Category | None:
        return self.session.get(Category, id)

    def select_all(self) -> list[Category]:
        return self.session.scalars(select(Category)).all()

    def insert(self, newCategory: Category) -> Category:
        self.session.add(newCategory)
        return newCategory

    # def update(self, updatedCategory: Category) -> Category | None:
    #     category = self.session.get(Category, updatedCategory.id)
    #     if category:
    #         category.name = updatedCategory.name
    #     return category

    def delete(self, id: UUID) -> bool:
        category = self.session.get(Category, id)
        if(category):
            self.session.delete(category)
            return True
        return False
