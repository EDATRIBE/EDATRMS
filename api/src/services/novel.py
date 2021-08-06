import string

from ..models import NovelModel
from .common import BaseService


class NovelService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = NovelModel

    async def infos_by_ip_id(self, ip_id):
        if not ip_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.ip_id==ip_id)
            )
            rows = await result.fetchall()

        return [dict(row) for row in rows]