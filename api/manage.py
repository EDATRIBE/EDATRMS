import logging
import asyncio

import fire

from .config import config, get_log_config
from .models import init_db, init_cache, close_cache, close_db
from .commands import Model, User

#TODO:
#   Solve The DeprecationWarning:
#       The loop argument is deprecated since Python 3.8, and scheduled for removal in Python 3.10.
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

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


if __name__ == '__main__':
    logging.config.dictConfig(get_log_config(config))

    manage = Manage(config)
    asyncio.get_event_loop().run_until_complete(
        manage.init()
    )

    fire.Fire({
        "model": manage.model,
        "user": manage.user
    })

    asyncio.get_event_loop().run_until_complete(
        manage.destruct()
    )
