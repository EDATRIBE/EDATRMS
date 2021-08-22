from sanic import Blueprint

from ..services import UserService
from .common import response_json
from .dupmer import dump_user_infos

user = Blueprint("user", url_prefix="/user")


@user.get("/list")
async def list_(request):
    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    users, total = await user_service.list_()

    return response_json(users=await dump_user_infos(request, users), total=total)
