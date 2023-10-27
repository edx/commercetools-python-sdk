# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.cart_discount import CartDiscount, CartDiscountDraft
from .by_project_key_in_store_key_by_store_key_cart_discounts_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartDiscountsByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_cart_discounts_key_by_key_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartDiscountsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartDiscountsRequestBuilder:
    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def with_key(
        self, key: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartDiscountsKeyByKeyRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartDiscountsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartDiscountsByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartDiscountsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def get(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "CartDiscount":
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/cart-discounts",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CartDiscount.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        where: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> None:
        """Checks if a CartDiscount exists for a given Query Predicate. Returns a `200 OK` status if any CartDiscounts match the Query Predicate or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/cart-discounts",
            params={"where": where},
            headers=headers,
            options=options,
        )
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "CartDiscountDraft",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "CartDiscount":
        """When using the endpoint, the Store specified in the path and the Stores specified in the payload's `stores` field are added to the CartDiscount."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/cart-discounts",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return CartDiscount.deserialize(response.json())
        warnings.warn("Unhandled status code %d" % response.status_code)
