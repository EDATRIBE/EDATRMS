import string

import sqlalchemy.sql as sasql

from ..models import IPTagModel
from .common import BaseService


class IPTagService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)

    def _init_model(self):
        self.model = IPTagModel

    async def tag_ids_by_ip_id(self, ip_id):
        if not ip_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.ip_id==ip_id)
            )
            rows = await result.fetchall()

        return [row['tag_id'] for row in rows]


    async def tag_ids_list_by_ip_ids(self, ip_ids):
        valid_ip_ids = [v for v in ip_ids if v is not None]

        if valid_ip_ids:
            d = {valid_ip_id: [] for valid_ip_id in valid_ip_ids}
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    self.model.select().where(self.model.c.ip_id.in_(valid_ip_ids))
                )
                for row in await result.fetchall():
                    d[row['ip_id']].append(dict(row)['tag_id'])
        else:
            d = {}

        return [d.get(ip_id) for ip_id in ip_ids]

    async def delete_by_ip_id(self, ip_id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(self.model).where(self.model.c.ip_id == ip_id))