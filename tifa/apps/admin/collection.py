"""
collectionChannelListingUpdate(...): CollectionChannelListingUpdate
"""
from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import AsyncDal, db
from ...models.menu import Menu


class TCategory(APIModel):
    id: str
    name: str


@bp.list("/categories", out=TCategory, summary="Category", tags=["ProductCategory"])
async def get_categories():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/category", out=TCategory, summary="Category", tags=["ProductCategory"])
async def get_category():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/category/create", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/category/update", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/category/delete", out=TCategory, summary="Category", tags=["ProductCategory"])
async def category_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/category/bulk_delete", out=TCategory, summary="Category", tags=["ProductCategory"]
)
async def category_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/category/translate", out=TCategory, summary="Category", tags=["ProductCategory"]
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


class TCollection(APIModel):
    id: str
    name: str


@bp.page(
    "/collections", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.item(
    "/collection", out=TCollection, summary="Collection", tags=["ProductCollection"]
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/create",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/update",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/bulk_delete",
    out=TCollection,
    summary="Collection",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/translate",
    out=TCollection,
    summary="Translate",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/add_products",
    out=TCollection,
    summary="AddProducts",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/remove_products",
    out=TCollection,
    summary="RemoveProducts",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/collection/reorder_products",
    out=TCollection,
    summary="ReorderProducts",
    tags=["ProductCollection"],
)
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
