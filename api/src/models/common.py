import sqlalchemy as sa
from marshmallow import Schema, fields, validate

metadata = sa.MetaData()


class BaiduCloudSchema(Schema):
    url = fields.String()
    password = fields.String()

    class Meta:
        ordered = True


class AliCloudSchema(Schema):
    url = fields.String()
    password = fields.String()

    class Meta:
        ordered = True


class SharingAddressesSchema(Schema):
    baiduCloud = fields.Nested("BaiduCloudSchema", attribute="baidu_cloud")
    aliCloud = fields.Nested("AliCloudSchema", attribute="ali_cloud")


class ReservedNamesSchema(Schema):
    jp = fields.String()
    cn = fields.String()
    en = fields.String()
    rm = fields.String()
    misc = fields.String()

    class Meta:
        ordered = True


class IntrosSchema(Schema):
    cn = fields.String(attribute="cn")
    en = fields.String(attribute="en")

    class Meta:
        ordered = True


class ImageIdsSchema(Schema):
    horizontal = fields.Integer()
    vertical = fields.Integer()
    reserved = fields.Integer()

    class Meta:
        ordered = True
