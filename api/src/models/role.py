import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

RoleModel = sa.Table(
    'role', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(),nullable=False),
    sa.Column('style', sa.JSON(),nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.UniqueConstraint('name',name='role_uqc_name')
)

class RoleReservedNamesSchema(Schema):
    cn = fields.String(attribute='cn')
    en = fields.String(attribute='en')

    class Meta:
        ordered = True


class RoleStyleSchema(Schema):
    icon = fields.String()
    color = fields.String()

    class Meta:
        ordered = True

class RoleSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(0,300))
    reservedNames = fields.Nested('RoleReservedNamesSchema', attribute='reserved_names')
    style = fields.Nested('RoleStyleSchema')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updatedBy = fields.Integer(attribute='updated_by')
    updatedAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True