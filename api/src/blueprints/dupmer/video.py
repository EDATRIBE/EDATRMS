from ...models import VideoSchema


async def dump_video_info(request, video):
    if video is None:
        return None

    visible_field = [
        'id', 'animationId', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment'
    ]
    video = VideoSchema(only=visible_field).dump(video)
    return video


async def dump_video_infos(request, videos):
    if not videos:
        return []

    visible_field = [
        'id', 'animationId', 'fileMeta',
        'createdBy', 'createdAt', 'updateBy', 'updateAt', 'comment'
    ]
    videos = [VideoSchema(only=visible_field).dump(v) for v in videos]
    return videos