from ...models import NovelSchema
from ...services import StorageService

from functools import reduce


async def dump_novel_info(request, novel):
    if novel is None:
        return None

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)

    vertical_image = await storage_service.info(novel['image_ids'].get('vertical'))
    horizontal_image = await storage_service.info(novel['image_ids'].get('horizontal'))
    novel['images'] = {
        'vertical': vertical_image,
        'horizontal': horizontal_image
    }
    
    novel = NovelSchema().dump(novel)
    return novel


async def dump_novel_infos(request, novels):
    if not novels:
        return []

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)

    vertical_image_ids = [novel['image_ids'].get('vertical') for novel in novels]
    horizontal_image_ids = [novel['image_ids'].get('horizontal') for novel in novels]
    vertical_images = await storage_service.infos(vertical_image_ids)
    horizontal_images = await storage_service.infos(horizontal_image_ids)

    for novel, vertical_image, horizontal_image in zip(
            novels,
            vertical_images,
            horizontal_images
    ):
        novel['images'] = {
            'vertical': vertical_image,
            'horizontal': horizontal_image
        }
        
    novels = [NovelSchema().dump(v) for v in novels]
    return novels