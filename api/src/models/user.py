import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

UserModel = sa.Table(
    'user', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('name', sa.VARCHAR(300), nullable=False),
    sa.Column('password', sa.CHAR(64), nullable=False),
    sa.Column('salt', sa.CHAR(64), nullable=False),
    sa.Column('email', sa.VARCHAR(300), nullable=False),
    sa.Column('qq', sa.CHAR(20), nullable=False, server_default=''),
    sa.Column('intro', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.Column('avatar_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('avatar_id',), ('file.id',),
                            ondelete='SET NULL', onupdate='CASCADE', name='user_fkc_avatar_id'),
    sa.Index('user_idx_name', 'name', unique=True),
    sa.Index('user_idx_email', 'email', unique=True)
)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(1,300))
    password = fields.String(validate=validate.Regexp(r'[a-zA-Z0-9_]{6,18}$'))
    email = fields.String(validate=validate.Email())
    qq = fields.String(validate=validate.Length(1,20))
    intro = fields.String(validate=validate.Length(0,300))
    avatarId = fields.Integer(attribute='avatar_id')
    createdAt = fields.DateTime(attribute='created_at')
    comment = fields.String(validate=validate.Length(0,300))

    avatar = fields.Nested('FileSchema')
    staff = fields.Boolean()
    roleIds = fields.List(fields.Integer(), attribute='role_ids')
    roles = fields.List(fields.Nested('RoleSchema'))

    class Meta:
        ordered = True


StaffModel = sa.Table(
    'staff', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False, unique=True),
    sa.Column('created_at', LocalDateTime(), nullable=False, server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=True, server_default=''),
    sa.ForeignKeyConstraint(('user_id',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='staff_fkc_user_id')
)
