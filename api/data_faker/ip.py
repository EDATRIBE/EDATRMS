import asyncio

from api.src.models import init_db
from api.src.services import IPService, UserService

from .common import config, fake3l

NEW_ROWS = 10


async def main():
    db = await init_db(config)
    user_service = UserService(config, db, None)
    ip_service = IPService(config, db, None)

    users, _ = await user_service.list_()
    user_ids = [user["id"] for user in users]
    is_staffs = await user_service.is_staff_by_ids(user_ids)
    staff_ids = [user["id"] for user, is_staff in zip(users, is_staffs) if is_staff]

    for _ in range(NEW_ROWS):
        data = {
            "name": fake3l.unique.text(max_nb_chars=10),
            "reserved_names": {
                "en": fake3l["en_US"].text(max_nb_chars=10),
                "cn": fake3l["zh_CN"].text(max_nb_chars=10),
                "jp": fake3l["ja_JP"].text(max_nb_chars=10),
                "rm": fake3l["en_US"].text(max_nb_chars=10),
                "reserved": fake3l.text(max_nb_chars=10)
                + fake3l.text(max_nb_chars=10)
                + fake3l.text(max_nb_chars=10),
            },
            "region": fake3l.random_element(elements=("CN", "JP", "OTHER")),
            "written_by": fake3l["ja_JP"].name(),
            "created_by": fake3l.random_element(elements=staff_ids),
            "updated_by": fake3l.random_element(elements=staff_ids),
            "comment": fake3l.paragraph(),
        }
        await ip_service.create(**data)


asyncio.run(main())
