import time
from pathlib import Path

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.staticfiles import StaticFiles

from tifa.settings import settings
from tifa.utils.pkg import import_submodules


def setup_routers(app: FastAPI):
    from tifa.apps import user, health, admin, home

    app.mount("/health", health.bp)
    app.mount("/admin", admin.bp)
    app.mount("/user", user.bp)
    app.mount("/", home.bp)


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
    print(settings.STATIC_DIR, settings.STATIC_PATH)
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
    setup_db_models(app)
    setup_static_files(app)
    setup_routers(app)
    setup_middleware(app)
    setup_logging(app)
    if settings.SENTRY_DSN:
        setup_sentry(app)

    return app


current_app = create_app()
