from fastapi_utils.api_model import APIModel

from tifa.apps.user import bp
from tifa.globals import AsyncDal, db
from tifa.models.menu import Menu


class TCheckout(APIModel):
    id: str
    name: str


@bp.page("/checkouts", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/checkout", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/create", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/complete", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/add_promo_code", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/remove_promo_code", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/payment_create", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/language_code_update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/email_update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/billing_address_update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/customer_attach", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/customer_detach", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/add", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/lines/delete", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/shipping_address/update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/checkout/shipping_method/update", out=TCheckout)
async def get_product_types():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
