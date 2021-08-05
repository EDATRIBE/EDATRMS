from ..models import (AnimationSchema, AnnouncementSchema, CaptionSchema, CaptionUserSchema, IPSchema, IPTagSchema,
                      NovelSchema, TagSchema, UserSchema, VideoSchema)
from ..services import (AnimationService, CaptionService, CaptionUserService, IPTagService, NovelService, RoleService,
                        StorageService, TagService, UserRoleService, UserService, VideoService)


async def dump_user_info(request, user):
    if user is None:
        return None

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    user['avatar'] = await storage_service.info(user['avatar_id'])

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user['staff'] = await user_service.is_staff_by_id(user['id'])

    user_role_service = UserRoleService(request.app.config, request.app.db, request.app.cache)
    role_service = RoleService(request.app.config, request.app.db, request.app.cache)
    role_ids = await user_role_service.role_ids_by_user_id(user['id'])
    roles = await role_service.infos(role_ids)
    user['roles'] = roles

    visible_field = ['id', 'name', 'email', 'qq', 'intro', 'avatar', 'createdAt', 'staff', 'roles']
    user = UserSchema(only=visible_field).dump(user)
    return user


async def dump_user_infos(request, users):
    if not users:
        return []

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    files = await storage_service.infos([v['avatar_id'] for v in users])
    for user, file in zip(users, files):
        user['avatar'] = file

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    is_staff_list = await user_service.is_staff_by_ids([v['id'] for v in users])
    for user, is_staff in zip(users, is_staff_list):
        user['staff'] = is_staff

    user_role_service = UserRoleService(request.app.config, request.app.db, request.app.cache)
    role_service = RoleService(request.app.config, request.app.db, request.app.cache)
    for user in users:
        role_ids = await user_role_service.role_ids_by_user_id(user['id'])
        roles = await role_service.infos(role_ids)
        user['roles'] = roles

    visible_field = ['id', 'name', 'email', 'qq', 'intro', 'avatar', 'createdAt', 'staff', 'roles']
    users = [UserSchema(only=visible_field).dump(v) for v in users]
    return users


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


async def dump_video_info(request, video):
    if video is None:
        return None

    visible_field = [
        'id', 'animationId', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment'
    ]
    video = VideoSchema(only=visible_field).dump(video)
    return video


async def dump_video_infos(request, videos):
    if not videos:
        return []

    visible_field = [
        'id', 'animationId', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment'
    ]
    videos = [VideoSchema(only=visible_field).dump(v) for v in videos]
    return videos


async def dump_caption_info(request, caption):
    if caption is None:
        return None

    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    contributor_ids = await caption_user_service.user_ids_by_caption_id(caption['id'])
    contributor = await user_service.infos(contributor_ids)
    caption['contributor_ids'] = contributor_ids
    caption['contributors'] = contributor

    visible_field = [
        'id', 'animationId', 'integrated', 'state', 'releasedAt', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment', 'contributors'
    ]
    caption = CaptionSchema(only=visible_field).dump(caption)
    return caption


async def dump_caption_infos(request, captions):
    if not captions:
        return []
    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    user_service = UserService(request.app.config, request.app.db, request.app.cache)

    for caption in captions:
        contributor_ids = await caption_user_service.user_ids_by_caption_id(caption['id'])
        contributor = await user_service.infos(contributor_ids)
        caption['contributor_ids'] = contributor_ids
        caption['contributors'] = contributor

    visible_field = [
        'id', 'animationId', 'integrated', 'state', 'releasedAt', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment', 'contributors'
    ]
    captions = [CaptionSchema(only=visible_field).dump(v) for v in captions]
    return captions


async def dump_caption_user_infos(request, caption_user_items):
    if not caption_user_items:
        return []

    caption_user_items = [CaptionUserSchema().dump(v) for v in caption_user_items]
    return caption_user_items


async def dump_novel_info(request, novel):
    if novel is None:
        return None

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    images = {}
    for key, value in novel['image_ids'].items():
        file = await storage_service.info(value)
        images[key] = file
    novel['images'] = images

    visible_field = [
        'id', 'ipId', 'name', 'reservedNames', 'intros',
        'volumesNum', 'integrated', 'fileMeta', 'sharingAddresses',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'images'
    ]
    novel = NovelSchema(only=visible_field).dump(novel)
    return novel


async def dump_novel_infos(request, novels):
    if not novels:
        return []

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for novel in novels:
        images = {}
        for key, value in novel['image_ids'].items():
            file = await storage_service.info(value)
            images[key] = file
        novel['images'] = images

    visible_field = [
        'id', 'ipId', 'name', 'reservedNames', 'intros',
        'volumesNum', 'integrated', 'fileMeta', 'sharingAddresses',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment',
        'images'
    ]
    novels = [NovelSchema(only=visible_field).dump(v) for v in novels]
    return novels


async def dump_tag_info(request, tag):
    if tag is None:
        return None

    visible_field = ['id', 'name', 'reservedNames', 'createdBy', 'createdAt',
                     'updateBy', 'updateAt', 'comment']
    tag = TagSchema(only=visible_field).dump(tag)
    return tag


async def dump_tag_infos(request, tags):
    if not tags:
        return []

    visible_field = ['id', 'name', 'reservedNames', 'createdBy', 'createdAt',
                     'updateBy', 'updateAt', 'comment']
    tags = [TagSchema(only=visible_field).dump(v) for v in tags]
    return tags


async def dump_ip_tag_infos(request, ip_tag_items):
    if not ip_tag_items:
        return []

    ip_tag_items = [IPTagSchema().dump(v) for v in ip_tag_items]
    return ip_tag_items


async def dump_announcement_infos(request, announcements):
    if not announcements:
        return []

    visible_field = ['title', 'uri', 'createdAt', 'updateAt']

    announcements = [AnnouncementSchema(only=visible_field).dump(v) for v in announcements]
    return announcements
