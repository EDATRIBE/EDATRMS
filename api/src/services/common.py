import sqlalchemy.sql as sasql


class ServiceException(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)

        self.message = message
        self.code = code


class BaseService:

    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache
        self._init_model()

    def _init_model(self):
        self.model = None
        raise NotImplementedError

    async def create(self, **data):
        async with self.db.acquire() as conn:
            result = await conn.execute(sasql.insert(self.model).values(**data))
            id = result.lastrowid

        return await self.info(id)

    async def edit(self, id, **data):
        data = {k: v for k, v in data.items() if v is not None}

        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.update(self.model).where(self.model.c.id == id).
                    values(**data)
            )

        return await self.info(id)

    async def delete(self, id):
        async with self.db.acquire() as conn:
            await conn.execute(
                sasql.delete(self.model).where(self.model.c.id == id))

    async def info(self, id):
        if id is None:
            return None

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.id == id)
            )
            row = await result.first()

        return None if row is None else dict(row)

    async def infos(self, ids):
        valid_ids = [v for v in ids if v is not None]

        if valid_ids:
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    self.model.select().where(self.model.c.id.in_(valid_ids))
                )
                d = {v['id']: dict(v) for v in await result.fetchall()}
        else:
            d = {}

        return [d.get(v) for v in ids]

    async def list_(self, *, limit=None, offset=None):
        select_sm = self.model.select()
        count_sm = sasql.select([sasql.func.count()]). \
            select_from(self.model)
        # select_sm = select_sm.order_by(self.model.c.id.desc())

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
