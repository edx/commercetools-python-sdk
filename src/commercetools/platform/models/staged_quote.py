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
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .business_unit import BusinessUnitKeyReference
    from .cart import CartReference
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .customer import CustomerReference
    from .quote_request import QuoteRequestReference, QuoteRequestResourceIdentifier
    from .state import StateReference, StateResourceIdentifier
    from .store import StoreKeyReference
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "StagedQuote",
    "StagedQuoteChangeStagedQuoteStateAction",
    "StagedQuoteDraft",
    "StagedQuotePagedQueryResponse",
    "StagedQuoteReference",
    "StagedQuoteResourceIdentifier",
    "StagedQuoteSetCustomFieldAction",
    "StagedQuoteSetCustomTypeAction",
    "StagedQuoteSetSellerCommentAction",
    "StagedQuoteSetValidToAction",
    "StagedQuoteState",
    "StagedQuoteTransitionStateAction",
    "StagedQuoteUpdate",
    "StagedQuoteUpdateAction",
]


class StagedQuote(BaseResource):
    #: User-specific unique identifier of the staged quote.
    key: typing.Optional[str]
    #: IDs and references that last modified the StagedQuote.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the StagedQuote.
    created_by: typing.Optional["CreatedBy"]
    #: Predefined states tracking the status of the Staged Quote.
    staged_quote_state: "StagedQuoteState"
    #: The [Buyer](/../api/quotes-overview#buyer) who requested the Quote.
    customer: typing.Optional["CustomerReference"]
    #: Quote Request related to the Staged Quote.
    quote_request: "QuoteRequestReference"
    #: [Cart](ctp:api:type:Cart) containing the offered items. May contain either [DirectDiscounts](ctp:api:type:DirectDiscount) or [CartDiscounts](ctp:api:type:CartDiscount).
    quotation_cart: "CartReference"
    #: Expiration date for the Quote.
    valid_to: typing.Optional[datetime.datetime]
    #: Message from the [Seller](/../api/quotes-overview#seller) included in the offer.
    seller_comment: typing.Optional[str]
    #: Custom Fields of the Staged Quote.
    custom: typing.Optional["CustomFields"]
    #: [State](ctp:api:type:State) of the Staged Quote.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]
    #: The Purchase Order Number is typically set by the [Buyer](/quotes-overview#buyer) on a [QuoteRequest](ctp:api:type:QuoteRequest) to
    #: track the purchase order during the [quote and order flow](/../api/quotes-overview#intended-workflow).
    purchase_order_number: typing.Optional[str]
    #: The [BusinessUnit](ctp:api:type:BusinessUnit) for the Staged Quote.
    business_unit: typing.Optional["BusinessUnitKeyReference"]
    #: The Store to which the [Buyer](/../api/quotes-overview#buyer) belongs.
    store: typing.Optional["StoreKeyReference"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        key: typing.Optional[str] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        staged_quote_state: "StagedQuoteState",
        customer: typing.Optional["CustomerReference"] = None,
        quote_request: "QuoteRequestReference",
        quotation_cart: "CartReference",
        valid_to: typing.Optional[datetime.datetime] = None,
        seller_comment: typing.Optional[str] = None,
        custom: typing.Optional["CustomFields"] = None,
        state: typing.Optional["StateReference"] = None,
        purchase_order_number: typing.Optional[str] = None,
        business_unit: typing.Optional["BusinessUnitKeyReference"] = None,
        store: typing.Optional["StoreKeyReference"] = None
    ):
        self.key = key
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.staged_quote_state = staged_quote_state
        self.customer = customer
        self.quote_request = quote_request
        self.quotation_cart = quotation_cart
        self.valid_to = valid_to
        self.seller_comment = seller_comment
        self.custom = custom
        self.state = state
        self.purchase_order_number = purchase_order_number
        self.business_unit = business_unit
        self.store = store

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StagedQuote":
        from ._schemas.staged_quote import StagedQuoteSchema

        return StagedQuoteSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteSchema

        return StagedQuoteSchema().dump(self)


class StagedQuoteDraft(_BaseType):
    #: QuoteRequest from which the StagedQuote is created.
    quote_request: "QuoteRequestResourceIdentifier"
    #: Current version of the QuoteRequest.
    quote_request_version: int
    #: If `true`, the `quoteRequestState` of the referenced [QuoteRequest](ctp:api:type:QuoteRequest) will be set to `Accepted`.
    quote_request_state_to_accepted: typing.Optional[bool]
    #: User-defined unique identifier for the StagedQuote.
    key: typing.Optional[str]
    #: [Custom Fields](/../api/projects/custom-fields) to be added to the StagedQuote.
    #:
    #: - If specified, the Custom Fields are merged with the Custom Fields on the referenced [QuoteRequest](ctp:api:type:QuoteRequest) and added to the StagedQuote.
    #: - If empty, the Custom Fields on the referenced [QuoteRequest](ctp:api:type:QuoteRequest) are added to the StagedQuote automatically.
    custom: typing.Optional["CustomFieldsDraft"]
    #: [State](ctp:api:type:State) of the Staged Quote.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]

    def __init__(
        self,
        *,
        quote_request: "QuoteRequestResourceIdentifier",
        quote_request_version: int,
        quote_request_state_to_accepted: typing.Optional[bool] = None,
        key: typing.Optional[str] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        state: typing.Optional["StateReference"] = None
    ):
        self.quote_request = quote_request
        self.quote_request_version = quote_request_version
        self.quote_request_state_to_accepted = quote_request_state_to_accepted
        self.key = key
        self.custom = custom
        self.state = state

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StagedQuoteDraft":
        from ._schemas.staged_quote import StagedQuoteDraftSchema

        return StagedQuoteDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteDraftSchema

        return StagedQuoteDraftSchema().dump(self)


class StagedQuotePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [StagedQuote](ctp:api:type:StagedQuote)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: Staged Quotes matching the query.
    results: typing.List["StagedQuote"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["StagedQuote"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.total = total
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuotePagedQueryResponse":
        from ._schemas.staged_quote import StagedQuotePagedQueryResponseSchema

        return StagedQuotePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuotePagedQueryResponseSchema

        return StagedQuotePagedQueryResponseSchema().dump(self)


class StagedQuoteReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [StagedQuote](ctp:api:type:StagedQuote)."""

    #: Contains the representation of the expanded StagedQuote.
    #: Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for StagedQuote.
    obj: typing.Optional["StagedQuote"]

    def __init__(self, *, id: str, obj: typing.Optional["StagedQuote"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.STAGED_QUOTE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StagedQuoteReference":
        from ._schemas.staged_quote import StagedQuoteReferenceSchema

        return StagedQuoteReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteReferenceSchema

        return StagedQuoteReferenceSchema().dump(self)


class StagedQuoteResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [StagedQuote](ctp:api:type:StagedQuote)."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STAGED_QUOTE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteResourceIdentifier":
        from ._schemas.staged_quote import StagedQuoteResourceIdentifierSchema

        return StagedQuoteResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteResourceIdentifierSchema

        return StagedQuoteResourceIdentifierSchema().dump(self)


class StagedQuoteState(enum.Enum):
    """Predefined states tracking the status of the Staged Quote."""

    IN_PROGRESS = "InProgress"
    SENT = "Sent"
    CLOSED = "Closed"


class StagedQuoteUpdate(_BaseType):
    #: Expected version of the [StagedQuote](ctp:api:type:StagedQuote) to which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the [StagedQuote](ctp:api:type:StagedQuote).
    actions: typing.List["StagedQuoteUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["StagedQuoteUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StagedQuoteUpdate":
        from ._schemas.staged_quote import StagedQuoteUpdateSchema

        return StagedQuoteUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteUpdateSchema

        return StagedQuoteUpdateSchema().dump(self)


class StagedQuoteUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteUpdateAction":
        if data["action"] == "changeStagedQuoteState":
            from ._schemas.staged_quote import (
                StagedQuoteChangeStagedQuoteStateActionSchema,
            )

            return StagedQuoteChangeStagedQuoteStateActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.staged_quote import StagedQuoteSetCustomFieldActionSchema

            return StagedQuoteSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.staged_quote import StagedQuoteSetCustomTypeActionSchema

            return StagedQuoteSetCustomTypeActionSchema().load(data)
        if data["action"] == "setSellerComment":
            from ._schemas.staged_quote import StagedQuoteSetSellerCommentActionSchema

            return StagedQuoteSetSellerCommentActionSchema().load(data)
        if data["action"] == "setValidTo":
            from ._schemas.staged_quote import StagedQuoteSetValidToActionSchema

            return StagedQuoteSetValidToActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.staged_quote import StagedQuoteTransitionStateActionSchema

            return StagedQuoteTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteUpdateActionSchema

        return StagedQuoteUpdateActionSchema().dump(self)


class StagedQuoteChangeStagedQuoteStateAction(StagedQuoteUpdateAction):
    #: New state to be set for the Staged Quote.
    staged_quote_state: "StagedQuoteState"

    def __init__(self, *, staged_quote_state: "StagedQuoteState"):
        self.staged_quote_state = staged_quote_state

        super().__init__(action="changeStagedQuoteState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteChangeStagedQuoteStateAction":
        from ._schemas.staged_quote import StagedQuoteChangeStagedQuoteStateActionSchema

        return StagedQuoteChangeStagedQuoteStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteChangeStagedQuoteStateActionSchema

        return StagedQuoteChangeStagedQuoteStateActionSchema().dump(self)


class StagedQuoteSetCustomFieldAction(StagedQuoteUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Removing a field that does not exist returns an [InvalidOperation](ctp:api:type:InvalidOperationError) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteSetCustomFieldAction":
        from ._schemas.staged_quote import StagedQuoteSetCustomFieldActionSchema

        return StagedQuoteSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteSetCustomFieldActionSchema

        return StagedQuoteSetCustomFieldActionSchema().dump(self)


class StagedQuoteSetCustomTypeAction(StagedQuoteUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the StagedQuote with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the StagedQuote.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the StagedQuote.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields

        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteSetCustomTypeAction":
        from ._schemas.staged_quote import StagedQuoteSetCustomTypeActionSchema

        return StagedQuoteSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteSetCustomTypeActionSchema

        return StagedQuoteSetCustomTypeActionSchema().dump(self)


class StagedQuoteSetSellerCommentAction(StagedQuoteUpdateAction):
    #: If `sellerComment` is absent or `null`, this field will be removed if it exists.
    seller_comment: typing.Optional[str]

    def __init__(self, *, seller_comment: typing.Optional[str] = None):
        self.seller_comment = seller_comment

        super().__init__(action="setSellerComment")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteSetSellerCommentAction":
        from ._schemas.staged_quote import StagedQuoteSetSellerCommentActionSchema

        return StagedQuoteSetSellerCommentActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteSetSellerCommentActionSchema

        return StagedQuoteSetSellerCommentActionSchema().dump(self)


class StagedQuoteSetValidToAction(StagedQuoteUpdateAction):
    #: If `validTo` is absent or `null`, this field will be removed if it exists.
    valid_to: typing.Optional[datetime.datetime]

    def __init__(self, *, valid_to: typing.Optional[datetime.datetime] = None):
        self.valid_to = valid_to

        super().__init__(action="setValidTo")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteSetValidToAction":
        from ._schemas.staged_quote import StagedQuoteSetValidToActionSchema

        return StagedQuoteSetValidToActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteSetValidToActionSchema

        return StagedQuoteSetValidToActionSchema().dump(self)


class StagedQuoteTransitionStateAction(StagedQuoteUpdateAction):
    """If the existing [State](ctp:api:type:State) has set `transitions`, there must be a direct transition to the new State. If `transitions` is not set, no validation is performed. This update action produces the [Staged Quote State Transition](ctp:api:type:StagedQuoteStateTransitionMessage) Message."""

    #: Value to set.
    #: If there is no State yet, the new State must be an initial State.
    state: "StateResourceIdentifier"
    #: Switch validations on or off.
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force

        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StagedQuoteTransitionStateAction":
        from ._schemas.staged_quote import StagedQuoteTransitionStateActionSchema

        return StagedQuoteTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.staged_quote import StagedQuoteTransitionStateActionSchema

        return StagedQuoteTransitionStateActionSchema().dump(self)
