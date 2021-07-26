from fastapi import FastAPI

from tifa.contrib.fastapi_plus import create_bp
from tifa.globals import celery
from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException

bp = create_bp()


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


@bp.get("/test_1_plus_1/{result}")
def test_1_plus_1(result: int):
    return {"result": result == 2}


@bp.get("/test/1_plus_1_{result}")
def test_1_plus_1_v2(result: int):
    return {"result": result == 2}
