from fastapi import FastAPI, HTTPException, Request
from pydantic import ValidationError, BaseModel, ConfigDict

from tifa.exceptions import ApiException, UnicornException


class ApiModel(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)


class FastAPIPlus(FastAPI):
    ...


def setup_error_handlers(app: FastAPI):
    @app.exception_handler(UnicornException)
    def unicorn_exception_handler(request: Request, exc: UnicornException):
        raise ApiException(exc.name, status_code=500)

    @app.exception_handler(ValidationError)
    async def validation_handler(request: Request, exc: ValidationError):
        raise ApiException(
            "validate error",
            status_code=500,
            errors=exc.errors(),
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        raise ApiException(exc.detail, exc.status_code)

    @app.exception_handler(Exception)
    def handle_exc(request: Request, exc):
        raise exc

    app.add_exception_handler(ApiException, lambda request, err: err.to_result())


def create_bp(dependencies: list = None) -> FastAPIPlus:
    if not dependencies:
        dependencies = []
    app = FastAPIPlus(dependencies=dependencies)
    setup_error_handlers(app)
    return app
