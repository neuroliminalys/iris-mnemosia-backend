from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from iris_mnemosia_backend.core.models.entities.categories_entity import (
    CategoryEntity,
)


class CategoryRepository:
    session: Session

    def __init__(self, session: Session) -> None:
        self.session = session

    def select_by_id(self, id: UUID) -> CategoryEntity | None:
        return self.session.get(CategoryEntity, id)

    def select_all(self) -> Sequence[CategoryEntity]:
        return self.session.scalars(select(CategoryEntity)).all()

    def insert(self, data: CategoryEntity) -> CategoryEntity:
        self.session.add(data)
        # Flushing so the database generated values are hydrated and
        # Pydantic model_validate wouldn't fail for missing database generated values
        self.session.flush()
        return data

    def delete(self, id: UUID) -> bool:
        found = self.session.get(CategoryEntity, id)
        if found:
            self.session.delete(found)
            return True
        return False
