import sqlalchemy as sa
from rich.console import Console
from rich.theme import Theme
from sqlalchemy.exc import SQLAlchemyError

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

        self.theme = Theme({
            'info': 'turquoise2',
            'warning': 'orange1',
            'danger': 'red'
        })
        self.console = Console(theme=self.theme)

    def list_models(self):
        tables = metadata.tables
        if not tables :
            self.console.print('[ NULL! ]', style='info')
            return
        for t in tables:
            self.console.print(t, style='info')

    def list_tables(self):
        try:
            temp_metadata = sa.MetaData()
            temp_metadata.reflect(self.engine)
            tables = temp_metadata.tables
        except SQLAlchemyError as err:
            self.console.print(err, style='danger')
            return

        if not tables:
            self.console.print('[ NULL! ]', style='info')
            return
        for t in tables:
            self.console.print(t, style='info')

    def create_tables(self):
        try:
            metadata.create_all(self.engine)
        except SQLAlchemyError as err:
            self.console.print(err, style='danger')
            return

        self.console.print('[ Done! ]', style='info')

    def drop_tables(self):
        try:
            temp_metadata = sa.MetaData()
            temp_metadata.reflect(self.engine)
            temp_metadata.drop_all(self.engine)
        except SQLAlchemyError as err:
            self.console.print(err, style='danger')
            return

        self.console.print('[ Done! ]', style='info')

    def drop_table(self,*table):
        try:
            temp_metadata = sa.MetaData()
            temp_metadata.reflect(self.engine)

            ts = [temp_metadata.tables[t] for t in table]

            temp_metadata.drop_all(self.engine,ts)
        except SQLAlchemyError as err:
            self.console.print(err, style='danger')
            return

        self.console.print('[ Done! ]', style='info')
