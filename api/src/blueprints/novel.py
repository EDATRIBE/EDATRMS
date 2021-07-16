from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import (IPSchema, NovelSchema, StorageBucket, StorageRegion,
                      UserSchema)
from ..services import IPService, NovelService, StorageService, UserService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     copy_file, required_field_validation, response_json,
                     sift_dict_by_key)
from .common_dumper import (dump_ip_info, dump_ip_infos, dump_novel_info,
                            dump_novel_infos, dump_user_info)

novel = Blueprint('novel', url_prefix='/novel')


@novel.post('/create')
@authenticated_staff()
async def create(request):
    data = NovelSchema().load(request.json)
    required_field_validation(
        data=data,
        required_field=['ip_id', 'name', 'written_by',
                        'volumes_num','integrated','file_addresses']
    )

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get('image_ids', {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)

    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novel = await novel_service.create(
        ip_id=data['ip_id'],
        name=data['name'],
        reserved_names=data.get('reserved_names', {}),
        intros=data.get('intros', {}),
        image_ids=data.get('image_ids', {}),
        written_by=data['written_by'],
        volumes_num=data.get('volumes_num'),
        integrated=data.get('integrated'),
        file_addresses=data['file_addresses'],
        file_meta=data.get('file_meta', {}),
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
            target_bucket=StorageBucket.NOVEL,
            target_path=str(novel['id'])
        )
        new_image_ids[key] = new_file['id']
    novel = await novel_service.edit(
        novel['id'],
        image_ids=new_image_ids
    )

    return response_json(novel=await dump_novel_info(request, novel))


@novel.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing novel id')

    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novel = await novel_service.info(id)
    if novel is None:
        raise NotFound('')

    return response_json(novel=await dump_novel_info(request, novel))


@novel.post('/edit')
@authenticated_staff()
async def edit(request):
    data = NovelSchema().load(request.json)
    required_field_validation(data=data, required_field=['id'])

    id = data['id']
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novel = await novel_service.info(id)
    if novel is None:
        raise NotFound('')

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.get('image_ids', {}).items():
        file = await storage_service.info(value)
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + key)
    new_image_ids = {}
    for key, value in data.get('image_ids', {}).items():
        if novel['image_ids'].get(key) == value:
            new_image_ids[key] = value
            continue
        file = await storage_service.info(value)
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.NOVEL,
            target_path=str(data['id'])
        )
        new_image_ids[key] = new_file['id']
    if data.get('image_ids') is not None:
        data['image_ids'] = new_image_ids

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=[
            'ip_id', 'name', 'reserved_names', 'intros', 'image_ids',
            'written_by', 'volumes_num','integrated','file_addresses','file_meta'
            'comment'
        ]
    )
    novel = await novel_service.edit(
        id,
        **allowed_data,
        updated_by=request.ctx.session['user']['id']
    )

    return response_json(novel=await dump_novel_info(request, novel))


@novel.post('/delete')
@authenticated_staff()
async def delete(request):
    data = NovelSchema().load(request.json)
    required_field_validation(data=data, required_field=['id'])

    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novel = await novel_service.info(data['id'])
    if novel is None:
        raise NotFound('')

    await novel_service.delete(data['id'])

    return response_json(novel=await dump_novel_info(request, novel))


@novel.get('/list')
async def list_all(request):
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novels, total = await novel_service.list_novels()

    return response_json(
        novels=await dump_novel_infos(request, novels),
        total=total
    )


@novel.get('/list/<limit:int>/<offset:int>')
async def list_(request, offset, limit):
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)
    novels, total = await novel_service.list_novels(limit=limit, offset=offset)

    return response_json(
        novels=await dump_novel_infos(request, novels),
        total=total
    )
