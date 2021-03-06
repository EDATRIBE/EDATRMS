import aioredis
from aiomysql.sa import create_engine

from .animation import AnimationModel, AnimationSchema
from .caption import CaptionModel, CaptionSchema
from .caption_user import CaptionUserModel, CaptionUserSchema, CaptionUsersSchema
from .common import metadata
from .ip import IPModel, IPSchema
from .ip_tag import IPTagModel, IPTagSchema, IPTagsSchema
from .novel import NovelModel, NovelSchema
from .role import RoleModel, RoleSchema
from .search import SearchLoadSchema
from .semi_static import AnnouncementModel, AnnouncementSchema
from .storage import FileModel, FileSchema, StorageBucket, StorageRegion
from .tag import TagModel, TagSchema
from .user import StaffModel, UserModel, UserSchema
from .user_role import UserRoleModel, UserRoleSchema
from .video import VideoModel, VideoSchema


async def init_db(config):
    db = await create_engine(
        minsize=config["MYSQL_POOL_MIN_SIZE"],
        maxsize=config["MYSQL_POOL_MIN_SIZE"],
        pool_recycle=3600,
        host=config["MYSQL_HOST"],
        port=config["MYSQL_PORT"],
        user=config["MYSQL_USER"],
        password=str(config["MYSQL_PASSWORD"]),
        db=config["MYSQL_DB"],
        echo=config["DEBUG"],
        charset="utf8mb4",
        connect_timeout=config["MYSQL_TIMEOUT"],
        autocommit=True,
    )
    return db


async def close_db(db):
    db.close()
    await db.wait_closed()


async def init_cache(config):
    cache = await aioredis.create_redis_pool(
        config["REDIS_URI"],
        timeout=config["REDIS_TIMEOUT"],
        minsize=config["REDIS_POOL_MIN_SIZE"],
        maxsize=config["REDIS_POOL_MAX_SIZE"],
    )
    return cache


async def close_cache(cache):
    cache.close()
    await cache.wait_closed()
