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
        if not tables :
            self.console.print("[ NULL! ]", style="info")
            return
        for t in tables:
            self.console.print(t, style="info")

    def list_tables(self):
        try:
            temp_metadata = sa.MetaData()
            temp_metadata.reflect(self.engine)
            temp_metadata.drop_all(self.engine)
            tables = temp_metadata.tables
            if not tables :
                self.console.print("[ NULL! ]", style="info")
                return
            for t in tables:
                self.console.print(t, style="info")
        except Exception as err:
            self.console.print(err, style="danger")
            return

    def create_tables(self):
        try:
            metadata.create_all(self.engine)
            self.console.print("[ Done! ]", style="info")
        except Exception as err:
            self.console.print(err, style="danger")
            return

    def drop_tables(self):
        try:
            temp_metadata = sa.MetaData()
            temp_metadata.reflect(self.engine)
            temp_metadata.drop_all(self.engine)
            self.console.print("[ Done! ]", style="info")
        except Exception as err:
            self.console.print(err, style="danger")
            return
