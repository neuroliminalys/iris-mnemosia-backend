from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from iris_mnemosia_backend.application.services.category_service import CategoryService
from iris_mnemosia_backend.core.usecases.category_usecase import CategoryUsecases
from iris_mnemosia_backend.infrastructure.database import open_new_session
from iris_mnemosia_backend.infrastructure.repositories.categories_repository import (
    CategoryRepository,
)

SessionDep = Annotated[
    Session,
    Depends(open_new_session),
]


def get_category_repository(session: SessionDep):
    return CategoryRepository(session)


CategoryRepositoryDep = Annotated[
    CategoryRepository,
    Depends(get_category_repository),
]


def get_category_service(repository: CategoryRepositoryDep):
    return CategoryService(repository)


CategoryServiceDep = Annotated[
    CategoryService,
    Depends(get_category_service),
]


def get_category_usecases(service: CategoryServiceDep):
    return CategoryUsecases(service)


CategoryUsecasesDep = Annotated[
    CategoryUsecases,
    Depends(get_category_usecases),
]
