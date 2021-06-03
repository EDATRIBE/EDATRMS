import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from ..utilities import LocalDateTime
from .common import metadata

AnimationModel = sa.Table(
    'animation', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('ip_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(), nullable=True),
    sa.Column('intros', sa.JSON(), nullable=True),
    sa.Column('image_ids', sa.JSON(), nullable=True),
    sa.Column('produced_by', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column("released_at", LocalDateTime(), nullable=True),
    sa.Column('written_by', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('type', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('episodes_num', sa.INTEGER(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_ip_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_updated_by')
)
