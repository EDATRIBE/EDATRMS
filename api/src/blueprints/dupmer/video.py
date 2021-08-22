from ...models import VideoSchema


async def dump_video_info(request, video):
    if video is None:
        return None

    video = VideoSchema().dump(video)
    return video


async def dump_video_infos(request, videos):
    if not videos:
        return []

    videos = [VideoSchema().dump(v) for v in videos]
    return videos
