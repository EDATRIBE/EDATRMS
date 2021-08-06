from ...models import CaptionSchema
from ...services import CaptionUserService


async def dump_caption_info(request, caption):
    if caption is None:
        return None

    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)

    userIds = await caption_user_service.user_ids_by_caption_id(caption['id'])
    caption['user_ids'] = userIds

    caption = CaptionSchema().dump(caption)
    return caption


async def dump_caption_infos(request, captions):
    if not captions:
        return []
    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)

    caption_ids = [caption['id'] for caption in captions]
    user_ids_list = await caption_user_service.user_ids_list_by_caption_ids(caption_ids)
    for caption, user_ids in zip(captions, user_ids_list):
        caption['user_ids'] = user_ids

    captions = [CaptionSchema().dump(v) for v in captions]
    return captions