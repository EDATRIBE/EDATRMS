import datetime
import os

from sanic import Blueprint

from ..models import AnnouncementModel
from .common import response_json
from .dupmer import dump_announcement_infos

semi_static = Blueprint("semi_static", url_prefix="/semi_static")


@semi_static.get("/announcements")
async def list_announcements(request):
    announcements_dir_path = os.path.join(
        request.app.config["DATA_PATH"],
        request.app.config["ANNOUNCEMENTS_DIR"],
    )

    md_file_path_list = []
    for root, dirs, files in os.walk(announcements_dir_path):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext == ".md":
                md_file_path_list.append(str(os.path.join(root, file)))

    marked_announcements_list = []
    unmarked_announcements_list = []
    for md_file_path in md_file_path_list:
        announcement = AnnouncementModel()
        _, full_name = os.path.split(md_file_path)
        name, _ = os.path.splitext(full_name)
        title_and_mark = name.split(request.app.config["ANNOUNCEMENTS_ORDER_PREFIX"], 1)

        announcement.title = title_and_mark[0]
        if len(title_and_mark) == 2:
            announcement.mark = title_and_mark[1]
        else:
            announcement.mark = None

        announcement.uri = md_file_path.replace(
            os.path.join(
                request.app.config["DATA_PATH"], request.app.config["ANNOUNCEMENTS_DIR"]
            ),
            "announcements",
        )

        announcement.created_at = datetime.datetime.fromtimestamp(
            os.path.getctime(md_file_path)
        )

        announcement.updated_at = datetime.datetime.fromtimestamp(
            os.path.getmtime(md_file_path)
        )

        if announcement.mark is not None:
            marked_announcements_list.append(announcement)
        else:
            unmarked_announcements_list.append(announcement)

    sorted_marked_announcements_list = list(
        sorted(marked_announcements_list, key=lambda x: x.mark)
    )

    sorted_unmarked_announcements_list = list(
        sorted(unmarked_announcements_list, key=lambda x: x.created_at, reverse=True),
    )

    sorted_announcements_list = (
        sorted_marked_announcements_list + sorted_unmarked_announcements_list
    )

    return response_json(
        announcements=await dump_announcement_infos(request, sorted_announcements_list)
    )
