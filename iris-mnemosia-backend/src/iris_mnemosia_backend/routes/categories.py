from uuid import UUID

from fastapi import APIRouter

from iris_mnemosia_backend.application.dto.category_dto import (
    CategoryInput,
)
from iris_mnemosia_backend.core.dependencies.category_dependencies import (
    CategoryUsecasesDep,
)

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", status_code=201)
def create(
    newCategory: CategoryInput,
    usecases: CategoryUsecasesDep,
):
    return usecases.create(newCategory)


@router.get("")
def get_all(usecases: CategoryUsecasesDep):
    return usecases.read_all()


@router.get("/{id}")
def get_by_id(id: UUID, usecases: CategoryUsecasesDep):
    return usecases.read_by_id(id)


@router.put("/{id}")
def edit(
    id: UUID,
    editCategory: CategoryInput,
    usecases: CategoryUsecasesDep,
):
    return usecases.update(id, editCategory)


@router.delete("/{id}", status_code=204)
def delete(id: UUID, usecases: CategoryUsecasesDep):
    return usecases.delete(id)
