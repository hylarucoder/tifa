import os

from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from yaml import load
from yaml import CLoader as Loader
from tifa.api import ApiException, TifaFastApi
import traceback

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response
#
#
# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
#
#
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )
#
#


# async def get_token_header(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")
from tifa.settings import TifaSettings


def setup_routers(app: FastAPI):
    from tifa.apps import admin

    app.include_router(admin.bp, prefix="/admin", tags=["entry_point admin"])

    from tifa.apps import user

    app.include_router(
        user.bp,
        prefix="/user",
        tags=["entry_point user"],
        # dependencies=[Depends(get_token_header)],
        dependencies=[],
        responses={404: {"description": "Not found"}},
    )

    @app.get("/", include_in_schema=False)
    def redirect_to_docs(response=RedirectResponse("/docs")) -> RedirectResponse:
        return response


def register_config(app: FastAPI, config: dict):
    config_path = os.environ.get("APP_SETTINGS", "config.yaml")
    with open(config_path) as f:
        config.update(load(f, Loader=Loader))
    app.config.update(config)


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(UnicornException, unicorn_exception_handler)

    def handle_exc(request: Request, exc):
        if isinstance(exc, HTTPException):
            return exc
        raise exc

    app.add_exception_handler(Exception, handle_exc)
    app.add_exception_handler(ApiException, lambda request, err: err.to_result())


def setup_cli(app: FastAPI):
    pass


def setup_logging(app: FastAPI):
    pass


def setup_db(app: FastAPI):
    async def db_session_middleware(request: Request, call_next):
        """
        TODO: weired , polish later
        per_session for per request
        """
        from tifa.db import Session

        request.state.db_session = Session()
        response = await call_next(request)
        request.state.db_session.close()
        return response

    app.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)


def create_app(settings: TifaSettings):
    # config = config or {}
    app = TifaFastApi(title="tifa")  # noqa
    # TODO
    # register_config(app, config)
    setup_routers(app)
    static_files_app = StaticFiles(directory=str(settings.static_dir))
    app.mount(path=settings.static_mount_path, app=static_files_app, name="static")

    setup_error_handlers(app)
    setup_db(app)
    setup_logging(app)

    setup_cli(app)

    return app


current_app = create_app()
