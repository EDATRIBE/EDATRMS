import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

UserModel = sa.Table(
    'contributor', metadata,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True, comment='贡献者ID'),
    sa.Column('name', sa.VARCHAR(30), nullable=False, comment='贡献者名字', unique=True),
    sa.Column('password', sa.CHAR(64), nullable=False, comment='已加密的密码'),
    sa.Column('salt', sa.CHAR(64), nullable=False, comment='密钥'),
    sa.Column('email', sa.VARCHAR(50), nullable=True, comment='邮箱'),
    sa.Column('mobile', sa.CHAR(20), nullable=True, comment='手机号'),
    sa.Column('intro', sa.TEXT, nullable=True, comment='自我介绍'),
    sa.Column('avatar_id', sa.Integer, nullable=True, comment='头像文件 ID'),

    sa.Column('created_at', LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),
              comment='创建时间'),
    sa.Column('updated_at', LocalDateTime, nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
              comment='更新时间'),

    sa.ForeignKeyConstraint(['avatar_id'], ['file.id'], ondelete='SET NULL', onupdate='CASCADE'),
    sa.Index('idx_username', 'name', unique=True),

    comment='贡献者'
)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    mobile = fields.String()
    intro = fields.String()
    avatarId = fields.Integer(attribute='avatar_id')
    createdAt = fields.DateTime(attribute='created_at')
    updatedAt = fields.DateTime(attribute='updated_at')

    avatar = fields.Nested('FileSchema')