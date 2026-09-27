from uuid import UUID

from fastapi import APIRouter

from iris_mnemosia_backend.application.dto.category_dto import CategoryInput, CategoryOutput
from iris_mnemosia_backend.core.dependencies.category_dependencies import (
    CategoryUsecasesDep,
)

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("")
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


@router.put("/edit")
def edit(
    editCategory: CategoryOutput,
    usecases: CategoryUsecasesDep,
):
    return usecases.update(editCategory)


@router.delete("/delete/{id}")
def delete(id: UUID, usecases: CategoryUsecasesDep):
    return usecases.delete(id)
