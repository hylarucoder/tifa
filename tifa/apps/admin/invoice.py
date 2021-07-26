from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.discount import DiscountVoucher


class TInvoice(APIModel):
    id: str
    name: str


@bp.list("/invoices", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.item("/invoice", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/create", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/update", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/request", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/request_delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op(
    "/invoice/invoice_send_notification",
    out=TInvoice,
    summary="Invoice",
    tags=["Invoice"],
)
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}
