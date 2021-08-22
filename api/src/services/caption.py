
from ..models import CaptionModel
from .common import BaseService


class CaptionService(BaseService):
    def __init__(self, config, db, cache):
        super().__init__(config, db, cache)

    def _init_model(self):
        self.model = CaptionModel

    async def infos_by_animation_id(self, animation_id):
        if not animation_id:
            return []

        async with self.db.acquire() as conn:
            result = await conn.execute(
                self.model.select().where(self.model.c.animation_id == animation_id)
            )
            rows = await result.fetchall()

        return [dict(row) for row in rows]

    async def infos_list_by_animations_ids(self, animation_ids):
        valid_animation_ids = [v for v in animation_ids if v is not None]

        if valid_animation_ids:
            d = {valid_animation_id: [] for valid_animation_id in valid_animation_ids}
            async with self.db.acquire() as conn:
                result = await conn.execute(
                    self.model.select().where(
                        self.model.c.animation_id.in_(valid_animation_ids)
                    )
                )
                for row in await result.fetchall():
                    d[row["animation_id"]].append(dict(row))
        else:
            d = {}

        return [d.get(animation_id) for animation_id in animation_ids]
