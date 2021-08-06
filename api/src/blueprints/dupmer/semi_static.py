from ...models import AnnouncementSchema


async def dump_announcement_infos(request, announcements):
    if not announcements:
        return []

    visible_field = ['title', 'uri', 'createdAt', 'updateAt']

    announcements = [AnnouncementSchema(only=visible_field).dump(v) for v in announcements]
    return announcements
