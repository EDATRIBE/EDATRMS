import string

import sqlalchemy.sql as sasql

from ..utilities import random_string, sha256_hash
from ..models import UserModel, StaffModel


class UserService:

    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

    async def create(self, **data):
        data['salt'] = random_string(64)
        data['password'] = sha256_hash(data['password'], data['salt'])

        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(UserModel).values(**data))
            id = result.lastrowid

        return await self.info(id)

    async def edit(self, id, **data):
        data = {k: v for k, v in data.items() if v is not None}

        if 'password' in data:
            user = self.info(id)
            data['password'] = sha256_hash(data['password'], user['salt'])

        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.update(UserModel).where(UserModel.c.id == id).
                values(**data)
            )

        return await self.info(id)

    async def info(self, id):
        if id is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                UserModel.select().where(UserModel.c.id == id)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_name(self, name):
        if name is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                UserModel.select().where(UserModel.c.name == name)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_mobile(self, mobile):
        if mobile is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                UserModel.select().where(UserModel.c.mobile == mobile)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def infos(self, ids):
        valid_ids = [v for v in ids if v is not None]
        if valid_ids:
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    UserModel.select().where(UserModel.c.id.in_(valid_ids))
                )
                d = {v['id']: dict(v) for v in await result.fetchall()}
        else:
            d = {}

        return [d.get(v) for v in ids]

    async def list_(self, *, limit=None, offset=None):
        select_sm = UserModel.select()
        count_sm = sasql.select([sasql.func.count()]).\
            select_from(UserModel)

        select_sm = select_sm.order_by(UserModel.c.id.desc())

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


    async def set_staff(self, **data):
        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(StaffModel).values(**data))
            id = result.lastrowid


    async def unset_staff(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(StaffModel).where(StaffModel.c.id == id))

