from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, TagSchema
from ..services import StorageService, UserService, TagService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, copy_file, validate_nullable, sift_dict_by_key,
                     response_json, dump_tag_info, dump_tag_infos)

tag = Blueprint('tag', url_prefix='/tag')


@tag.post('/publish')
@authenticated_staff()
async def publish(request):
    data = TagSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["name"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.create(
        name=data["name"],
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get("comment", '')
    )
    return response_json(tag=await dump_tag_info(request, tag))

@tag.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing tag id')

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.info(id)
    if tag is None:
        raise NotFound('')

    return response_json(tag=await dump_tag_info(request, tag))


@tag.post('/edit')
@authenticated_staff()
async def edit(request):
    data = TagSchema().load(request.json)
    validate_nullable(data=data,not_null_field=["id"])
    id = data["id"]

    allowed_data = sift_dict_by_key(data=data,allowed_key=["name","comment"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.edit(
        id,
        **allowed_data,
        updated_by=request['session']['user']['id']
    )

    return response_json(tag=await dump_tag_info(request, tag))

@tag.post('/delete')
@authenticated_staff()
async def delete(request):
    data = TagSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["id"])

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tag = await tag_service.info(data["id"])
    if tag is None:
        raise NotFound('')

    await tag_service.delete(data["id"])

    return response_json(tag=await dump_tag_info(request, tag))

@tag.get('/list')
async def list_all(request):

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tags, total = await tag_service.list_tags()

    return response_json(
        tags=await dump_tag_infos(request, tags),
        total=total
    )

@tag.get('/list/<limit:int>/<offset:int>')
async def list(request, offset, limit):

    tag_service = TagService(request.app.config, request.app.db, request.app.cache)
    tags, total = await tag_service.list_tags(limit=limit, offset=offset)

    return response_json(
        tags=await dump_tag_infos(request, tags),
        total=total
    )