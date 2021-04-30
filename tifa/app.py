import os
import pkgutil
import time

import devtools
from devtools import debug
from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from tifa.api import TifaFastApi
from tifa.exceptions import ApiException, UnicornException, unicorn_exception_handler
import traceback

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
from tifa.settings import TifaSettings, get_settings
from tifa.utils.pkg import import_submodules


def setup_routers(app: FastAPI):
    from tifa.apps import user, admin

    app.include_router(admin.bp, prefix="/admin", tags=["admin"])
    app.include_router(user.bp, prefix="/user", tags=["user"])
    from prometheus_client import make_asgi_app

    prometheus_app = make_asgi_app()
    app.mount("/metrics", app=prometheus_app, name="prometheus_metrics")  # noqa


def redirect_to_docs(response=RedirectResponse("/docs")) -> RedirectResponse:
    return response


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


def setup_middleware(app: FastAPI):
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    app.add_middleware(BaseHTTPMiddleware, dispatch=add_process_time_header)


def setup_static_files(app: FastAPI, settings: TifaSettings):
    return  # noqa
    static_files_app = StaticFiles(directory=settings.STATIC_DIR)
    app.mount(path=settings.STATIC_PATH, app=static_files_app, name="static")


def setup_db_models(app):
    m = import_submodules("tifa.models")
    register_tortoise(
        app,
        db_url=get_settings().POSTGRES_DATABASE_URI,
        modules={
            "models": ["tifa.models"],
        },
    )
    app.TORTOISE_ORM = TORTOISE_ORM


def create_app(settings: TifaSettings):
    app = TifaFastApi(
        debug=settings.DEBUG, title=settings.TITLE, description=settings.DESCRIPTION,
    )
    setup_db_models(app)
    # 初始化路由
    setup_routers(app)
    setup_static_files(app, settings)
    # 初始化全局 error_handler
    setup_error_handlers(app)
    # 初始化全局 middleware
    setup_middleware(app)
    # 初始化全局 middleware
    setup_cli(app)
    setup_logging(app)
    return app


current_app = create_app(settings=get_settings())

TORTOISE_ORM = current_app.TORTOISE_ORM
print(TORTOISE_ORM)
