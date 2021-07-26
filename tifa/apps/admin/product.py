"""
productAttributeAssign(...): ProductAttributeAssign
productAttributeUnassign(...): ProductAttributeUnassign

productVariantChannelListingUpdate(...): ProductVariantChannelListingUpdate
productChannelListingUpdate(...): ProductChannelListingUpdate
"""

from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import AsyncDal, db
from ...models.menu import Menu


class TProductType(APIModel):
    id: str
    name: str


@bp.list(
    "/product_types", out=TProductType, summary="ProductType", tags=["ProductType"]
)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/product_type", out=TProductType, summary="ProductType", tags=["ProductType"])
async def get_product_type():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_type/create",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_type/update",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_type/delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_type/bulk_delete",
    out=TProductType,
    summary="ProductType",
    tags=["ProductType"],
)
async def product_type_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_type/reorder_attributes",
    out=TProductType,
    summary="ProductType-reorder_attributes",
    tags=["ProductType"],
)
async def product_type_reorder_attributes():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


class TProduct(APIModel):
    id: str
    name: str


@bp.list("/products", out=TProduct, summary="Product", tags=["Product"])
async def get_products():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/product", out=TProduct, summary="Product", tags=["Product"])
async def get_product():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/create", out=TProduct, summary="Product", tags=["Product"])
async def product_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/update", out=TProduct, summary="Product", tags=["Product"])
async def product_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/delete", out=TProduct, summary="Product", tags=["Product"])
async def product_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/bulk_delete", out=TProduct, summary="Product", tags=["Product"])
async def product_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/product/translate", out=TProduct, summary="Product", tags=["Product"])
async def product_translate():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product/reorder_attribute_values",
    out=TProduct,
    summary="Product-reorder_attribute_values",
    tags=["Product"],
)
async def product_reorder_attribute_values():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


class TProductVariant(APIModel):
    id: str
    name: str


@bp.list(
    "/product_variants",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def get_product_variants():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.item(
    "/product_variant",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def get_product_variant():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/bulk_create",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_bulk_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/update",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/bulk_delete",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/reorder",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_reorder():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/reorder_attribute_values",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_reorder_attribute_values():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/translate",
    out=TProductVariant,
    summary="ProductVariant",
    tags=["ProductVariant"],
)
async def product_variant_translate():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/set_default",
    out=TProductVariant,
    summary="ProductVariant-set default",
    tags=["ProductVariant"],
)
async def product_variant_set_default():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/create",
    out=TProductVariant,
    summary="ProductVariant-stocks-create",
    tags=["ProductVariant"],
)
async def product_variant_stocks_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/update",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
async def product_variant_stocks_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op(
    "/product_variant/stocks/delete",
    out=TProductVariant,
    summary="ProductVariant-stocks-update",
    tags=["ProductVariant"],
)
async def product_variant_stocks_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
