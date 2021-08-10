import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

TagModel = sa.Table(
    'tag', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(),nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column('updated_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='tag_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='tag_fkc_updated_by'),
    sa.UniqueConstraint('name',name='tag_uqc_name')
)

class TagReservedNamesSchema(Schema):
    cn = fields.String()
    en = fields.String()
    class Meta:
        ordered = True

class TagSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(1,300))
    reservedNames = fields.Nested('TagReservedNamesSchema', attribute='reserved_names')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updatedBy = fields.Integer(attribute='updated_by')
    updatedAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True