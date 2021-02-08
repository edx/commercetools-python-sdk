# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
from commercetools.client import BaseClient

from .by_project_key_request_builder import ByProjectKeyRequestBuilder


class Client(BaseClient):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("url", "https://import.europe-west1.gcp.commercetools.com")
        super().__init__(self, **kwargs)

    def with_project_key_value(self, project_key: str) -> ByProjectKeyRequestBuilder:
        return ByProjectKeyRequestBuilder(
            project_key=project_key,
            client=self,
        )
