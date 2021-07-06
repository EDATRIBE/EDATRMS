import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields,validate

from ..utilities import LocalDateTime
from .common import metadata,BaiduCloudSchema

CaptionModel = sa.Table(
    'caption', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('animation_id', sa.INTEGER(), nullable=False),
    sa.Column('integrated', sa.Boolean(), nullable=False),
    sa.Column('state', sa.VARCHAR(300), nullable=False),
    sa.Column("released_at", LocalDateTime(), nullable=True),
    sa.Column('file_addresses', sa.JSON(), nullable=False),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('animation_id',), ('animation.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_animation_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_updated_by')
)

class CaptionFileAddressesSchema(Schema):
    baiduCloud = fields.Nested('BaiduCloudSchema',attribute='baidu_cloud')
    class Meta:
        ordered = True

class CaptionFileMetaSchema(Schema):
    name = fields.String()
    type = fields.String(validate=validate.OneOf(['SRT','ASS','VTT','SUP','SSA']))
    size = fields.Integer()
    class Meta:
        ordered = True

class CaptionSchema(Schema):
    id = fields.Integer()
    animationId = fields.Integer(attribute='animation_id')
    integrated = fields.Boolean()
    state = fields.String(validate=validate.OneOf(['TODO','DOING','DONE']))
    releasedAt = fields.DateTime(attribute='released_at')
    fileAddresses = fields.Nested('CaptionFileAddressesSchema',attribute='file_addresses')
    fileMeta = fields.Nested('CaptionFileMetaSchema',attribute='file_meta')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updateBy = fields.Integer(attribute='updated_by')
    updateAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))


    contributorIds = fields.List(fields.Integer(), attribute='contributor_ids')
    contributors = fields.List(fields.Nested('UserSchema'))

    class Meta:
        ordered = True