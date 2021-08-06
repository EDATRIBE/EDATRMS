import string

from ..models import IPModel
from .common import BaseService


class IPService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = IPModel