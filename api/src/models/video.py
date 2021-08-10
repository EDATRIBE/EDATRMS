import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

VideoModel = sa.Table(
    'video', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('animation_id', sa.INTEGER(), nullable=False),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column('updated_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('animation_id',), ('animation.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_animation_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_updated_by')
)




class VideoFileMetaSchema(Schema):
    name = fields.String()
    type = fields.String(validate=validate.OneOf(['MP4','MKV','AV1','OGG']))
    size = fields.Integer()
    quality = fields.String(validate=validate.OneOf(['360p','640P','720P','960P','1080P']))
    class Meta:
        ordered = True


class VideoSchema(Schema):
    id = fields.Integer()
    animationId = fields.Integer(attribute='animation_id')
    fileMeta = fields.Nested('VideoFileMetaSchema',attribute='file_meta')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updatedBy = fields.Integer(attribute='updated_by')
    updatedAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True
