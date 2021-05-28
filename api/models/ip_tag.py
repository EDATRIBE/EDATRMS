import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

IPTagModel = sa.Table(
    'ip_tag', metadata,
    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True, comment='ip_tag ID'),
    sa.Column('ip_id', sa.INTEGER(), nullable=False, comment='IP ID'),
    sa.Column('tag_id', sa.INTEGER(), nullable=False, comment='tag ID'),
    sa.Column('created_by', sa.INTEGER(), nullable=False, comment='创建者 ID'),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.INTEGER(), nullable=False, comment='最近修改者 ID'),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='最近修改时间'),
    sa.Column('comment', sa.TEXT(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_ip_id'),
    sa.ForeignKeyConstraint(('tag_id',), ('tag.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_tag_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_tag_fkc_updated_by'),
    comment='ip_tag 表'
)