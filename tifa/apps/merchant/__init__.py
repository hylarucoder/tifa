from enum import auto

from fastapi_utils.api_model import APIModel
from fastapi_utils.enums import StrEnum

from tifa.contrib.fastapi_plus import create_bp
from tifa.globals import db, AsyncDal, Dal
from tifa.models.system import Staff

bp = create_bp()


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


class TWebhookEvent(APIModel):
    id: str
    eventType: TWebhookEventType


@bp.list("/webhooks", TWebhookEvent)
def webhooks():
    return []


@bp.post("/login")
async def login():
    pass


class TMe(APIModel):
    id: str
    name: str


@bp.item("/me", out=TMe)
async def profile():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Staff)
    return {"item": merchant}


class TStaff(APIModel):
    id: str
    name: str


@bp.item("/staff", out=TStaff)
def get_staff():
    dal = Dal(db.session)
    staff = dal.first_or_404(Staff)
    return {"item": staff}


"""
_entities(...): [_Entity]
_service: _Service
address(...): Address
addressCreate(...): AddressCreate
addressDelete(...): AddressDelete
addressSetDefault(...): AddressSetDefault
addressUpdate(...): AddressUpdate
addressValidationRules(...): AddressValidationData
app(...): App
appActivate(...): AppActivate
appCreate(...): AppCreate
appDeactivate(...): AppDeactivate
appDelete(...): AppDelete
appDeleteFailedInstallation(...): AppDeleteFailedInstallation
appFetchManifest(...): AppFetchManifest
appInstall(...): AppInstall
appRetryInstall(...): AppRetryInstall
appTokenCreate(...): AppTokenCreate
appTokenDelete(...): AppTokenDelete
appTokenVerify(...): AppTokenVerify
appUpdate(...): AppUpdate
apps(...): AppCountableConnection
appsInstallations: [AppInstallation!]!
assignNavigation(...): AssignNavigation
assignWarehouseShippingZone(...): WarehouseShippingZoneAssign
attribute(...): Attribute
attributeBulkDelete(...): AttributeBulkDelete
attributeCreate(...): AttributeCreate
attributeDelete(...): AttributeDelete
attributeReorderValues(...): AttributeReorderValues
attributeTranslate(...): AttributeTranslate
attributeUpdate(...): AttributeUpdate
attributeValueBulkDelete(...): AttributeValueBulkDelete
attributeValueCreate(...): AttributeValueCreate
attributeValueDelete(...): AttributeValueDelete
attributeValueTranslate(...): AttributeValueTranslate
attributeValueUpdate(...): AttributeValueUpdate
attributes(...): AttributeCountableConnection
channel(...): Channel
channelActivate(...): ChannelActivate
channelCreate(...): ChannelCreate
channelDeactivate(...): ChannelDeactivate
channelDelete(...): ChannelDelete
channelUpdate(...): ChannelUpdate
channels: [Channel!]
confirmAccount(...): ConfirmAccount
confirmEmailChange(...): ConfirmEmailChange
createWarehouse(...): WarehouseCreate
customerBulkDelete(...): CustomerBulkDelete
customerCreate(...): CustomerCreate
customerDelete(...): CustomerDelete
customerUpdate(...): CustomerUpdate
customers(...): UserCountableConnection
deleteMetadata(...): DeleteMetadata
deletePrivateMetadata(...): DeletePrivateMetadata
deleteWarehouse(...): WarehouseDelete
digitalContent(...): DigitalContent
digitalContentCreate(...): DigitalContentCreate
digitalContentDelete(...): DigitalContentDelete
digitalContentUpdate(...): DigitalContentUpdate
digitalContentUrlCreate(...): DigitalContentUrlCreate
digitalContents(...): DigitalContentCountableConnection
draftOrderBulkDelete(...): DraftOrderBulkDelete
draftOrderComplete(...): DraftOrderComplete
draftOrderCreate(...): DraftOrderCreate
draftOrderDelete(...): DraftOrderDelete
draftOrderLinesBulkDelete(...): DraftOrderLinesBulkDelete
draftOrderUpdate(...): DraftOrderUpdate
draftOrders(...): OrderCountableConnection
exportFile(...): ExportFile
exportFiles(...): ExportFileCountableConnection
exportProducts(...): ExportProducts
externalAuthenticationUrl(...): ExternalAuthenticationUrl
externalLogout(...): ExternalLogout
externalObtainAccessTokens(...): ExternalObtainAccessTokens
externalRefresh(...): ExternalRefresh
externalVerify(...): ExternalVerify
fileUpload(...): FileUpload
giftCard(...): GiftCard
giftCardActivate(...): GiftCardActivate
giftCardCreate(...): GiftCardCreate
giftCardDeactivate(...): GiftCardDeactivate
giftCardUpdate(...): GiftCardUpdate
giftCards(...): GiftCardCountableConnection
homepageEvents(...): OrderEventCountableConnection
invoiceCreate(...): InvoiceCreate
invoiceDelete(...): InvoiceDelete
invoiceRequest(...): InvoiceRequest
invoiceRequestDelete(...): InvoiceRequestDelete
invoiceSendNotification(...): InvoiceSendNotification
invoiceUpdate(...): InvoiceUpdate
menu(...): Menu
menuBulkDelete(...): MenuBulkDelete
menuCreate(...): MenuCreate
menuDelete(...): MenuDelete
menuItem(...): MenuItem
menuItemBulkDelete(...): MenuItemBulkDelete
menuItemCreate(...): MenuItemCreate
menuItemDelete(...): MenuItemDelete
menuItemMove(...): MenuItemMove
menuItemTranslate(...): MenuItemTranslate
menuItemUpdate(...): MenuItemUpdate
menuItems(...): MenuItemCountableConnection
menuUpdate(...): MenuUpdate
menus(...): MenuCountableConnection
order(...): Order
orderAddNote(...): OrderAddNote
orderBulkCancel(...): OrderBulkCancel
orderByToken(...): Order
orderCancel(...): OrderCancel
orderCapture(...): OrderCapture
orderConfirm(...): OrderConfirm
orderDiscountAdd(...): OrderDiscountAdd
orderDiscountDelete(...): OrderDiscountDelete
orderDiscountUpdate(...): OrderDiscountUpdate
orderFulfill(...): OrderFulfill
orderFulfillmentCancel(...): FulfillmentCancel
orderFulfillmentRefundProducts(...): FulfillmentRefundProducts
orderFulfillmentReturnProducts(...): FulfillmentReturnProducts
orderFulfillmentUpdateTracking(...): FulfillmentUpdateTracking
orderLineDelete(...): OrderLineDelete
orderLineDiscountRemove(...): OrderLineDiscountRemove
orderLineDiscountUpdate(...): OrderLineDiscountUpdate
orderLineUpdate(...): OrderLineUpdate
orderLinesCreate(...): OrderLinesCreate
orderMarkAsPaid(...): OrderMarkAsPaid
orderRefund(...): OrderRefund
orderSettings: OrderSettings
orderSettingsUpdate(...): OrderSettingsUpdate
orderUpdate(...): OrderUpdate
orderUpdateShipping(...): OrderUpdateShipping
orderVoid(...): OrderVoid
orders(...): OrderCountableConnection
ordersTotal(...): TaxedMoney
page(...): Page
pageAttributeAssign(...): PageAttributeAssign
pageAttributeUnassign(...): PageAttributeUnassign
pageBulkDelete(...): PageBulkDelete
pageBulkPublish(...): PageBulkPublish
pageCreate(...): PageCreate
pageDelete(...): PageDelete
pageReorderAttributeValues(...): PageReorderAttributeValues
pageTranslate(...): PageTranslate
pageType(...): PageType
pageTypeBulkDelete(...): PageTypeBulkDelete
pageTypeCreate(...): PageTypeCreate
pageTypeDelete(...): PageTypeDelete
pageTypeReorderAttributes(...): PageTypeReorderAttributes
pageTypeUpdate(...): PageTypeUpdate
pageTypes(...): PageTypeCountableConnection
pageUpdate(...): PageUpdate
pages(...): PageCountableConnection
passwordChange(...): PasswordChange
payment(...): Payment
paymentCapture(...): PaymentCapture
paymentInitialize(...): PaymentInitialize
paymentRefund(...): PaymentRefund
paymentVoid(...): PaymentVoid
payments(...): PaymentCountableConnection
permissionGroup(...): Group
permissionGroupCreate(...): PermissionGroupCreate
permissionGroupDelete(...): PermissionGroupDelete
permissionGroupUpdate(...): PermissionGroupUpdate
permissionGroups(...): GroupCountableConnection
plugin(...): Plugin
pluginUpdate(...): PluginUpdate
plugins(...): PluginCountableConnection
reportProductSales(...): ProductVariantCountableConnection
requestEmailChange(...): RequestEmailChange
requestPasswordReset(...): RequestPasswordReset
sale(...): Sale
saleBulkDelete(...): SaleBulkDelete
saleCataloguesAdd(...): SaleAddCatalogues
saleCataloguesRemove(...): SaleRemoveCatalogues
saleChannelListingUpdate(...): SaleChannelListingUpdate
saleCreate(...): SaleCreate
saleDelete(...): SaleDelete
saleTranslate(...): SaleTranslate
saleUpdate(...): SaleUpdate
sales(...): SaleCountableConnection
setPassword(...): SetPassword
shippingMethodChannelListingUpdate(...): ShippingMethodChannelListingUpdate
shippingPriceBulkDelete(...): ShippingPriceBulkDelete
shippingPriceCreate(...): ShippingPriceCreate
shippingPriceDelete(...): ShippingPriceDelete
shippingPriceExcludeProducts(...): ShippingPriceExcludeProducts
shippingPriceRemoveProductFromExclude(...): ShippingPriceRemoveProductFromExclude
shippingPriceTranslate(...): ShippingPriceTranslate
shippingPriceUpdate(...): ShippingPriceUpdate
shippingZone(...): ShippingZone
shippingZoneBulkDelete(...): ShippingZoneBulkDelete
shippingZoneCreate(...): ShippingZoneCreate
shippingZoneDelete(...): ShippingZoneDelete
shippingZoneUpdate(...): ShippingZoneUpdate
shippingZones(...): ShippingZoneCountableConnection
shop: Shop!
shopAddressUpdate(...): ShopAddressUpdate
shopDomainUpdate(...): ShopDomainUpdate
shopFetchTaxRates: ShopFetchTaxRates
shopSettingsTranslate(...): ShopSettingsTranslate
shopSettingsUpdate(...): ShopSettingsUpdate
stock(...): Stock
stocks(...): StockCountableConnection
taxTypes: [TaxType]
tokenCreate(...): CreateToken
tokenRefresh(...): RefreshToken
tokenVerify(...): VerifyToken
tokensDeactivateAll: DeactivateAllUserTokens
translation(...): TranslatableItem
translations(...): TranslatableItemConnection
unassignWarehouseShippingZone(...): WarehouseShippingZoneUnassign
updateMetadata(...): UpdateMetadata
updatePrivateMetadata(...): UpdatePrivateMetadata
updateWarehouse(...): WarehouseUpdate
user(...): User
userAvatarDelete: UserAvatarDelete
userAvatarUpdate(...): UserAvatarUpdate
userBulkSetActive(...): UserBulkSetActive
variantMediaAssign(...): VariantMediaAssign
variantMediaUnassign(...): VariantMediaUnassign
voucher(...): Voucher
voucherBulkDelete(...): VoucherBulkDelete
voucherCataloguesAdd(...): VoucherAddCatalogues
voucherCataloguesRemove(...): VoucherRemoveCatalogues
voucherChannelListingUpdate(...): VoucherChannelListingUpdate
voucherCreate(...): VoucherCreate
voucherDelete(...): VoucherDelete
voucherTranslate(...): VoucherTranslate
voucherUpdate(...): VoucherUpdate
vouchers(...): VoucherCountableConnection
warehouse(...): Warehouse
warehouses(...): WarehouseCountableConnection
webhook(...): Webhook
webhookCreate(...): WebhookCreate
webhookDelete(...): WebhookDelete
webhookEvents: [WebhookEvent]
webhookSamplePayload(...): JSONString
webhookUpdate(...): WebhookUpdate
"""
