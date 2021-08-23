"""
pageAttributeAssign(...): PageAttributeAssign
pageAttributeUnassign(...): PageAttributeUnassign

pageReorderAttributeValues(...): PageReorderAttributeValues
pageTypeReorderAttributes(...): PageTypeReorderAttributes
"""
from fastapi_utils.api_model import APIModel

from tifa.apps.admin.router import bp
from tifa.apps.admin.local import g
from tifa.models.page import Page


class TPageType(APIModel):
    id: str
    name: str


@bp.list("/page_types", out=TPageType, summary="PageType", tags=["PageType"])
async def get_page_types():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.item("/page_type", out=TPageType, summary="PageType", tags=["PageType"])
async def get_page_type():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/create", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_create():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/update", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_update():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/delete", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_delete():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/bulk_delete", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_bulk_delete():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


class TPage(APIModel):
    id: str
    name: str


@bp.list("/pages", out=TPage, summary="Page", tags=["Page"])
async def get_pages():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.item("/page", out=TPage, summary="Page", tags=["Page"])
async def get_page():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/create", out=TPage, summary="Page", tags=["Page"])
async def page_create():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/update", out=TPage, summary="Page", tags=["Page"])
async def page_update():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/delete", out=TPage, summary="Page", tags=["Page"])
async def page_delete():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/bulk_delete", out=TPage, summary="Page", tags=["Page"])
async def page_bulk_delete():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/bulk_publish", out=TPage, summary="Page", tags=["Page"])
async def page_bulk_publish():
    ins = await g.adal.first_or_404(Page)
    return {"items": ins}
