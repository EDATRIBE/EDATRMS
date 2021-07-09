import string

import sqlalchemy.sql as sasql

from ..models import CaptionUserModel


class CaptionUserService:

    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

    async def create(self, **data):
        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(CaptionUserModel).values(**data))
            id = result.lastrowid

        return await self.info(id)

    async def edit(self, id, **data):
        data = {k: v for k, v in data.items() if v is not None}

        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.update(CaptionUserModel).where(CaptionUserModel.c.id == id).
                    values(**data)
            )

        return await self.info(id)

    async def delete(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(CaptionUserModel).where(CaptionUserModel.c.id == id))

    async def delete_by_caption_id(self,caption_id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(CaptionUserModel).where(CaptionUserModel.c.caption_id == caption_id))

    async def info(self, id):
        if id is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                CaptionUserModel.select().where(CaptionUserModel.c.id == id)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def infos(self, ids):
        valid_ids = [v for v in ids if v is not None]

        if valid_ids:
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    CaptionUserModel.select().where(CaptionUserModel.c.id.in_(valid_ids))
                )
                d = {v['id']: dict(v) for v in await result.fetchall()}
        else:
            d = {}

        return [d.get(v) for v in ids]

    async def list_caption_user_items(self, *, caption_id=None,user_id=None,limit=None, offset=None):
        select_sm = CaptionUserModel.select()
        count_sm = sasql.select([sasql.func.count()]). \
            select_from(CaptionUserModel)

        # select_sm = select_sm.order_by(UserModel.c.id.desc())
        if caption_id is not None:
            clause = CaptionUserModel.c.caption_id == caption_id
            select_sm = select_sm.where(clause)
            count_sm = count_sm.where(clause)
        if user_id is not None:
            clause = CaptionUserModel.c.user_id == user_id
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