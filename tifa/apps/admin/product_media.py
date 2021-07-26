from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import AsyncDal, db
from tifa.models.menu import Menu


class TProductMedia(APIModel):
    id: str
    name: str


@bp.op(
    "/product_media/create",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_media/update",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_media/delete",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_media/bulk_delete",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_media/reorder",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_reorder():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
