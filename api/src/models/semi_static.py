from marshmallow import Schema, fields, validate


class AnnouncementModel(object):
    __slots__ = (
        'title',
        'mark',
        'uri',
        'created_at',
        'updated_at'
    )


class AnnouncementSchema(Schema):
    title = fields.String()
    mark = fields.String()
    uri = fields.String()
    createdAt = fields.DateTime(attribute='created_at')
    updateAt = fields.DateTime(attribute='updated_at')

    class Meta:
        ordered = True
