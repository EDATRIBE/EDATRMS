from ...models import RoleSchema


async def dump_role_infos(request, roles):
    if not roles:
        return []

    roles = [RoleSchema().dump(v) for v in roles]
    return roles