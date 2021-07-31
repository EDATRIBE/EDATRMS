from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import AnimationSchema, StorageBucket
from ..services import AnimationService, StorageService
from .common import (ResponseCode, authenticated_staff, copy_file, required_field_validation, response_json,
                     sift_dict_by_key)
from .common_dumper import dump_animation_info, dump_animation_infos

animation = Blueprint('animation', url_prefix='/animation')


@animation.post('/create')
@authenticated_staff()
async def create(request):
    data = AnimationSchema().load(request.json)
    required_field_validation(
        data=data,
        required_field=[
            'ip_id',
            'name',
            'released_at',
            'type',
            'episodes_num'
        ]
    )

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get('image_ids', {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)

    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.create(
        ip_id=data['ip_id'],
        name=data['name'],
        reserved_names=data.get('reserved_names', {}),
        intros=data.get('intros', {}),
        image_ids=data.get('image_ids', {}),
        produced_by=data.get('produced_by', ''),
        released_at=data.get('released_at'),
        type=data.get('type'),
        episodes_num=data.get('episodes_num'),
        sharing_addresses=data.get('sharing_addresses', {}),
        created_by=request.ctx.session['user']['id'],
        updated_by=request.ctx.session['user']['id'],
        comment=data.get('comment', '')
    )

    new_image_ids = {}
    for key, value in data.get('image_ids', {}).items():
        file = await storage_service.info(value)
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.ANIMATION,
            target_path=str(animation['id'])
        )
        new_image_ids[key] = new_file['id']
    animation = await animation_service.edit(
        animation['id'],
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
    required_field_validation(data=data, required_field=['id'])

    id = data['id']
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.info(id)
    if animation is None:
        raise NotFound('')

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get('image_ids', {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)
    new_image_ids = {}
    for key, value in data.get('image_ids', {}).items():
        if animation['image_ids'].get(key) == value:
            new_image_ids[key] = value
            continue
        file = await storage_service.info(value)
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.ANIMATION,
            target_path=str(data['id'])
        )
        new_image_ids[key] = new_file['id']
    if data.get('image_ids') is not None:
        data['image_ids'] = new_image_ids

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=[
            'name',
            'reserved_names',
            'intros',
            'image_ids',
            'produced_by',
            'released_at',
            'type',
            'episodes_num',
            'sharing_addresses',
            'comment'
        ]
    )
    animation = await animation_service.edit(
        id,
        **allowed_data,
        updated_by=request.ctx.session['user']['id']
    )

    return response_json(animation=await dump_animation_info(request, animation))


@animation.post('/delete')
@authenticated_staff()
async def delete(request):
    data = AnimationSchema().load(request.json)
    required_field_validation(data=data, required_field=['id'])

    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animation = await animation_service.info(data['id'])
    if animation is None:
        raise NotFound('')

    await animation_service.delete(data['id'])

    return response_json(animation=await dump_animation_info(request, animation))


@animation.get('/list')
async def list_all(request):
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animations, total = await animation_service.list_animations()

    return response_json(
        animations=await dump_animation_infos(request, animations),
        total=total
    )


@animation.get('/list/<limit:int>/<offset:int>')
async def list_(request, offset, limit):
    animation_service = AnimationService(request.app.config, request.app.db, request.app.cache)
    animations, total = await animation_service.list_animations(limit=limit, offset=offset)

    return response_json(
        animations=await dump_animation_infos(request, animations),
        total=total
    )
