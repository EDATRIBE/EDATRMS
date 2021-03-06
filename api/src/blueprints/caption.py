from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import CaptionSchema, CaptionUsersSchema
from ..services import CaptionService, CaptionUserService, UserService
from .common import (
    ResponseCode,
    authenticated_staff,
    required_field_validation,
    response_json,
    sift_dict_by_key,
)
from .dupmer import dump_caption_info, dump_caption_infos, dump_caption_user_infos

caption = Blueprint("caption", url_prefix="/caption")


@caption.post("/create")
@authenticated_staff()
async def create(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(
        data=data, required_field=["animation_id", "integrated", "state"]
    )

    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption = await caption_service.create(
        animation_id=data["animation_id"],
        integrated=data["integrated"],
        state=data["state"],
        released_at=data["released_at"],
        file_meta=data.get("file_meta", {}),
        created_by=request.ctx.session["user"]["id"],
        updated_by=request.ctx.session["user"]["id"],
        comment=data.get("comment", ""),
    )

    return response_json(caption=await dump_caption_info(request, caption))


@caption.get("/info/<id:int>")
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message="Missing caption id")

    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption = await caption_service.info(id)
    if caption is None:
        raise NotFound("")

    return response_json(caption=await dump_caption_info(request, caption))


@caption.post("/edit")
@authenticated_staff()
async def edit(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])
    id = data["id"]
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption = await caption_service.info(id)
    if caption is None:
        raise NotFound("")

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=["integrated", "state", "released_at", "file_meta", "comment"],
    )

    caption = await caption_service.edit(
        id, **allowed_data, updated_by=request.ctx.session["user"]["id"]
    )

    return response_json(caption=await dump_caption_info(request, caption))


@caption.post("/delete")
@authenticated_staff()
async def delete(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption = await caption_service.info(data["id"])
    if caption is None:
        raise NotFound("")

    await caption_service.delete(data["id"])

    return response_json(caption=await dump_caption_info(request, caption))


@caption.get("/list")
async def list_all(request):
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    captions, total = await caption_service.list_()

    return response_json(
        captions=await dump_caption_infos(request, captions), total=total
    )


@caption.get("/list/<limit:int>/<offset:int>")
async def list_(request, offset, limit):
    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    captions, total = await caption_service.list_(limit=limit, offset=offset)

    return response_json(
        captions=await dump_caption_infos(request, captions), total=total
    )


@caption.post("/set/users")
@authenticated_staff()
async def caption_user_create(request):
    data = CaptionUsersSchema().load(request.json)
    required_field_validation(data=data, required_field=["caption_id", "user_ids"])

    caption_service = CaptionService(
        request.app.config, request.app.db, request.app.cache
    )
    caption = await caption_service.info(data["caption_id"])
    if caption is None:
        raise NotFound("")

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    for user_id in data["user_ids"]:
        user = await user_service.info(user_id)
        if user is None:
            raise NotFound("")

    caption_user_service = CaptionUserService(
        request.app.config, request.app.db, request.app.cache
    )
    await caption_user_service.delete_by_caption_id(data["caption_id"])
    caption_user_items = []
    for user_id in data["user_ids"]:
        caption_user_item = await caption_user_service.create(
            caption_id=data["caption_id"],
            user_id=user_id,
            created_by=request.ctx.session["user"]["id"],
            updated_by=request.ctx.session["user"]["id"],
            comment=data.get("comment", ""),
        )
        caption_user_items.append(caption_user_item)

    return response_json(
        caption_user_items=await dump_caption_user_infos(request, caption_user_items)
    )
