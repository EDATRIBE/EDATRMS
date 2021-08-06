import string

from ..models import VideoModel
from .common import BaseService


class VideoService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = VideoModel

    async def infos_by_animation_id(self, animation_id):
        if not animation_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.animation_id==animation_id)
            )
            rows = await result.fetchall()

        return [dict(row) for row in rows]