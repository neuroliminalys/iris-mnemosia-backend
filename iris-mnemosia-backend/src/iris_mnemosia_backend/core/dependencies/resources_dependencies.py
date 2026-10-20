from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from iris_mnemosia_backend.application.services.resource_service import ResourceService
from iris_mnemosia_backend.core.config.database import open_new_session
from iris_mnemosia_backend.core.usecases.resource_usecases import ResourcesUsecases
from iris_mnemosia_backend.infrastructure.repositories.resource_repository import (
    ResourceRepository,
)

SessionDep = Annotated[
    Session,
    Depends(open_new_session),
]


def get_repository(session: SessionDep):
    return ResourceRepository(session)


RepositoryDep = Annotated[
    ResourceRepository,
    Depends(get_repository),
]


def get_service(repository: RepositoryDep):
    return ResourceService(repository)


ServiceDep = Annotated[
    ResourceService,
    Depends(get_service),
]


def get_usecases(service: ServiceDep):
    return ResourcesUsecases(service)


ResourcesUsecasesDep = Annotated[
    ResourcesUsecases,
    Depends(get_usecases),
]
