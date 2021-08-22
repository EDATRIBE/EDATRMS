from ..models import IPModel
from .common import BaseService, SearchKeywordInNameMixin


class IPService(BaseService, SearchKeywordInNameMixin):
    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)

    def _init_model(self):
        self.model = IPModel
