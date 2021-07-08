import os
from enum import Enum

import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, post_dump, validate

from ..config import config
from ..utilities import LocalDateTime
from .common import metadata


class StorageRegion(Enum):
    LOCAL = 'local'

class StorageBucket(Enum):
    LIMBO = 'limbo'
    USER = 'user'
    ANIMATION = 'animation'
    NOVEL = 'novel'



FileModel = sa.Table(
    'file', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('region', sa.VARCHAR(300), nullable=False),
    sa.Column('bucket', sa.VARCHAR(300), nullable=False),
    sa.Column('path', sa.VARCHAR(300), nullable=False),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column('updated_at', LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='file_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='file_fkc_updated_by')
)


class FileMetaSchema(Schema):
    name = fields.String()
    type = fields.String()
    size = fields.Integer()
    class Meta:
        ordered = True

class FileSchema(Schema):
    id = fields.Integer()
    region = fields.String(validate=validate.OneOf([
        StorageRegion.LOCAL.value
    ]))
    bucket = fields.String(validate=validate.OneOf([
        StorageBucket.LIMBO.value,
        StorageBucket.USER.value,
        StorageBucket.ANIMATION.value,
        StorageBucket.NOVEL.value,
    ]))
    path = fields.String()
    fileMeta = fields.Nested('FileMetaSchema',attribute='file_meta')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updateBy = fields.Integer(attribute='updated_by')
    updateAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True

    @post_dump
    def add_url(self, data, many):
        url = ''
        if data['region'] == StorageRegion.LOCAL.value:
            url = '{}{}'.format(config['LOCAL_FILES_URL_BASE'],
                                os.path.join(data['bucket'], data['path']))
        return dict(data, url=url)
