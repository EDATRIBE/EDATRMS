from enum import Enum
import traceback
from functools import wraps

from sanic import response
from sanic.exceptions import SanicException, Unauthorized
from pymysql.err import IntegrityError

from ..models import  UserSchema
from ..services import ServiceException

class ResponseCode(Enum):
    OK = 'ok'
    FAIL = 'fail'
    DUPLICATE = 'duplicate'

def response_json(code=ResponseCode.OK, message='', status=200, **data):
    return response.json(
        {'code': code.value, 'message': message, 'data': data},
        status
    )

def handle_exception(request, e):
    code = ResponseCode.FAIL
    message = repr(e)
    status = 500

    if isinstance(e, SanicException):
        status = e.status_code
    elif isinstance(e, IntegrityError):
        code = ResponseCode.DUPLICATE
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

    return response_json(code, message, status, **data)

def authenticated():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if request['session'].get('user.py') is None:
                raise Unauthorized('Not authenticated')

            return await f(request, *args, **kwargs)

        return decorated_function

    return decorator