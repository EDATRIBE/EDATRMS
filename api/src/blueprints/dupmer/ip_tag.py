from ...models import IPTagSchema


async def dump_ip_tag_infos(request, ip_tag_items):
    if not ip_tag_items:
        return []

    ip_tag_items = [IPTagSchema().dump(v) for v in ip_tag_items]
    return ip_tag_items
