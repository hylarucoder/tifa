from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.discount import DiscountVoucher


class TVoucher(APIModel):
    id: str
    name: str


@bp.list("/vouchers", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def vouchers_page():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.item("/voucher", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_item():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/translate", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_translate():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/create", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_create():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/update", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_update():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_delete():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/bulk_delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_bulk_delete():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/add", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_catalog_add():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/remove", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_catalog_remove():
    ins = await g.adal.first_or_404(DiscountVoucher)
    return {"items": ins}


"""
voucherVoucherListingUpdate(...): VoucherVoucherListingUpdate
"""
