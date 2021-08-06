from ...models import TagSchema


async def dump_tag_info(request, tag):
    if tag is None:
        return None

    tag = TagSchema().dump(tag)
    return tag


async def dump_tag_infos(request, tags):
    if not tags:
        return []

    tags = [TagSchema().dump(v) for v in tags]
    return tags