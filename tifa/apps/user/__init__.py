from typing import List, Optional

from fastapi import Query, FastAPI
from pydantic import Field, BaseModel
from starlette.websockets import WebSocket

bp = FastAPI()


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


class ILogin(BaseModel):
    username: str
    password: str


class OLogin(BaseModel):
    username: str
    password: str


@bp.post("/login", response_model=OLogin, summary="登陆", description="描述")
def login(params: ILogin):
    return params


@bp.get("/profile")
def profile():
    return "this is profile of {}"


class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@bp.get("/test")
def test(a):
    return {"a": a}


@bp.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()
