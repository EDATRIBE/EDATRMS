from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema
from ..services import StorageService, UserService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, move_files, validate_nullable,sift_dict_by_key,
                     response_json)

account = Blueprint('account', url_prefix='/account')


@account.post('/login')
async def login(request):
    data = UserSchema().load(request.json)
    validate_nullable(data=data, not_null_field=["name", "password"])

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user = await user_service.info_by_name(data['name'])

    if user is None or sha256_hash(data['password'], user['salt']) != user['password']:
        return response_json(code=ResponseCode.FAILURE, message='Incorrect name or password')

    request['session']['user'] = await dump_user_info(request, user)

    return response_json(user=request['session']['user'])


@account.get('/info')
@authenticated_user()
async def info(request):
    user_repr = request['session']['user']

    return response_json(user=user_repr)


@account.post('/edit')
@authenticated_user()
async def edit(request):
    user = request['session']['user']
    data = UserSchema().load(request.json)
    data = sift_dict_by_key(data=data,allowed_key=["name", "password", "mobile", "email", "intro", "avatar_id"])

    if data.get("avatar_id") is not None:
        storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
        file = await storage_service.info(data["avatar_id"])
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + data.get("avatar_id"))
        if file['created_by'] != user['id']:
            return response_json(code=ResponseCode.FAILURE, message='Access deny')
        await move_files(request,files=[file],target_bucket=StorageBucket.USER,target_path=str(user['id']))

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user = await user_service.edit(user['id'], **data)

    if data.get("password") is not None:
        await user_service.force_logout(user['id'])
        request['session'].pop('user', None)
    else:
        request['session']['user'] = await dump_user_info(request, user)

    return response_json(user=request['session']['user'])


@account.get('/logout')
async def logout(request):
    user_repr = request['session'].pop('user', None)

    return response_json(user=user_repr)
