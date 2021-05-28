import sqlalchemy as sa
import sqlalchemy.sql as sasql
from marshmallow import Schema, fields

from .common import metadata
from ..utilities import LocalDateTime

AnimationModel = sa.Table(
    'animation', metadata,
    sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True, comment='Animation ID'),
    sa.Column('ip_id', sa.INTEGER(), nullable=False, comment='IP ID'),
    sa.Column('name', sa.VARCHAR(30), nullable=False, comment='IP名'),
    sa.Column('reserved_names', sa.JSON(), nullable=True, comment='备用IP名 dict'),
    sa.Column('intros', sa.JSON(), nullable=True, comment='简介 dict'),
    sa.Column('image_ids', sa.JSON(), nullable=True, comment='图片ID dict'),
    sa.Column('produced_by', sa.VARCHAR(100), nullable=False,server_default='', comment='出品公司'),
    sa.Column("released_at", LocalDateTime(), nullable=True, comment='上映日期'),
    sa.Column('written_by', sa.VARCHAR(100), nullable=False,server_default='', comment='原著作者'),
    sa.Column('type', sa.VARCHAR(20), nullable=False,server_default='', comment='类型：OVA/OAD etc.'),
    sa.Column('episodes_num', sa.INTEGER(), nullable=False, comment='集数'),
    sa.Column('created_by', sa.INTEGER(), nullable=False, comment='创建者 ID'),
    sa.Column("created_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='创建时间'),
    sa.Column('updated_by', sa.INTEGER(), nullable=False, comment='最近修改者 ID'),
    sa.Column("updated_at", LocalDateTime(), nullable=False,
              server_default=sasql.text('CURRENT_TIMESTAMP'),comment='最近修改时间'),
    sa.Column('comment', sa.TEXT(), nullable=True, comment='备注'),
    sa.ForeignKeyConstraint(('ip_id',), ('ip.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_ip_id'),
    sa.ForeignKeyConstraint(('created_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_created_by'),
    sa.ForeignKeyConstraint(('updated_by',), ('user.id',),
                            ondelete='CASCADE', onupdate='CASCADE', name='animation_fkc_updated_by'),
    comment='animation表'
)