import logging

from fastapi.requests import Request
from fastapi.responses import JSONResponse

from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException

logger = logging.getLogger(__name__)


def business_exception_handler(request: Request, exception: BusinessException):
    request.state.message = exception.message
    return JSONResponse(
        status_code=exception.status_code, content={"message": exception.message}
    )
