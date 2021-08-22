from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import TagSchema
from ..services import TagService
from .common import (
    ResponseCode,
    authenticated_staff,
    required_field_validation,
    response_json,
    sift_dict_by_key,
)
from .dupmer import dump_tag_info, dump_tag_infos

tag = Blueprint("tag", url_prefix="/tag")


@tag.post("/create")
@authenticated_staff()
async def create(request):
    data = TagSchema().load(request.json)
    required_field_validation(data=data, required_field=["name"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.create(
        name=data["name"],
        reserved_names=data.get("reserved_names", {}),
        created_by=request.ctx.session["user"]["id"],
        updated_by=request.ctx.session["user"]["id"],
        comment=data.get("comment", ""),
    )
    return response_json(tag=await dump_tag_info(request, tag))


@tag.get("/info/<id:int>")
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message="Missing tag id")

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.info(id)
    if tag is None:
        raise NotFound("")

    return response_json(tag=await dump_tag_info(request, tag))


@tag.post("/edit")
@authenticated_staff()
async def edit(request):
    data = TagSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    id = data["id"]
    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.info(id)
    if tag is None:
        raise NotFound("")

    allowed_data = sift_dict_by_key(
        data=data, allowed_key=["name", "reserved_names", "comment"]
    )

    tag = await tag_service.edit(
        id, **allowed_data, updated_by=request.ctx.session["user"]["id"]
    )

    return response_json(tag=await dump_tag_info(request, tag))


@tag.post("/delete")
@authenticated_staff()
async def delete(request):
    data = TagSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.info(data["id"])
    if tag is None:
        raise NotFound("")

    await tag_service.delete(data["id"])

    return response_json(tag=await dump_tag_info(request, tag))


@tag.get("/list")
async def list_all(request):

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tags, total = await tag_service.list_()

    return response_json(tags=await dump_tag_infos(request, tags), total=total)


@tag.get("/list/<limit:int>/<offset:int>")
async def list_(request, offset, limit):

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tags, total = await tag_service.list_(limit=limit, offset=offset)

    return response_json(tags=await dump_tag_infos(request, tags), total=total)
