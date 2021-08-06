from ...models import AnimationSchema
from ...services import CaptionService, StorageService, VideoService


async def dump_animation_info(request, animation):
    if animation is None:
        return None

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    images = {}
    for key, value in animation['image_ids'].items():
        file = await storage_service.info(value)
        images[key] = file
    animation['images'] = images

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    videos = await video_service.infos_by_animation_id(animation['id'])
    captions = await caption_service.infos_by_animation_id(animation['id'])
    animation['videos'] = videos
    animation['captions'] = captions

    visible_field = [
        'id', 'ipId', 'name', 'reservedNames', 'intros',
        'producedBy', 'releasedAt', 'type', 'episodesNum', 'sharingAddresses',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'images', 'videos', 'captions'
    ]
    animation = AnimationSchema(only=visible_field).dump(animation)
    return animation


async def dump_animation_infos(request, animations):
    if not animations:
        return []

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for animation in animations:
        images = {}
        for key, value in animation['image_ids'].items():
            file = await storage_service.info(value)
            images[key] = file
        animation['images'] = images

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)

    for animation in animations:
        videos = await video_service.infos_by_animation_id(animation['id'])
        captions = await caption_service.infos_by_animation_id(animation['id'])
        animation['videos'] = videos
        animation['captions'] = captions

    visible_field = [
        'id', 'ipId', 'name', 'reservedNames', 'intros',
        'producedBy', 'releasedAt', 'type', 'episodesNum', 'sharingAddresses',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'images', 'videos', 'captions'
    ]
    animations = [AnimationSchema(only=visible_field).dump(v) for v in animations]
    return animations