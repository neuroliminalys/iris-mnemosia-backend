import logging
from uuid import UUID

from fastapi import Request, Response

logger = logging.getLogger(__name__)


async def request_logger(request: Request, call_next) -> Response:
    # DO NOT OVERRIDE THESE VALUES
    host: str
    route: str
    http_verb: str

    # These are overwritable
    account: UUID | str

    request.state.account = None
    request.state.message = None

    resp = await call_next(request)

    if request.client:
        host = request.client.host
        port = request.client.port
    else:
        host = "unknown"
        port = None

    account = "User id : " + request.state.account if request.state.account else "Not authenticated"
    http_verb = request.method
    route = request.url.path

    logger.info(f"{host}:{port} | ({account}) : {http_verb} {route} | CODE HTTP : {resp.status_code} --> {request.state.message}")

    return resp
