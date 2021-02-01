# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from ..shipping_method import ShippingRateTierType
from .common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

# Fields


# Marshmallow Schemas
class PriceFunctionSchema(helpers.BaseSchema):
    currency_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="currencyCode"
    )
    function = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PriceFunction(**data)


class ShippingMethodSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    localized_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        missing=None,
        data_key="localizedDescription",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".tax_category.TaxCategoryReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    zone_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isDefault"
    )
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethod(**data)


class ShippingMethodDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    name = marshmallow.fields.String(allow_none=True, missing=None)
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    localized_description = LocalizedStringField(
        allow_none=True,
        values=marshmallow.fields.String(allow_none=True),
        metadata={"omit_empty": True},
        missing=None,
        data_key="localizedDescription",
    )
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )
    zone_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ZoneRateDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="zoneRates",
    )
    is_default = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isDefault"
    )
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethodDraft(**data)


class ShippingMethodPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingMethodSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethodPagedQueryResponse(**data)


class ShippingMethodReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingMethodSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShippingMethodReference(**data)


class ShippingMethodResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ShippingMethodResourceIdentifier(**data)


class ShippingMethodUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addShippingRate": helpers.absmod(
                    __name__, ".ShippingMethodAddShippingRateActionSchema"
                ),
                "addZone": helpers.absmod(
                    __name__, ".ShippingMethodAddZoneActionSchema"
                ),
                "changeIsDefault": helpers.absmod(
                    __name__, ".ShippingMethodChangeIsDefaultActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ShippingMethodChangeNameActionSchema"
                ),
                "changeTaxCategory": helpers.absmod(
                    __name__, ".ShippingMethodChangeTaxCategoryActionSchema"
                ),
                "removeShippingRate": helpers.absmod(
                    __name__, ".ShippingMethodRemoveShippingRateActionSchema"
                ),
                "removeZone": helpers.absmod(
                    __name__, ".ShippingMethodRemoveZoneActionSchema"
                ),
                "setDescription": helpers.absmod(
                    __name__, ".ShippingMethodSetDescriptionActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ShippingMethodSetKeyActionSchema"),
                "setLocalizedDescription": helpers.absmod(
                    __name__, ".ShippingMethodSetLocalizedDescriptionActionSchema"
                ),
                "setPredicate": helpers.absmod(
                    __name__, ".ShippingMethodSetPredicateActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingMethodUpdate(**data)


class ShippingMethodUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodUpdateAction(**data)


class ShippingRateSchema(helpers.BaseSchema):
    price = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(
                __name__, ".common.CentPrecisionMoneySchema"
            ),
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
        },
        missing=None,
    )
    free_above = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(
                __name__, ".common.CentPrecisionMoneySchema"
            ),
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="freeAbove",
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isMatching",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                ),
                "CartScore": helpers.absmod(__name__, ".CartScoreTierSchema"),
                "CartValue": helpers.absmod(__name__, ".CartValueTierSchema"),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingRate(**data)


class ShippingRateDraftSchema(helpers.BaseSchema):
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    free_above = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="freeAbove",
    )
    tiers = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "CartClassification": helpers.absmod(
                    __name__, ".CartClassificationTierSchema"
                ),
                "CartScore": helpers.absmod(__name__, ".CartScoreTierSchema"),
                "CartValue": helpers.absmod(__name__, ".CartValueTierSchema"),
            },
        ),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShippingRateDraft(**data)


class ShippingRatePriceTierSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        ShippingRateTierType, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRatePriceTier(**data)


class CartClassificationTierSchema(ShippingRatePriceTierSchema):
    value = marshmallow.fields.String(allow_none=True, missing=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartClassificationTier(**data)


class CartScoreTierSchema(ShippingRatePriceTierSchema):
    score = marshmallow.fields.Float(allow_none=True, missing=None)
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    price_function = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PriceFunctionSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="priceFunction",
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartScoreTier(**data)


class CartValueTierSchema(ShippingRatePriceTierSchema):
    minimum_cent_amount = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="minimumCentAmount"
    )
    price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.MoneySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    is_matching = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="isMatching",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartValueTier(**data)


class ZoneRateSchema(helpers.BaseSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneRate(**data)


class ZoneRateDraftSchema(helpers.BaseSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rates = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ZoneRateDraft(**data)


class ShippingMethodAddShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodAddShippingRateAction(**data)


class ShippingMethodAddZoneActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodAddZoneAction(**data)


class ShippingMethodChangeIsDefaultActionSchema(ShippingMethodUpdateActionSchema):
    is_default = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="isDefault"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeIsDefaultAction(**data)


class ShippingMethodChangeNameActionSchema(ShippingMethodUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeNameAction(**data)


class ShippingMethodChangeTaxCategoryActionSchema(ShippingMethodUpdateActionSchema):
    tax_category = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="taxCategory",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodChangeTaxCategoryAction(**data)


class ShippingMethodRemoveShippingRateActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    shipping_rate = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShippingRateDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="shippingRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodRemoveShippingRateAction(**data)


class ShippingMethodRemoveZoneActionSchema(ShippingMethodUpdateActionSchema):
    zone = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodRemoveZoneAction(**data)


class ShippingMethodSetDescriptionActionSchema(ShippingMethodUpdateActionSchema):
    description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetDescriptionAction(**data)


class ShippingMethodSetKeyActionSchema(ShippingMethodUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetKeyAction(**data)


class ShippingMethodSetLocalizedDescriptionActionSchema(
    ShippingMethodUpdateActionSchema
):
    localized_description = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="localizedDescription",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetLocalizedDescriptionAction(**data)


class ShippingMethodSetPredicateActionSchema(ShippingMethodUpdateActionSchema):
    predicate = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ShippingMethodSetPredicateAction(**data)
