from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, IPSchema,IPTagSchema
from ..services import StorageService, UserService, IPService,TagService,IPTagService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, copy_file, required_field_validation, sift_dict_by_key,
                     response_json, dump_ip_info, dump_ip_infos)

ip = Blueprint('ip', url_prefix='/ip')


@ip.post('/create')
@authenticated_staff()
async def create(request):
    data = IPSchema().load(request.json)
    required_field_validation(data=data, required_field=["name"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag_ids = data.get('tag_ids',[])
    for tag_id in tag_ids:
        tag = await tag_service.info(tag_id)
        if tag is None:
            raise NotFound('')

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.create(
        name=data["name"],
        reserved_names=data.get("reserved_names",{}),
        region=data.get("region",''),
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get("comment", '')
    )

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    for tag_id in tag_ids:
        await ip_tag_service.create(
            ip_id=ip['id'],
            tag_id=tag_id,
            created_by=request['session']['user']['id'],
            updated_by=request['session']['user']['id'],
            comment=data.get("comment", '')
        )

    return response_json(ip=await dump_ip_info(request, ip))

@ip.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing ip id')

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.info(id)
    if ip is None:
        raise NotFound('')

    return response_json(ip=await dump_ip_info(request, ip))


@ip.post('/edit')
@authenticated_staff()
async def edit(request):
    data = IPSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])
    id = data["id"]
    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.info(id)
    if ip is None:
        raise NotFound('')

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=["name", "reserved_names", "region", "comment"]
    )

    ip = await ip_service.edit(
        id,
        **allowed_data,
        updated_by=request['session']['user']['id']
    )
    if ip is None:
        raise NotFound('')

    return response_json(ip=await dump_ip_info(request, ip))

@ip.post('/delete')
@authenticated_staff()
async def delete(request):
    data = IPSchema().load(request.json)
    required_field_validation(data=data, required_field=["id"])

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.info(data["id"])
    if ip is None:
        raise NotFound('')

    await ip_service.delete(data["id"])

    return response_json(ip=await dump_ip_info(request, ip))

@ip.get('/list')
async def list_all(request):

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ips, total = await ip_service.list_ips()

    return response_json(
        ips=await dump_ip_infos(request, ips),
        total=total
    )

@ip.get('/list/<limit:int>/<offset:int>')
async def list_(request, offset, limit):

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ips, total = await ip_service.list_ips(limit=limit, offset=offset)

    return response_json(
        ips=await dump_ip_infos(request, ips),
        total=total
    )

@ip.post('/tag/create')
async def ip_tag_create(request):
    data = IPTagSchema().load(request.json)
    required_field_validation(data=data, required_field=["ip_id", "tag_id"])

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = ip_service.info(data["ip_id"])
    if ip is None:
        raise NotFound('')

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = tag_service.info(data["tag_id"])
    if tag is None:
        raise NotFound('')

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    ip_tag_item = await ip_tag_service.create(
        ip_id=data["ip_id"],
        tag_id=data["tag_id"],
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get("comment", '')
    )

    return response_json(ip_tag_item=IPTagSchema().dump(ip_tag_item))


@ip.post('/tag/delete')
async def ip_tag_delete(request):
    data = IPTagSchema().load(request.json)
    required_field_validation(data=data, required_field=["ip_id", "tag_id"])

    ip_tag_service = IPTagService(request.app.config, request.app.db, request.app.cache)
    ip_tag_items,total = await ip_tag_service.list_ip_tag_items(
        ip_id=data['ip_id'],
        tag_id=data['tag_id']
    )
    if total < 1:
        raise NotFound('')

    await ip_tag_service.delete(ip_tag_items[0]["id"])

    return response_json(ip_tag_item=IPTagSchema().dump(ip_tag_items[0]))
