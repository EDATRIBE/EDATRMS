import string

import sqlalchemy.sql as sasql

from ..models import CaptionUserModel
from .common import BaseService

class CaptionUserService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = CaptionUserModel

    async def delete_by_caption_id(self,caption_id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(self.model).where(self.model.c.caption_id == caption_id))

    async def user_ids_by_caption_id(self, caption_id):
        if not caption_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.caption_id==caption_id)
            )
            rows = await result.fetchall()

        return [row['user_id'] for row in rows]
