import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

IPModel = sa.Table(
    'ip', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(), nullable=False),
    sa.Column('region', sa.VARCHAR(300), nullable=False,server_default=''),
    sa.Column('written_by', sa.VARCHAR(300), nullable=False,server_default=''),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column('updated_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False,server_default=''),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_updated_by'),
    sa.UniqueConstraint('name',name='ip_uqc_name')
)


class IPReservedNamesSchema(Schema):
    jp = fields.String()
    cn = fields.String()
    en = fields.String()
    rm = fields.String()
    misc = fields.String()

    class Meta:
        ordered = True


class IPSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(0,300))
    reservedNames = fields.Nested('IPReservedNamesSchema',attribute='reserved_names')
    region = fields.String(validate=validate.OneOf(['CN','JP','OTHER']))
    writtenBy = fields.String(attribute='written_by',validate=validate.Length(0,300))
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updateBy = fields.Integer(attribute='updated_by')
    updateAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    tags = fields.List(fields.Nested('TagSchema'))
    animations = fields.List(fields.Nested('AnimationSchema'))
    novels = fields.List(fields.Nested('NovelSchema'))

    class Meta:
        ordered = True