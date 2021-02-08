# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from .image_search.by_project_key_image_search_request_builder import (
    ByProjectKeyImageSearchRequestBuilder,
)
from .missing_data.by_project_key_missing_data_request_builder import (
    ByProjectKeyMissingDataRequestBuilder,
)
from .recommendations.by_project_key_recommendations_request_builder import (
    ByProjectKeyRecommendationsRequestBuilder,
)
from .similarities.by_project_key_similarities_request_builder import (
    ByProjectKeySimilaritiesRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ..base_client import BaseClient


class ByProjectKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def image_search(self) -> ByProjectKeyImageSearchRequestBuilder:
        """Search for similar products using an image as search input."""
        return ByProjectKeyImageSearchRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def recommendations(self) -> ByProjectKeyRecommendationsRequestBuilder:
        return ByProjectKeyRecommendationsRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def missing_data(self) -> ByProjectKeyMissingDataRequestBuilder:
        return ByProjectKeyMissingDataRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )

    def similarities(self) -> ByProjectKeySimilaritiesRequestBuilder:
        return ByProjectKeySimilaritiesRequestBuilder(
            project_key=self._project_key,
            client=self._client,
        )
