from functools import reduce

from ...models import AnimationSchema
from ...services import CaptionService, CaptionUserService, StorageService, VideoService


async def dump_animation_info(request, animation):
    if animation is None:
        return None

    storage_service = StorageService(
        request.app.config, request.app.db, request.app.cache
    )
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption_user_service = CaptionUserService(
        request.app.config, request.app.db, request.app.cache
    )

    videos = await video_service.infos_by_animation_id(animation["id"])
    captions = await caption_service.infos_by_animation_id(animation["id"])
    vertical_image = await storage_service.info(animation["image_ids"].get("vertical"))
    horizontal_image = await storage_service.info(
        animation["image_ids"].get("horizontal")
    )
    animation["videos"] = videos
    animation["captions"] = captions
    animation["images"] = {"vertical": vertical_image, "horizontal": horizontal_image}

    caption_ids = [caption["id"] for caption in captions]
    user_ids_list = await caption_user_service.user_ids_list_by_caption_ids(caption_ids)
    for caption, user_ids in zip(captions, user_ids_list):
        caption["user_ids"] = user_ids

    animation = AnimationSchema().dump(animation)
    return animation


async def dump_animation_infos(request, animations):
    if not animations:
        return []

    storage_service = StorageService(
        request.app.config, request.app.db, request.app.cache
    )
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption_user_service = CaptionUserService(
        request.app.config, request.app.db, request.app.cache
    )

    animation_ids = [animation["id"] for animation in animations]
    videos_list = await video_service.infos_list_by_animation_ids(animation_ids)
    captions_list = await caption_service.infos_list_by_animations_ids(animation_ids)
    vertical_image_ids = [
        animation["image_ids"].get("vertical") for animation in animations
    ]
    horizontal_image_ids = [
        animation["image_ids"].get("horizontal") for animation in animations
    ]
    vertical_images = await storage_service.infos(vertical_image_ids)
    horizontal_images = await storage_service.infos(horizontal_image_ids)
    for animation, videos, captions, vertical_image, horizontal_image in zip(
        animations, videos_list, captions_list, vertical_images, horizontal_images
    ):
        animation["videos"] = videos
        animation["captions"] = captions
        animation["images"] = {
            "vertical": vertical_image,
            "horizontal": horizontal_image,
        }

    all_captions = reduce(lambda l1, l2: l1 + l2, captions_list, [])
    all_caption_ids = [caption["id"] for caption in all_captions]
    user_ids_list = await caption_user_service.user_ids_list_by_caption_ids(
        all_caption_ids
    )
    for caption, user_ids in zip(all_captions, user_ids_list):
        caption["user_ids"] = user_ids

    animations = [AnimationSchema().dump(v) for v in animations]
    return animations
