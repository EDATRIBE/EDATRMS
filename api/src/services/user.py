import json
import string

import sqlalchemy.sql as sasql

from ..models import StaffModel, UserModel
from ..utilities import random_string, sha256_hash


class UserService:

    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

    async def force_logout(self,id):
        keys = await self.cache.keys(pattern=self.config.get('PREFIX')+'*')
        for key in keys:
            bytes_value = await self.cache.get(key)
            try:
                value = json.loads(bytes_value.decode())
            except json.decoder.JSONDecodeError:
                continue
            if type(value) is dict and value.get('user') is not None and value.get('user').get('id') == id:
                await self.cache.set(key, json.dumps({}), expire=self.config.get('SESSION_EXPIRY'))

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
            user = await self.info(id)
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

    async def info_by_name(self, name):
        if name is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                UserModel.select().where(UserModel.c.name == name)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def info_by_email(self, email):
        if email is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                UserModel.select().where(UserModel.c.email == email)
            )
            row = await result.first()

        return None if row is None else dict(row)


    async def list_users(self, *, limit=None, offset=None):
        select_sm = UserModel.select()
        count_sm = sasql.select([sasql.func.count()]). \
            select_from(UserModel)

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

    async def set_staff(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.insert(StaffModel).values(user_id=id)
            )

    async def unset_staff(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(StaffModel).where(StaffModel.c.user_id == id)
            )

    async def is_staff_by_id(self, id):
        if id is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                StaffModel.select().where(StaffModel.c.user_id == id)
            )
            row = await result.first()

        return False if row is None else True

    async def is_staff_by_ids(self, ids):
        valid_ids = [v for v in ids if v is not None]

        if valid_ids:
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    StaffModel.select().where(StaffModel.c.user_id.in_(valid_ids))
                )
                d = {v['user_id']: dict(v) for v in await result.fetchall()}
        else:
            d = {}

        return [d.get(v) != None for v in ids]

