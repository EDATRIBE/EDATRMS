from enum import Enum
import os

import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, post_dump

from ..config import config
from ..utilities import LocalDateTime
from .common import metadata


class StorageRegion(Enum):
    LOCAL = 'local'


FileModel = sa.Table(
    'file', metadata,
    sa.Column("id", sa.Integer, nullable=False, primary_key=True, comment='ID'),
    sa.Column('region', sa.VARCHAR(30), nullable=False, comment='区域'),
    sa.Column('bucket', sa.VARCHAR(30), nullable=False, comment='桶'),
    sa.Column('path', sa.VARCHAR(100), nullable=False, comment='路径'),
    sa.Column('meta', sa.JSON, nullable=False, comment='元信息'),

    sa.Column('created_by', sa.Integer, nullable=False, comment='上传者 ID'),
    sa.Column("created_at", LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.Integer, nullable=False, comment='最近修改者ID'),
    sa.Column("updated_at", LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='最近更新时间'),

    sa.ForeignKeyConstraint(['created_by', 'updated_by'], ['user.id', 'user.id'],
                            ondelete='CASCADE', onupdate='CASCADE'),

    comment='文件',
)


class FileSchema(Schema):
    id = fields.Integer()
    region = fields.String()
    bucket = fields.String()
    path = fields.String()
    meta = fields.Dict()

    @post_dump
    def add_url(self, data, many):
        url = ''
        if data['region'] == StorageRegion.LOCAL.value:
            url = '{}{}'.format(config['UPLOAD_FILE_URL_BASE'],
                                os.path.join(data['bucket'], data['path']))
        return dict(data, url=url)
