from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import (AnimationSchema, CaptionSchema, CaptionUserSchema,
                      IPSchema, StorageBucket, StorageRegion, UserSchema,
                      VideoSchema)
from ..services import (AnimationService, CaptionService, CaptionUserService,
                        IPService, StorageService, UserService, VideoService)
from ..utilities import sha256_hash
from .common import (ResponseCode, authenticated_staff, authenticated_user,
                     copy_file, required_field_validation, response_json,
                     sift_dict_by_key)
from .common_dumper import (dump_animation_info, dump_animation_infos,
                            dump_caption_info, dump_caption_infos,
                            dump_ip_info, dump_ip_infos, dump_user_info)

caption = Blueprint('caption', url_prefix='/caption')


@caption.post('/create')
@authenticated_staff()
async def create(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(data=data, required_field=['animation_id', 'integrated', 'state', 'file_addresses'])

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    contributor_ids = data.get('contributor_ids',[])
    for contributor_id in contributor_ids:
        contributor = await user_service.info(contributor_id)
        if contributor is None:
            raise NotFound('')

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.create(
        animation_id=data['animation_id'],
        integrated=data['integrated'],
        state=data['state'],
        released_at=data['released_at'],
        file_addresses=data['file_addresses'],
        file_meta=data.get('file_meta', {}),
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get('comment', '')
    )

    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    for contributor_id in contributor_ids:
        await caption_user_service.create(
            caption_id=caption['id'],
            user_id=contributor_id,
            created_by=request['session']['user']['id'],
            updated_by=request['session']['user']['id'],
            comment=data.get('comment', '')
        )


    return response_json(caption=await dump_caption_info(request, caption))

@caption.get('/info/<id:int>')
async def info(request, id):
    if id is None:
        return response_json(code=ResponseCode.DIRTY, message='Missing caption id')

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.info(id)
    if caption is None:
        raise NotFound('')

    return response_json(caption=await dump_caption_info(request, caption))


@caption.post('/edit')
@authenticated_staff()
async def edit(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(data=data, required_field=['id'])
    id = data['id']
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.info(id)
    if caption is None:
        raise NotFound('')

    allowed_data = sift_dict_by_key(
        data=data,
        allowed_key=['animation_id','integrated','state', 'file_addresses', 'file_meta', 'comment']
    )

    caption = await caption_service.edit(
        id,
        **allowed_data,
        updated_by=request['session']['user']['id']
    )

    return response_json(caption=await dump_caption_info(request, caption))

@caption.post('/delete')
@authenticated_staff()
async def delete(request):
    data = CaptionSchema().load(request.json)
    required_field_validation(data=data, required_field=['id'])

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = await caption_service.info(data['id'])
    if caption is None:
        raise NotFound('')

    await caption_service.delete(data['id'])

    return response_json(caption=await dump_caption_info(request, caption))

@caption.get('/list')
async def list_all(request):
    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    captions, total = await caption_service.list_captions()

    return response_json(
        captions=await dump_caption_infos(request, captions),
        total=total
    )

@caption.get('/list/<limit:int>/<offset:int>')
async def list_(request, offset, limit):

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    captions, total = await caption_service.list_captions(limit=limit, offset=offset)

    return response_json(
        captions=await dump_caption_infos(request, captions),
        total=total
    )

@caption.post('/contributor/create')
async def caption_contributor_create(request):
    data = CaptionUserSchema().load(request.json)
    required_field_validation(data=data, required_field=['caption_id', 'contributor_id'])

    caption_service = CaptionService(request.app.config, request.app.db, request.app.cache)
    caption = caption_service.info(data['caption_id'])
    if caption is None:
        raise NotFound('')

    user_service = UserService(request.app.config, request.app.db, request.app.cache)
    contributor = user_service.info(data['contributor_id'])
    if contributor is None:
        raise NotFound('')

    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    caption_user_item = await caption_user_service.create(
        caption_id=data['caption_id'],
        user_id=data['contributor_id'],
        created_by=request['session']['user']['id'],
        updated_by=request['session']['user']['id'],
        comment=data.get('comment', '')
    )

    return response_json(ip_tag_item=CaptionUserSchema().dump(caption_user_item))


@caption.post('/contributor/delete')
async def caption_contributor_delete(request):
    data = CaptionUserSchema().load(request.json)
    required_field_validation(data=data, required_field=['caption_id', 'contributor_id'])

    caption_user_service = CaptionUserService(request.app.config, request.app.db, request.app.cache)
    caption_user_items,total = await caption_user_service.list_caption_user_items(
        caption_id=data['caption_id'],
        user_id=data['contributor_id']
    )
    if total < 1:
        raise NotFound('')

    await caption_user_service.delete(caption_user_items[0]['id'])

    return response_json(ip_tag_item=CaptionUserSchema().dump(caption_user_items[0]))
