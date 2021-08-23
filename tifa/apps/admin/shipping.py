"""
shippingMethodChannelListingUpdate(...): ShippingMethodChannelListingUpdate
"""

from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.shipping import ShippingZone


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
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/create",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_create():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/update",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_update():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/delete",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_delete():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/bulk_delete",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_bulk_delete():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/translate",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_translate():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/exclude_products",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_exclude_products():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_price/remove_product_from_exclude",
    out=TShippingPrice,
    summary="ShippingPrice",
    tags=["Shipping"],
)
async def shipping_price_remove_product_from_exclude():
    ins = await g.adal.first_or_404(ShippingZone)
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
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.item(
    "/shipping_zone", out=TShippingZone, summary="ShippingPrice", tags=["Shipping"]
)
async def get_shipping_zone():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/create",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_create():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/update",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_update():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/delete",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_delete():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}


@bp.op(
    "/shipping_zone/bulk_delete",
    out=TShippingZone,
    summary="ShippingZone",
    tags=["Shipping"],
)
async def shipping_zone_bulk_delete():
    ins = await g.adal.first_or_404(ShippingZone)
    return {"items": ins}
