from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import StorageBucket, StorageRegion, UserSchema, IPSchema
from ..services import StorageService, UserService,IPService
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     dump_user_info, move_files, validate_nullable,sift_dict_by_key,
                     response_json)

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
        comment=data.get("comment",'')
    )
    return response_json(ddd=ip)
