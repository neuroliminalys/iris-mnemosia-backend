from uuid import UUID, uuid7

from sqlalchemy.orm import Mapped, mapped_column

from iris_mnemosia_backend.core.config.database import DatabaseModel


class User(DatabaseModel):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(
        primary_key=True, default=uuid7, unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
