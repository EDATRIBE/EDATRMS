from ...models import IPSchema
from ...services import (AnimationService, CaptionService, CaptionUserService,
                         IPTagService, NovelService,
                         StorageService, VideoService)
from functools import reduce


async def dump_ip_info(request, ip):
    if ip is None:
        return None

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)

    tag_ids = await ip_tag_service.tag_ids_by_ip_id(ip['id'])
    animations = await animation_service.infos_by_ip_id(ip['id'])
    novels = await novel_service.infos_by_ip_id(ip['id'])
    ip['tag_ids'] = tag_ids
    ip['animations'] = animations
    ip['novels'] = novels

    animation_ids = [animation['id'] for animation in animations]
    videos_list = await video_service.infos_list_by_animations_ids(animation_ids)
    captions_list = await caption_service.infos_list_by_animations_ids(animation_ids)
    animation_vertical_image_ids = [animation['image_ids'].get('vertical') for animation in animations]
    animation_horizontal_image_ids = [animation['image_ids'].get('horizontal') for animation in animations]
    animation_vertical_images = await storage_service.infos(animation_vertical_image_ids)
    animation_horizontal_images = await storage_service.infos(animation_horizontal_image_ids)
    for animation, videos, captions, animation_vertical_image, animation_horizontal_image in zip(
            animations,
            videos_list,
            captions_list,
            animation_vertical_images,
            animation_horizontal_images
    ):
        animation['videos'] = videos
        animation['captions'] = captions
        animation['images'] = {
            'vertical':animation_vertical_image,
            'horizontal':animation_horizontal_image
        }

    novel_vertical_image_ids = [novel['image_ids'].get('vertical') for novel in novels]
    novel_horizontal_image_ids = [novel['image_ids'].get('horizontal') for novel in novels]
    novel_vertical_images = await storage_service.infos(novel_vertical_image_ids)
    novel_horizontal_images = await storage_service.infos(novel_horizontal_image_ids)
    for novel, novel_vertical_image, novel_horizontal_image in zip(
            novels,
            novel_vertical_images,
            novel_horizontal_images
    ):
        novel['images'] = {
            'vertical': novel_vertical_image,
            'horizontal': novel_horizontal_image
        }

    all_captions = reduce(lambda l1, l2: l1 + l2, captions_list, [])
    all_caption_ids = [caption['id'] for caption in all_captions]
    user_ids_list = await caption_user_service.user_ids_list_by_caption_ids(all_caption_ids)
    for caption, user_ids in zip(all_captions, user_ids_list):
        caption['user_ids'] = user_ids

    ip = IPSchema().dump(ip)
    return ip


async def dump_ip_infos(request, ips):
    if not ips:
        return []

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)

    ip_ids = [ip['id'] for ip in ips]
    tag_ids_list = await ip_tag_service.tag_ids_list_by_ip_ids(ip_ids)
    animations_list = await animation_service.infos_list_by_ip_ids(ip_ids)
    novels_list = await novel_service.infos_list_by_ip_ids(ip_ids)
    for ip, animations, novels, tag_ids in zip(ips, animations_list, novels_list, tag_ids_list):
        ip['tag_ids'] = tag_ids
        ip['animations'] = animations
        ip['novels'] = novels

    all_animations = reduce(lambda l1, l2: l1 + l2, animations_list, [])
    all_animation_ids = [animation['id'] for animation in all_animations]
    videos_list = await video_service.infos_list_by_animations_ids(all_animation_ids)
    captions_list = await caption_service.infos_list_by_animations_ids(all_animation_ids)
    all_animation_vertical_image_ids = [animation['image_ids'].get('vertical') for animation in all_animations]
    all_animation_horizontal_image_ids = [animation['image_ids'].get('horizontal') for animation in all_animations]
    all_animation_vertical_images = await storage_service.infos(all_animation_vertical_image_ids)
    all_animation_horizontal_images = await storage_service.infos(all_animation_horizontal_image_ids)
    for animation, videos, captions, animation_vertical_image, animation_horizontal_image in zip(
            all_animations,
            videos_list,
            captions_list,
            all_animation_vertical_images,
            all_animation_horizontal_images
    ):
        animation['videos'] = videos
        animation['captions'] = captions
        animation['images'] = {
            'vertical':animation_vertical_image,
            'horizontal':animation_horizontal_image
        }

    all_novels = reduce(lambda l1, l2: l1 + l2, novels_list, [])
    all_novel_vertical_image_ids = [novel['image_ids'].get('vertical') for novel in all_novels]
    all_novel_horizontal_image_ids = [novel['image_ids'].get('horizontal') for novel in all_novels]
    all_novel_vertical_images = await storage_service.infos(all_novel_vertical_image_ids)
    all_novel_horizontal_images = await storage_service.infos(all_novel_horizontal_image_ids)
    for novel,novel_vertical_image, novel_horizontal_image in zip(
            all_novels,
            all_novel_vertical_images,
            all_novel_horizontal_images
    ):
        novel['images'] = {
            'vertical':novel_vertical_image,
            'horizontal':novel_horizontal_image
        }

    all_captions = reduce(lambda l1, l2: l1 + l2, captions_list, [])
    all_caption_ids = [caption['id'] for caption in all_captions]
    user_ids_list = await caption_user_service.user_ids_list_by_caption_ids(all_caption_ids)
    for caption, user_ids in zip(all_captions, user_ids_list):
        caption['user_ids'] = user_ids

    ips = [IPSchema().dump(v) for v in ips]
    return ips
