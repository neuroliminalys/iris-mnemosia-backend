from datetime import datetime, timezone
from uuid import UUID, uuid7

from iris_mnemosia_backend.infrastructure.database import DatabaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Resource(DatabaseModel):
    __tablename__ = "resources"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column(nullable=False)
    createdAt: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)