import asyncio
import logging

import fire

from .commands import Model, User
from .config import config, get_log_config
from .models import close_cache, close_db, init_cache, init_db


class Manage:
    def __init__(self, config):
        self.config = config

    async def init(self):
        self.db = await init_db(self.config)
        self.cache = await init_cache(self.config)

        self.model = Model(self.config, self.db, self.cache)
        self.user = User(self.config, self.db, self.cache)

    async def destruct(self):
        await close_cache(self.cache)
        await close_db(self.db)


if __name__ == "__main__":
    logging.config.dictConfig(get_log_config(config))

    manage = Manage(config)
    asyncio.get_event_loop().run_until_complete(manage.init())

    fire.Fire({"model": manage.model, "user": manage.user})

    asyncio.get_event_loop().run_until_complete(manage.destruct())
