# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.services import abstract, traits
from commercetools.typing import OptionalListStr


class _InventoryEntryQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _InventoryEntryUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _InventoryEntryDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class InventoryEntryService(abstract.AbstractService):
    """Inventory allows you to track stock quantities."""

    def get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> types.InventoryEntry:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"inventory/{id}",
            params=params,
            schema_cls=schemas.InventoryEntrySchema,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> types.InventoryPagedQueryResponse:
        """Inventory allows you to track stock quantities.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "withTotal": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _InventoryEntryQuerySchema,
        )
        return self._client._get(
            endpoint="inventory",
            params=params,
            schema_cls=schemas.InventoryPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.InventoryEntryDraft, *, expand: OptionalListStr = None
    ) -> types.InventoryEntry:
        """Inventory allows you to track stock quantities.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="inventory",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.InventoryEntryDraftSchema,
            response_schema_cls=schemas.InventoryEntrySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.InventoryEntryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.InventoryEntry:
        params = self._serialize_params({"expand": expand}, _InventoryEntryUpdateSchema)
        update_action = types.InventoryEntryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"inventory/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.InventoryEntryUpdateSchema,
            response_schema_cls=schemas.InventoryEntrySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.InventoryEntry:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _InventoryEntryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"inventory/{id}",
            params=params,
            response_schema_cls=schemas.InventoryEntrySchema,
            force_delete=force_delete,
        )
