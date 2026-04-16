import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.metrics import REQUEST_COUNT, REQUEST_LATENCY


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        endpoint = request.url.path

        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

        start_time = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start_time

        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)

        return response