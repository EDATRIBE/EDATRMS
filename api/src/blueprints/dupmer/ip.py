from ...models import IPSchema
from ...services import (AnimationService, CaptionService, CaptionUserService,
                         IPTagService, NovelService,
                         StorageService, VideoService)


async def dump_ip_info(request, ip):
    if ip is None:
        return None

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    tag_ids = await ip_tag_service.tag_ids_by_ip_id(ip['id'])
    ip['tag_ids'] = tag_ids

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    animations = await animation_service.infos_by_ip_id(ip['id'])
    for animation in animations:
        images = {}
        for key, value in animation['image_ids'].items():
            file = await storage_service.info(value)
            images[key] = file
        animation['images'] = images
        videos = await video_service.infos_by_animation_id(animation['id'])
        captions = await caption_service.infos_by_animation_id(animation['id'])
        animation['videos'] = videos
        animation['captions'] = captions
    novels = await novel_service.infos_by_ip_id(ip['id'])
    ip['animations'] = animations
    ip['novels'] = novels
    for novel in novels:
        images = {}
        for key, value in novel['image_ids'].items():
            file = await storage_service.info(value)
            images[key] = file
        novel['images'] = images

    visible_field = [
        'id', 'name', 'reservedNames', 'region', 'writtenBy',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'tagIds', 'animations', 'novels'
    ]
    ip = IPSchema(only=visible_field).dump(ip)
    return ip


async def dump_ip_infos(request, ips):
    if not ips:
        return []

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    tag_ids_list = await ip_tag_service.tag_ids_list_by_ip_ids([ip['id'] for ip in ips])
    for ip,tag_ids in zip(ips,tag_ids_list):
        ip['tag_ids'] = tag_ids

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    for ip in ips:
        animations = await animation_service.infos_by_ip_id(ip['id'])
        for animation in animations:
            images = {}
            for key, value in animation['image_ids'].items():
                file = await storage_service.info(value)
                images[key] = file
            animation['images'] = images
            videos = await video_service.infos_by_animation_id(animation['id'])
            captions = await caption_service.infos_by_animation_id(animation['id'])
            user_ids_list = await caption_user_service.user_ids_list_by_caption_ids([caption['id'] for caption in captions])
            for caption,user_ids in zip(captions,user_ids_list):
                caption['user_ids'] = user_ids
            animation['videos'] = videos
            animation['captions'] = captions
        novels = await novel_service.infos_by_ip_id(ip['id'])
        for novel in novels:
            images = {}
            for key, value in novel['image_ids'].items():
                file = await storage_service.info(value)
                images[key] = file
            novel['images'] = images

        ip['animations'] = animations
        ip['novels'] = novels

    visible_field = [
        'id', 'name', 'reservedNames', 'region', 'writtenBy',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'tagIds', 'animations', 'novels'
    ]
    ips = [IPSchema(only=visible_field).dump(v) for v in ips]
    return ips