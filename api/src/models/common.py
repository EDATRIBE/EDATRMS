import sqlalchemy as sa
from marshmallow import Schema, fields, validate

metadata = sa.MetaData()

class BaiduCloudSchema(Schema):
    url = fields.String()
    password = fields.String()
    class Meta:
        ordered = True
