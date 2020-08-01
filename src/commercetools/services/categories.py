# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.services import abstract, traits
from commercetools.typing import OptionalListStr


class _CategoryQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _CategoryUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _CategoryDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class CategoryService(abstract.AbstractService):
    """Categories are used to organize products in a hierarchical structure."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> types.Category:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"categories/{id}",
            params=params,
            schema_cls=schemas.CategorySchema,
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> types.Category:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"categories/key={key}",
            params=params,
            schema_cls=schemas.CategorySchema,
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
    ) -> types.CategoryPagedQueryResponse:
        """Categories are used to organize products in a hierarchical structure.
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
            _CategoryQuerySchema,
        )
        return self._client._get(
            endpoint="categories",
            params=params,
            schema_cls=schemas.CategoryPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.CategoryDraft, *, expand: OptionalListStr = None
    ) -> types.Category:
        """Creating a category produces the CategoryCreated message.

        Categories are used to organize products in a hierarchical structure.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="categories",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.CategoryDraftSchema,
            response_schema_cls=schemas.CategorySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.CategoryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Category:
        params = self._serialize_params({"expand": expand}, _CategoryUpdateSchema)
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CategoryUpdateSchema,
            response_schema_cls=schemas.CategorySchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.CategoryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Category:
        params = self._serialize_params({"expand": expand}, _CategoryUpdateSchema)
        update_action = types.CategoryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"categories/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.CategoryUpdateSchema,
            response_schema_cls=schemas.CategorySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.Category:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CategoryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"categories/{id}",
            params=params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.Category:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _CategoryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"categories/key={key}",
            params=params,
            response_schema_cls=schemas.CategorySchema,
            force_delete=force_delete,
        )
