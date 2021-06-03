import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from ..utilities import LocalDateTime
from .common import metadata

VideoModel = sa.Table(
    'video', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('animation_id', sa.INTEGER(), nullable=False),
    sa.Column('file_url', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('file_meta', sa.JSON(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('animation_id',), ('animation.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_animation_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='video_fkc_updated_by')
)
