import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

NovelModel = sa.Table(
    'novel', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('ip_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(), nullable=False),
    sa.Column('intros', sa.JSON(), nullable=False),
    sa.Column('image_ids', sa.JSON(), nullable=False),
    sa.Column('written_by', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('volumes_num', sa.INTEGER(), nullable=False),
    sa.Column('integrated', sa.Boolean(), nullable=False),
    sa.Column('file_url', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='novel_fkc_ip_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='novel_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='novel_fkc_updated_by')
)


class NovelReservedNamesSchema(Schema):
    jpName = fields.String(attribute='jp_name')
    cnName = fields.String(attribute='cn_name')
    enName = fields.String(attribute='en_name')
    rmName = fields.String(attribute='rm_name')
    miscName = fields.String(attribute='misc_name')
    class Meta:
        ordered = True

class NovelIntrosSchema(Schema):
    cnIntro = fields.String(attribute='cn_intro')
    enIntro = fields.String(attribute='en_intro')
    class Meta:
        ordered = True

class NovelImageIdsSchema(Schema):
    horizontalImageId = fields.Integer(attribute='horizontal_image_id')
    verticalImageId = fields.Integer(attribute='vertical_image_id')
    reversedImageId = fields.Integer(attribute='reversed_image_id')
    class Meta:
        ordered = True


class NovelFileMetaSchema(Schema):
    name = fields.String()
    type = fields.String(validate=validate.OneOf(['TXT','PDF','EPUB']))
    size = fields.Integer()
    class Meta:
        ordered = True

class NovelSchema(Schema):
    id = fields.Integer()
    ipId = fields.Integer(attribute="ip_id")
    name = fields.String(validate=validate.Length(0,300))
    reservedNames = fields.Nested('NovelReservedNamesSchema',attribute='reserved_names')
    intros = fields.Nested('NovelIntrosSchema')
    imageIds = fields.Nested('NovelImageIdsSchema',attribute='image_ids')
    writtenBy = fields.String(validate=validate.Length(0,300),attribute='written_by')
    volumesNum = fields.Integer(attribute='volumes_num')
    integrated = fields.Boolean()
    fileUrl = fields.String(validate=validate.Length(0, 300), attribute='file_url')
    fileMeta = fields.Nested('NovelFileMetaSchema', attribute='file_meta')
    createdBy = fields.Integer(attribute='created_by')
    createdAt = fields.DateTime(attribute='created_at')
    updateBy = fields.Integer(attribute='updated_by')
    updateAt = fields.DateTime(attribute='updated_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True