import string

import sqlalchemy.sql as sasql

from ..models import UserRoleModel
from .common import BaseService

class UserRoleService(BaseService):

    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)
        
    def _init_model(self):
        self.model = UserRoleModel

    async def delete_by_user_id_and_role_id(self,*,user_id=None,role_id=None):
        async with self.db.acquire() as conn:
            delete_sm = sasql.delete(self.model)

            if user_id is not None:
                clause = self.model.c.user_id == user_id
                delete_sm = delete_sm.where(clause)
            if role_id is not None:
                clause = self.model.c.role_id == role_id
                delete_sm = delete_sm.where(clause)

            await conn.execute(delete_sm)

    async def role_ids_by_user_id(self, user_id):
        if not user_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.user_id==user_id)
            )
            rows = await result.fetchall()

        return [row['role_id'] for row in rows]

