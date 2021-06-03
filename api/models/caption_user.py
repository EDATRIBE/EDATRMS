import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

CaptionUserModel = sa.Table(
    'caption_user', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('caption_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('caption_id',), ('caption.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_caption_id'),
    sa.ForeignKeyConstraint(('user_id',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_user_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_user_fkc_updated_by')
)
