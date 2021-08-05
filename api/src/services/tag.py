import string

from ..models import TagModel
from .common import BaseService

class TagService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = TagModel
