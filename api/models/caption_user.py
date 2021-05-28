import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

CaptionUserModel = sa.Table(
    'caption_user', metadata,
    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True, comment='caption_user ID'),
    sa.Column('caption_id', sa.INTEGER(), nullable=False, comment='caption ID'),
    sa.Column('user_id', sa.INTEGER(), nullable=False, comment='user ID'),
    sa.Column('created_by', sa.INTEGER(), nullable=False, comment='创建者 ID'),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.INTEGER(), nullable=False, comment='最近修改者 ID'),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='最近修改时间'),
    sa.Column('comment', sa.TEXT(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(('caption_id',), ('caption.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_caption_id'),
    sa.ForeignKeyConstraint(('user_id',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_user_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_updated_by'),
    comment='caption_user 表'
)