from sanic import Blueprint

from ..services import RoleService
from .common import response_json
from .dupmer import  dump_role_infos


role = Blueprint('role', url_prefix='/role')

@role.get('/list')
async def list_(request):
    role_service = RoleService(request.app.config, request.app.db, request.app.cache)
    roles, total = await role_service.list_()

    return response_json(
        roles=await dump_role_infos(request, roles),
        total=total
    )
