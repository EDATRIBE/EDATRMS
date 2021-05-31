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
    name = data.get('name')
    password = data['password']

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    if name is not None:
        user = await user_service.info_by_name(name)
    else:
        user = None

    if user is None or sha256_hash(password, user['salt']) != user['password']:
        return response_json(code=ResponseCode.FAILURE, message='Incorrect name or password')

    request['session']['user'] = await dump_user_info(request, user)

    return response_json(user=request['session'].get('user'))


@account.get('/info')
@authenticated_user()
async def info(request):
    user_repr = request['session'].get('user')

    return response_json(user=user_repr)


@account.post('/edit')
@authenticated_user()
async def edit(request):
    id = request['session']['user']['id']

    data = UserSchema().load(request.json)
    username = data.get('username')
    password = data.get('password')
    mobile = data.get('mobile')
    email = data.get('email')
    intro = data.get('intro')
    avatar_id = data.get('avatar_id')

    user_service = UserService(request.app.config, request.app.db, request.app.cache)

    user = await user_service.edit(
        id, username=username, password=password, mobile=mobile,
        email=email, avatar_id=avatar_id, intro=intro
    )

    request['session']['user'] = await dump_user_info(request, user)
    if password is not None:
        await user_service.force_logout(id)
        request['session'].pop('user', None)

    return response_json(user=request['session'].get('user'))


@account.get('/logout')
async def logout(request):
    user_repr = request['session'].pop('user', None)

    return response_json(user=user_repr)
