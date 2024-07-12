# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.product import ProductProjection

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyProductProjectionsKeyByKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str
    _key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._key = key
        self._client = client

    def get(
        self,
        *,
        staged: bool = None,
        price_currency: str = None,
        price_country: str = None,
        price_customer_group: str = None,
        price_channel: str = None,
        locale_projection: typing.List["str"] = None,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductProjection"]:
        """Gets the current or staged representation of a [Product](ctp:api:type:Product) by its key in the specified [Store](ctp:api:type:Store).
        If the Store has defined some languages, countries, distribution, supply Channels, and/or Product Selection,
        they are used for projections based on [locale](ctp:api:type:ProductProjectionLocales), [price](ctp:api:type:ProductProjectionPrices),
        and [inventory](ctp:api:type:ProductProjectionInventoryEntries).

        If [ProductSelection](ctp:api:type:ProductSelection) is used, it affects the [availability of the Product](/projects/stores#products-available-in-store) in the specified Store.

        When used with an API Client that has the `view_published_products:{projectKey}` scope, this endpoint only returns published (current) Product Projections.

        """
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/product-projections/key={self._key}",
            params={
                "staged": staged,
                "priceCurrency": price_currency,
                "priceCountry": price_country,
                "priceCustomerGroup": price_customer_group,
                "priceChannel": price_channel,
                "localeProjection": locale_projection,
                "expand": expand,
            },
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductProjection.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def head(
        self,
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional[None]:
        """Checks if the current or staged representations of a Product exists for a given `key` in the specified [Store](ctp:api:type:Store). Returns a `200 OK` status if the ProductProjection exists or a `404 Not Found` otherwise."""
        headers = {} if headers is None else headers
        response = self._client._head(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/product-projections/key={self._key}",
            params={},
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return None
        elif response.status_code == 404:
            return None
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
