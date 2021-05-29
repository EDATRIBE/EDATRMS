import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

CaptionModel = sa.Table(
    'caption', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('animation_id', sa.INTEGER(), nullable=False),
    sa.Column('integrated', sa.Boolean(), nullable=False),
    sa.Column('status', sa.VARCHAR(300), nullable=False),
    sa.Column("finished_at", LocalDateTime(), nullable=True),
    sa.Column('file_url', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('file_meta', sa.JSON(), nullable=True),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('animation_id',), ('animation.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_animation_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='caption_fkc_updated_by')
)
