import string

import sqlalchemy.sql as sasql

from ..models import IPTagModel


class IPTagService:

    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

    async def create(self, **data):
        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(IPTagModel).values(**data))
            id = result.lastrowid

        return await self.info(id)

    async def edit(self, id, **data):
        data = {k: v for k, v in data.items() if v is not None}

        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.update(IPTagModel).where(IPTagModel.c.id == id).
                    values(**data)
            )

        return await self.info(id)

    async def delete(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(IPTagModel).where(IPTagModel.c.id == id))

    async def info(self, id):
        if id is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                IPTagModel.select().where(IPTagModel.c.id == id)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def infos(self, ids):
        valid_ids = [v for v in ids if v is not None]

        if valid_ids:
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    IPTagModel.select().where(IPTagModel.c.id.in_(valid_ids))
                )
                d = {v['id']: dict(v) for v in await result.fetchall()}
        else:
            d = {}

        return [d.get(v) for v in ids]

    async def list_ip_tag_items(self, *, ip_id=None,tag_id=None,limit=None, offset=None):
        select_sm = IPTagModel.select()
        count_sm = sasql.select([sasql.func.count()]). \
            select_from(IPTagModel)

        # select_sm = select_sm.order_by(UserModel.c.id.desc())
        if ip_id is not None:
            clause = IPTagModel.c.ip_id == ip_id
            select_sm = select_sm.where(clause)
            count_sm = count_sm.where(clause)
        if tag_id is not None:
            clause = IPTagModel.c.tag_id == tag_id
            select_sm = select_sm.where(clause)
            count_sm = count_sm.where(clause)
        if limit is not None:
            select_sm = select_sm.limit(limit)
        if offset is not None:
            select_sm = select_sm.offset(offset)

        async with self.db.acquire() as conn:
            result = await conn.execute(select_sm)
            rows = [dict(v) for v in await result.fetchall()]

            result = await conn.execute(count_sm)
            total = await result.scalar()

        return (rows, total)