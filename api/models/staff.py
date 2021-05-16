import sqlalchemy as sa
import sqlalchemy.sql as sasql

from .common import metadata
from ..utilities import LocalDateTime

UserModel = sa.Table(
    'staff', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='工作人员ID'),
    sa.Column('contributor_id', sa.Integer, nullable=False, comment='贡献者ID', unique=True),

    sa.Column('created_at', LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='创建时间'),

    comment='工作人员'
)
