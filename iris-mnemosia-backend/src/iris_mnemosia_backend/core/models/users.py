from uuid import UUID, uuid7

from iris_mnemosia_backend.infrastructure.database import DatabaseModel
from sqlalchemy.orm import Mapped, mapped_column


class User(DatabaseModel):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)