from marshmallow import Schema, fields

class ItemSchema(Schema):
    ItemName = fields.Str(required=True)
    Price = fields.Int(required=True)