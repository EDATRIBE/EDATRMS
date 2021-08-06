from ...models import UserSchema
from ...services import (RoleService, StorageService, UserRoleService,
                         UserService)


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