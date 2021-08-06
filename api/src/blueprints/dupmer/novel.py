from ...models import NovelSchema
from ...services import StorageService


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