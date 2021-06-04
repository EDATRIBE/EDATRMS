from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, IPSchema
from ..services import StorageService, UserService, IPService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, move_files, validate_nullable, sift_dict_by_key,
                     response_json, dump_ip_info,dump_ip_infos)

ip = Blueprint('ip', url_prefix='/ip')


@ip.post('/publish')
@authenticated_staff()
async def login(request):
    data = IPSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["name"])
    data["reserved_names"] = sift_dict_by_key(
        data=data.get("reserved_names"),
        allowed_key=["jp_name", "cn_name", "en_name", "rm_name", "misc_name"]
    )
    data["intros"] = sift_dict_by_key(
        data=data.get("intros"),
        allowed_key=["cn_intro", "en_intro"]
    )

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.create(
        name=data["name"],
        reserved_names=data["reserved_names"],
        intros=data["intros"],
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
    validate_nullable(data=data,not_null_field=["id"])
    id = data["id"]
    if data.get("reserved_names"):
        data["reserved_names"] = sift_dict_by_key(
            data=data.get("reserved_names"),
            allowed_key=["jp_name", "cn_name", "en_name", "rm_name", "misc_name"]
        )
    if data.get("intros"):
        data["intros"] = sift_dict_by_key(
            data=data.get("intros"),
            allowed_key=["cn_intro", "en_intro"]
        )
    data = sift_dict_by_key(
        data=data,
        allowed_key=["name", "reservedNames", "intros", "comment"]
    )

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ip = await ip_service.edit(
        id,
        **data,
        updated_by=request['session']['user']['id']
    )

    return response_json(ip=await dump_ip_info(request, ip))

@ip.post('/delet')
@authenticated_staff()
async def delet(request):
    data = IPSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["id"])

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
async def list(request, offset, limit):

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    ips, total = await ip_service.list_ips(limit=limit, offset=offset)

    return response_json(
        ips=await dump_ip_infos(request, ips),
        total=total
    )