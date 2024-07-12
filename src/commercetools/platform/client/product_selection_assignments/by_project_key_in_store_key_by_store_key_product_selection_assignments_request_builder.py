# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.product_selection import ProductsInStorePagedQueryResponse

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyProductSelectionAssignmentsRequestBuilder:

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

    def get(
        self,
        *,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        expand: typing.List["str"] = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["ProductsInStorePagedQueryResponse"]:
        """Queries Product Selection assignments in a specific [Store](ctp:api:type:Store).

        The response will include duplicate Products whenever more than one active Product Selection of the Store
        includes a Product. To make clear through which Product Selection a Product is available in the Store
        the response contains assignments including both the Product and the Product Selection.
        Only Products of Product Selections that are activated in the Store will be returned.

        """
        params = {
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "expand": expand,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/product-selection-assignments",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return ProductsInStorePagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
