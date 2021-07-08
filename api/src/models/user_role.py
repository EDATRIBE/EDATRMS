import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

UserRoleModel = sa.Table(
    'user_role', metadata,
    sa.Column('id', sa.INTEGER(), primary_key=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('role_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', LocalDateTime(), nullable=False,server_default=sasql.text('CURRENT_TIMESTAMP')),
    sa.Column('comment', sa.VARCHAR(300), nullable=False, server_default=''),
    sa.ForeignKeyConstraint(('user_id',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='user_role_fkc_user_id'),
    sa.ForeignKeyConstraint(('role_id',), ('role.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='user_role_fkc_role_id'),
    sa.UniqueConstraint('user_id', 'role_id', name='user_role_uqc')
)
class UserRoleSchema(Schema):
    id = fields.Integer()
    userId = fields.Integer(attribute='user_id')
    roleId = fields.Integer(attribute='role_id')
    createdAt = fields.DateTime(attribute='created_at')
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True