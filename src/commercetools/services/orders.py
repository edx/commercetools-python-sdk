# DO NOT EDIT! This file is automatically generated
import typing

from commercetools import schemas, types
from commercetools.services import abstract, traits
from commercetools.typing import OptionalListStr


class _OrderQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _OrderUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _OrderDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class OrderService(abstract.AbstractService):
    """An order can be created from a order, usually after a checkout process has
    been completed."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> types.Order:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"orders/{id}", params=params, schema_cls=schemas.OrderSchema
        )

    def get_by_order_number(
        self, order_number: str, *, expand: OptionalListStr = None
    ) -> types.Order:
        """In case the orderNumber does not match the regular expression
        [a-zA-Z0-9_\\-]+,

        it should be provided in URL-encoded format.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"orders/order-number={order_number}",
            params=params,
            schema_cls=schemas.OrderSchema,
        )

    def order_edit_get_by_id(
        self, id: str, *, expand: OptionalListStr = None
    ) -> types.OrderEdit:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"orders/edits/{id}",
            params=params,
            schema_cls=schemas.OrderEditSchema,
        )

    def order_edit_get_by_key(
        self, key: str, *, expand: OptionalListStr = None
    ) -> types.OrderEdit:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"orders/edits/key={key}",
            params=params,
            schema_cls=schemas.OrderEditSchema,
        )

    def order_edit_query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> types.OrderEditPagedQueryResponse:
        """OrderEdit are containers for financial changes after an Order has been
        placed.
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
            _OrderQuerySchema,
        )
        return self._client._get(
            endpoint="orders/edits",
            params=params,
            schema_cls=schemas.OrderEditPagedQueryResponseSchema,
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
    ) -> types.OrderPagedQueryResponse:
        """An order can be created from a order, usually after a checkout process
        has been completed.
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
            _OrderQuerySchema,
        )
        return self._client._get(
            endpoint="orders",
            params=params,
            schema_cls=schemas.OrderPagedQueryResponseSchema,
        )

    def create(
        self, draft: types.OrderFromCartDraft, *, expand: OptionalListStr = None
    ) -> types.Order:
        """Creates an order from a Cart.

        The cart must have a shipping address set before creating an order. When
        using the Platform TaxMode, the shipping address is used for tax
        calculation.   An order can be created from a order, usually after a
        checkout process has been completed.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="orders",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.OrderFromCartDraftSchema,
            response_schema_cls=schemas.OrderSchema,
        )

    def order_edit_create(
        self, draft: types.OrderEditDraft, *, expand: OptionalListStr = None
    ) -> types.OrderEdit:
        """OrderEdit are containers for financial changes after an Order has been
        placed.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="orders/edits",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.OrderEditDraftSchema,
            response_schema_cls=schemas.OrderEditSchema,
        )

    def order_edit_update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.OrderEditUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.OrderEdit:
        params = self._serialize_params({"expand": expand}, _OrderUpdateSchema)
        update_action = types.OrderEditUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/edits/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.OrderEditUpdateSchema,
            response_schema_cls=schemas.OrderEditSchema,
            force_update=force_update,
        )

    def order_edit_update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[types.OrderEditUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.OrderEdit:
        params = self._serialize_params({"expand": expand}, _OrderUpdateSchema)
        update_action = types.OrderEditUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/edits/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.OrderEditUpdateSchema,
            response_schema_cls=schemas.OrderEditSchema,
            force_update=force_update,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[types.OrderUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Order:
        params = self._serialize_params({"expand": expand}, _OrderUpdateSchema)
        update_action = types.OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.OrderUpdateSchema,
            response_schema_cls=schemas.OrderSchema,
            force_update=force_update,
        )

    def update_by_order_number(
        self,
        order_number: str,
        version: int,
        actions: typing.List[types.OrderUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> types.Order:
        params = self._serialize_params({"expand": expand}, _OrderUpdateSchema)
        update_action = types.OrderUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"orders/order-number={order_number}",
            params=params,
            data_object=update_action,
            request_schema_cls=schemas.OrderUpdateSchema,
            response_schema_cls=schemas.OrderSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.Order:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _OrderDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"orders/{id}",
            params=params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )

    def delete_by_order_number(
        self,
        order_number: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> types.Order:
        params = self._serialize_params(
            {"version": version, "expand": expand, "dataErasure": data_erasure},
            _OrderDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"orders/order-number={order_number}",
            params=params,
            response_schema_cls=schemas.OrderSchema,
            force_delete=force_delete,
        )

    def order_edit_delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.OrderEdit:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _OrderDeleteSchema
        )
        return self._client._delete(
            endpoint=f"orders/edits/{id}",
            params=params,
            response_schema_cls=schemas.OrderEditSchema,
            force_delete=force_delete,
        )

    def order_edit_delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> types.OrderEdit:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _OrderDeleteSchema
        )
        return self._client._delete(
            endpoint=f"orders/edits/key={key}",
            params=params,
            response_schema_cls=schemas.OrderEditSchema,
            force_delete=force_delete,
        )

    def import_(self, draft: types.OrderImportDraft) -> types.Order:
        """Create an Order by Import"""
        params = {}
        return self._client._post(
            endpoint="orders/import",
            params=params,
            data_object=draft,
            request_schema_cls=schemas.OrderImportDraftSchema,
            response_schema_cls=schemas.OrderSchema,
        )

    def order_edit_apply(self, action: types.OrderEditApply) -> types.OrderEdit:
        params = {}
        return self._client._post(
            endpoint="orders/edits/apply",
            params=params,
            data_object=action,
            request_schema_cls=schemas.OrderEditApplySchema,
            response_schema_cls=schemas.OrderEditSchema,
        )
