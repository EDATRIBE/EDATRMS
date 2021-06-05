from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, IPSchema, AnimationSchema,VideoSchema,CaptionSchema
from ..services import StorageService, UserService, IPService, AnimationService,VideoService,CaptionService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, copy_file, validate_nullable, sift_dict_by_key,
                     response_json, dump_ip_info, dump_ip_infos, dump_animation_info, dump_animation_infos,
                     dump_caption_info,dump_caption_infos)

caption = Blueprint('caption', url_prefix='/caption')


@caption.post('/publish')
@authenticated_staff()
async def publish(request):
    data = CaptionSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["animation_id","integrated","state", "file_url"])

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.create(
        animation_id=data["animation_id"],
        integrated=data["integrated"],
        state=data["state"],
        released_at=data["released_at"],
        file_url=data["file_url"],
        file_meta=data.get("file_meta", {}),
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get("comment", '')
    )

    return response_json(caption=await dump_caption_info(request, caption))

@caption.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing caption id')

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.info(id)
    if caption is None:
        raise NotFound('')

    return response_json(caption=await dump_caption_info(request, caption))


@caption.post('/edit')
@authenticated_staff()
async def edit(request):
    data = CaptionSchema().load(request.json)
    validate_nullable(data=data,not_null_field=["id"])
    id = data["id"]

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=["animation_id","integrated","state", "file_url", "file_meta", "comment"]
    )

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.edit(
        id,
        **allowed_data,
        updated_by=request['session']['user']['id']
    )

    return response_json(caption=await dump_caption_info(request, caption))

@caption.post('/delete')
@authenticated_staff()
async def delete(request):
    data = CaptionSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["id"])

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.info(data["id"])
    if caption is None:
        raise NotFound('')

    await caption_service.delete(data["id"])

    return response_json(caption=await dump_caption_info(request, caption))

@caption.get('/list')
async def list_all(request):
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    captions, total = await caption_service.list_captions()

    return response_json(
        captions=await dump_caption_infos(request, captions),
        total=total
    )

@caption.get('/list/<limit:int>/<offset:int>')
async def list(request, offset, limit):

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    captions, total = await caption_service.list_captions(limit=limit, offset=offset)

    return response_json(
        captions=await dump_caption_infos(request, captions),
        total=total
    )
