from marshmallow import Schema, fields, post_dump

from commercetools.helpers import OptionalList


class RemoveEmptyValuesMixin:
    @post_dump
    def remove_empty_values(self, data):
        """Remove the key, value pairs for which the value is None.continue

        This doesn't work if allow_none is set. And in the future we might also
        want to remove values which are already the default to minimise the
        params.

        """
        result = {}
        for k, v in data.items():
            if v is not None:
                result[k] = v
        return result


class AbstractDeleteSchema(Schema, RemoveEmptyValuesMixin):
    version = fields.Integer()


class AbstractQuerySchema(Schema, RemoveEmptyValuesMixin):
    where = OptionalList(fields.String())
    sort = OptionalList(fields.String())
    expand = OptionalList(fields.String())
    limit = OptionalList(fields.Int())
    offset = OptionalList(fields.Int())
