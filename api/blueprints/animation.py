from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, IPSchema, AnimationSchema
from ..services import StorageService, UserService, IPService, AnimationService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, copy_file, validate_nullable, sift_dict_by_key,
                     response_json, dump_ip_info, dump_ip_infos, dump_animation_info, dump_animation_infos)

animation = Blueprint('animation', url_prefix='/animation')


@animation.post('/publish')
@authenticated_staff()
async def publish(request):
    data = AnimationSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["ip_id", "name", "released_at", "type", "episodes_num"])

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get("image_ids", {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)

    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.create(
        ip_id=data["ip_id"],
        name=data["name"],
        reserved_names=data.get("reserved_names", {}),
        intros=data.get("intros", {}),
        image_ids=data.get("image_ids", {}),
        produced_by=data.get("produced_by", ''),
        released_at=data.get("released_at"),
        written_by=data.get("written_by", ''),
        type=data.get("type"),
        episodes_num=data.get("episodes_num"),
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get("comment", '')
    )

    new_image_ids = {}
    for key, value in data.get("image_ids", {}).items():
        file = await storage_service.info(value)
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.ANIMATION,
            target_path=str(animation["id"])
        )
        new_image_ids[key] = new_file["id"]
    animation = await animation_service.edit(
        animation["id"],
        image_ids=new_image_ids
    )

    return response_json(animation=await dump_animation_info(request, animation))


@animation.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing animation id')

    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.info(id)
    if animation is None:
        raise NotFound('')

    return response_json(animation=await dump_animation_info(request, animation))


@animation.post('/edit')
@authenticated_staff()
async def edit(request):
    data = AnimationSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["id"])
    id = data["id"]

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get("image_ids", {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)
    new_image_ids = {}
    for key, value in data.get("image_ids", {}).items():
        file = await storage_service.info(value)
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.ANIMATION,
            target_path=str(data["id"])
        )
        new_image_ids[key] = new_file["id"]
    if data.get("image_ids") is not None:
        data["image_ids"] = new_image_ids

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=[
            "ip_id", "name", "reserved_names", "intros", "image_ids",
            "produced_by", "released_at", "written_by", "type", "episodes_num",
            "comment"
        ]
    )
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.edit(
        id,
        **allowed_data,
        updated_by=request['session']['user']['id']
    )

    return response_json(animation=await dump_animation_info(request, animation))


@animation.post('/delete')
@authenticated_staff()
async def delete(request):
    data = AnimationSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["id"])

    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.info(data["id"])
    if animation is None:
        raise NotFound('')

    await animation_service.delete(data["id"])

    return response_json(animation=await dump_animation_info(request, animation))


@animation.get('/list')
async def list_all(request):
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animations, total = await animation_service.list_animations()

    return response_json(
        ips=await dump_animation_infos(request, animations),
        total=total
    )


@animation.get('/list/<limit:int>/<offset:int>')
async def list(request, offset, limit):
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animations, total = await animation_service.list_animations(limit=limit, offset=offset)

    return response_json(
        ips=await dump_animation_infos(request, animations),
        total=total
    )
