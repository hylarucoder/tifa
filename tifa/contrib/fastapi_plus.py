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
    def item(self, path, out, summary: str = "Item", tags: Optional[list[str]] = None):
        if "-Item" not in summary:
            summary = summary + "-Item"
        cls_name = "Item" + path_to_cls_name(path)
        item_schema = create_model(
            cls_name,
            item=(out, ...),
        )
        return self.get(path, response_model=item_schema, tags=tags, summary=summary)

    def list(self, path, out, summary: str = "List", tags: Optional[list[str]] = None):
        if "-List" not in summary:
            summary = summary + "-List"
        cls_name = "List" + path_to_cls_name(path)
        list_schema = create_model(
            cls_name,
            items=(list[out], ...),
        )
        return self.get(path, response_model=list_schema, tags=tags, summary=summary)

    def page(self, path, out, summary: str = "Page", tags: Optional[List[str]] = None):
        if "-Page" not in summary:
            summary = summary + "-Page"
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
        cls_name = "Item" + path_to_cls_name(path)
        item_schema = create_model(
            cls_name,
            item=(out, ...),
        )
        return self.post(path, response_model=item_schema, tags=tags, summary=summary)


def suffix_summary(path, summary):
    kv = {
        "/create": "-Create",
        "/bulk_create": "-BulkCreate",
        "/update": "-Update",
        "/refresh": "-Refresh",
        "/verify": "-Verify",
        "/reorder": "-Reorder",
        "/delete": "-Delete",
        "/bulk_delete": "-BulkDelete",
        "/publish": "-Publish",
        "/bulk_publish": "-BulkPublish",
        "/translate": "-Translate",
        "/activate": "-Activate",
        "/deactivate": "-Deactivate",
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


def create_bp() -> FastAPIPlus:
    app = FastAPIPlus()
    setup_error_handlers(app)
    return app
