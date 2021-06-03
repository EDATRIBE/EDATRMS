import os
import traceback
from enum import Enum
from functools import wraps

import aiofiles
from marshmallow import Schema, ValidationError, fields
from pymysql.err import DatabaseError
from sanic import response
from sanic.exceptions import SanicException, Unauthorized

from ..models import StorageBucket, StorageRegion, UserSchema
from ..services import ServiceException, StorageService, UserService
from ..utilities import random_string


def authenticated_user():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if request['session'].get('user') is None:
                raise Unauthorized('Not authenticated user')

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator


def authenticated_staff():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if request['session'].get('user') is None:
                raise Unauthorized('Not authenticated user')
            elif request['session'].get('user').get("staff") is not True:
                raise Unauthorized('Not authenticated staff')

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator


class ResponseCode(Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    DIRTY = 'dirty'


def response_json(*, status=200, code=ResponseCode.SUCCESS, message='', **data):
    return response.json(
        {'code': code.value, 'message': message, 'data': data},
        status
    )


def validate_nullable(*, data, not_null_field):
    for key in not_null_field:
        if data.get(key) is None:
            return response_json(code=ResponseCode.DIRTY, message='Missing field: ' + key)

def sift_dict_by_key(*,data,allowed_key):
    if data is None:
        return {}
    else:
        return dict([(key, value) for key, value in data.items() if key in allowed_key])


def handle_exception(request, e):
    status = 500
    code = ResponseCode.FAILURE
    message = repr(e)

    if isinstance(e, SanicException):
        status = e.status_code
    elif isinstance(e, DatabaseError):
        status = 200
        code = ResponseCode.DIRTY
    elif isinstance(e, ValidationError):
        message = e.messages
        code = ResponseCode.DIRTY
        status = 200
    elif isinstance(e, ServiceException):
        message = e.message
        if e.code is not None:
            code = e.code
        status = 200

    data = {}
    if request.app.config['DEBUG']:
        traceback.print_exc()
        data['exception'] = traceback.format_exc()

    return response_json(status=status, code=code, message=message, **data)


async def dump_user_info(request, user):
    if user is None:
        return None

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    user['avatar'] = await storage_service.info(user['avatar_id'])

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    user["staff"] = await user_service.is_staff_by_id(user['id'])

    visible_field = ["id", "name", "email", "mobile", "intro", "avatar", "createdAt", "staff"]
    user = UserSchema(only=visible_field).dump(user)
    return user


async def dump_user_infos(request, users):
    if not users:
        return []

    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)
    files = await storage_service.infos([v['avatar_id'] for v in users])
    for user, file in zip(users, files):
        user['avatar'] = file

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    is_staff_list = await user_service.is_staff_by_ids([v['id'] for v in users])
    for user, is_staff in zip(users, is_staff_list):
        user['staff'] = is_staff

    visible_field = ["id", "name", "email", "mobile", "intro", "avatar", "createdAt", "staff"]
    users = [UserSchema(only=visible_field).dump(v) for v in users]
    return users


async def move_files(request, *, files, target_bucket, target_path):
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)

    local_files = [file for file in files if file["region"] == StorageRegion.LOCAL.value]
    target_dir = os.path.join(
        request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
        target_bucket.value, target_path
    )
    os.makedirs(target_dir, 0o755, True)
    for local_file in local_files:
        source_posi = os.path.join(
            request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
            local_file['bucket'], local_file['path']
        )
        async with aiofiles.open(source_posi, 'rb') as f:
            body = await f.read()

        _, ext = os.path.splitext(local_file["file_meta"]['name'])
        file_name = '{}{}'.format(random_string(16), ext)
        target_posi = os.path.join(target_dir, file_name)
        async with aiofiles.open(target_posi, 'wb') as f:
            await f.write(body)

        await storage_service.edit_file(
            local_file['id'],
            bucket=target_bucket.value,
            path=os.path.join(target_path, file_name),
            updated_by=request['session']['user']['id']
        )
