from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from tifa.contrib.socketio_router import socketio_server
from tifa.settings import get_settings

sio = socketio_server(get_settings().WHITEBOARD_URI)


@sio.on("connect")
async def on_connect(sid, environ, auth):
    # await sio.emit("drawing", kwargs)
    ...


@sio.on("drawing")
async def on_drawing(sid, data):
    await sio.emit("drawing", data, broadcast=True)


bp = APIRouter()

templates = Jinja2Templates(directory=get_settings().TEMPLATE_PATH)


@bp.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "/whiteboard/index.html", {
            "request": request,
            "id": 1
        }
    )
