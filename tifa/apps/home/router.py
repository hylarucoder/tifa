from fastapi import Depends, Request
from tifa.contrib.fastapi_plus import create_bp
from fastapi.templating import Jinja2Templates

from tifa.settings import settings

bp = create_bp()

templates = Jinja2Templates(directory=settings.TEMPLATE_PATH)


@bp.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": 1}
    )


@bp.post("/clicked")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="clicked.html", context={"id": 1}
    )


@bp.get("/modal")
async def get_modal(request: Request):
    return templates.TemplateResponse(
        request=request, name="modal.html", context={"id": 1}
    )
