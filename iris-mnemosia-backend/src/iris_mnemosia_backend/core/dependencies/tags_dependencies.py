from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from iris_mnemosia_backend.application.services.tag_service import TagService
from iris_mnemosia_backend.core.config.database import open_new_session
from iris_mnemosia_backend.core.usecases.tag_usecases import TagUsecases
from iris_mnemosia_backend.infrastructure.repositories.tag_repository import (
    TagRepository,
)

SessionDep = Annotated[
    Session,
    Depends(open_new_session),
]


def get_repository(session: SessionDep):
    return TagRepository(session)


RepositoryDep = Annotated[
    TagRepository,
    Depends(get_repository),
]


def get_service(repository: RepositoryDep):
    return TagService(repository)


ServiceDep = Annotated[
    TagService,
    Depends(get_service),
]


def get_usecases(service: ServiceDep):
    return TagUsecases(service)


TagUsecasesDep = Annotated[
    TagUsecases,
    Depends(get_usecases),
]
