import sqlalchemy as sa
import sqlalchemy.sql as sasql

from .common import metadata
from ..utilities import LocalDateTime

UserModel = sa.Table(
    'staff', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='工作人员ID'),
    sa.Column('user_id', sa.Integer, nullable=False, comment='用户ID', unique=True),

    sa.Column('created_at', LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='创建时间'),

    sa.ForeignKeyConstraint(['user_id'], ['user.id'],ondelete='CASCADE', onupdate='CASCADE'),

    comment='工作人员'
)
