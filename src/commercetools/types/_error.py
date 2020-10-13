# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType

if typing.TYPE_CHECKING:
    from ._channel import ChannelReference
    from ._common import LocalizedString, Price, PriceDraft, Reference, ReferenceTypeId
    from ._customer_group import CustomerGroupReference
    from ._product import Attribute
__all__ = [
    "AccessDeniedError",
    "ConcurrentModificationError",
    "DiscountCodeNonApplicableError",
    "DuplicateAttributeValueError",
    "DuplicateAttributeValuesError",
    "DuplicateFieldError",
    "DuplicateFieldWithConflictingResourceError",
    "DuplicatePriceScopeError",
    "DuplicateVariantValuesError",
    "EnumValueIsUsedError",
    "ErrorByExtension",
    "ErrorObject",
    "ErrorResponse",
    "ExtensionBadResponseError",
    "ExtensionNoResponseError",
    "ExtensionUpdateActionsFailedError",
    "InsufficientScopeError",
    "InvalidCredentialsError",
    "InvalidCurrentPasswordError",
    "InvalidFieldError",
    "InvalidInputError",
    "InvalidItemShippingDetailsError",
    "InvalidJsonInputError",
    "InvalidOperationError",
    "InvalidSubjectError",
    "InvalidTokenError",
    "LanguageUsedInStoresError",
    "MatchingPriceNotFoundError",
    "MissingTaxRateForCountryError",
    "NoMatchingProductDiscountFoundError",
    "OutOfStockError",
    "PriceChangedError",
    "ReferenceExistsError",
    "ReferencedResourceNotFoundError",
    "RequiredFieldError",
    "ResourceNotFoundError",
    "ShippingMethodDoesNotMatchCartError",
    "VariantValues",
]


class ErrorByExtension(_BaseType):
    #: :class:`str`
    id: str
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, id: str, key: typing.Optional[str] = None) -> None:
        self.id = id
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return "ErrorByExtension(id=%r, key=%r)" % (self.id, self.key)


class ErrorObject(_BaseType):
    #: :class:`str`
    code: str
    #: :class:`str`
    message: str

    def __init__(self, *, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__()

    def __repr__(self) -> str:
        return "ErrorObject(code=%r, message=%r)" % (self.code, self.message)


class ErrorResponse(_BaseType):
    #: :class:`int` `(Named` ``statusCode`` `in Commercetools)`
    status_code: int
    #: :class:`str`
    message: str
    #: Optional :class:`str`
    error: typing.Optional[str]
    #: Optional :class:`str`
    error_description: typing.Optional[str]
    #: Optional :class:`list`
    errors: typing.Optional[list]

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        errors: typing.Optional[list] = None
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.error = error
        self.error_description = error_description
        self.errors = errors
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ErrorResponse(status_code=%r, message=%r, error=%r, error_description=%r, errors=%r)"
            % (
                self.status_code,
                self.message,
                self.error,
                self.error_description,
                self.errors,
            )
        )


class VariantValues(_BaseType):
    #: Optional :class:`str`
    sku: typing.Optional[str]
    #: List of :class:`commercetools.types.PriceDraft`
    prices: typing.List["PriceDraft"]
    #: List of :class:`commercetools.types.Attribute`
    attributes: typing.List["Attribute"]

    def __init__(
        self,
        *,
        prices: typing.List["PriceDraft"],
        attributes: typing.List["Attribute"],
        sku: typing.Optional[str] = None
    ) -> None:
        self.sku = sku
        self.prices = prices
        self.attributes = attributes
        super().__init__()

    def __repr__(self) -> str:
        return "VariantValues(sku=%r, prices=%r, attributes=%r)" % (
            self.sku,
            self.prices,
            self.attributes,
        )


class AccessDeniedError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="access_denied", message=message)

    def __repr__(self) -> str:
        return "AccessDeniedError(code=%r, message=%r)" % (self.code, self.message)


class ConcurrentModificationError(ErrorObject):
    #: Optional :class:`int` `(Named` ``currentVersion`` `in Commercetools)`
    current_version: typing.Optional[int]

    def __init__(
        self, *, message: str, current_version: typing.Optional[int] = None
    ) -> None:
        self.current_version = current_version
        super().__init__(code="ConcurrentModification", message=message)

    def __repr__(self) -> str:
        return (
            "ConcurrentModificationError(code=%r, message=%r, current_version=%r)"
            % (self.code, self.message, self.current_version)
        )


class DiscountCodeNonApplicableError(ErrorObject):
    #: Optional :class:`str` `(Named` ``discountCode`` `in Commercetools)`
    discount_code: typing.Optional[str]
    #: Optional :class:`str`
    reason: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``dicountCodeId`` `in Commercetools)`
    dicount_code_id: typing.Optional[str]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validityCheckTime`` `in Commercetools)`
    validity_check_time: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        message: str,
        discount_code: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        dicount_code_id: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        validity_check_time: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.discount_code = discount_code
        self.reason = reason
        self.dicount_code_id = dicount_code_id
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.validity_check_time = validity_check_time
        super().__init__(code="DiscountCodeNonApplicable", message=message)

    def __repr__(self) -> str:
        return (
            "DiscountCodeNonApplicableError(code=%r, message=%r, discount_code=%r, reason=%r, dicount_code_id=%r, valid_from=%r, valid_until=%r, validity_check_time=%r)"
            % (
                self.code,
                self.message,
                self.discount_code,
                self.reason,
                self.dicount_code_id,
                self.valid_from,
                self.valid_until,
                self.validity_check_time,
            )
        )


class DuplicateAttributeValueError(ErrorObject):
    #: :class:`commercetools.types.Attribute`
    attribute: "Attribute"

    def __init__(self, *, message: str, attribute: "Attribute") -> None:
        self.attribute = attribute
        super().__init__(code="DuplicateAttributeValue", message=message)

    def __repr__(self) -> str:
        return "DuplicateAttributeValueError(code=%r, message=%r, attribute=%r)" % (
            self.code,
            self.message,
            self.attribute,
        )


class DuplicateAttributeValuesError(ErrorObject):
    #: List of :class:`commercetools.types.Attribute`
    attributes: typing.List["Attribute"]

    def __init__(self, *, message: str, attributes: typing.List["Attribute"]) -> None:
        self.attributes = attributes
        super().__init__(code="DuplicateAttributeValues", message=message)

    def __repr__(self) -> str:
        return "DuplicateAttributeValuesError(code=%r, message=%r, attributes=%r)" % (
            self.code,
            self.message,
            self.attributes,
        )


class DuplicateFieldError(ErrorObject):
    #: Optional :class:`str`
    field: typing.Optional[str]
    #: Optional :class:`typing.Any` `(Named` ``duplicateValue`` `in Commercetools)`
    duplicate_value: typing.Optional[typing.Any]
    #: Optional :class:`commercetools.types.Reference` `(Named` ``conflictingResource`` `in Commercetools)`
    conflicting_resource: typing.Optional["Reference"]

    def __init__(
        self,
        *,
        message: str,
        field: typing.Optional[str] = None,
        duplicate_value: typing.Optional[typing.Any] = None,
        conflicting_resource: typing.Optional["Reference"] = None
    ) -> None:
        self.field = field
        self.duplicate_value = duplicate_value
        self.conflicting_resource = conflicting_resource
        super().__init__(code="DuplicateField", message=message)

    def __repr__(self) -> str:
        return (
            "DuplicateFieldError(code=%r, message=%r, field=%r, duplicate_value=%r, conflicting_resource=%r)"
            % (
                self.code,
                self.message,
                self.field,
                self.duplicate_value,
                self.conflicting_resource,
            )
        )


class DuplicateFieldWithConflictingResourceError(ErrorObject):
    #: :class:`str`
    field: str
    #: :class:`typing.Any` `(Named` ``duplicateValue`` `in Commercetools)`
    duplicate_value: typing.Any
    #: :class:`commercetools.types.Reference` `(Named` ``conflictingResource`` `in Commercetools)`
    conflicting_resource: "Reference"

    def __init__(
        self,
        *,
        message: str,
        field: str,
        duplicate_value: typing.Any,
        conflicting_resource: "Reference"
    ) -> None:
        self.field = field
        self.duplicate_value = duplicate_value
        self.conflicting_resource = conflicting_resource
        super().__init__(code="DuplicateFieldWithConflictingResource", message=message)

    def __repr__(self) -> str:
        return (
            "DuplicateFieldWithConflictingResourceError(code=%r, message=%r, field=%r, duplicate_value=%r, conflicting_resource=%r)"
            % (
                self.code,
                self.message,
                self.field,
                self.duplicate_value,
                self.conflicting_resource,
            )
        )


class DuplicatePriceScopeError(ErrorObject):
    #: List of :class:`commercetools.types.Price` `(Named` ``conflictingPrices`` `in Commercetools)`
    conflicting_prices: typing.List["Price"]

    def __init__(
        self, *, message: str, conflicting_prices: typing.List["Price"]
    ) -> None:
        self.conflicting_prices = conflicting_prices
        super().__init__(code="DuplicatePriceScope", message=message)

    def __repr__(self) -> str:
        return (
            "DuplicatePriceScopeError(code=%r, message=%r, conflicting_prices=%r)"
            % (self.code, self.message, self.conflicting_prices)
        )


class DuplicateVariantValuesError(ErrorObject):
    #: :class:`commercetools.types.VariantValues` `(Named` ``variantValues`` `in Commercetools)`
    variant_values: "VariantValues"

    def __init__(self, *, message: str, variant_values: "VariantValues") -> None:
        self.variant_values = variant_values
        super().__init__(code="DuplicateVariantValues", message=message)

    def __repr__(self) -> str:
        return "DuplicateVariantValuesError(code=%r, message=%r, variant_values=%r)" % (
            self.code,
            self.message,
            self.variant_values,
        )


class EnumValueIsUsedError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="EnumValueIsUsed", message=message)

    def __repr__(self) -> str:
        return "EnumValueIsUsedError(code=%r, message=%r)" % (self.code, self.message)


class ExtensionBadResponseError(ErrorObject):
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``localizedMessage`` `in Commercetools)`
    localized_message: typing.Optional["LocalizedString"]
    #: Optional :class:`object` `(Named` ``extensionExtraInfo`` `in Commercetools)`
    extension_extra_info: typing.Optional[object]
    #: :class:`commercetools.types.ErrorByExtension` `(Named` ``errorByExtension`` `in Commercetools)`
    error_by_extension: "ErrorByExtension"

    def __init__(
        self,
        *,
        message: str,
        error_by_extension: "ErrorByExtension",
        localized_message: typing.Optional["LocalizedString"] = None,
        extension_extra_info: typing.Optional[object] = None
    ) -> None:
        self.localized_message = localized_message
        self.extension_extra_info = extension_extra_info
        self.error_by_extension = error_by_extension
        super().__init__(code="ExtensionBadResponse", message=message)

    def __repr__(self) -> str:
        return (
            "ExtensionBadResponseError(code=%r, message=%r, localized_message=%r, extension_extra_info=%r, error_by_extension=%r)"
            % (
                self.code,
                self.message,
                self.localized_message,
                self.extension_extra_info,
                self.error_by_extension,
            )
        )


class ExtensionNoResponseError(ErrorObject):
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``localizedMessage`` `in Commercetools)`
    localized_message: typing.Optional["LocalizedString"]
    #: Optional :class:`object` `(Named` ``extensionExtraInfo`` `in Commercetools)`
    extension_extra_info: typing.Optional[object]
    #: :class:`commercetools.types.ErrorByExtension` `(Named` ``errorByExtension`` `in Commercetools)`
    error_by_extension: "ErrorByExtension"

    def __init__(
        self,
        *,
        message: str,
        error_by_extension: "ErrorByExtension",
        localized_message: typing.Optional["LocalizedString"] = None,
        extension_extra_info: typing.Optional[object] = None
    ) -> None:
        self.localized_message = localized_message
        self.extension_extra_info = extension_extra_info
        self.error_by_extension = error_by_extension
        super().__init__(code="ExtensionNoResponse", message=message)

    def __repr__(self) -> str:
        return (
            "ExtensionNoResponseError(code=%r, message=%r, localized_message=%r, extension_extra_info=%r, error_by_extension=%r)"
            % (
                self.code,
                self.message,
                self.localized_message,
                self.extension_extra_info,
                self.error_by_extension,
            )
        )


class ExtensionUpdateActionsFailedError(ErrorObject):
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``localizedMessage`` `in Commercetools)`
    localized_message: typing.Optional["LocalizedString"]
    #: Optional :class:`object` `(Named` ``extensionExtraInfo`` `in Commercetools)`
    extension_extra_info: typing.Optional[object]
    #: :class:`commercetools.types.ErrorByExtension` `(Named` ``errorByExtension`` `in Commercetools)`
    error_by_extension: "ErrorByExtension"

    def __init__(
        self,
        *,
        message: str,
        error_by_extension: "ErrorByExtension",
        localized_message: typing.Optional["LocalizedString"] = None,
        extension_extra_info: typing.Optional[object] = None
    ) -> None:
        self.localized_message = localized_message
        self.extension_extra_info = extension_extra_info
        self.error_by_extension = error_by_extension
        super().__init__(code="ExtensionUpdateActionsFailed", message=message)

    def __repr__(self) -> str:
        return (
            "ExtensionUpdateActionsFailedError(code=%r, message=%r, localized_message=%r, extension_extra_info=%r, error_by_extension=%r)"
            % (
                self.code,
                self.message,
                self.localized_message,
                self.extension_extra_info,
                self.error_by_extension,
            )
        )


class InsufficientScopeError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="insufficient_scope", message=message)

    def __repr__(self) -> str:
        return "InsufficientScopeError(code=%r, message=%r)" % (self.code, self.message)


class InvalidCredentialsError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidCredentials", message=message)

    def __repr__(self) -> str:
        return "InvalidCredentialsError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


class InvalidCurrentPasswordError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidCurrentPassword", message=message)

    def __repr__(self) -> str:
        return "InvalidCurrentPasswordError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


class InvalidFieldError(ErrorObject):
    #: :class:`str`
    field: str
    #: :class:`typing.Any` `(Named` ``invalidValue`` `in Commercetools)`
    invalid_value: typing.Any
    #: Optional :class:`list` `(Named` ``allowedValues`` `in Commercetools)`
    allowed_values: typing.Optional[list]

    def __init__(
        self,
        *,
        message: str,
        field: str,
        invalid_value: typing.Any,
        allowed_values: typing.Optional[list] = None
    ) -> None:
        self.field = field
        self.invalid_value = invalid_value
        self.allowed_values = allowed_values
        super().__init__(code="InvalidField", message=message)

    def __repr__(self) -> str:
        return (
            "InvalidFieldError(code=%r, message=%r, field=%r, invalid_value=%r, allowed_values=%r)"
            % (
                self.code,
                self.message,
                self.field,
                self.invalid_value,
                self.allowed_values,
            )
        )


class InvalidInputError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidInput", message=message)

    def __repr__(self) -> str:
        return "InvalidInputError(code=%r, message=%r)" % (self.code, self.message)


class InvalidItemShippingDetailsError(ErrorObject):
    #: :class:`str`
    subject: str
    #: :class:`str` `(Named` ``itemId`` `in Commercetools)`
    item_id: str

    def __init__(self, *, message: str, subject: str, item_id: str) -> None:
        self.subject = subject
        self.item_id = item_id
        super().__init__(code="InvalidItemShippingDetails", message=message)

    def __repr__(self) -> str:
        return (
            "InvalidItemShippingDetailsError(code=%r, message=%r, subject=%r, item_id=%r)"
            % (self.code, self.message, self.subject, self.item_id)
        )


class InvalidJsonInputError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidJsonInput", message=message)

    def __repr__(self) -> str:
        return "InvalidJsonInputError(code=%r, message=%r)" % (self.code, self.message)


class InvalidOperationError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidOperation", message=message)

    def __repr__(self) -> str:
        return "InvalidOperationError(code=%r, message=%r)" % (self.code, self.message)


class InvalidSubjectError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="InvalidSubject", message=message)

    def __repr__(self) -> str:
        return "InvalidSubjectError(code=%r, message=%r)" % (self.code, self.message)


class InvalidTokenError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="invalid_token", message=message)

    def __repr__(self) -> str:
        return "InvalidTokenError(code=%r, message=%r)" % (self.code, self.message)


class LanguageUsedInStoresError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="LanguageUsedInStores", message=message)

    def __repr__(self) -> str:
        return "LanguageUsedInStoresError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


class MatchingPriceNotFoundError(ErrorObject):
    #: :class:`str` `(Named` ``productId`` `in Commercetools)`
    product_id: str
    #: :class:`int` `(Named` ``variantId`` `in Commercetools)`
    variant_id: int
    #: Optional :class:`str`
    currency: typing.Optional[str]
    #: Optional :class:`str`
    country: typing.Optional[str]
    #: Optional :class:`commercetools.types.CustomerGroupReference` `(Named` ``customerGroup`` `in Commercetools)`
    customer_group: typing.Optional["CustomerGroupReference"]
    #: Optional :class:`commercetools.types.ChannelReference`
    channel: typing.Optional["ChannelReference"]

    def __init__(
        self,
        *,
        message: str,
        product_id: str,
        variant_id: int,
        currency: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None
    ) -> None:
        self.product_id = product_id
        self.variant_id = variant_id
        self.currency = currency
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        super().__init__(code="MatchingPriceNotFound", message=message)

    def __repr__(self) -> str:
        return (
            "MatchingPriceNotFoundError(code=%r, message=%r, product_id=%r, variant_id=%r, currency=%r, country=%r, customer_group=%r, channel=%r)"
            % (
                self.code,
                self.message,
                self.product_id,
                self.variant_id,
                self.currency,
                self.country,
                self.customer_group,
                self.channel,
            )
        )


class MissingTaxRateForCountryError(ErrorObject):
    #: :class:`str` `(Named` ``taxCategoryId`` `in Commercetools)`
    tax_category_id: str
    #: Optional :class:`str`
    country: typing.Optional[str]
    #: Optional :class:`str`
    state: typing.Optional[str]

    def __init__(
        self,
        *,
        message: str,
        tax_category_id: str,
        country: typing.Optional[str] = None,
        state: typing.Optional[str] = None
    ) -> None:
        self.tax_category_id = tax_category_id
        self.country = country
        self.state = state
        super().__init__(code="MissingTaxRateForCountry", message=message)

    def __repr__(self) -> str:
        return (
            "MissingTaxRateForCountryError(code=%r, message=%r, tax_category_id=%r, country=%r, state=%r)"
            % (self.code, self.message, self.tax_category_id, self.country, self.state)
        )


class NoMatchingProductDiscountFoundError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="NoMatchingProductDiscountFound", message=message)

    def __repr__(self) -> str:
        return "NoMatchingProductDiscountFoundError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


class OutOfStockError(ErrorObject):
    #: List of :class:`str` `(Named` ``lineItems`` `in Commercetools)`
    line_items: typing.List[str]
    #: List of :class:`str`
    skus: typing.List[str]

    def __init__(
        self, *, message: str, line_items: typing.List[str], skus: typing.List[str]
    ) -> None:
        self.line_items = line_items
        self.skus = skus
        super().__init__(code="OutOfStock", message=message)

    def __repr__(self) -> str:
        return "OutOfStockError(code=%r, message=%r, line_items=%r, skus=%r)" % (
            self.code,
            self.message,
            self.line_items,
            self.skus,
        )


class PriceChangedError(ErrorObject):
    #: List of :class:`str` `(Named` ``lineItems`` `in Commercetools)`
    line_items: typing.List[str]
    #: :class:`bool`
    shipping: bool

    def __init__(
        self, *, message: str, line_items: typing.List[str], shipping: bool
    ) -> None:
        self.line_items = line_items
        self.shipping = shipping
        super().__init__(code="PriceChanged", message=message)

    def __repr__(self) -> str:
        return "PriceChangedError(code=%r, message=%r, line_items=%r, shipping=%r)" % (
            self.code,
            self.message,
            self.line_items,
            self.shipping,
        )


class ReferenceExistsError(ErrorObject):
    #: Optional :class:`commercetools.types.ReferenceTypeId` `(Named` ``referencedBy`` `in Commercetools)`
    referenced_by: typing.Optional["ReferenceTypeId"]

    def __init__(
        self, *, message: str, referenced_by: typing.Optional["ReferenceTypeId"] = None
    ) -> None:
        self.referenced_by = referenced_by
        super().__init__(code="ReferenceExists", message=message)

    def __repr__(self) -> str:
        return "ReferenceExistsError(code=%r, message=%r, referenced_by=%r)" % (
            self.code,
            self.message,
            self.referenced_by,
        )


class ReferencedResourceNotFoundError(ErrorObject):
    #: :class:`commercetools.types.ReferenceTypeId` `(Named` ``typeId`` `in Commercetools)`
    type_id: "ReferenceTypeId"
    #: Optional :class:`str`
    id: typing.Optional[str]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        message: str,
        type_id: "ReferenceTypeId",
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.type_id = type_id
        self.id = id
        self.key = key
        super().__init__(code="ReferencedResourceNotFound", message=message)

    def __repr__(self) -> str:
        return (
            "ReferencedResourceNotFoundError(code=%r, message=%r, type_id=%r, id=%r, key=%r)"
            % (self.code, self.message, self.type_id, self.id, self.key)
        )


class RequiredFieldError(ErrorObject):
    #: :class:`str`
    field: str

    def __init__(self, *, message: str, field: str) -> None:
        self.field = field
        super().__init__(code="RequiredField", message=message)

    def __repr__(self) -> str:
        return "RequiredFieldError(code=%r, message=%r, field=%r)" % (
            self.code,
            self.message,
            self.field,
        )


class ResourceNotFoundError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="ResourceNotFound", message=message)

    def __repr__(self) -> str:
        return "ResourceNotFoundError(code=%r, message=%r)" % (self.code, self.message)


class ShippingMethodDoesNotMatchCartError(ErrorObject):
    def __init__(self, *, message: str) -> None:
        super().__init__(code="ShippingMethodDoesNotMatchCart", message=message)

    def __repr__(self) -> str:
        return "ShippingMethodDoesNotMatchCartError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )
