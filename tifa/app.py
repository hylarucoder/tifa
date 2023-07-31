import time

from fastapi import FastAPI, Request
from prometheus_client import make_asgi_app  # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.staticfiles import StaticFiles

from tifa.contrib.globals import GlobalsMiddleware
from tifa.settings import settings
from tifa.utils.pkg import import_submodules


def setup_routers(app: FastAPI):
    from tifa.apps import user, health, whiteboard, admin

    app.mount("/health", health.bp)
    # app.mount("/admin", admin.bp)
    app.mount("/user", user.bp)
    app.mount("/whiteboard", whiteboard.bp)
    app.mount("/metrics", make_asgi_app())


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


def setup_static_files(app: FastAPI):
    static_files_app = StaticFiles(directory=settings.STATIC_DIR)
    app.mount(path=settings.STATIC_PATH, app=static_files_app, name="static")


def setup_db_models(app):
    import_submodules("tifa.models")


def setup_sentry(app):
    import sentry_sdk

    sentry_sdk.init(
        "sentry_sdk",
    )


def create_app():
    app = FastAPI(
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
    setup_static_files(app)
    # 初始化全局 middleware
    setup_middleware(app)
    # 初始化全局 middleware
    setup_logging(app)
    # 初始化 sentry
    if settings.SENTRY_DSN:
        setup_sentry(app)

    return app


current_app = create_app()
