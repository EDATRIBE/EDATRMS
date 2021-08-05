import string

import sqlalchemy.sql as sasql

from ..models import RoleModel
from .common import BaseService

class RoleService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)

    def _init_model(self):
        self.model = RoleModel
