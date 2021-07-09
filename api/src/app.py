import os

from sanic import Sanic
from sanic_session import AIORedisSessionInterface, Session

from .blueprints import (account, animation, caption, handle_exception, ip,
                         novel, semi_static, storage, tag, video, user)
from .config import config, log_config
from .models import close_cache, close_db, init_cache, init_db

os.makedirs(config['DATA_PATH'], 0o755, True)

app = Sanic(config['NAME'].capitalize(), log_config=log_config)
app.config.update(config)

app.error_handler.add(Exception, handle_exception)

app.static('/local', os.path.join(config['DATA_PATH'], config['LOCAL_FILES_DIR']),
           stream_large_files=True)
app.static('/announcements', os.path.join(config['DATA_PATH'], config['ANNOUNCEMENTS_DIR']),
           stream_large_files=True)

app.blueprint(account)
app.blueprint(storage)
app.blueprint(ip)
app.blueprint(animation)
app.blueprint(video)
app.blueprint(caption)
app.blueprint(novel)
app.blueprint(tag)
app.blueprint(semi_static)
app.blueprint(user)

@app.listener('before_server_start')
async def server_init(app, loop):
    app.db = await init_db(config)
    app.cache = await init_cache(config)

    Session(
        app,
        AIORedisSessionInterface(
            app.cache, expiry=config['SESSION_EXPIRY'],prefix= config.get('PREFIX')
        )
    )


@app.listener('after_server_stop')
async def server_clean(app, loop):
    await close_cache(app.cache)
    await close_db(app.db)


if __name__ == '__main__':
    app.run(
        host=config['HOST'],
        port=config['PORT'],
        debug=config['DEBUG'],
        auto_reload=config['AUTO_RELOAD'],
        access_log=config['ACCESS_LOG'],
        workers=config['WORKERS']
    )
