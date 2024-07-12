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
from .common import BaseResource

if typing.TYPE_CHECKING:
    from .approval_rule import ApprovalRule, RuleApprover
    from .business_unit import Associate, BusinessUnitKeyReference
    from .common import CreatedBy, LastModifiedBy
    from .order import OrderReference
    from .type import CustomFields, FieldContainer, TypeResourceIdentifier

__all__ = [
    "ApprovalFlow",
    "ApprovalFlowApproval",
    "ApprovalFlowApproveAction",
    "ApprovalFlowPagedQueryResponse",
    "ApprovalFlowRejectAction",
    "ApprovalFlowRejection",
    "ApprovalFlowSetCustomFieldAction",
    "ApprovalFlowSetCustomTypeAction",
    "ApprovalFlowStatus",
    "ApprovalFlowUpdate",
    "ApprovalFlowUpdateAction",
]


class ApprovalFlow(BaseResource):
    #: IDs and references that created the ApprovalFlow.
    created_by: typing.Optional["CreatedBy"]
    #: IDs and references that last modified the ApprovalFlow.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: [Order](ctp:api:type:Order) that needs to be approved.
    order: "OrderReference"
    #: [Business Unit](ctp:api:type:BusinessUnit) the Approval Flow belongs to.
    business_unit: "BusinessUnitKeyReference"
    #: Approval Rules that matched the [Order](ctp:api:type:Order).
    rules: typing.List["ApprovalRule"]
    #: Indicates whether the Approval Flow is under review, approved, or rejected.
    status: "ApprovalFlowStatus"
    #: Present when the [status](ctp:api:type:ApprovalFlowStatus) of the Approval Flow is `Rejected`.
    rejection: typing.Optional["ApprovalFlowRejection"]
    #: Existing approvals in the Approval Flow.
    approvals: typing.List["ApprovalFlowApproval"]
    #: Associate Roles that can approve according to the approver hierarchy tiers defined in `rules`.
    #: Associates are allowed to reject even after they have given approval, as long as the current approver hierarchy tier still contains their role.
    eligible_approvers: typing.List["RuleApprover"]
    #: Associate Roles required for approval based on the approver hierarchy tiers defined in `rules` across all remaining tiers.
    pending_approvers: typing.List["RuleApprover"]
    #: Associate Roles required for approval based on the approver hierarchy tiers defined in `rules` only for the currently active tier(s).
    current_tier_pending_approvers: typing.List["RuleApprover"]
    #: Custom Fields on the Approval Flow.
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        created_by: typing.Optional["CreatedBy"] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        order: "OrderReference",
        business_unit: "BusinessUnitKeyReference",
        rules: typing.List["ApprovalRule"],
        status: "ApprovalFlowStatus",
        rejection: typing.Optional["ApprovalFlowRejection"] = None,
        approvals: typing.List["ApprovalFlowApproval"],
        eligible_approvers: typing.List["RuleApprover"],
        pending_approvers: typing.List["RuleApprover"],
        current_tier_pending_approvers: typing.List["RuleApprover"],
        custom: typing.Optional["CustomFields"] = None
    ):
        self.created_by = created_by
        self.last_modified_by = last_modified_by
        self.order = order
        self.business_unit = business_unit
        self.rules = rules
        self.status = status
        self.rejection = rejection
        self.approvals = approvals
        self.eligible_approvers = eligible_approvers
        self.pending_approvers = pending_approvers
        self.current_tier_pending_approvers = current_tier_pending_approvers
        self.custom = custom

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApprovalFlow":
        from ._schemas.approval_flow import ApprovalFlowSchema

        return ApprovalFlowSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowSchema

        return ApprovalFlowSchema().dump(self)


class ApprovalFlowApproval(_BaseType):
    #: Associate who approved the [Approval Flow](ctp:api:type:ApprovalFlow).
    approver: "Associate"
    #: Date and time (UTC) the [Approval Flow](ctp:api:type:ApprovalFlow) was approved.
    approved_at: datetime.datetime

    def __init__(self, *, approver: "Associate", approved_at: datetime.datetime):
        self.approver = approver
        self.approved_at = approved_at

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApprovalFlowApproval":
        from ._schemas.approval_flow import ApprovalFlowApprovalSchema

        return ApprovalFlowApprovalSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowApprovalSchema

        return ApprovalFlowApprovalSchema().dump(self)


class ApprovalFlowPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [ApprovalFlow](ctp:api:type:ApprovalFlow)."""

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
    #: Approval Flows matching the query.
    results: typing.List["ApprovalFlow"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["ApprovalFlow"]
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
    ) -> "ApprovalFlowPagedQueryResponse":
        from ._schemas.approval_flow import ApprovalFlowPagedQueryResponseSchema

        return ApprovalFlowPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowPagedQueryResponseSchema

        return ApprovalFlowPagedQueryResponseSchema().dump(self)


class ApprovalFlowRejection(_BaseType):
    #: Associate who rejected the [Approval Flow](ctp:api:type:ApprovalFlow).
    rejecter: "Associate"
    #: Date and time (UTC) the [Approval Flow](ctp:api:type:ApprovalFlow) was rejected.
    rejected_at: datetime.datetime
    #: The reason for the rejection of the [Approval Flow](ctp:api:type:ApprovalFlow).
    reason: typing.Optional[str]

    def __init__(
        self,
        *,
        rejecter: "Associate",
        rejected_at: datetime.datetime,
        reason: typing.Optional[str] = None
    ):
        self.rejecter = rejecter
        self.rejected_at = rejected_at
        self.reason = reason

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApprovalFlowRejection":
        from ._schemas.approval_flow import ApprovalFlowRejectionSchema

        return ApprovalFlowRejectionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowRejectionSchema

        return ApprovalFlowRejectionSchema().dump(self)


class ApprovalFlowStatus(enum.Enum):
    """Indicates whether the [Approval Flow](ctp:api:type:ApprovalFlow) is under review, approved, or rejected."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ApprovalFlowUpdate(_BaseType):
    #: Expected version of the [Approval Flow](ctp:api:type:ApprovalFlow) to which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the [Approval Flow](ctp:api:type:ApprovalFlow).
    actions: typing.List["ApprovalFlowUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["ApprovalFlowUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ApprovalFlowUpdate":
        from ._schemas.approval_flow import ApprovalFlowUpdateSchema

        return ApprovalFlowUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowUpdateSchema

        return ApprovalFlowUpdateSchema().dump(self)


class ApprovalFlowUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ApprovalFlowUpdateAction":
        if data["action"] == "approve":
            from ._schemas.approval_flow import ApprovalFlowApproveActionSchema

            return ApprovalFlowApproveActionSchema().load(data)
        if data["action"] == "reject":
            from ._schemas.approval_flow import ApprovalFlowRejectActionSchema

            return ApprovalFlowRejectActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.approval_flow import ApprovalFlowSetCustomFieldActionSchema

            return ApprovalFlowSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.approval_flow import ApprovalFlowSetCustomTypeActionSchema

            return ApprovalFlowSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowUpdateActionSchema

        return ApprovalFlowUpdateActionSchema().dump(self)


class ApprovalFlowApproveAction(ApprovalFlowUpdateAction):
    """This update action allows an [Associate](ctp:api:type:Associate) to approve an Approval Flow. The process takes into account all [Associate Roles](ctp:api:type:AssociateRole) held by the Associate, aligning with the matched [Approval Rules](ctp:api:type:ApprovalRule) and their respective approver hierarchies.

    When every required Associate has given their approval, the Approval Flow achieves a fully approved state, automatically updating its status to `Approved`. An Associate is eligible to approve only if their roles are within tiers of the Approval Rule hierarchy that are yet to be fully approved or rejected. As such, an Associate may be able to give their approval more than once.

    """

    def __init__(self):

        super().__init__(action="approve")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ApprovalFlowApproveAction":
        from ._schemas.approval_flow import ApprovalFlowApproveActionSchema

        return ApprovalFlowApproveActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowApproveActionSchema

        return ApprovalFlowApproveActionSchema().dump(self)


class ApprovalFlowRejectAction(ApprovalFlowUpdateAction):
    """This update action allows an [Associate](ctp:api:type:Associate) to reject an Approval Flow, setting its status to `Rejected`.
    The process takes into account all [Associate Roles](ctp:api:type:AssociateRole) held by the Associate, aligning with the matched [Approval Rules](ctp:api:type:ApprovalRule) and their respective approver hierarchies.
    Even a single rejection in the process will result in the rejection of the entire Approval Flow.

    An Associate is eligible to reject only if their roles are within tiers of the Approval Rule hierarchy that are yet to be rejected. An Associate may alter a prior approval into a rejection.

    """

    #: The reason for the rejection of the [Approval Flow](ctp:api:type:ApprovalFlow).
    reason: typing.Optional[str]

    def __init__(self, *, reason: typing.Optional[str] = None):
        self.reason = reason

        super().__init__(action="reject")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ApprovalFlowRejectAction":
        from ._schemas.approval_flow import ApprovalFlowRejectActionSchema

        return ApprovalFlowRejectActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowRejectActionSchema

        return ApprovalFlowRejectActionSchema().dump(self)


class ApprovalFlowSetCustomFieldAction(ApprovalFlowUpdateAction):
    #: Name of the [Custom Field](ctp:api:type:CustomFields).
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
    ) -> "ApprovalFlowSetCustomFieldAction":
        from ._schemas.approval_flow import ApprovalFlowSetCustomFieldActionSchema

        return ApprovalFlowSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowSetCustomFieldActionSchema

        return ApprovalFlowSetCustomFieldActionSchema().dump(self)


class ApprovalFlowSetCustomTypeAction(ApprovalFlowUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the ApprovalFlow with [Custom Fields](ctp:api:type:CustomFields).
    #: If absent, any existing Type and Custom Fields are removed from the ApprovalFlow.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](ctp:api:type:CustomFields) fields for the ApprovalFlow.
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
    ) -> "ApprovalFlowSetCustomTypeAction":
        from ._schemas.approval_flow import ApprovalFlowSetCustomTypeActionSchema

        return ApprovalFlowSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.approval_flow import ApprovalFlowSetCustomTypeActionSchema

        return ApprovalFlowSetCustomTypeActionSchema().dump(self)
