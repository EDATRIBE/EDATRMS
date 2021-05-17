import sqlalchemy as sa
from ..services import UserService
import asyncio

class User:
    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

        self.engine = sa.create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
                config['MYSQL_USER'],
                config['MYSQL_PASSWORD'],
                config['MYSQL_HOST'],
                config['MYSQL_PORT'],
                config['MYSQL_DB'])
        )

        self.user_service = UserService(config, db, cache)

    def list_users(self):
        l = asyncio.get_event_loop().run_until_complete(
            self.user_service.list_(
            )
        )
        print(l)

    def create_user(self,name,password):
        asyncio.get_event_loop().run_until_complete(
            self.user_service.create(
                name=str(name),
                password=str(password)
            )
        )

    def edit_user(self):
        pass

    def inspect_user(self):
        pass

    def list_staffs(self):
        pass

    def set_staff(self):
        pass

    def unset_staff(self):
        pass
