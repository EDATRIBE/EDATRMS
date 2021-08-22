from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import VideoSchema
from ..services import VideoService
from .common import (
    ResponseCode,
    authenticated_staff,
    required_field_validation,
    response_json,
    sift_dict_by_key,
)
from .dupmer import dump_video_info, dump_video_infos

video = Blueprint("video", url_prefix="/video")


@video.post("/create")
@authenticated_staff()
async def create(request):
    data = VideoSchema().load(request.json)
    required_field_validation(data=data, required_field=["animation_id"])

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    video = await video_service.create(
        animation_id=data["animation_id"],
        file_meta=data.get("file_meta", {}),
        created_by=request.ctx.session["user"]["id"],
        updated_by=request.ctx.session["user"]["id"],
        comment=data.get("comment", ""),
    )

    return response_json(video=await dump_video_info(request, video))


@video.get("/info/<id:int>")
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message="Missing video id")

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    video = await video_service.info(id)
    if video is None:
        raise NotFound("")

    return response_json(video=await dump_video_info(request, video))


@video.post("/edit")
@authenticated_staff()
async def edit(request):
    data = VideoSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    id = data["id"]
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    video = await video_service.info(id)
    if video is None:
        raise NotFound("")

    allowed_data = sift_dict_by_key(data=data, allowed_key=["file_meta", "comment"])

    video = await video_service.edit(
        id, **allowed_data, updated_by=request.ctx.session["user"]["id"]
    )

    return response_json(video=await dump_video_info(request, video))


@video.post("/delete")
@authenticated_staff()
async def delete(request):
    data = VideoSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    video = await video_service.info(data["id"])
    if video is None:
        raise NotFound("")

    await video_service.delete(data["id"])

    return response_json(video=await dump_video_info(request, video))


@video.get("/list")
async def list_all(request):
    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    videos, total = await video_service.list_()

    return response_json(videos=await dump_video_infos(request, videos), total=total)


@video.get("/list/<limit:int>/<offset:int>")
async def list_(request, offset, limit):

    video_service = VideoService(request.app.config, request.app.db, request.app.cache)
    videos, total = await video_service.list_(limit=limit, offset=offset)

    return response_json(videos=await dump_video_infos(request, videos), total=total)
