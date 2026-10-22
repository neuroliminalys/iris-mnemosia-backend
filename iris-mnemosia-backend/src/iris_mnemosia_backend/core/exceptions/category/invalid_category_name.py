from http.client import UNPROCESSABLE_CONTENT

from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException


class InvalidCategoryName(BusinessException):
    def __init__(self) -> None:
        super().__init__( "Category's name is not valid", UNPROCESSABLE_CONTENT)
