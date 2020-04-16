import os
import time

from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
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
from tifa.globals import db
from tifa.settings import TifaSettings, get_settings


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
    async def db_session_middleware(request: Request, call_next):
        """
        TODO: weired , polish later
        per_session for per request
        """
        from tifa.globals import db

        request.state.db_session = db.session
        response = await call_next(request)
        request.state.db_session.close()
        return response

    app.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

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
    from tifa import models
    pass


def create_app(settings: TifaSettings):
    app = TifaFastApi(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
    )
    # 初始化数据库相关 model
    db.setup_plugin(app)
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
