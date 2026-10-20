from http.client import CONFLICT

from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException


class ResourceAlreadyExists(BusinessException):
    def __init__(self) -> None:
        super().__init__("Resource already exists", CONFLICT)
