# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    KeyReference,
    LoggedResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString
__all__ = [
    "Store",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreResourceIdentifier",
    "StoreSetNameAction",
    "StoreUpdate",
    "StoreUpdateAction",
]


class Store(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

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
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.key = key
        self.name = name
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
            "Store(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
            )
        )


class StoreDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreDraftSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.key = key
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "StoreDraft(key=%r, name=%r)" % (self.key, self.name)


class StoreKeyReference(KeyReference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreKeyReferenceSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.STORE, key=key)

    def __repr__(self) -> str:
        return "StoreKeyReference(type_id=%r, key=%r)" % (self.type_id, self.key)


class StorePagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StorePagedQueryResponseSchema`."
    #: :class:`int`
    limit: typing.Optional[int]
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.Store`
    results: typing.Optional[typing.Sequence["Store"]]

    def __init__(
        self,
        *,
        limit: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Store"]] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "StorePagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class StoreReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreReferenceSchema`."
    #: Optional :class:`commercetools.types.Store`
    obj: typing.Optional["Store"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["Store"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.STORE, id=id)

    def __repr__(self) -> str:
        return "StoreReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class StoreResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.STORE, id=id, key=key)

    def __repr__(self) -> str:
        return "StoreResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class StoreUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "StoreUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class StoreUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "StoreUpdateAction(action=%r)" % (self.action,)


class StoreSetNameAction(StoreUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreSetNameActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setName")

    def __repr__(self) -> str:
        return "StoreSetNameAction(action=%r, name=%r)" % (self.action, self.name)
