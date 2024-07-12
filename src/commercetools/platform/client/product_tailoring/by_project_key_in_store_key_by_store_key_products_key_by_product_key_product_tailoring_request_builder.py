# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.cart import ProductTailoringUpdate
from ...models.error import ErrorResponse
from ...models.product_tailoring import ProductTailoring
from ..images.by_project_key_in_store_key_by_store_key_products_key_by_product_key_product_tailoring_images_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringImagesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _product_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        product_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._product_key = product_key
        self._client = client

    def images(
        self,
    ) -> ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringImagesRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyProductsKeyByProductKeyProductTailoringImagesRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            product_key=self._product_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductTailoring"]:
        """Gets the current or staged representation of a [Product Tailoring](ctp:api:type:ProductTailoring) by its Product key in the specified [Store](ctp:api:type:Store)."""
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/products/key={self._product_key}/product-tailoring",
            params={"expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductTailoring.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "ProductTailoringUpdate",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductTailoring"]:
        """Updates the current or staged representation of a [Product Tailoring](ctp:api:type:ProductTailoring) by its Product key in the specified [Store](ctp:api:type:Store)."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/products/key={self._product_key}/product-tailoring",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code == 200:
            return ProductTailoring.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def delete(
        self,
        *,
        version: int,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductTailoring"]:
        """Generates the [ProductTailoringDeleted](ctp:api:type:ProductTailoringDeletedMessage) Message."""
        headers = {} if headers is None else headers
        response = self._client._delete(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/products/key={self._product_key}/product-tailoring",
            params={"version": version, "expand": expand},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductTailoring.deserialize(response.json())
        elif response.status_code in (409, 400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
