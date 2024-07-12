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
from .common import (
    BaseResource,
    KeyReference,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, ReferenceTypeId
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "AssociateRole",
    "AssociateRoleAddPermissionAction",
    "AssociateRoleChangeBuyerAssignableAction",
    "AssociateRoleDraft",
    "AssociateRoleKeyReference",
    "AssociateRolePagedQueryResponse",
    "AssociateRoleReference",
    "AssociateRoleRemovePermissionAction",
    "AssociateRoleResourceIdentifier",
    "AssociateRoleSetCustomFieldAction",
    "AssociateRoleSetCustomTypeAction",
    "AssociateRoleSetNameAction",
    "AssociateRoleSetPermissionsAction",
    "AssociateRoleUpdate",
    "AssociateRoleUpdateAction",
    "Permission",
]


class AssociateRole(BaseResource):
    #: IDs and references that last modified the AssociateRole.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the AssociateRole.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique and immutable identifier of the AssociateRole.
    key: str
    #: Whether the AssociateRole can be assigned to an Associate by a [buyer](/../api/associates-overview#buyer). If false, the AssociateRole can only be assigned using the [general endpoint](/../api/associates-overview#through-the-general-endpoints).
    buyer_assignable: bool
    #: Name of the AssociateRole.
    name: typing.Optional[str]
    #: List of Permissions for the AssociateRole.
    permissions: typing.List["Permission"]
    #: Custom Fields for the AssociateRole.
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str,
        buyer_assignable: bool,
        name: typing.Optional[str] = None,
        permissions: typing.List["Permission"],
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.buyer_assignable = buyer_assignable
        self.name = name
        self.permissions = permissions
        self.custom = custom

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssociateRole":
        from ._schemas.associate_role import AssociateRoleSchema

        return AssociateRoleSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleSchema

        return AssociateRoleSchema().dump(self)


class AssociateRoleDraft(_BaseType):
    #: User-defined unique and immutable identifier for the AssociateRole.
    key: str
    #: Name of the AssociateRole.
    name: typing.Optional[str]
    #: Whether the AssociateRole can be assigned to an Associate by a [buyer](/../api/associates-overview#buyer).
    buyer_assignable: typing.Optional[bool]
    #: List of Permissions for the AssociateRole.
    permissions: typing.Optional[typing.List["Permission"]]
    #: Custom Fields for the AssociateRole.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: str,
        name: typing.Optional[str] = None,
        buyer_assignable: typing.Optional[bool] = None,
        permissions: typing.Optional[typing.List["Permission"]] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.name = name
        self.buyer_assignable = buyer_assignable
        self.permissions = permissions
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssociateRoleDraft":
        from ._schemas.associate_role import AssociateRoleDraftSchema

        return AssociateRoleDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleDraftSchema

        return AssociateRoleDraftSchema().dump(self)


class AssociateRoleKeyReference(KeyReference):
    """[KeyReference](ctp:api:type:KeyReference) to an [AssociateRole](ctp:api:type:AssociateRole)."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceTypeId.ASSOCIATE_ROLE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleKeyReference":
        from ._schemas.associate_role import AssociateRoleKeyReferenceSchema

        return AssociateRoleKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleKeyReferenceSchema

        return AssociateRoleKeyReferenceSchema().dump(self)


class AssociateRolePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [AssociateRole](ctp:api:type:AssociateRole)."""

    #: Number of requested [results](/../api/general-concepts#limit).
    limit: int
    #: Number of elements [skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: [AssociateRoles](ctp:api:type:AssociateRole) matching the query.
    results: typing.List["AssociateRole"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["AssociateRole"]
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
    ) -> "AssociateRolePagedQueryResponse":
        from ._schemas.associate_role import AssociateRolePagedQueryResponseSchema

        return AssociateRolePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRolePagedQueryResponseSchema

        return AssociateRolePagedQueryResponseSchema().dump(self)


class AssociateRoleReference(Reference):
    """[Reference](ctp:api:type:Reference) to an [AssociateRole](ctp:api:type:AssociateRole)."""

    #: Contains the representation of the expanded AssociateRole. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for AssociateRole.
    obj: typing.Optional["AssociateRole"]

    def __init__(self, *, id: str, obj: typing.Optional["AssociateRole"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.ASSOCIATE_ROLE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleReference":
        from ._schemas.associate_role import AssociateRoleReferenceSchema

        return AssociateRoleReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleReferenceSchema

        return AssociateRoleReferenceSchema().dump(self)


class AssociateRoleResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:TypeResourceIdentifier) of an [AssociateRole](ctp:api:type:AssociateRole). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.ASSOCIATE_ROLE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleResourceIdentifier":
        from ._schemas.associate_role import AssociateRoleResourceIdentifierSchema

        return AssociateRoleResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleResourceIdentifierSchema

        return AssociateRoleResourceIdentifierSchema().dump(self)


class AssociateRoleUpdate(_BaseType):
    #: Expected version of the AssociateRole on which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the AssociateRole.
    actions: typing.List["AssociateRoleUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["AssociateRoleUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssociateRoleUpdate":
        from ._schemas.associate_role import AssociateRoleUpdateSchema

        return AssociateRoleUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleUpdateSchema

        return AssociateRoleUpdateSchema().dump(self)


class AssociateRoleUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleUpdateAction":
        if data["action"] == "addPermission":
            from ._schemas.associate_role import AssociateRoleAddPermissionActionSchema

            return AssociateRoleAddPermissionActionSchema().load(data)
        if data["action"] == "changeBuyerAssignable":
            from ._schemas.associate_role import (
                AssociateRoleChangeBuyerAssignableActionSchema,
            )

            return AssociateRoleChangeBuyerAssignableActionSchema().load(data)
        if data["action"] == "removePermission":
            from ._schemas.associate_role import (
                AssociateRoleRemovePermissionActionSchema,
            )

            return AssociateRoleRemovePermissionActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.associate_role import AssociateRoleSetCustomFieldActionSchema

            return AssociateRoleSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.associate_role import AssociateRoleSetCustomTypeActionSchema

            return AssociateRoleSetCustomTypeActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.associate_role import AssociateRoleSetNameActionSchema

            return AssociateRoleSetNameActionSchema().load(data)
        if data["action"] == "setPermissions":
            from ._schemas.associate_role import AssociateRoleSetPermissionsActionSchema

            return AssociateRoleSetPermissionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleUpdateActionSchema

        return AssociateRoleUpdateActionSchema().dump(self)


class Permission(enum.Enum):
    """Permissions grant granular access to [Approval Rules](ctp:api:type:ApprovalRule), [Approval Flows](ctp:api:type:ApprovalFlow), [Business Units](ctp:api:type:BusinessUnit), [Carts](ctp:api:type:Cart), [Orders](ctp:api:type:Order), [Quotes](ctp:api:type:Quote), and [Quote Requests](ctp:api:type:QuoteRequest)."""

    ADD_CHILD_UNITS = "AddChildUnits"
    UPDATE_ASSOCIATES = "UpdateAssociates"
    UPDATE_BUSINESS_UNIT_DETAILS = "UpdateBusinessUnitDetails"
    UPDATE_PARENT_UNIT = "UpdateParentUnit"
    VIEW_MY_CARTS = "ViewMyCarts"
    VIEW_OTHERS_CARTS = "ViewOthersCarts"
    UPDATE_MY_CARTS = "UpdateMyCarts"
    UPDATE_OTHERS_CARTS = "UpdateOthersCarts"
    CREATE_MY_CARTS = "CreateMyCarts"
    CREATE_OTHERS_CARTS = "CreateOthersCarts"
    DELETE_MY_CARTS = "DeleteMyCarts"
    DELETE_OTHERS_CARTS = "DeleteOthersCarts"
    VIEW_MY_ORDERS = "ViewMyOrders"
    VIEW_OTHERS_ORDERS = "ViewOthersOrders"
    UPDATE_MY_ORDERS = "UpdateMyOrders"
    UPDATE_OTHERS_ORDERS = "UpdateOthersOrders"
    CREATE_MY_ORDERS_FROM_MY_CARTS = "CreateMyOrdersFromMyCarts"
    CREATE_MY_ORDERS_FROM_MY_QUOTES = "CreateMyOrdersFromMyQuotes"
    CREATE_ORDERS_FROM_OTHERS_CARTS = "CreateOrdersFromOthersCarts"
    CREATE_ORDERS_FROM_OTHERS_QUOTES = "CreateOrdersFromOthersQuotes"
    VIEW_MY_QUOTES = "ViewMyQuotes"
    VIEW_OTHERS_QUOTES = "ViewOthersQuotes"
    ACCEPT_MY_QUOTES = "AcceptMyQuotes"
    ACCEPT_OTHERS_QUOTES = "AcceptOthersQuotes"
    DECLINE_MY_QUOTES = "DeclineMyQuotes"
    DECLINE_OTHERS_QUOTES = "DeclineOthersQuotes"
    RENEGOTIATE_MY_QUOTES = "RenegotiateMyQuotes"
    RENEGOTIATE_OTHERS_QUOTES = "RenegotiateOthersQuotes"
    REASSIGN_MY_QUOTES = "ReassignMyQuotes"
    REASSIGN_OTHERS_QUOTES = "ReassignOthersQuotes"
    VIEW_MY_QUOTE_REQUESTS = "ViewMyQuoteRequests"
    VIEW_OTHERS_QUOTE_REQUESTS = "ViewOthersQuoteRequests"
    UPDATE_MY_QUOTE_REQUESTS = "UpdateMyQuoteRequests"
    UPDATE_OTHERS_QUOTE_REQUESTS = "UpdateOthersQuoteRequests"
    CREATE_MY_QUOTE_REQUESTS_FROM_MY_CARTS = "CreateMyQuoteRequestsFromMyCarts"
    CREATE_QUOTE_REQUESTS_FROM_OTHERS_CARTS = "CreateQuoteRequestsFromOthersCarts"
    CREATE_APPROVAL_RULES = "CreateApprovalRules"
    UPDATE_APPROVAL_RULES = "UpdateApprovalRules"
    UPDATE_APPROVAL_FLOWS = "UpdateApprovalFlows"


class AssociateRoleAddPermissionAction(AssociateRoleUpdateAction):
    """Adding a Permission to an [AssociateRole](ctp:api:type:AssociateRole) generates an [AssociateRolePermissionAdded](ctp:api:type:AssociateRolePermissionAddedMessage) Message."""

    #: Permission to be added to the AssociateRole.
    permission: "Permission"

    def __init__(self, *, permission: "Permission"):
        self.permission = permission

        super().__init__(action="addPermission")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleAddPermissionAction":
        from ._schemas.associate_role import AssociateRoleAddPermissionActionSchema

        return AssociateRoleAddPermissionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleAddPermissionActionSchema

        return AssociateRoleAddPermissionActionSchema().dump(self)


class AssociateRoleChangeBuyerAssignableAction(AssociateRoleUpdateAction):
    """Changing the `buyerAssignable` value of an AssociateRole generates an [AssociateRoleBuyerAssignableChanged](ctp:api:type:AssociateRoleBuyerAssignableChangedMessage) Message."""

    #: The new value of the `buyerAssignable` field of the AssociateRole.
    buyer_assignable: bool

    def __init__(self, *, buyer_assignable: bool):
        self.buyer_assignable = buyer_assignable

        super().__init__(action="changeBuyerAssignable")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleChangeBuyerAssignableAction":
        from ._schemas.associate_role import (
            AssociateRoleChangeBuyerAssignableActionSchema,
        )

        return AssociateRoleChangeBuyerAssignableActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import (
            AssociateRoleChangeBuyerAssignableActionSchema,
        )

        return AssociateRoleChangeBuyerAssignableActionSchema().dump(self)


class AssociateRoleRemovePermissionAction(AssociateRoleUpdateAction):
    """Removing a Permission from an [AssociateRole](ctp:api:type:AssociateRole) generates an [AssociateRolePermissionRemoved](ctp:api:type:AssociateRolePermissionRemovedMessage) Message."""

    #: Permission to be removed from the AssociateRole.
    permission: "Permission"

    def __init__(self, *, permission: "Permission"):
        self.permission = permission

        super().__init__(action="removePermission")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleRemovePermissionAction":
        from ._schemas.associate_role import AssociateRoleRemovePermissionActionSchema

        return AssociateRoleRemovePermissionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleRemovePermissionActionSchema

        return AssociateRoleRemovePermissionActionSchema().dump(self)


class AssociateRoleSetCustomFieldAction(AssociateRoleUpdateAction):
    #: Name of the [Custom Field](ctp:api:type:CustomFields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Trying to remove a field that does not exist will fail with an [InvalidOperationError](ctp:api:type:InvalidOperationError) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleSetCustomFieldAction":
        from ._schemas.associate_role import AssociateRoleSetCustomFieldActionSchema

        return AssociateRoleSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleSetCustomFieldActionSchema

        return AssociateRoleSetCustomFieldActionSchema().dump(self)


class AssociateRoleSetCustomTypeAction(AssociateRoleUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the AssociateRole with [Custom Fields](ctp:api:type:CustomFields).
    #: If absent, any existing Type and Custom Fields are removed from the AssociateRole.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](ctp:api:type:CustomFields) for the AssociateRole.
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
    ) -> "AssociateRoleSetCustomTypeAction":
        from ._schemas.associate_role import AssociateRoleSetCustomTypeActionSchema

        return AssociateRoleSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleSetCustomTypeActionSchema

        return AssociateRoleSetCustomTypeActionSchema().dump(self)


class AssociateRoleSetNameAction(AssociateRoleUpdateAction):
    """Updating the name of an [AssociateRole](ctp:api:type:AssociateRole) generates an [AssociateRoleNameSet](ctp:api:type:AssociateRoleNameSetMessage) Message."""

    #: New name to set.
    #: If `name` is absent or `null`, the existing name, if any, will be removed.
    name: typing.Optional[str]

    def __init__(self, *, name: typing.Optional[str] = None):
        self.name = name

        super().__init__(action="setName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleSetNameAction":
        from ._schemas.associate_role import AssociateRoleSetNameActionSchema

        return AssociateRoleSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleSetNameActionSchema

        return AssociateRoleSetNameActionSchema().dump(self)


class AssociateRoleSetPermissionsAction(AssociateRoleUpdateAction):
    """Updating the Permissions on an [AssociateRole](ctp:api:type:AssociateRole) generates an [AssociateRolePermissionsSet](ctp:api:type:AssociateRolePermissionsSetMessage) Message."""

    #: Overrides the current list of Permissions for the AssociateRole.
    permissions: typing.Optional[typing.List["Permission"]]

    def __init__(
        self, *, permissions: typing.Optional[typing.List["Permission"]] = None
    ):
        self.permissions = permissions

        super().__init__(action="setPermissions")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssociateRoleSetPermissionsAction":
        from ._schemas.associate_role import AssociateRoleSetPermissionsActionSchema

        return AssociateRoleSetPermissionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.associate_role import AssociateRoleSetPermissionsActionSchema

        return AssociateRoleSetPermissionsActionSchema().dump(self)
