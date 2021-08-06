from ...models import TagSchema


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