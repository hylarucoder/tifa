import socketio
from fastapi import Request
from socketio import AsyncServer, AsyncRedisManager
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from tifa.contrib.fastapi_plus import create_bp
from tifa.settings import settings

sio = AsyncServer(
    client_manager=AsyncRedisManager(settings.WHITEBOARD_URI),
    async_mode="asgi",
    cors_allowed_origins=["*"],
)

bp = create_bp()

bp.mount(
    "/whiteboard",
    app=socketio.ASGIApp(socketio_server=sio, socketio_path="/socket.io"),  # type: ignore
)


@sio.on("connect")
async def on_connect(sid, environ, auth):
    ...


@sio.on("drawing")
async def on_drawing(sid, data):
    await sio.emit("drawing", data, broadcast=True)


templates = Jinja2Templates(directory=settings.TEMPLATE_PATH)


@bp.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "/whiteboard/index.html", {"request": request, "id": 1}
    )
