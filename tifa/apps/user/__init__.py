from typing import List, Optional

from fastapi import APIRouter, Query, Path
from pydantic import BaseModel
from starlette.websockets import WebSocket

bp = APIRouter()


@bp.get("/")
def index():
    return "welcome to flask world!"


@bp.get("/path/1_plus_1/{result}")
def v1_one_plus_one(result: int):
    return result == 2


@bp.get("/path/1_plus_1_{result}")
def v2_one_plus_one(result: int):
    return result == 2


@bp.get("/collections/{col_id}/posts")
def collections_posts(
        col_id: int,
        q: str = Query(None, min_length=3, max_length=50),
        page: int = 1,
        per_page: int = 10,
):
    return {
        col_id,
        q,
        page,
        per_page,
    }


class WeiboImage(BaseModel):
    name: str
    url: str


class Weibo(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    images: List[WeiboImage]


@bp.post("/weibo/post")
def post_weibo(weibo: Weibo):
    """
    复杂表单一般还是很难生成文档的
    """
    return {weibo}


@bp.post("/login")
def login(name):
    return ""


@bp.get("/profile")
def profile():
    return "this is profile of {}"


@bp.get("/test")
def test(a):
    return {"a": a}


@bp.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()
