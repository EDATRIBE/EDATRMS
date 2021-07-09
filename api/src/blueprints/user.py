from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema
from ..services import StorageService, UserService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     copy_file, required_field_validation, response_json,
                     sift_dict_by_key)
from .common_dumper import dump_user_info, dump_user_infos

user = Blueprint('user', url_prefix='/user')

@user.get('/list')
async def list_(request):
    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    users, total = await user_service.list_users()

    return response_json(
        users=await dump_user_infos(request, users),
        total=total
    )
