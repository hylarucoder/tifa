from enum import auto

from fastapi_utils.api_model import APIModel
from fastapi_utils.enums import StrEnum

from tifa.apps.merchant import bp


class TWebhookEventType(StrEnum):
    ANY_EVENTS = auto()
    ORDER_CREATED = auto()
    ORDER_CONFIRMED = auto()
    ORDER_FULLY_PAID = auto()
    ORDER_UPDATED = auto()
    ORDER_CANCELLED = auto()
    ORDER_FULFILLED = auto()
    INVOICE_REQUESTED = auto()
    INVOICE_DELETED = auto()
    INVOICE_SENT = auto()
    CUSTOMER_CREATED = auto()
    CUSTOMER_UPDATED = auto()
    PRODUCT_CREATED = auto()
    PRODUCT_UPDATED = auto()
    PRODUCT_DELETED = auto()
    PRODUCT_VARIANT_CREATED = auto()
    PRODUCT_VARIANT_UPDATED = auto()
    PRODUCT_VARIANT_DELETED = auto()
    CHECKOUT_CREATED = auto()
    CHECKOUT_UPDATED = auto()
    FULFILLMENT_CREATED = auto()
    NOTIFY_USER = auto()
    PAGE_CREATED = auto()
    PAGE_UPDATED = auto()
    PAGE_DELETED = auto()
    PAYMENT_AUTHORIZE = auto()
    PAYMENT_CAPTURE = auto()
    PAYMENT_CONFIRM = auto()
    PAYMENT_LIST_GATEWAYS = auto()
    PAYMENT_PROCESS = auto()
    PAYMENT_REFUND = auto()
    PAYMENT_VOID = auto()


class TWebhook(APIModel):
    id: str
    name: str


@bp.list(
    "/webhooks",
    out=TWebhook,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_list():
    return []


@bp.item(
    "/webhook",
    out=TWebhook,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_item():
    return []


@bp.op(
    "/webhook/create",
    out=TWebhook,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_create():
    return []


@bp.op(
    "/webhook/update",
    out=TWebhook,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_update():
    return []


class TWebhookEvent(APIModel):
    id: str
    name: str


@bp.list(
    "/webhook/events",
    out=TWebhookEvent,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_update():
    return []


@bp.list(
    "/webhook/sample_payload",
    out=TWebhookEvent,
    summary="webhooks",
    tags=["Webhook"],
)
def webhook_update():
    return []
