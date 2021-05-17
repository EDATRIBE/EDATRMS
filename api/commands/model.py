import sqlalchemy as sa

from ..models import metadata


class Model:
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

    def list_models(self):
        tables = metadata.tables
        for t in tables:
            print(t)

    def create_tables(self, tables=None):
        if isinstance(tables, str):
            tables = [tables]

        metadata.create_all(self.engine, tables)

    def drop_tables(self, tables=None):
        if isinstance(tables, str):
            tables = [tables]

        metadata.drop_all(self.engine, tables)
