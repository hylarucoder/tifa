from typing import Optional, List

from fastapi import FastAPI, HTTPException
from fastapi_utils.api_model import APIModel
from pydantic import create_model, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from tifa.exceptions import ApiException, UnicornException, unicorn_exception_handler


def snake_convert(s):
    if not isinstance(s, str):
        return s
    components = s.split("_")
    return "".join(x.title() for x in components)


def path_to_cls_name(path):
    return snake_convert(path[1:].replace("/", "_"))


class FastAPIPlus(FastAPI):
    def item(self, path, out, summary: str = "详细", tags: Optional[list[str]] = None):
        if "-详细" not in summary:
            summary = summary + "-详细"
        cls_name = "Item" + path_to_cls_name(path)
        item_schema = create_model(
            cls_name,
            item=(out, ...),
        )
        return self.get(path, response_model=item_schema, tags=tags, summary=summary)

    def list(self, path, out, summary: str = "列表", tags: Optional[list[str]] = None):
        if "-列表" not in summary:
            summary = summary + "-列表"
        cls_name = "List" + path_to_cls_name(path)
        list_schema = create_model(
            cls_name,
            items=(list[out], ...),
        )
        return self.get(path, response_model=list_schema, tags=tags, summary=summary)

    def page(self, path, out, summary: str = "分页", tags: Optional[List[str]] = None):
        if "-分页" not in summary:
            summary = summary + "-分页"
        cls_name = "Page" + path_to_cls_name(path)
        list_schema = create_model(
            cls_name,
            items=(list[out], ...),
            page=(int, ...),
            per_page=(int, ...),
            total=(int, ...),
            __base__=APIModel,
        )
        return self.get(path, response_model=list_schema, tags=tags, summary=summary)

    def op(
        self, path: str, out=None, summary: str = "操作", tags: Optional[List[str]] = None
    ):
        summary = suffix_summary(path, summary)
        return self.post(path, response_model=out, tags=tags, summary=summary)


def suffix_summary(path, summary):
    kv = {
        "/add": "-新增",
        "/edit": "-编辑",
        "/sort": "-排序",
        "/delete": "-删除",
        "/enable": "-启用",
        "/disable": "-停用",
    }
    for k, v in kv.items():
        if path.endswith(k):
            if v not in summary:
                summary = summary + v
    return summary


def setup_error_handlers(app: FastAPI):
    app.add_exception_handler(UnicornException, unicorn_exception_handler)

    async def validation_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=400,
            content={
                "message": "参数错误",
                "errors": exc.errors(),
            },
        )

    app.add_exception_handler(ValidationError, validation_handler)

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


def create_bp():
    app = FastAPIPlus()
    setup_error_handlers(app)
    return app
