"""
shippingMethodChannelListingUpdate(...): ShippingMethodChannelListingUpdate
"""

from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.shipping import ShippingZone


class TShippingPrice(APIModel):
    id: str
    name: str


@bp.list(
    "/shipping_prices",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def get_shipping_prices():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/create",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/update",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/delete",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/bulk_delete",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_bulk_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/translate",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_translate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/exclude_products",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_exclude_products():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/remove_product_from_exclude",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_remove_product_from_exclude():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


class TShippingZone(APIModel):
    id: str
    name: str


@bp.list(
    "/shipping_zones",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def get_shipping_zones():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.item(
    "/shipping_zone", out=TShippingZone, summary="ShippingPrice", tags=["Shipping"]
)
async def get_shipping_zone():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/create",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/update",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/delete",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/bulk_delete",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_bulk_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(ShippingZone)
    return {"items": ins}
