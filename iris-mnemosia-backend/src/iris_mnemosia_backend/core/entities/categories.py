from uuid import UUID, uuid7

from iris_mnemosia_backend.infrastructure.database import DatabaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Category(DatabaseModel):
    __tablename__ = "categories"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)