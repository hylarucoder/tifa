from tifa.contrib.fastapi_plus import create_bp

bp = create_bp()

from .app import *  # noqa
from .attribute import *  # noqa
from .channel import *  # noqa
from .collection import *  # noqa
from .discount import *  # noqa
from .gift_card import *  # noqa
from .invoice import *  # noqa
from .menu import *  # noqa
from .order import *  # noqa
from .page import *  # noqa
from .product import *  # noqa
from .product_media import *  # noqa
from .shipping import *  # noqa
from .staff import *  # noqa
from .warehouse import *  # noqa
from .webhook import *  # noqa

"""
assignNavigation(...): AssignNavigation
assignWarehouseShippingZone(...): WarehouseShippingZoneAssign
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
homepageEvents(...): OrderEventCountableConnection
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
shop: Shop!
shopAddressUpdate(...): ShopAddressUpdate
shopDomainUpdate(...): ShopDomainUpdate
shopFetchTaxRates: ShopFetchTaxRates
shopSettingsTranslate(...): ShopSettingsTranslate
shopSettingsUpdate(...): ShopSettingsUpdate
stock(...): Stock
stocks(...): StockCountableConnection
taxTypes: [TaxType]
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
"""
