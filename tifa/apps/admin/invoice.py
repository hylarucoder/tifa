from fastapi_utils.api_model import APIModel

from tifa.apps.admin.router import bp
from tifa.apps.admin.local import g
from tifa.models.discount import DiscountVoucher
from tifa.models.invoice import Invoice


class TInvoice(APIModel):
    id: str
    name: str


@bp.list("/invoices", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_list():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.item("/invoice", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_item():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op("/invoice/create", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_create():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op("/invoice/update", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_update():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op("/invoice/delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_delete():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op("/invoice/request", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_request():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op("/invoice/request_delete", out=TInvoice, summary="Invoice", tags=["Invoice"])
async def invoice_request_delete():
    ins = g.adal.first_or_404(Invoice)
    return {"items": ins}


@bp.op(
    "/invoice/send_notification",
    out=TInvoice,
    summary="Invoice",
    tags=["Invoice"],
)
async def invoice_send_notification():
    ins = g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}
