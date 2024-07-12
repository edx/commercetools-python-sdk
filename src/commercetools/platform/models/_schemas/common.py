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
from ..common import AttributionSource, MoneyType, ReferenceTypeId


# Fields
class LocalizedStringField(marshmallow.fields.Dict):

    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return models.LocalizedString(**result)


# Marshmallow Schemas
class PagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, load_default=None)
    offset = marshmallow.fields.Integer(allow_none=True, load_default=None)
    count = marshmallow.fields.Integer(allow_none=True, load_default=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".BaseResourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    meta = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PagedQueryResponse(**data)


class UpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    actions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".UpdateActionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Update(**data)


class UpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.UpdateAction(**data)


class AssetSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    sources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetSourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        load_default=None,
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Asset(**data)


class AssetDimensionsSchema(helpers.BaseSchema):
    w = marshmallow.fields.Integer(allow_none=True, load_default=None)
    h = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetDimensions(**data)


class AssetDraftSchema(helpers.BaseSchema):
    sources = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetSourceSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    name = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        load_default=None,
    )
    description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        load_default=None,
    )
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetDraft(**data)


class AssetSourceSchema(helpers.BaseSchema):
    uri = marshmallow.fields.String(allow_none=True, load_default=None)
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    dimensions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AssetDimensionsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    content_type = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="contentType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AssetSource(**data)


class AttributionSchema(helpers.BaseSchema):
    client_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="clientId",
    )
    source = marshmallow_enum.EnumField(
        AttributionSource, by_value=True, allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Attribution(**data)


class BaseAddressSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    country = marshmallow.fields.String(allow_none=True, load_default=None)
    title = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    salutation = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    first_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="firstName",
    )
    last_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastName",
    )
    street_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="streetName",
    )
    street_number = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="streetNumber",
    )
    additional_street_info = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="additionalStreetInfo",
    )
    postal_code = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="postalCode",
    )
    city = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    region = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    state = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    company = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    department = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    building = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    apartment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    p_o_box = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="pOBox",
    )
    phone = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    mobile = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    email = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    fax = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    additional_address_info = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="additionalAddressInfo",
    )
    external_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="externalId",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BaseAddress(**data)


class AddressSchema(BaseAddressSchema):
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Address(**data)


class AddressDraftSchema(BaseAddressSchema):
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.AddressDraft(**data)


class BaseResourceSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, load_default=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, load_default=None, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BaseResource(**data)


class ClientLoggingSchema(helpers.BaseSchema):
    client_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="clientId",
    )
    external_user_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="externalUserId",
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="anonymousId",
    )
    associate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ClientLogging(**data)


class CreatedBySchema(ClientLoggingSchema):
    attributed_to = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="attributedTo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CreatedBy(**data)


class DiscountedPriceSchema(helpers.BaseSchema):
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        load_default=None,
    )
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".product_discount.ProductDiscountReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedPrice(**data)


class DiscountedPriceDraftSchema(helpers.BaseSchema):
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    discount = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".product_discount.ProductDiscountReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.DiscountedPriceDraft(**data)


class GeoJsonSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.GeoJson(**data)


class GeoJsonPointSchema(GeoJsonSchema):
    coordinates = marshmallow.fields.List(
        marshmallow.fields.Float(allow_none=True), allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.GeoJsonPoint(**data)


class ImageSchema(helpers.BaseSchema):
    url = marshmallow.fields.String(allow_none=True, load_default=None)
    dimensions = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ImageDimensionsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    label = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Image(**data)


class ImageDimensionsSchema(helpers.BaseSchema):
    w = marshmallow.fields.Integer(allow_none=True, load_default=None)
    h = marshmallow.fields.Integer(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImageDimensions(**data)


class KeyReferenceSchema(helpers.BaseSchema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        load_default=None,
        data_key="typeId",
    )
    key = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.KeyReference(**data)


class LastModifiedBySchema(ClientLoggingSchema):
    attributed_to = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".AttributionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="attributedTo",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.LastModifiedBy(**data)


class MoneySchema(helpers.BaseSchema):
    cent_amount = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="centAmount"
    )
    currency_code = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="currencyCode"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Money(**data)


class PriceSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        load_default=None,
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Price(**data)


class PriceDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceDraft(**data)


class PriceTierSchema(helpers.BaseSchema):
    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="minimumQuantity"
    )
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceTier(**data)


class PriceTierDraftSchema(helpers.BaseSchema):
    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="minimumQuantity"
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceTierDraft(**data)


class QueryPriceSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    value = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    tiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceTierDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QueryPrice(**data)


class ReferenceSchema(helpers.BaseSchema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        load_default=None,
        data_key="typeId",
    )
    id = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.Reference(**data)


class ResourceIdentifierSchema(helpers.BaseSchema):
    type_id = marshmallow_enum.EnumField(
        ReferenceTypeId,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="typeId",
    )
    id = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ResourceIdentifier(**data)


class ScopedPriceSchema(helpers.BaseSchema):
    id = marshmallow.fields.String(allow_none=True, load_default=None)
    value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        load_default=None,
    )
    current_value = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(__name__, ".CentPrecisionMoneySchema"),
            "highPrecision": helpers.absmod(__name__, ".HighPrecisionMoneySchema"),
        },
        load_default=None,
        data_key="currentValue",
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, load_default=None
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validFrom",
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="validUntil",
    )
    discounted = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".DiscountedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ScopedPrice(**data)


class TypedMoneySchema(MoneySchema):
    type = marshmallow_enum.EnumField(
        MoneyType, by_value=True, allow_none=True, load_default=None
    )
    fraction_digits = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="fractionDigits"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TypedMoney(**data)


class CentPrecisionMoneySchema(TypedMoneySchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CentPrecisionMoney(**data)


class HighPrecisionMoneySchema(TypedMoneySchema):
    precise_amount = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.HighPrecisionMoney(**data)


class TypedMoneyDraftSchema(MoneySchema):
    type = marshmallow_enum.EnumField(
        MoneyType,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    fraction_digits = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="fractionDigits",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.TypedMoneyDraft(**data)


class CentPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CentPrecisionMoneyDraft(**data)


class HighPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):
    precise_amount = marshmallow.fields.Integer(
        allow_none=True, load_default=None, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.HighPrecisionMoneyDraft(**data)
