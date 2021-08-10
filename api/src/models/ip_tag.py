import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

IPTagModel = sa.Table(
    'ip_tag', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('ip_id', sa.INTEGER(), nullable=False),
    sa.Column('tag_id', sa.INTEGER(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False,server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column('updated_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_ip_id'),
    sa.ForeignKeyConstraint(('tag_id',), ('tag.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_tag_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_updated_by'),
    sa.UniqueConstraint('ip_id', 'tag_id', name='ip_tag_uqc')
)


class IPTagSchema(Schema):
    id = fields.Integer()
    ipId = fields.Integer(attribute='ip_id')
    tagId = fields.Integer(attribute='tag_id')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updatedBy = fields.Integer(attribute='updated_by')
    updatedAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True

class IPTagsSchema(Schema):
    ipId = fields.Integer(attribute='ip_id')
    tagIds = fields.List(fields.Integer(),attribute='tag_ids')

    class Meta:
        ordered = True