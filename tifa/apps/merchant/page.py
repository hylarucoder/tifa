"""
pageAttributeAssign(...): PageAttributeAssign
pageAttributeUnassign(...): PageAttributeUnassign

pageReorderAttributeValues(...): PageReorderAttributeValues
pageTypeReorderAttributes(...): PageTypeReorderAttributes
"""
from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.page import Page


class TPageType(APIModel):
    id: str
    name: str


@bp.list("/page_types", out=TPageType, summary="PageType", tags=["PageType"])
async def get_page_types():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.item("/page_type", out=TPageType, summary="PageType", tags=["PageType"])
async def get_page_type():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/create", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/update", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/delete", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page_type/bulk_delete", out=TPageType, summary="PageType", tags=["PageType"])
async def page_type_bulk_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


class TPage(APIModel):
    id: str
    name: str


@bp.list("/pages", out=TPage, summary="Page", tags=["Page"])
async def get_pages():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.item("/page", out=TPage, summary="Page", tags=["Page"])
async def get_page():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/create", out=TPage, summary="Page", tags=["Page"])
async def page_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/update", out=TPage, summary="Page", tags=["Page"])
async def page_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/delete", out=TPage, summary="Page", tags=["Page"])
async def page_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/bulk_delete", out=TPage, summary="Page", tags=["Page"])
async def page_bulk_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/bulk_publish", out=TPage, summary="Page", tags=["Page"])
async def page_bulk_publish():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}


@bp.op("/page/translate", out=TPage, summary="Page", tags=["Page"])
async def page_translate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Page)
    return {"items": ins}
