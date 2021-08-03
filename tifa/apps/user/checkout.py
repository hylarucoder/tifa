from fastapi_utils.api_model import APIModel

from tifa.apps.user.base import bp
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.models.menu import Menu


class TCheckout(APIModel):
    id: str
    name: str


@bp.page("/checkouts", out=TCheckout)
async def checkouts_item():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/checkout", out=TCheckout)
async def checkout_item():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/create", out=TCheckout)
async def checkout_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/complete", out=TCheckout)
async def checkout_complete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/add_promo_code", out=TCheckout)
async def checkout_add_promo_code():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/remove_promo_code", out=TCheckout)
async def checkout_remove_promo_code():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/payment_create", out=TCheckout)
async def checkout_payment_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/language_code_update", out=TCheckout)
async def checkout_language_code_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/email_update", out=TCheckout)
async def checkout_email_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/billing_address_update", out=TCheckout)
async def checkout_billing_address_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/customer_attach", out=TCheckout)
async def checkout_customer_attach():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/customer_detach", out=TCheckout)
async def checkout_customer_detach():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines", out=TCheckout)
async def checkout_lines():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/add", out=TCheckout)
async def checkout_lines_add():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/update", out=TCheckout)
async def checkout_lines_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/delete", out=TCheckout)
async def checkout_lines_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/shipping_address/update", out=TCheckout)
async def checkout_shipping_address_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/shipping_method/update", out=TCheckout)
async def checkout_shipping_method_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
