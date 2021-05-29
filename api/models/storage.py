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
    sa.Column("id", sa.INTEGER(), primary_key=True),
    sa.Column('region', sa.VARCHAR(300), nullable=False),
    sa.Column('bucket', sa.VARCHAR(300), nullable=False),
    sa.Column('path', sa.VARCHAR(300), nullable=False),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='file_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='file_fkc_updated_by')
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
            url = '{}{}'.format(config['FILES_URL_BASE'],
                                os.path.join(data['bucket'], data['path']))
        return dict(data, url=url)
