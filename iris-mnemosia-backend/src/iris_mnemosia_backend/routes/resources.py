from uuid import UUID

from fastapi import APIRouter

from iris_mnemosia_backend.application.dto.resource_dto import ResourceInput
from iris_mnemosia_backend.core.dependencies.resources_dependencies import (
    ResourcesUsecasesDep,
)

router = APIRouter(prefix="/resources", tags=["resources"])


@router.post("", status_code=201)
def create(
    data: ResourceInput,
    usecases: ResourcesUsecasesDep,
):
    return usecases.create(data)


@router.get("")
def get_all(usecases: ResourcesUsecasesDep):
    return usecases.read_all()


@router.get("/{id}")
def get_by_id(target_id: UUID, usecases: ResourcesUsecasesDep):
    return usecases.read_by_id(target_id)


@router.put("/{id}")
def edit(
    target_id: UUID,
    data: ResourceInput,
    usecases: ResourcesUsecasesDep,
):
    return usecases.update(target_id, data)


@router.delete("/{id}", status_code=204)
def delete(target_id: UUID, usecases: ResourcesUsecasesDep):
    return usecases.delete(target_id)
