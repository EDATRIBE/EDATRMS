import sqlalchemy as sa
from marshmallow import Schema, fields, validate

metadata = sa.MetaData()

class BaiduCloudSchema(Schema):
    url = fields.String(attribute='url')
    password = fields.String(attribute='password')
    class Meta:
        ordered = True
