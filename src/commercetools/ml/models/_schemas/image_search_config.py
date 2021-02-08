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
from ..image_search_config import ImageSearchConfigStatus

# Fields


# Marshmallow Schemas


class ImageSearchConfigUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ImageSearchConfigUpdateAction(**data)


class ChangeStatusUpdateActionSchema(ImageSearchConfigUpdateActionSchema):
    status = marshmallow_enum.EnumField(
        ImageSearchConfigStatus, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ChangeStatusUpdateAction(**data)


class ImageSearchConfigRequestSchema(helpers.BaseSchema):
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeStatus": helpers.absmod(
                    __name__, ".ChangeStatusUpdateActionSchema"
                )
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageSearchConfigRequest(**data)


class ImageSearchConfigResponseSchema(helpers.BaseSchema):
    status = marshmallow_enum.EnumField(
        ImageSearchConfigStatus, by_value=True, allow_none=True, missing=None
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageSearchConfigResponse(**data)
