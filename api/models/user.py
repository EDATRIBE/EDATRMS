import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

UserModel = sa.Table(
    'user', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('password', sa.CHAR(64), nullable=False),
    sa.Column('salt', sa.CHAR(64), nullable=False),
    sa.Column('email', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('mobile', sa.CHAR(20), nullable=False, server_default=''),
    sa.Column('intro', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('avatar_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('avatar_id',), ('file.id',),
                            ondelete='SET NULL', onupdate='CASCADE', name='user_fkc_avatar_id'),
    sa.Index('idx_username', 'name', unique=True)
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


StaffModel = sa.Table(
    'staff', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False, unique=True),
    sa.Column('created_at', LocalDateTime, nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('user_id',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='staff_fkc_user_id')
)
