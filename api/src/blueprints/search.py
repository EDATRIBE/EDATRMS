from sanic import Blueprint
from sanic.exceptions import NotFound

from ..models import IPTagsSchema, SearchLoadSchema
from ..services import AnimationService, IPService, NovelService
from .common import (
    ResponseCode,
    authenticated_staff,
    required_field_validation,
    response_json,
    sift_dict_by_key,
)
from .dupmer import dump_ip_info, dump_ip_infos, dump_ip_tag_infos

search = Blueprint("search", url_prefix="/search")


@search.post("/keywords")
async def keywords(request):
    data = SearchLoadSchema().load(request.json)
    required_field_validation(data=data, required_field=["keywords_string"])

    ip_service = IPService(request.app.config, request.app.db, request.app.cache)
    animation_service = AnimationService(
        request.app.config, request.app.db, request.app.cache
    )
    novel_service = NovelService(request.app.config, request.app.db, request.app.cache)

    keywords = data["keywords_string"].split()

    result_ip_ids = set()

    for keyword in keywords:
        ips = await ip_service.search_keyword_in_names(keyword)
        animations = await animation_service.search_keyword_in_names(keyword)
        novels = await novel_service.search_keyword_in_names(keyword)

        result_ip_ids |= (
            set([ip["id"] for ip in ips])
            | set([animation["ip_id"] for animation in animations])
            | set([novel["ip_id"] for novel in novels])
        )

    result_ips = await ip_service.infos(list(result_ip_ids))

    return response_json(ips=await dump_ip_infos(request, result_ips))
