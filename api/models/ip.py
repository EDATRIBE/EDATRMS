import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

IpModel = sa.Table(
    'ip', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('reserved_names', sa.JSON(), nullable=True),
    sa.Column('intros', sa.JSON(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_updated_by')
)
