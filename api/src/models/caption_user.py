import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields, validate

from ..utilities import LocalDateTime
from .common import metadata

CaptionUserModel = sa.Table(
    "caption_user",
    metadata,
    sa.Column("id", sa.INTEGER(), primary_key=True),
    sa.Column("caption_id", sa.INTEGER(), nullable=False),
    sa.Column("user_id", sa.INTEGER(), nullable=False),
    sa.Column("created_by", sa.INTEGER(), nullable=False),
    sa.Column(
        "created_at",
        LocalDateTime(),
        nullable=False,
        server_default=sasql.text("CURRENT_TIMESTAMP"),
    ),
    sa.Column("updated_by", sa.INTEGER(), nullable=False),
    sa.Column(
        "updated_at",
        LocalDateTime(),
        nullable=False,
        server_default=sasql.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    ),
    sa.Column("comment", sa.VARCHAR(300), nullable=False, server_default=""),
    sa.ForeignKeyConstraint(
        ("caption_id",),
        ("caption.id",),
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="caption_user_fkc_caption_id",
    ),
    sa.ForeignKeyConstraint(
        ("user_id",),
        ("user.id",),
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="caption_user_fkc_user_id",
    ),
    sa.ForeignKeyConstraint(
        ("created_by",),
        ("user.id",),
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="caption_user_fkc_created_by",
    ),
    sa.ForeignKeyConstraint(
        ("updated_by",),
        ("user.id",),
        ondelete="CASCADE",
        onupdate="CASCADE",
        name="caption_user_fkc_updated_by",
    ),
    sa.UniqueConstraint("caption_id", "user_id", name="caption_user_uqc"),
)


class CaptionUserSchema(Schema):
    id = fields.Integer()
    captionId = fields.Integer(attribute="caption_id")
    userId = fields.Integer(attribute="user_id")
    createdBy = fields.Integer(attribute="created_by")
    createdAt = fields.DateTime(attribute="created_at")
    updatedBy = fields.Integer(attribute="updated_by")
    updatedAt = fields.DateTime(attribute="updated_at")
    comment = fields.String(validate=validate.Length(0, 300))

    class Meta:
        ordered = True


class CaptionUsersSchema(Schema):
    captionId = fields.Integer(attribute="caption_id")
    userIds = fields.List(fields.Integer(), attribute="user_ids")

    class Meta:
        ordered = True
