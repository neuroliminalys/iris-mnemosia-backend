from http.client import NOT_FOUND

from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException


class TagNotFound(BusinessException):
    def __init__(self) -> None:
        super().__init__("Tag not found", NOT_FOUND)
