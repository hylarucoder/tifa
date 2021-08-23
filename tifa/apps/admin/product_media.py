from fastapi_utils.api_model import APIModel

from tifa.apps.admin.router import bp
from tifa.apps.admin.local import g
from tifa.models.product_media import ProductMedia


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
    merchant = await g.adal.first_or_404(ProductMedia)
    return {"item": merchant}


@bp.op(
    "/product_media/update",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_update():
    merchant = await g.adal.first_or_404(ProductMedia)
    return {"item": merchant}


@bp.op(
    "/product_media/delete",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_delete():
    merchant = await g.adal.first_or_404(ProductMedia)
    return {"item": merchant}


@bp.op(
    "/product_media/bulk_delete",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_bulk_delete():
    merchant = await g.adal.first_or_404(ProductMedia)
    return {"item": merchant}


@bp.op(
    "/product_media/reorder",
    out=TProductMedia,
    summary="ProductMedia",
    tags=["ProductMedia"],
)
async def product_media_reorder():
    merchant = await g.adal.first_or_404(ProductMedia)
    return {"item": merchant}
