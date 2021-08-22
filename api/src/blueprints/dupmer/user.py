from functools import reduce

from ...models import UserSchema
from ...services import (
    CaptionService,
    CaptionUserService,
    StorageService,
    UserRoleService,
    UserService,
)


async def dump_user_info(request, user):
    if user is None:
        return None

    storage_service = StorageService(
        request.app.config, request.app.db, request.app.cache
    )
    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user_role_service = UserRoleService(
        request.app.config, request.app.db, request.app.cache
    )

    user["avatar"] = await storage_service.info(user["avatar_id"])
    user["staff"] = await user_service.is_staff_by_id(user["id"])
    user["roleIds"] = await user_role_service.role_ids_by_user_id(user["id"])

    visible_field = [
        "id",
        "name",
        "email",
        "qq",
        "intro",
        "avatar",
        "createdAt",
        "staff",
        "roleIds",
    ]
    user = UserSchema(only=visible_field).dump(user)
    return user


async def dump_user_infos(request, users):
    if not users:
        return []

    storage_service = StorageService(
        request.app.config, request.app.db, request.app.cache
    )
    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user_role_service = UserRoleService(
        request.app.config, request.app.db, request.app.cache
    )
    caption_user_service = CaptionUserService(
        request.app.config, request.app.db, request.app.cache
    )
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )

    avatars = await storage_service.infos([v["avatar_id"] for v in users])
    is_staff_list = await user_service.is_staff_by_ids([v["id"] for v in users])
    role_ids_list = await user_role_service.role_ids_list_by_user_ids(
        [v["id"] for v in users]
    )

    caption_ids_list = await caption_user_service.caption_ids_list_by_user_ids(
        [v["id"] for v in users]
    )
    all_caption_ids = list(set(reduce(lambda l1, l2: l1 + l2, caption_ids_list, [])))
    all_captions = await caption_service.infos(all_caption_ids)
    d = {}
    for caption in all_captions:
        d[caption["id"]] = caption["animation_id"]

    for user, avatar, is_staff, role_ids, caption_ids in zip(
        users, avatars, is_staff_list, role_ids_list, caption_ids_list
    ):
        user["avatar"] = avatar
        user["staff"] = is_staff
        user["role_ids"] = role_ids
        user["animation_ids"] = []
        for caption_id in caption_ids:
            user["animation_ids"].append(d.get(caption_id))

    visible_field = [
        "id",
        "name",
        "email",
        "qq",
        "intro",
        "avatar",
        "createdAt",
        "staff",
        "roleIds",
        "animationIds",
    ]

    users = [UserSchema(only=visible_field).dump(v) for v in users]
    return users
