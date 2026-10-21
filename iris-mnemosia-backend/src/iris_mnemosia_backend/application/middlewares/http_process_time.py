import time

from fastapi import Request, Response


async def http_process_time(request: Request, call_next) -> Response:
    start_time = time.perf_counter()
    resp = await call_next(request)
    process_time = time.perf_counter() - start_time
    resp.headers["X-Process-Time"] = str(process_time)
    return resp