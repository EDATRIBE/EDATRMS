import os

import sqlalchemy.sql as sasql

from ..models import FileModel
from .common import BaseService

class StorageService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)

    def _init_model(self):
        self.model = FileModel
