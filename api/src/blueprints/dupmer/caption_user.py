from ...models import CaptionUserSchema


async def dump_caption_user_infos(request, caption_user_items):
    if not caption_user_items:
        return []

    caption_user_items = [CaptionUserSchema().dump(v) for v in caption_user_items]
    return caption_user_items
