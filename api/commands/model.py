import sqlalchemy as sa

from ..models import metadata

from rich.theme import Theme
from rich.console import Console


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

        self.theme = Theme({
            "info": "green_yellow",
            "warning": "orange1",
            "danger": "red"
        })
        self.console = Console(theme=self.theme)

    def list_models(self):
        tables = metadata.tables
        for t in tables:
            self.console.print(t, style="info")

    def create_tables(self, tables=None):
        if isinstance(tables, str):
            tables = [tables]

        try:
            metadata.create_all(self.engine, tables)

            self.console.print("Done!", style="info")


        except Exception as err:
            self.console.print(err, style="danger")
            return

    def drop_tables(self, tables=None):
        if isinstance(tables, str):
            tables = [tables]

        try:
            metadata.drop_all(self.engine, tables)

            self.console.print("Done!", style="info")

        except Exception as err:
            self.console.print(err, style="danger")
            return
