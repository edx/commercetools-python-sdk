# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..project import CustomerIndexingStatus

# Fields


# Marshmallow Schemas
class CustomerIndexingProgressSchema(helpers.BaseSchema):
    indexed = marshmallow.fields.Integer(allow_none=True, load_default=None)
    failed = marshmallow.fields.Integer(allow_none=True, load_default=None)
    estimated_total = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="estimatedTotal"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerIndexingProgress(**data)


class CustomerPagedSearchResponseSchema(helpers.BaseSchema):
    total = marshmallow.fields.Integer(allow_none=True, load_default=None)
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomerSearchResultSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerPagedSearchResponse(**data)


class CustomerSearchIndexingStatusResponseSchema(helpers.BaseSchema):
    status = marshmallow_enum.EnumField(
        CustomerIndexingStatus, by_value=True, allow_none=True, load_default=None
    )
    states = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CustomerIndexingProgressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    started_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="startedAt",
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastModifiedAt",
    )
    retry_count = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="retryCount",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerSearchIndexingStatusResponse(**data)


class CustomerSearchRequestSchema(helpers.BaseSchema):
    query = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchQuerySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    sort = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".search.SearchSortingSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    limit = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    offset = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerSearchRequest(**data)


class CustomerSearchResultSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    relevance = marshmallow.fields.Float(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CustomerSearchResult(**data)
