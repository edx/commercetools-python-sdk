# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString
__all__ = [
    "CustomFieldBooleanType",
    "CustomFieldDateTimeType",
    "CustomFieldDateType",
    "CustomFieldEnumType",
    "CustomFieldEnumValue",
    "CustomFieldLocalizedEnumType",
    "CustomFieldLocalizedEnumValue",
    "CustomFieldLocalizedStringType",
    "CustomFieldMoneyType",
    "CustomFieldNumberType",
    "CustomFieldReferenceType",
    "CustomFieldSetType",
    "CustomFieldStringType",
    "CustomFieldTimeType",
    "CustomFields",
    "CustomFieldsDraft",
    "FieldContainer",
    "FieldDefinition",
    "FieldType",
    "ResourceTypeId",
    "Type",
    "TypeAddEnumValueAction",
    "TypeAddFieldDefinitionAction",
    "TypeAddLocalizedEnumValueAction",
    "TypeChangeEnumValueLabelAction",
    "TypeChangeEnumValueOrderAction",
    "TypeChangeFieldDefinitionLabelAction",
    "TypeChangeFieldDefinitionOrderAction",
    "TypeChangeInputHintAction",
    "TypeChangeKeyAction",
    "TypeChangeLabelAction",
    "TypeChangeLocalizedEnumValueLabelAction",
    "TypeChangeLocalizedEnumValueOrderAction",
    "TypeChangeNameAction",
    "TypeDraft",
    "TypePagedQueryResponse",
    "TypeReference",
    "TypeRemoveFieldDefinitionAction",
    "TypeResourceIdentifier",
    "TypeSetDescriptionAction",
    "TypeTextInputHint",
    "TypeUpdate",
    "TypeUpdateAction",
]


class CustomFieldEnumValue(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldEnumValueSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    label: typing.Optional[str]

    def __init__(
        self, *, key: typing.Optional[str] = None, label: typing.Optional[str] = None
    ) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "CustomFieldEnumValue(key=%r, label=%r)" % (self.key, self.label)


class CustomFieldLocalizedEnumValue(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldLocalizedEnumValueSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
    ) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "CustomFieldLocalizedEnumValue(key=%r, label=%r)" % (
            self.key,
            self.label,
        )


class CustomFields(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldsSchema`."
    #: :class:`commercetools.types.TypeReference`
    type: typing.Optional["TypeReference"]
    #: :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeReference"] = None,
        fields: typing.Optional["FieldContainer"] = None,
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__()

    def __repr__(self) -> str:
        return "CustomFields(type=%r, fields=%r)" % (self.type, self.fields)


class CustomFieldsDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldsDraftSchema`."
    #: :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None,
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__()

    def __repr__(self) -> str:
        return "CustomFieldsDraft(type=%r, fields=%r)" % (self.type, self.fields)


class FieldContainer(typing.Dict[(str, typing.Any)]):
    def __repr__(self) -> str:
        return "FieldContainer(%s)" % (", ".join(f"{k}={v!r}" for k, v in self.items()))


class FieldDefinition(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.FieldDefinitionSchema`."
    #: :class:`commercetools.types.FieldType`
    type: typing.Optional["FieldType"]
    #: :class:`str`
    name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]
    #: :class:`bool`
    required: typing.Optional[bool]
    #: Optional :class:`commercetools.types.TypeTextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: typing.Optional["TypeTextInputHint"]

    def __init__(
        self,
        *,
        type: typing.Optional["FieldType"] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
        required: typing.Optional[bool] = None,
        input_hint: typing.Optional["TypeTextInputHint"] = None,
    ) -> None:
        self.type = type
        self.name = name
        self.label = label
        self.required = required
        self.input_hint = input_hint
        super().__init__()

    def __repr__(self) -> str:
        return (
            "FieldDefinition(type=%r, name=%r, label=%r, required=%r, input_hint=%r)"
            % (self.type, self.name, self.label, self.required, self.input_hint)
        )


class FieldType(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.FieldTypeSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "FieldType(name=%r)" % (self.name,)


class ResourceTypeId(enum.Enum):
    ASSET = "asset"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    ORDER = "order"
    ORDER_EDIT = "order-edit"
    INVENTORY_ENTRY = "inventory-entry"
    LINE_ITEM = "line-item"
    CUSTOM_LINE_ITEM = "custom-line-item"
    PRODUCT_PRICE = "product-price"
    PAYMENT = "payment"
    PAYMENT_INTERFACE_INTERACTION = "payment-interface-interaction"
    REVIEW = "review"
    SHOPPING_LIST = "shopping-list"
    SHOPPING_LIST_TEXT_LINE_ITEM = "shopping-list-text-line-item"
    DISCOUNT_CODE = "discount-code"
    CART_DISCOUNT = "cart-discount"
    CUSTOMER_GROUP = "customer-group"


class Type(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: List of :class:`commercetools.types.ResourceTypeId` `(Named` ``resourceTypeIds`` `in Commercetools)`
    resource_type_ids: typing.Optional[typing.List["ResourceTypeId"]]
    #: List of :class:`commercetools.types.FieldDefinition` `(Named` ``fieldDefinitions`` `in Commercetools)`
    field_definitions: typing.Optional[typing.List["FieldDefinition"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        resource_type_ids: typing.Optional[typing.List["ResourceTypeId"]] = None,
        field_definitions: typing.Optional[typing.List["FieldDefinition"]] = None,
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.resource_type_ids = resource_type_ids
        self.field_definitions = field_definitions
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
        )

    def __repr__(self) -> str:
        return (
            "Type(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r, description=%r, resource_type_ids=%r, field_definitions=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
                self.description,
                self.resource_type_ids,
                self.field_definitions,
            )
        )


class TypeDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeDraftSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: List of :class:`commercetools.types.ResourceTypeId` `(Named` ``resourceTypeIds`` `in Commercetools)`
    resource_type_ids: typing.Optional[typing.List["ResourceTypeId"]]
    #: Optional list of :class:`commercetools.types.FieldDefinition` `(Named` ``fieldDefinitions`` `in Commercetools)`
    field_definitions: typing.Optional[typing.List["FieldDefinition"]]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        resource_type_ids: typing.Optional[typing.List["ResourceTypeId"]] = None,
        field_definitions: typing.Optional[typing.List["FieldDefinition"]] = None,
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.resource_type_ids = resource_type_ids
        self.field_definitions = field_definitions
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TypeDraft(key=%r, name=%r, description=%r, resource_type_ids=%r, field_definitions=%r)"
            % (
                self.key,
                self.name,
                self.description,
                self.resource_type_ids,
                self.field_definitions,
            )
        )


class TypePagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypePagedQueryResponseSchema`."
    #: :class:`int`
    limit: typing.Optional[int]
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.Type`
    results: typing.Optional[typing.Sequence["Type"]]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Type"]] = None,
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TypePagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class TypeReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeReferenceSchema`."
    #: Optional :class:`commercetools.types.Type`
    obj: typing.Optional["Type"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["Type"] = None,
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.TYPE, id=id)

    def __repr__(self) -> str:
        return "TypeReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class TypeResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.TYPE, id=id, key=key)

    def __repr__(self) -> str:
        return "TypeResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class TypeTextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class TypeUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None,
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "TypeUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class TypeUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "TypeUpdateAction(action=%r)" % (self.action,)


class CustomFieldBooleanType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldBooleanTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="Boolean")

    def __repr__(self) -> str:
        return "CustomFieldBooleanType(name=%r)" % (self.name,)


class CustomFieldDateTimeType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldDateTimeTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="DateTime")

    def __repr__(self) -> str:
        return "CustomFieldDateTimeType(name=%r)" % (self.name,)


class CustomFieldDateType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldDateTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="Date")

    def __repr__(self) -> str:
        return "CustomFieldDateType(name=%r)" % (self.name,)


class CustomFieldEnumType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldEnumTypeSchema`."
    #: List of :class:`commercetools.types.CustomFieldEnumValue`
    values: typing.Optional[typing.List["CustomFieldEnumValue"]]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["CustomFieldEnumValue"]] = None,
    ) -> None:
        self.values = values
        super().__init__(name="Enum")

    def __repr__(self) -> str:
        return "CustomFieldEnumType(name=%r, values=%r)" % (self.name, self.values)


class CustomFieldLocalizedEnumType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldLocalizedEnumTypeSchema`."
    #: List of :class:`commercetools.types.CustomFieldLocalizedEnumValue`
    values: typing.Optional[typing.List["CustomFieldLocalizedEnumValue"]]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        values: typing.Optional[typing.List["CustomFieldLocalizedEnumValue"]] = None,
    ) -> None:
        self.values = values
        super().__init__(name="LocalizedEnum")

    def __repr__(self) -> str:
        return "CustomFieldLocalizedEnumType(name=%r, values=%r)" % (
            self.name,
            self.values,
        )


class CustomFieldLocalizedStringType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldLocalizedStringTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="LocalizedString")

    def __repr__(self) -> str:
        return "CustomFieldLocalizedStringType(name=%r)" % (self.name,)


class CustomFieldMoneyType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldMoneyTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="Money")

    def __repr__(self) -> str:
        return "CustomFieldMoneyType(name=%r)" % (self.name,)


class CustomFieldNumberType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldNumberTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="Number")

    def __repr__(self) -> str:
        return "CustomFieldNumberType(name=%r)" % (self.name,)


class CustomFieldReferenceType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldReferenceTypeSchema`."
    #: :class:`commercetools.types.ReferenceTypeId` `(Named` ``referenceTypeId`` `in Commercetools)`
    reference_type_id: typing.Optional["ReferenceTypeId"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        reference_type_id: typing.Optional["ReferenceTypeId"] = None,
    ) -> None:
        self.reference_type_id = reference_type_id
        super().__init__(name="Reference")

    def __repr__(self) -> str:
        return "CustomFieldReferenceType(name=%r, reference_type_id=%r)" % (
            self.name,
            self.reference_type_id,
        )


class CustomFieldSetType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldSetTypeSchema`."
    #: :class:`commercetools.types.FieldType` `(Named` ``elementType`` `in Commercetools)`
    element_type: typing.Optional["FieldType"]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = None,
        element_type: typing.Optional["FieldType"] = None,
    ) -> None:
        self.element_type = element_type
        super().__init__(name="Set")

    def __repr__(self) -> str:
        return "CustomFieldSetType(name=%r, element_type=%r)" % (
            self.name,
            self.element_type,
        )


class CustomFieldStringType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldStringTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="String")

    def __repr__(self) -> str:
        return "CustomFieldStringType(name=%r)" % (self.name,)


class CustomFieldTimeType(FieldType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomFieldTimeTypeSchema`."

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        super().__init__(name="Time")

    def __repr__(self) -> str:
        return "CustomFieldTimeType(name=%r)" % (self.name,)


class TypeAddEnumValueAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeAddEnumValueActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.CustomFieldEnumValue`
    value: typing.Optional["CustomFieldEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        value: typing.Optional["CustomFieldEnumValue"] = None,
    ) -> None:
        self.field_name = field_name
        self.value = value
        super().__init__(action="addEnumValue")

    def __repr__(self) -> str:
        return "TypeAddEnumValueAction(action=%r, field_name=%r, value=%r)" % (
            self.action,
            self.field_name,
            self.value,
        )


class TypeAddFieldDefinitionAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeAddFieldDefinitionActionSchema`."
    #: :class:`commercetools.types.FieldDefinition` `(Named` ``fieldDefinition`` `in Commercetools)`
    field_definition: typing.Optional["FieldDefinition"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_definition: typing.Optional["FieldDefinition"] = None,
    ) -> None:
        self.field_definition = field_definition
        super().__init__(action="addFieldDefinition")

    def __repr__(self) -> str:
        return "TypeAddFieldDefinitionAction(action=%r, field_definition=%r)" % (
            self.action,
            self.field_definition,
        )


class TypeAddLocalizedEnumValueAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeAddLocalizedEnumValueActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.CustomFieldLocalizedEnumValue`
    value: typing.Optional["CustomFieldLocalizedEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        value: typing.Optional["CustomFieldLocalizedEnumValue"] = None,
    ) -> None:
        self.field_name = field_name
        self.value = value
        super().__init__(action="addLocalizedEnumValue")

    def __repr__(self) -> str:
        return "TypeAddLocalizedEnumValueAction(action=%r, field_name=%r, value=%r)" % (
            self.action,
            self.field_name,
            self.value,
        )


class TypeChangeEnumValueLabelAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeEnumValueLabelActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.CustomFieldEnumValue`
    value: typing.Optional["CustomFieldEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        value: typing.Optional["CustomFieldEnumValue"] = None,
    ) -> None:
        self.field_name = field_name
        self.value = value
        super().__init__(action="changeEnumValueLabel")

    def __repr__(self) -> str:
        return "TypeChangeEnumValueLabelAction(action=%r, field_name=%r, value=%r)" % (
            self.action,
            self.field_name,
            self.value,
        )


class TypeChangeEnumValueOrderAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeEnumValueOrderActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: List of :class:`str`
    keys: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
    ) -> None:
        self.field_name = field_name
        self.keys = keys
        super().__init__(action="changeEnumValueOrder")

    def __repr__(self) -> str:
        return "TypeChangeEnumValueOrderAction(action=%r, field_name=%r, keys=%r)" % (
            self.action,
            self.field_name,
            self.keys,
        )


class TypeChangeFieldDefinitionLabelAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeFieldDefinitionLabelActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
    ) -> None:
        self.field_name = field_name
        self.label = label
        super().__init__(action="changeFieldDefinitionLabel")

    def __repr__(self) -> str:
        return (
            "TypeChangeFieldDefinitionLabelAction(action=%r, field_name=%r, label=%r)"
            % (self.action, self.field_name, self.label)
        )


class TypeChangeFieldDefinitionOrderAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeFieldDefinitionOrderActionSchema`."
    #: List of :class:`str` `(Named` ``fieldNames`` `in Commercetools)`
    field_names: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_names: typing.Optional[typing.List[str]] = None,
    ) -> None:
        self.field_names = field_names
        super().__init__(action="changeFieldDefinitionOrder")

    def __repr__(self) -> str:
        return "TypeChangeFieldDefinitionOrderAction(action=%r, field_names=%r)" % (
            self.action,
            self.field_names,
        )


class TypeChangeInputHintAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeInputHintActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.TypeTextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: typing.Optional["TypeTextInputHint"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        input_hint: typing.Optional["TypeTextInputHint"] = None,
    ) -> None:
        self.field_name = field_name
        self.input_hint = input_hint
        super().__init__(action="changeInputHint")

    def __repr__(self) -> str:
        return "TypeChangeInputHintAction(action=%r, field_name=%r, input_hint=%r)" % (
            self.action,
            self.field_name,
            self.input_hint,
        )


class TypeChangeKeyAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeKeyActionSchema`."
    #: :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="changeKey")

    def __repr__(self) -> str:
        return "TypeChangeKeyAction(action=%r, key=%r)" % (self.action, self.key)


class TypeChangeLabelAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeLabelActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    label: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        label: typing.Optional["LocalizedString"] = None,
    ) -> None:
        self.field_name = field_name
        self.label = label
        super().__init__(action="changeLabel")

    def __repr__(self) -> str:
        return "TypeChangeLabelAction(action=%r, field_name=%r, label=%r)" % (
            self.action,
            self.field_name,
            self.label,
        )


class TypeChangeLocalizedEnumValueLabelAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeLocalizedEnumValueLabelActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: :class:`commercetools.types.CustomFieldLocalizedEnumValue`
    value: typing.Optional["CustomFieldLocalizedEnumValue"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        value: typing.Optional["CustomFieldLocalizedEnumValue"] = None,
    ) -> None:
        self.field_name = field_name
        self.value = value
        super().__init__(action="changeLocalizedEnumValueLabel")

    def __repr__(self) -> str:
        return (
            "TypeChangeLocalizedEnumValueLabelAction(action=%r, field_name=%r, value=%r)"
            % (self.action, self.field_name, self.value)
        )


class TypeChangeLocalizedEnumValueOrderAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeLocalizedEnumValueOrderActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]
    #: List of :class:`str`
    keys: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
    ) -> None:
        self.field_name = field_name
        self.keys = keys
        super().__init__(action="changeLocalizedEnumValueOrder")

    def __repr__(self) -> str:
        return (
            "TypeChangeLocalizedEnumValueOrderAction(action=%r, field_name=%r, keys=%r)"
            % (self.action, self.field_name, self.keys)
        )


class TypeChangeNameAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeChangeNameActionSchema`."
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None,
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "TypeChangeNameAction(action=%r, name=%r)" % (self.action, self.name)


class TypeRemoveFieldDefinitionAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeRemoveFieldDefinitionActionSchema`."
    #: :class:`str` `(Named` ``fieldName`` `in Commercetools)`
    field_name: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        field_name: typing.Optional[str] = None,
    ) -> None:
        self.field_name = field_name
        super().__init__(action="removeFieldDefinition")

    def __repr__(self) -> str:
        return "TypeRemoveFieldDefinitionAction(action=%r, field_name=%r)" % (
            self.action,
            self.field_name,
        )


class TypeSetDescriptionAction(TypeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypeSetDescriptionActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None,
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "TypeSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )
