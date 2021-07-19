from fastapi import FastAPI

from tifa.globals import celery
from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException

bp = FastAPI()


@bp.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return ORJSONResponse(
        {
            "message": exc.detail,
        },
        status_code=exc.status_code,
    )


@bp.get("/test_celery")
def test_celery():
    celery.send_task("test_celery", args=("words????",))
    return "ok"


@bp.get("/test_sentry")
def test_sentry():
    1 / 0
