import logging
from uuid import UUID

from fastapi import Request, Response

logger = logging.getLogger(__name__)


async def request_logger(request: Request, call_next) -> Response:
    account: UUID | str

    host: str = request.client.host if request.client else "unknown"

    try:
        foundAccount = request.state.account
        account = foundAccount
    except AttributeError:
        account = "Not authenticated"

    http_verb: str = request.method
    route: str = request.url.path

    logger.info(f"{host} | {account} | {http_verb} | {route}")

    resp = await call_next(request)
    return resp
