# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ReferenceTypeId
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class ReviewSchema(BaseResourceSchema):
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
    uniqueness_value = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="uniquenessValue",
    )
    locale = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    author_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="authorName",
    )
    title = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    text = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
            "discount-code": helpers.absmod(
                __name__, ".discount_code.DiscountCodeReferenceSchema"
            ),
            "inventory-entry": helpers.absmod(
                __name__, ".inventory.InventoryEntryReferenceSchema"
            ),
            "order-edit": helpers.absmod(
                __name__, ".order_edit.OrderEditReferenceSchema"
            ),
            "order": helpers.absmod(__name__, ".order.OrderReferenceSchema"),
            "payment": helpers.absmod(__name__, ".payment.PaymentReferenceSchema"),
            "product-discount": helpers.absmod(
                __name__, ".product_discount.ProductDiscountReferenceSchema"
            ),
            "product-type": helpers.absmod(
                __name__, ".product_type.ProductTypeReferenceSchema"
            ),
            "product": helpers.absmod(__name__, ".product.ProductReferenceSchema"),
            "review": helpers.absmod(__name__, ".ReviewReferenceSchema"),
            "shipping-method": helpers.absmod(
                __name__, ".shipping_method.ShippingMethodReferenceSchema"
            ),
            "shopping-list": helpers.absmod(
                __name__, ".shopping_list.ShoppingListReferenceSchema"
            ),
            "state": helpers.absmod(__name__, ".state.StateReferenceSchema"),
            "store": helpers.absmod(__name__, ".store.StoreReferenceSchema"),
            "tax-category": helpers.absmod(
                __name__, ".tax_category.TaxCategoryReferenceSchema"
            ),
            "type": helpers.absmod(__name__, ".type.TypeReferenceSchema"),
            "zone": helpers.absmod(__name__, ".zone.ZoneReferenceSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
    )
    included_in_statistics = marshmallow.fields.Boolean(
        allow_none=True, missing=None, data_key="includedInStatistics"
    )
    rating = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Review(**data)


class ReviewDraftSchema(helpers.BaseSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    uniqueness_value = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="uniquenessValue",
    )
    locale = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    author_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="authorName",
    )
    title = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    text = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountResourceIdentifierSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartResourceIdentifierSchema"),
            "category": helpers.absmod(
                __name__, ".category.CategoryResourceIdentifierSchema"
            ),
            "channel": helpers.absmod(
                __name__, ".channel.ChannelResourceIdentifierSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
            ),
            "customer": helpers.absmod(
                __name__, ".customer.CustomerResourceIdentifierSchema"
            ),
            "discount-code": helpers.absmod(
                __name__, ".discount_code.DiscountCodeResourceIdentifierSchema"
            ),
            "inventory-entry": helpers.absmod(
                __name__, ".inventory.InventoryEntryResourceIdentifierSchema"
            ),
            "order-edit": helpers.absmod(
                __name__, ".order_edit.OrderEditResourceIdentifierSchema"
            ),
            "order": helpers.absmod(__name__, ".order.OrderResourceIdentifierSchema"),
            "payment": helpers.absmod(
                __name__, ".payment.PaymentResourceIdentifierSchema"
            ),
            "product-discount": helpers.absmod(
                __name__, ".product_discount.ProductDiscountResourceIdentifierSchema"
            ),
            "product-type": helpers.absmod(
                __name__, ".product_type.ProductTypeResourceIdentifierSchema"
            ),
            "product": helpers.absmod(
                __name__, ".product.ProductResourceIdentifierSchema"
            ),
            "review": helpers.absmod(__name__, ".ReviewResourceIdentifierSchema"),
            "shipping-method": helpers.absmod(
                __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
            ),
            "shopping-list": helpers.absmod(
                __name__, ".shopping_list.ShoppingListResourceIdentifierSchema"
            ),
            "state": helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
            "store": helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
            "tax-category": helpers.absmod(
                __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
            ),
            "type": helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
            "zone": helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    rating = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReviewDraft(**data)


class ReviewPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReviewSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReviewPagedQueryResponse(**data)


class ReviewRatingStatisticsSchema(helpers.BaseSchema):
    average_rating = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="averageRating"
    )
    highest_rating = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="highestRating"
    )
    lowest_rating = marshmallow.fields.Float(
        allow_none=True, missing=None, data_key="lowestRating"
    )
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    ratings_distribution = marshmallow.fields.Raw(
        allow_none=True, missing=None, data_key="ratingsDistribution"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ReviewRatingStatistics(**data)


class ReviewReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ReviewSchema"),
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
        return models.ReviewReference(**data)


class ReviewResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.ReviewResourceIdentifier(**data)


class ReviewUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "setAuthorName": helpers.absmod(
                    __name__, ".ReviewSetAuthorNameActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".ReviewSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".ReviewSetCustomTypeActionSchema"
                ),
                "setCustomer": helpers.absmod(
                    __name__, ".ReviewSetCustomerActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".ReviewSetKeyActionSchema"),
                "setLocale": helpers.absmod(__name__, ".ReviewSetLocaleActionSchema"),
                "setRating": helpers.absmod(__name__, ".ReviewSetRatingActionSchema"),
                "setTarget": helpers.absmod(__name__, ".ReviewSetTargetActionSchema"),
                "setText": helpers.absmod(__name__, ".ReviewSetTextActionSchema"),
                "setTitle": helpers.absmod(__name__, ".ReviewSetTitleActionSchema"),
                "transitionState": helpers.absmod(
                    __name__, ".ReviewTransitionStateActionSchema"
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

        return models.ReviewUpdate(**data)


class ReviewUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewUpdateAction(**data)


class ReviewSetAuthorNameActionSchema(ReviewUpdateActionSchema):
    author_name = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="authorName",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetAuthorNameAction(**data)


class ReviewSetCustomFieldActionSchema(ReviewUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetCustomFieldAction(**data)


class ReviewSetCustomTypeActionSchema(ReviewUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True,
        values=marshmallow.fields.Raw(allow_none=True),
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetCustomTypeAction(**data)


class ReviewSetCustomerActionSchema(ReviewUpdateActionSchema):
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetCustomerAction(**data)


class ReviewSetKeyActionSchema(ReviewUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetKeyAction(**data)


class ReviewSetLocaleActionSchema(ReviewUpdateActionSchema):
    locale = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetLocaleAction(**data)


class ReviewSetRatingActionSchema(ReviewUpdateActionSchema):
    rating = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetRatingAction(**data)


class ReviewSetTargetActionSchema(ReviewUpdateActionSchema):
    target = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountResourceIdentifierSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartResourceIdentifierSchema"),
            "category": helpers.absmod(
                __name__, ".category.CategoryResourceIdentifierSchema"
            ),
            "channel": helpers.absmod(
                __name__, ".channel.ChannelResourceIdentifierSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupResourceIdentifierSchema"
            ),
            "customer": helpers.absmod(
                __name__, ".customer.CustomerResourceIdentifierSchema"
            ),
            "discount-code": helpers.absmod(
                __name__, ".discount_code.DiscountCodeResourceIdentifierSchema"
            ),
            "inventory-entry": helpers.absmod(
                __name__, ".inventory.InventoryEntryResourceIdentifierSchema"
            ),
            "order-edit": helpers.absmod(
                __name__, ".order_edit.OrderEditResourceIdentifierSchema"
            ),
            "order": helpers.absmod(__name__, ".order.OrderResourceIdentifierSchema"),
            "payment": helpers.absmod(
                __name__, ".payment.PaymentResourceIdentifierSchema"
            ),
            "product-discount": helpers.absmod(
                __name__, ".product_discount.ProductDiscountResourceIdentifierSchema"
            ),
            "product-type": helpers.absmod(
                __name__, ".product_type.ProductTypeResourceIdentifierSchema"
            ),
            "product": helpers.absmod(
                __name__, ".product.ProductResourceIdentifierSchema"
            ),
            "review": helpers.absmod(__name__, ".ReviewResourceIdentifierSchema"),
            "shipping-method": helpers.absmod(
                __name__, ".shipping_method.ShippingMethodResourceIdentifierSchema"
            ),
            "shopping-list": helpers.absmod(
                __name__, ".shopping_list.ShoppingListResourceIdentifierSchema"
            ),
            "state": helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
            "store": helpers.absmod(__name__, ".store.StoreResourceIdentifierSchema"),
            "tax-category": helpers.absmod(
                __name__, ".tax_category.TaxCategoryResourceIdentifierSchema"
            ),
            "type": helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
            "zone": helpers.absmod(__name__, ".zone.ZoneResourceIdentifierSchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetTargetAction(**data)


class ReviewSetTextActionSchema(ReviewUpdateActionSchema):
    text = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetTextAction(**data)


class ReviewSetTitleActionSchema(ReviewUpdateActionSchema):
    title = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewSetTitleAction(**data)


class ReviewTransitionStateActionSchema(ReviewUpdateActionSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ReviewTransitionStateAction(**data)
