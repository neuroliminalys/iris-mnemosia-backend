from uuid import UUID

from fastapi import APIRouter

from iris_mnemosia_backend.application.dto.tag_dto import TagInput
from iris_mnemosia_backend.core.dependencies.tags_dependencies import TagUsecasesDep

router = APIRouter(prefix="/tags", tags=["tags"])


@router.post("", status_code=201)
def create(
    data: TagInput,
    usecases: TagUsecasesDep,
):
    return usecases.create(data)


@router.get("")
def get_all(usecases: TagUsecasesDep):
    return usecases.read_all()


@router.get("/{id}")
def get_by_id(target_id: UUID, usecases: TagUsecasesDep):
    return usecases.read_by_id(target_id)


@router.put("/{id}")
def edit(
    target_id: UUID,
    data: TagInput,
    usecases: TagUsecasesDep,
):
    return usecases.update(target_id, data)


@router.delete("/{id}", status_code=204)
def delete(target_id: UUID, usecases: TagUsecasesDep):
    return usecases.delete(target_id)
