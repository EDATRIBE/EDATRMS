import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

IpModel = sa.Table(
    'ip', metadata,
    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True, comment='IP ID'),
    sa.Column('name', sa.VARCHAR(30), nullable=False, comment='IP名'),
    sa.Column('reserved_names', sa.JSON(), nullable=True, comment='备用IP名dict'),
    sa.Column('intros', sa.JSON(), nullable=True, comment='简介dict'),
    sa.Column('created_by', sa.Integer(), nullable=False, comment='创建者 ID'),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.INTEGER(), nullable=False, comment='最近修改者 ID'),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='最近修改时间'),
    sa.Column('comment', sa.TEXT(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='ip_fkc_updated_by'),
    comment='IP表'
)