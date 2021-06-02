from sanic import Blueprint

from ..utilities import sha256_hash
from ..models import UserSchema
from ..services import UserService
from ..models import UserSchema
from .common import response_json, ResponseCode, authenticated_user, authenticated_staff, dump_user_info

account = Blueprint('account', url_prefix='/account')


@account.post('/login')
async def login(request):
    data = UserSchema().load(request.json)
    for key in ["name","password"]:
        if data.get(key) is None:
            return response_json(code=ResponseCode.FAILURE, message='Missing key: '+key)

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
    id = request['session']['user']['id']
    data = UserSchema().load(request.json)

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    for key, value in data.items():
        if key not in ["name", "password", "mobile", "email", "intro", "avatar_id"]:
            del data[key]
    user = await user_service.edit(id, **data)

    if data.get("password") is not None:
        await user_service.force_logout(id)
        request['session'].pop('user', None)
    else:
        request['session']['user'] = await dump_user_info(request, user)

    return response_json(user=request['session']['user'])


@account.get('/logout')
async def logout(request):
    user_repr = request['session'].pop('user', None)

    return response_json(user=user_repr)
