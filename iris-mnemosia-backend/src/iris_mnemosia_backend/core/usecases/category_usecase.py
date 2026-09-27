from http.client import NO_CONTENT, NOT_FOUND
from uuid import UUID

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from iris_mnemosia_backend.application.dto.category_dto import (
    CategoryInput,
    CategoryOutput,
)
from iris_mnemosia_backend.application.services.category_service import CategoryService


class CategoryUsecases:
    service: CategoryService

    def __init__(self, service: CategoryService) -> None:
        self.service = service

    def create(self, newCategory: CategoryInput) -> JSONResponse | None:
        try:
            resp = self.service.create(newCategory)
            self.service.repository.session.commit()
            return JSONResponse(resp.model_dump(mode="json"))
        except Exception:
            self.service.repository.session.rollback()
            # TODO: log e
            raise

    def read_all(self) -> JSONResponse:
        categories = self.service.read_all()
        return JSONResponse(
            content=[category.model_dump(mode="json") for category in categories]
        )

    def read_by_id(self, id: UUID) -> JSONResponse | HTTPException:
        resp = self.service.read_by_id(id)
        if resp:
            return JSONResponse(resp.model_dump(mode="json"))
        raise HTTPException(status_code=NOT_FOUND)

    def update(self, updatedCategory: CategoryOutput) -> (
        JSONResponse | HTTPException
    ) | None:
        try:
            resp = self.service.update(updatedCategory)
            if resp:
                self.service.repository.session.commit()
                return JSONResponse(resp.model_dump(mode="json"))
            self.service.repository.session.rollback()
            raise HTTPException(status_code=NOT_FOUND)
        except Exception:
            self.service.repository.session.rollback()
            # TODO: log e
            raise

    def delete(self, id: UUID) -> HTTPException:
        resp = self.service.delete(id)
        if resp == True:
            self.service.repository.session.commit()
            raise HTTPException(status_code=NO_CONTENT)
        self.service.repository.session.rollback()
        raise HTTPException(status_code=NOT_FOUND)
