import os
import traceback
from enum import Enum
from functools import wraps

import aiofiles
from marshmallow import ValidationError
from pymysql.err import DatabaseError
from sanic import response
from sanic.exceptions import SanicException, ServerError, Unauthorized

from ..models import StorageRegion
from ..services import ServiceException, StorageService
from ..utilities import random_string


class ResponseCode(Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    DIRTY = 'dirty'


def response_json(*, status=200, code=ResponseCode.SUCCESS, message='', **data):
    return response.json(
        {'code': code.value, 'message': message, 'data': data},
        status
    )


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


def authenticated_user():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if request.ctx.session.get('user') is None:
                raise Unauthorized('Not authenticated user')

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator


def authenticated_staff():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if request.ctx.session.get('user') is None:
                raise Unauthorized('Not authenticated user')
            elif request.ctx.session.get('user').get('staff') is not True:
                raise Unauthorized('Not authenticated staff')

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator


def required_field_validation(*, data, required_field):
    for key in required_field:
        if data.get(key) is None:
            raise ValidationError(message='Missing field: ' + key)


def sift_dict_by_key(*, data, allowed_key):
    if data is None:
        return {}
    else:
        return dict([(key, value) for key, value in data.items() if key in allowed_key])


@authenticated_user()
async def copy_file(request, *, file, target_bucket, target_path):
    if file is None:
        raise ServerError('invalid usage of func copy_files!')
    storage_service = StorageService(request.app.config, request.app.db, request.app.cache)

    if file['region'] == StorageRegion.LOCAL.value:
        target_dir = os.path.join(
            request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
            target_bucket.value, target_path
        )

        os.makedirs(target_dir, 0o755, True)

        source_posi = os.path.join(
            request.app.config['DATA_PATH'], request.app.config['LOCAL_FILES_DIR'],
            file['bucket'], file['path']
        )
        async with aiofiles.open(source_posi, 'rb') as f:
            body = await f.read()

        _, ext = os.path.splitext(file['file_meta']['name'])
        new_file_name = '{}{}'.format(random_string(16), ext)
        target_posi = os.path.join(target_dir, new_file_name)
        async with aiofiles.open(target_posi, 'wb') as f:
            await f.write(body)

        new_file = await storage_service.create_file(
            region=StorageRegion.LOCAL.value,
            bucket=target_bucket.value,
            path=os.path.join(target_path, new_file_name),
            file_meta=file['file_meta'],
            created_by=request.ctx.session['user']['id'],
            updated_by=request.ctx.session['user']['id']
        )
        return new_file
    else:
        raise ServerError('invalid usage of func copy_files!')



