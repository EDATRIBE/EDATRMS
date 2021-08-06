from sanic import Blueprint

from ..models import StorageBucket, UserSchema
from ..services import StorageService, UserService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_user, copy_file, required_field_validation, response_json,
                     sift_dict_by_key)
from .dupmer import dump_user_info

account = Blueprint('account', url_prefix='/account')


@account.post('/login')
async def login(request):
    data = UserSchema().load(request.json)
    required_field_validation(data=data, required_field=['email', 'password'])

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user = await user_service.info_by_email(data['email'])

    if user is None or sha256_hash(data['password'], user['salt']) != user['password']:
        return response_json(code=ResponseCode.FAILURE, message='Incorrect name or password')

    request.ctx.session['user'] = await dump_user_info(request, user)

    return response_json(user=request.ctx.session['user'])


@account.get('/info')
@authenticated_user()
async def info(request):
    user_repr = request.ctx.session['user']

    return response_json(user=user_repr)


@account.post('/edit')
@authenticated_user()
async def edit(request):
    data = UserSchema().load(request.json)
    data = sift_dict_by_key(
        data=data,
        allowed_key=[
            'password',
            'qq',
            'email',
            'intro',
            'avatar_id'
        ]
    )

    cond1 = data.get('avatar_id') is not None
    cond2 = (request.ctx.session['user'].get('avatar') is None or
                    request.ctx.session['user'].get('avatar').get('id') != data.get('avatar_id'))
    if cond1 and cond2:
        storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
        file = await storage_service.info(data['avatar_id'])
        if file is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing file: ' + data.get('avatar_id'))
        if file['created_by'] != request.ctx.session['user']['id']:
            return response_json(code=ResponseCode.FAILURE, message='Access deny')
        new_file = await copy_file(
            request,
            file=file,
            target_bucket=StorageBucket.USER,
            target_path=str(request.ctx.session['user']['id'])
        )
        data['avatar_id'] = new_file['id']

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user = await user_service.edit(
        request.ctx.session['user']['id'],
        **data
    )

    if data.get('password') is not None:
        await user_service.force_logout(request.ctx.session['user']['id'])
        request.ctx.session.pop('user', None)
    else:
        request.ctx.session['user'] = await dump_user_info(request, user)

    return response_json(user=request.ctx.session.get('user',{}))


@account.get('/logout')
async def logout(request):
    user_repr = request.ctx.session.pop('user', None)

    return response_json(user=user_repr)

