import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

IPTagModel = sa.Table(
    'ip_tag', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('ip_id', sa.INTEGER(), nullable=False),
    sa.Column('tag_id', sa.INTEGER(), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column("created_at", LocalDateTime(), nullable=False,server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('updated_by', sa.INTEGER(), nullable=False),
    sa.Column("updated_at", LocalDateTime(), nullable=False,server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_ip_id'),
    sa.ForeignKeyConstraint(('tag_id',), ('tag.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_tag_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_updated_by')
)
