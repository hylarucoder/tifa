import datetime
from typing import Optional

import pydantic as pt
from fastapi_utils.api_model import APIModel

from tifa.apps.user.local import g
from tifa.apps.user.router import bp
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.models.menu import Menu


class TCartItemActivity(APIModel):
    act_id: str
    act_type: str
    act_title: str


class TCartItem(APIModel):
    item_id: str
    parent_item_id: Optional[str] = pt.Field(description="绑定的父item_id")
    order_id: Optional[str] = pt.Field(description="绑定的订单号")
    sku: str = pt.Field(description="sku")
    spu: str = pt.Field(description="spu")
    channel: str = pt.Field(description="售卖渠道")
    quantity: int = pt.Field(description="商品数量")
    status: int = pt.Field(description="status")  # 失效?过期?
    sale_price: int = pt.Field(description="记录加车时候的销售价格")
    special_price: int = pt.Field(description="指定价格加购物车")
    post_free: bool = pt.Field(description="是否免邮")
    activities: list[TCartItemActivity] = pt.Field(description="参加的活动记录")
    created_at: datetime.datetime
    updated_at: datetime.datetime
    expired_at: datetime.datetime = pt.Field(description="有效时间")


class TCart(APIModel):
    items: str
    updated_at: datetime.datetime
    version: int
    # uid: cart_type


@bp.item("/cart", out=TCart)
async def cart():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/cart/add_item", out=TCart)
async def cart_add_item():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/cart/change_item_quantity", out=TCart)
async def cart_edit_item_quantity():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/cart/change_item_spec", out=TCart)
async def cart_change_item_spec():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/cart/delete_item", out=TCart)
async def checkout_clean():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/preview_order", out=TCart)
async def preview_order():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/make_order", out=TCart)
async def make_order():
    merchant = await g.adal.first_or_404(Menu)
    return {"item": merchant}
