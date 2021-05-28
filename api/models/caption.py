import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

CaptionModel = sa.Table(
    'caption', metadata,
    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True, comment='Caption ID'),
    sa.Column('animation_id', sa.INTEGER(), nullable=False, comment='Animation ID'),
    sa.Column('integrated', sa.Boolean(), nullable=False, comment='字幕完整性'),
    sa.Column('status', sa.VARCHAR(30), nullable=False, comment='字幕状态：doing/todo/done'),
    sa.Column("finished_at", LocalDateTime(), nullable=True, comment='完成日期'),
    sa.Column('file_url', sa.TEXT(), nullable=False, comment='文件url'),
    sa.Column('file_meta', sa.JSON(), nullable=True, comment='文件元信息'),
    sa.Column('created_by', sa.INTEGER(), nullable=False, comment='创建者 ID'),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.INTEGER(), nullable=False, comment='最近修改者 ID'),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='最近修改时间'),
    sa.Column('comment', sa.TEXT(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(('animation_id',), ('animation.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_animation_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_updated_by'),
    comment='caption 表'
)