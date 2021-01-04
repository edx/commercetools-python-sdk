# DO NOT EDIT! This file is automatically generated
import typing

from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.platform.models._schemas.zone import (
    ZoneDraftSchema,
    ZonePagedQueryResponseSchema,
    ZoneSchema,
    ZoneUpdateSchema,
)
from commercetools.platform.models.zone import (
    Zone,
    ZoneDraft,
    ZonePagedQueryResponse,
    ZoneUpdate,
    ZoneUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ZoneQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ZoneUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ZoneDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class ZoneService(abstract.AbstractService):
    """Zones allow defining ShippingRates for specific Locations."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> Zone:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"zones/{id}", params=params, schema_cls=ZoneSchema
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> Zone:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"zones/key={key}", params=params, schema_cls=ZoneSchema
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
    ) -> ZonePagedQueryResponse:
        """Zones allow defining ShippingRates for specific Locations."""
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _ZoneQuerySchema,
        )
        return self._client._get(
            endpoint="zones", params=params, schema_cls=ZonePagedQueryResponseSchema
        )

    def create(self, draft: ZoneDraft, *, expand: OptionalListStr = None) -> Zone:
        """Zones allow defining ShippingRates for specific Locations."""
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="zones",
            params=params,
            data_object=draft,
            request_schema_cls=ZoneDraftSchema,
            response_schema_cls=ZoneSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ZoneUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Zone:
        params = self._serialize_params({"expand": expand}, _ZoneUpdateSchema)
        update_action = ZoneUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"zones/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=ZoneUpdateSchema,
            response_schema_cls=ZoneSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[ZoneUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Zone:
        params = self._serialize_params({"expand": expand}, _ZoneUpdateSchema)
        update_action = ZoneUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"zones/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=ZoneUpdateSchema,
            response_schema_cls=ZoneSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Zone:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ZoneDeleteSchema
        )
        return self._client._delete(
            endpoint=f"zones/{id}",
            params=params,
            response_schema_cls=ZoneSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Zone:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ZoneDeleteSchema
        )
        return self._client._delete(
            endpoint=f"zones/key={key}",
            params=params,
            response_schema_cls=ZoneSchema,
            force_delete=force_delete,
        )
