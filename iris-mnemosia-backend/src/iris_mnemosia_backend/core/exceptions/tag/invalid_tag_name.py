from http.client import UNPROCESSABLE_CONTENT

from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException


class InvalidTagName(BusinessException):
    def __init__(self) -> None:
        super().__init__("Tag's name is not valid", UNPROCESSABLE_CONTENT)
