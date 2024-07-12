# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType

if typing.TYPE_CHECKING:
    from .change import Change
    from .common import KeyReference, Reference, ResourceIdentifier
    from .label import Label

__all__ = [
    "ChangeHistoryResourceType",
    "DateStringFilter",
    "ErrorObject",
    "ErrorResponse",
    "ModifiedBy",
    "PlatformInitiatedChange",
    "Record",
    "RecordPagedQueryResponse",
    "Source",
    "UpdateType",
]


class Record(_BaseType):
    """Captures the differences between the previous and next version of a resource.

    The maximum number of Records that can be stored and their retention period are subject to a [limit](/../api/limits#records).

    """

    #: Version of the resource after the change.
    #:
    #: For more information on how the version is incremented, see [Optimistic Concurrency Control](/../api/general-concepts#optimistic-concurrency-control).
    version: int
    #: Version of the resource before the change.
    previous_version: int
    #: Indicates the type of change.
    #: For creation, update, or deletion, the value is `"ResourceCreated"`, `"ResourceUpdated"`, or `"ResourceDeleted"` respectively.
    type: str
    #: Information about the user or API Client who performed the change.
    modified_by: "ModifiedBy"
    #: Date and time (UTC) the change was made.
    modified_at: str
    #: Information that describes the resource after the change.
    label: "Label"
    #: Information that describes the resource before the change.
    previous_label: "Label"
    #: Shows the differences in the resource between `previousVersion` and `version`.
    #:
    #: The value is not identical to the actual array of update actions sent and is not limited to update actions (see, for example, [Optimistic  Concurrency Control](/general-concepts#optimistic-concurrency-control)).
    changes: typing.List["Change"]
    #: ResourceIdentifier of the changed resource.
    resource: "ResourceIdentifier"
    #: References to the [Stores](ctp:api:type:Store) associated with the [Change](ctp:history:type:Change).
    stores: typing.List["KeyReference"]
    #: Reference to the [Business Unit](ctp:api:type:BusinessUnit) associated with the [Change](ctp:history:type:Change).
    business_unit: typing.Optional["KeyReference"]
    #: `true` if no change was detected.
    #:
    #: The version number of the resource can be increased even without any change in the resource.
    without_changes: bool

    def __init__(
        self,
        *,
        version: int,
        previous_version: int,
        type: str,
        modified_by: "ModifiedBy",
        modified_at: str,
        label: "Label",
        previous_label: "Label",
        changes: typing.List["Change"],
        resource: "ResourceIdentifier",
        stores: typing.List["KeyReference"],
        business_unit: typing.Optional["KeyReference"] = None,
        without_changes: bool
    ):
        self.version = version
        self.previous_version = previous_version
        self.type = type
        self.modified_by = modified_by
        self.modified_at = modified_at
        self.label = label
        self.previous_label = previous_label
        self.changes = changes
        self.resource = resource
        self.stores = stores
        self.business_unit = business_unit
        self.without_changes = without_changes

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Record":
        from ._schemas.change_history import RecordSchema

        return RecordSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.change_history import RecordSchema

        return RecordSchema().dump(self)


class RecordPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with `results` containing an array of [Record](ctp:history:type:Record)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation and not [strongly consistent](/../api/general-concepts#strong-consistency).
    total: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Records matching the query.
    results: typing.List["Record"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        total: int,
        offset: int,
        results: typing.List["Record"]
    ):
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "RecordPagedQueryResponse":
        from ._schemas.change_history import RecordPagedQueryResponseSchema

        return RecordPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.change_history import RecordPagedQueryResponseSchema

        return RecordPagedQueryResponseSchema().dump(self)


class ChangeHistoryResourceType(enum.Enum):
    """This data type represents the supported resource types.
    The value must be one of the following:

    """

    ASSOCIATE_ROLE = "associate-role"
    BUSINESS_UNIT = "business-unit"
    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    DISCOUNT_CODE = "discount-code"
    INVENTORY_ENTRY = "inventory-entry"
    KEY_VALUE_DOCUMENT = "key-value-document"
    ORDER = "order"
    PAYMENT = "payment"
    PRODUCT = "product"
    PRODUCT_DISCOUNT = "product-discount"
    PRODUCT_SELECTION = "product-selection"
    PRODUCT_TYPE = "product-type"
    QUOTE_REQUEST = "quote-request"
    QUOTE = "quote"
    REVIEW = "review"
    SHOPPING_LIST = "shopping-list"
    STAGED_QUOTE = "staged-quote"
    STATE = "state"
    STORE = "store"
    TAX_CATEGORY = "tax-category"
    TYPE = "type"
    ZONE = "zone"


class DateStringFilter(enum.Enum):
    """This type consists of one enum value:"""

    NOW = "now"


class ErrorObject(_BaseType):
    code: str
    message: str

    def __init__(self, *, code: str, message: str):
        self.code = code
        self.message = message

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorObject":
        from ._schemas.change_history import ErrorObjectSchema

        return ErrorObjectSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.change_history import ErrorObjectSchema

        return ErrorObjectSchema().dump(self)


class ErrorResponse(_BaseType):
    status_code: int
    message: str
    error: typing.Optional[str]
    error_description: typing.Optional[str]
    errors: typing.Optional[typing.List["ErrorObject"]]

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        errors: typing.Optional[typing.List["ErrorObject"]] = None
    ):
        self.status_code = status_code
        self.message = message
        self.error = error
        self.error_description = error_description
        self.errors = errors

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorResponse":
        from ._schemas.change_history import ErrorResponseSchema

        return ErrorResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.change_history import ErrorResponseSchema

        return ErrorResponseSchema().dump(self)


class ModifiedBy(_BaseType):
    """Information about the user or API Client who performed the change. This is a variant of [LastModifiedBy](ctp:api:type:LastModifiedBy)."""

    #: [ID](/general-concepts#identifier) of the Merchant Center user who made the change.
    #:
    #: Present only if the change was made in the Merchant Center.
    id: str
    #: Indicates who performed the change.
    #:
    #: - If the change was made by a user, the value is `"user"`.
    #: - If the change was made by an API Client with or without an [external user ID](/general-concepts#external-user-ids), the value is `"external-user"`.
    #: - If the change was made by an [Associate](ctp:api:type:Associate), the value is `"associate"`.
    type: str
    #: [ID](/general-concepts#identifier) of the [API Client](ctp:api:type:ApiClient) that made the change.
    #:
    #: Present only if the change was made using an API Client.
    client_id: typing.Optional[str]
    #: Present only if the change was made using a token from an [anonymous session](/authorization#tokens-for-anonymous-sessions).
    anonymous_id: typing.Optional[str]
    #: The [Customer](ctp:api:type:Customer) who made the change.
    #:
    #: Present only if the change was made using a token from the [password flow](/authorization#password-flow).
    customer: typing.Optional["Reference"]
    #: The [Associate](ctp:api:type:Associate) who made the change in the context of a [Business Unit](ctp:api:type:BusinessUnit). Present only if the Associate acts on behalf of a company using the [associate endpoints](/associates-overview#on-the-associate-endpoints).
    associate: typing.Optional["Reference"]
    #: `true` if the change was made using the Merchant Center or [ImpEx](https://impex.europe-west1.gcp.commercetools.com/).
    is_platform_client: bool

    def __init__(
        self,
        *,
        id: str,
        type: str,
        client_id: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None,
        customer: typing.Optional["Reference"] = None,
        associate: typing.Optional["Reference"] = None,
        is_platform_client: bool
    ):
        self.id = id
        self.type = type
        self.client_id = client_id
        self.anonymous_id = anonymous_id
        self.customer = customer
        self.associate = associate
        self.is_platform_client = is_platform_client

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ModifiedBy":
        from ._schemas.change_history import ModifiedBySchema

        return ModifiedBySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.change_history import ModifiedBySchema

        return ModifiedBySchema().dump(self)


class PlatformInitiatedChange(enum.Enum):
    """Updates that are triggered automatically as a result of a user-initiated change."""

    EXCLUDE_ALL = "excludeAll"
    CHANGE_LINE_ITEM_NAME = "changeLineItemName"
    CHANGE_REVIEW_RATING_STATISTICS = "changeReviewRatingStatistics"
    SET_APPLICATION_VERSION = "setApplicationVersion"
    SET_IS_VALID = "setIsValid"
    SET_VARIANT_AVAILABILITY = "setVariantAvailability"


class Source(enum.Enum):
    """Values for the Source enumeration."""

    MERCHANT_CENTER = "MerchantCenter"
    IMP_EX = "ImpEx"
    API_CLIENT = "ApiClient"


class UpdateType(enum.Enum):
    ADD_ADDRESS = "addAddress"
    ADD_ASSET = "addAsset"
    ADD_ASSOCIATE = "addAssociate"
    ADD_ATTRIBUTE_DEFINITION = "addAttributeDefinition"
    ADD_BILLING_ADDRESS_ID = "addBillingAddressId"
    ADD_CUSTOM_LINE_ITEM = "addCustomLineItem"
    ADD_DELIVERY = "addDelivery"
    ADD_DISCOUNT_CODE = "addDiscountCode"
    ADD_ENUM_VALUE = "addEnumValue"
    ADD_EXTERNAL_IMAGE = "addExternalImage"
    ADD_FIELD_DEFINITION = "addFieldDefinition"
    ADD_INTERFACE_INTERACTION = "addInterfaceInteraction"
    ADD_ITEM_SHIPPING_ADDRESS = "addItemShippingAddress"
    ADD_LINE_ITEM = "addLineItem"
    ADD_LOCALIZED_ENUM_VALUE = "addLocalizedEnumValue"
    ADD_LOCATION = "addLocation"
    ADD_PARCEL_TO_DELIVERY = "addParcelToDelivery"
    ADD_PAYMENT = "addPayment"
    ADD_PLAIN_ENUM_VALUE = "addPlainEnumValue"
    ADD_PRICE = "addPrice"
    ADD_PRODUCT = "addProduct"
    ADD_PRODUCT_SELECTION = "addProductSelection"
    ADD_PROPERTY = "addProperty"
    ADD_RETURN_INFO = "addReturnInfo"
    ADD_ROLES = "addRoles"
    ADD_SHIPPING_ADDRESS_ID = "addShippingAddressId"
    ADD_TAX_RATE = "addTaxRate"
    ADD_TEXT_LINE_ITEM = "addTextLineItem"
    ADD_TO_CATEGORY = "addToCategory"
    ADD_TRANSACTION = "addTransaction"
    ADD_VARIANT = "addVariant"
    CHANGE_ADDRESS = "changeAddress"
    CHANGE_AMOUNT_AUTHORIZED = "changeAmountAuthorized"
    CHANGE_AMOUNT_PLANNED = "changeAmountPlanned"
    CHANGE_ASSET_NAME = "changeAssetName"
    CHANGE_ASSET_ORDER = "changeAssetOrder"
    CHANGE_ASSOCIATE = "changeAssociate"
    CHANGE_ASSOCIATE_MODE = "changeAssociateMode"
    CHANGE_ATTRIBUTE_CONSTRAINT = "changeAttributeConstraint"
    CHANGE_ATTRIBUTE_NAME = "changeAttributeName"
    CHANGE_ATTRIBUTE_ORDER_BY_NAME = "changeAttributeOrderByName"
    CHANGE_CART_DISCOUNTS = "changeCartDiscounts"
    CHANGE_CART_PREDICATE = "changeCartPredicate"
    CHANGE_CUSTOM_LINE_ITEM_QUANTITY = "changeCustomLineItemQuantity"
    CHANGE_DESCRIPTION = "changeDescription"
    CHANGE_EMAIL = "changeEmail"
    CHANGE_ENUM_KEY = "changeEnumKey"
    CHANGE_ENUM_VALUE_LABEL = "changeEnumValueLabel"
    CHANGE_ENUM_VALUE_ORDER = "changeEnumValueOrder"
    CHANGE_FIELD_DEFINITION_ORDER = "changeFieldDefinitionOrder"
    CHANGE_GROUPS = "changeGroups"
    CHANGE_INITIAL = "changeInitial"
    CHANGE_INPUT_HINT = "changeInputHint"
    CHANGE_IS_ACTIVE = "changeIsActive"
    CHANGE_IS_SEARCHABLE = "changeIsSearchable"
    CHANGE_KEY = "changeKey"
    CHANGE_LABEL = "changeLabel"
    CHANGE_LINE_ITEM_NAME = "changeLineItemName"
    CHANGE_LINE_ITEM_QUANTITY = "changeLineItemQuantity"
    CHANGE_LINE_ITEMS_ORDER = "changeLineItemsOrder"
    CHANGE_LOCALIZED_ENUM_VALUE_LABEL = "changeLocalizedEnumValueLabel"
    CHANGE_LOCALIZED_ENUM_VALUE_ORDER = "changeLocalizedEnumValueOrder"
    CHANGE_MASTER_VARIANT = "changeMasterVariant"
    CHANGE_NAME = "changeName"
    CHANGE_ORDER_HINT = "changeOrderHint"
    CHANGE_ORDER_STATE = "changeOrderState"
    CHANGE_PARENT = "changeParent"
    CHANGE_PARENT_UNIT = "changeParentUnit"
    CHANGE_PAYMENT_STATE = "changePaymentState"
    CHANGE_PLAIN_ENUM_VALUE_LABEL = "changePlainEnumValueLabel"
    CHANGE_PREDICATE = "changePredicate"
    CHANGE_PRICE = "changePrice"
    CHANGE_PRODUCT_SELECTION_ACTIVE = "changeProductSelectionActive"
    CHANGE_QUANTITY = "changeQuantity"
    CHANGE_QUOTE_REQUEST_STATE = "changeQuoteRequestState"
    CHANGE_QUOTE_STATE = "changeQuoteState"
    CHANGE_REQUIRES_DISCOUNT_CODE = "changeRequiresDiscountCode"
    CHANGE_REVIEW_RATING_STATISTICS = "changeReviewRatingStatistics"
    CHANGE_SHIPMENT_STATE = "changeShipmentState"
    CHANGE_SLUG = "changeSlug"
    CHANGE_SORT_ORDER = "changeSortOrder"
    CHANGE_STACKING_MODE = "changeStackingMode"
    CHANGE_STAGED_QUOTE_STATE = "changeStagedQuoteState"
    CHANGE_STATUS = "changeStatus"
    CHANGE_TARGET = "changeTarget"
    CHANGE_TAX_CALCULATION_MODE = "changeTaxCalculationMode"
    CHANGE_TAX_MODE = "changeTaxMode"
    CHANGE_TAX_ROUNDING_MODE = "changeTaxRoundingMode"
    CHANGE_TEXT_LINE_ITEM_NAME = "changeTextLineItemName"
    CHANGE_TEXT_LINE_ITEM_QUANTITY = "changeTextLineItemQuantity"
    CHANGE_TEXT_LINE_ITEMS_ORDER = "changeTextLineItemsOrder"
    CHANGE_TRANSACTION_INTERACTION_ID = "changeTransactionInteractionId"
    CHANGE_TRANSACTION_STATE = "changeTransactionState"
    CHANGE_TRANSACTION_TIMESTAMP = "changeTransactionTimestamp"
    CHANGE_TYPE = "changeType"
    CHANGE_VALUE = "changeValue"
    MOVE_IMAGE_TO_POSITION = "moveImageToPosition"
    PUBLISH = "publish"
    REMOVE_ADDRESS = "removeAddress"
    REMOVE_ASSET = "removeAsset"
    REMOVE_ASSOCIATE = "removeAssociate"
    REMOVE_ATTRIBUTE_DEFINITION = "removeAttributeDefinition"
    REMOVE_BILLING_ADDRESS_ID = "removeBillingAddressId"
    REMOVE_CUSTOM_LINE_ITEM = "removeCustomLineItem"
    REMOVE_DELIVERY = "removeDelivery"
    REMOVE_DISCOUNT_CODE = "removeDiscountCode"
    REMOVE_ENUM_VALUES = "removeEnumValues"
    REMOVE_FIELD_DEFINITION = "removeFieldDefinition"
    REMOVE_FROM_CATEGORY = "removeFromCategory"
    REMOVE_IMAGE = "removeImage"
    REMOVE_ITEM_SHIPPING_ADDRESS = "removeItemShippingAddress"
    REMOVE_LINE_ITEM = "removeLineItem"
    REMOVE_LOCATION = "removeLocation"
    REMOVE_PARCEL_FROM_DELIVERY = "removeParcelFromDelivery"
    REMOVE_PAYMENT = "removePayment"
    REMOVE_PRICE = "removePrice"
    REMOVE_PRODUCT = "removeProduct"
    REMOVE_PRODUCT_SELECTION = "removeProductSelection"
    REMOVE_PROPERTY = "removeProperty"
    REMOVE_ROLES = "removeRoles"
    REMOVE_SHIPPING_ADDRESS_ID = "removeShippingAddressId"
    REMOVE_TAX_RATE = "removeTaxRate"
    REMOVE_TEXT_LINE_ITEM = "removeTextLineItem"
    REMOVE_VARIANT = "removeVariant"
    REQUEST_QUOTE_RENEGOTIATION = "requestQuoteRenegotiation"
    SET_ADDRESS = "setAddress"
    SET_ADDRESS_CUSTOM_FIELD = "setAddressCustomField"
    SET_ADDRESS_CUSTOM_TYPE = "setAddressCustomType"
    SET_ANONYMOUS_ID = "setAnonymousId"
    SET_APPLICATION_VERSION = "setApplicationVersion"
    SET_ASSET_CUSTOM_FIELD = "setAssetCustomField"
    SET_ASSET_CUSTOM_TYPE = "setAssetCustomType"
    SET_ASSET_DESCRIPTION = "setAssetDescription"
    SET_ASSET_SOURCES = "setAssetSources"
    SET_ASSET_TAGS = "setAssetTags"
    SET_ASSSET_KEY = "setAsssetKey"
    SET_ATTRIBUTE = "setAttribute"
    SET_AUTHENTICATION_MODE = "setAuthenticationMode"
    SET_AUTHOR_NAME = "setAuthorName"
    SET_BILLING_ADDRESS = "setBillingAddress"
    SET_CART_PREDICATE = "setCartPredicate"
    SET_CATEGORY_ORDER_HINT = "setCategoryOrderHint"
    SET_COMPANY_NAME = "setCompanyName"
    SET_CONTACT_EMAIL = "setContactEmail"
    SET_COUNTRIES = "setCountries"
    SET_COUNTRY = "setCountry"
    SET_CUSTOM_FIELD = "setCustomField"
    SET_CUSTOM_LINE_ITEM_CUSTOM_FIELD = "setCustomLineItemCustomField"
    SET_CUSTOM_LINE_ITEM_CUSTOM_TYPE = "setCustomLineItemCustomType"
    SET_CUSTOM_LINE_ITEM_MONEY = "setCustomLineItemMoney"
    SET_CUSTOM_LINE_ITEM_SHIPPING_DETAILS = "setCustomLineItemShippingDetails"
    SET_CUSTOM_LINE_ITEM_TAX_AMOUNT = "setCustomLineItemTaxAmount"
    SET_CUSTOM_LINE_ITEM_TAX_CATEGORY = "setCustomLineItemTaxCategory"
    SET_CUSTOM_LINE_ITEM_TAX_RATE = "setCustomLineItemTaxRate"
    SET_CUSTOM_LINE_ITEM_TAXED_PRICE = "setCustomLineItemTaxedPrice"
    SET_CUSTOM_LINE_ITEM_TOTAL_PRICE = "setCustomLineItemTotalPrice"
    SET_CUSTOM_SHIPPING_METHOD = "setCustomShippingMethod"
    SET_CUSTOM_TYPE = "setCustomType"
    SET_CUSTOMER = "setCustomer"
    SET_CUSTOMER_EMAIL = "setCustomerEmail"
    SET_CUSTOMER_GROUP = "setCustomerGroup"
    SET_CUSTOMER_ID = "setCustomerId"
    SET_CUSTOMER_NUMBER = "setCustomerNumber"
    SET_DATE_OF_BIRTH = "setDateOfBirth"
    SET_DEFAULT_BILLING_ADDRESS = "setDefaultBillingAddress"
    SET_DEFAULT_SHIPPING_ADDRESS = "setDefaultShippingAddress"
    SET_DELETE_DAYS_AFTER_LAST_MODIFICATION = "setDeleteDaysAfterLastModification"
    SET_DELIVERY_ADDRESS = "setDeliveryAddress"
    SET_DELIVERY_ITEMS = "setDeliveryItems"
    SET_DESCRIPTION = "setDescription"
    SET_DISCOUNTED_PRICE = "setDiscountedPrice"
    SET_DISTRIBUTION_CHANNELS = "setDistributionChannels"
    SET_EXPECTED_DELIVERY = "setExpectedDelivery"
    SET_EXTERNAL_ID = "setExternalId"
    SET_FIRST_NAME = "setFirstName"
    SET_GEO_LOCATION = "setGeoLocation"
    SET_IMAGE_LABEL = "setImageLabel"
    SET_INPUT_TIP = "setInputTip"
    SET_INTERFACE_ID = "setInterfaceId"
    SET_IS_VALID = "setIsValid"
    SET_KEY = "setKey"
    SET_LANGUAGES = "setLanguages"
    SET_LAST_NAME = "setLastName"
    SET_LINE_ITEM_CUSTOM_FIELD = "setLineItemCustomField"
    SET_LINE_ITEM_CUSTOM_TYPE = "setLineItemCustomType"
    SET_LINE_ITEM_DEACTIVATED_AT = "setLineItemDeactivatedAt"
    SET_LINE_ITEM_DISCOUNTED_PRICE = "setLineItemDiscountedPrice"
    SET_LINE_ITEM_DISCOUNTED_PRICE_PER_QUANTITY = (
        "setLineItemDiscountedPricePerQuantity"
    )
    SET_LINE_ITEM_DISTRIBUTION_CHANNEL = "setLineItemDistributionChannel"
    SET_LINE_ITEM_PRICE = "setLineItemPrice"
    SET_LINE_ITEM_PRODUCT_KEY = "setLineItemProductKey"
    SET_LINE_ITEM_PRODUCT_SLUG = "setLineItemProductSlug"
    SET_LINE_ITEM_SHIPPING_DETAILS = "setLineItemShippingDetails"
    SET_LINE_ITEM_TAX_AMOUNT = "setLineItemTaxAmount"
    SET_LINE_ITEM_TAX_RATE = "setLineItemTaxRate"
    SET_LINE_ITEM_TAXED_PRICE = "setLineItemTaxedPrice"
    SET_LINE_ITEM_TOTAL_PRICE = "setLineItemTotalPrice"
    SET_LOCALE = "setLocale"
    SET_MAX_APPLICATIONS = "setMaxApplications"
    SET_MAX_APPLICATIONS_PER_CUSTOMER = "setMaxApplicationsPerCustomer"
    SET_META_DESCRIPTION = "setMetaDescription"
    SET_META_KEYWORDS = "setMetaKeywords"
    SET_META_TITLE = "setMetaTitle"
    SET_METHOD_INFO_INTERFACE = "setMethodInfoInterface"
    SET_METHOD_INFO_METHOD = "setMethodInfoMethod"
    SET_METHOD_INFO_NAME = "setMethodInfoName"
    SET_MIDDLE_NAME = "setMiddleName"
    SET_NAME = "setName"
    SET_ORDER_NUMBER = "setOrderNumber"
    SET_ORDER_TAXED_PRICE = "setOrderTaxedPrice"
    SET_ORDER_TOTAL_PRICE = "setOrderTotalPrice"
    SET_ORDER_TOTAL_TAX = "setOrderTotalTax"
    SET_PARCEL_ITEMS = "setParcelItems"
    SET_PARCEL_MEASUREMENTS = "setParcelMeasurements"
    SET_PARCEL_TRACKING_DATA = "setParcelTrackingData"
    SET_PASSWORD = "setPassword"
    SET_PRICES = "setPrices"
    SET_PRODUCT_COUNT = "setProductCount"
    SET_PRODUCT_PRICE_CUSTOM_FIELD = "setProductPriceCustomField"
    SET_PRODUCT_PRICE_CUSTOM_TYPE = "setProductPriceCustomType"
    SET_PRODUCT_SELECTIONS = "setProductSelections"
    SET_PRODUCT_VARIANT_KEY = "setProductVariantKey"
    SET_PROPERTY = "setProperty"
    SET_PURCHASE_ORDER_NUMBER = "setPurchaseOrderNumber"
    SET_RATING = "setRating"
    SET_RESERVATIONS = "setReservations"
    SET_RESTOCKABLE_IN_DAYS = "setRestockableInDays"
    SET_RETURN_PAYMENT_STATE = "setReturnPaymentState"
    SET_RETURN_SHIPMENT_STATE = "setReturnShipmentState"
    SET_ROLES = "setRoles"
    SET_SALUTATION = "setSalutation"
    SET_SEARCH_KEYWORDS = "setSearchKeywords"
    SET_SELLER_COMMENT = "setSellerComment"
    SET_SHIPPING_ADDRESS = "setShippingAddress"
    SET_SHIPPING_INFO_PRICE = "setShippingInfoPrice"
    SET_SHIPPING_INFO_TAXED_PRICE = "setShippingInfoTaxedPrice"
    SET_SHIPPING_METHOD = "setShippingMethod"
    SET_SHIPPING_METHOD_TAX_AMOUNT = "setShippingMethodTaxAmount"
    SET_SHIPPING_METHOD_TAX_RATE = "setShippingMethodTaxRate"
    SET_SHIPPING_RATE = "setShippingRate"
    SET_SHIPPING_RATE_INPUT = "setShippingRateInput"
    SET_SKU = "setSku"
    SET_SLUG = "setSlug"
    SET_STATUS_INTERFACE_CODE = "setStatusInterfaceCode"
    SET_STATUS_INTERFACE_TEXT = "setStatusInterfaceText"
    SET_STORE = "setStore"
    SET_STORE_MODE = "setStoreMode"
    SET_STORES = "setStores"
    SET_SUPPLY_CHANNEL = "setSupplyChannel"
    SET_SUPPLY_CHANNELS = "setSupplyChannels"
    SET_TARGET = "setTarget"
    SET_TAX_CATEGORY = "setTaxCategory"
    SET_TEXT = "setText"
    SET_TEXT_LINE_ITEM_CUSTOM_FIELD = "setTextLineItemCustomField"
    SET_TEXT_LINE_ITEM_CUSTOM_TYPE = "setTextLineItemCustomType"
    SET_TEXT_LINE_ITEM_DESCRIPTION = "setTextLineItemDescription"
    SET_TITLE = "setTitle"
    SET_TRANSITIONS = "setTransitions"
    SET_VALID_FROM = "setValidFrom"
    SET_VALID_FROM_AND_UNTIL = "setValidFromAndUntil"
    SET_VALID_TO = "setValidTo"
    SET_VALID_UNTIL = "setValidUntil"
    SET_VALUE = "setValue"
    SET_VARIANT_AVAILABILITY = "setVariantAvailability"
    SET_VARIANT_SELECTION = "setVariantSelection"
    SET_VAT_ID = "setVatId"
    TRANSITION_CUSTOM_LINE_ITEM_STATE = "transitionCustomLineItemState"
    TRANSITION_LINE_ITEM_STATE = "transitionLineItemState"
    TRANSITION_STATE = "transitionState"
    UNPUBLISH = "unpublish"
    UPDATE_ITEM_SHIPPING_ADDRESS = "updateItemShippingAddress"
    UPDATE_SYNC_INFO = "updateSyncInfo"
    VERIFY_EMAIL = "verifyEmail"
