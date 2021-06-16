import time

from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from tifa.api import TifaFastApi
from tifa.contrib.globals import GlobalsMiddleware
from tifa.exceptions import ApiException, UnicornException, unicorn_exception_handler
from tifa.settings import TifaSettings, get_settings
from tifa.utils.pkg import import_submodules
import socketio


def setup_routers(app: FastAPI):
    from tifa.apps import user, admin, whiteboard

    app.include_router(admin.bp, prefix="/admin", tags=["admin"])
    app.include_router(user.bp, prefix="/user", tags=["user"])
    app.include_router(whiteboard.bp, prefix="/whiteboard", tags=["whiteboard"])
    from prometheus_client import make_asgi_app

    prometheus_app = make_asgi_app()
    app.mount("/metrics", app=prometheus_app, name="prometheus_metrics")  # noqa

    # 正在注册 - socket.io 路由"
    from .apps.whiteboard import sio as whiteboard_router

    app.mount(
        "/whiteboard/",
        app=socketio.ASGIApp(
            socketio_server=whiteboard_router, socketio_path="/socket.io"
        ),
        name="whiteboard socket.io",
    )  # noqa
    from tifa.apps.admin.graphql import graphql_app as graphql_app_admin

    app.mount(
        "/admin/graphql",
        app=graphql_app_admin,
        name="graphql_app_admin",
    )  # noqa


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(UnicornException, unicorn_exception_handler)

    app.add_exception_handler(ApiException, lambda request, err: err.to_result())

    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    app.add_exception_handler(HTTPException, http_exception_handler)

    def handle_exc(request: Request, exc):
        raise exc

    app.add_exception_handler(Exception, handle_exc)


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
    static_files_app = StaticFiles(directory=settings.STATIC_DIR)
    app.mount(path=settings.STATIC_PATH, app=static_files_app, name="static")


def setup_db_models(app):
    import_submodules("tifa.models")


def setup_sentry(app):
    import sentry_sdk

    sentry_sdk.init(
        "sentry_sdk",
    )


def create_app(settings: TifaSettings):
    app = TifaFastApi(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
    )
    # thread local just flask like g
    app.add_middleware(GlobalsMiddleware)
    # 注册 db models
    setup_db_models(app)
    # 初始化路由
    setup_routers(app)
    # 初始化静态资源路径
    setup_static_files(app, settings)
    # 初始化全局 middleware
    setup_middleware(app)
    # 初始化全局 middleware
    setup_logging(app)
    # 初始化全局 error handling
    setup_error_handlers(app)
    # 初始化 sentry
    if settings.SENTRY_DSN:
        setup_sentry(app)

    return app


current_app = create_app(settings=get_settings())
