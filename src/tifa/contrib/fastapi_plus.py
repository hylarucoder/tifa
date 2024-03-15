from fastapi import FastAPI, HTTPException
from pydantic import ValidationError, BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

from tifa.exceptions import ApiException, UnicornException, unicorn_exception_handler


class ApiModel(BaseModel):
    ...


class FastAPIPlus(FastAPI):
    ...


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(UnicornException, unicorn_exception_handler)
    app.add_exception_handler(ApiException, lambda request, err: err.to_result())

    @app.exception_handler(ValidationError)
    async def validation_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=400,
            content={
                "message": "参数错误",
                "errors": exc.errors(),
            },
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(Exception)
    def handle_exc(request: Request, exc):
        raise exc


def create_bp(dependencies: list = None) -> FastAPIPlus:
    if not dependencies:
        dependencies = []
    app = FastAPIPlus(dependencies=dependencies)
    setup_error_handlers(app)
    return app
