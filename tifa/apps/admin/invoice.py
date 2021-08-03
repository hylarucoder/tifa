from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.models.discount import DiscountVoucher


class TInvoice(APIModel):
    id: str
    name: str


@bp.list("/invoices", out=TInvoice, summary="Invoice", tags=["Invoice"])
def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.item("/invoice", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_item():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/create", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_create():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/update", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_update():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_delete():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/request", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_request():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/invoice/request_delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
def invoice_request_delete():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op(
    "/invoice/send_notification",
    out=TInvoice,
    summary="Invoice",
    tags=["Invoice"],
)
def invoice_send_notification():
    adal = AsyncDal(db.async_session)
    ins = adal.first_or_404(DiscountVoucher)
    return {"items": ins}
