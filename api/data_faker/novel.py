import asyncio

from api.src.models import init_db
from api.src.services import IPService, NovelService, StorageService, UserService

from .common import config, fake3l

NEW_ROWS = 200


async def main():
    db = await init_db(config)
    user_service = UserService(config, db, None)
    ip_service = IPService(config, db, None)
    novel_service = NovelService(config, db, None)
    storage_service = StorageService(config, db, None)

    users, _ = await user_service.list_()
    user_ids = [user["id"] for user in users]
    is_staffs = await user_service.is_staff_by_ids(user_ids)
    staff_ids = [user["id"] for user, is_staff in zip(users, is_staffs) if is_staff]

    ips, _ = await ip_service.list_()
    ip_ids = [ip["id"] for ip in ips]

    images, _ = await storage_service.list_()
    limbo_image_ids = [image["id"] for image in images if image["bucket"] == "limbo"]

    for _ in range(NEW_ROWS):
        data = {
            "ip_id": fake3l.random_element(elements=ip_ids),
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
            "intros": {
                "en": fake3l["en_US"].paragraph(nb_sentences=5),
                "cn": fake3l["zh_CN"].paragraph(nb_sentences=5),
            },
            "image_ids": {"vertical": fake3l.random_element(elements=limbo_image_ids)},
            "volumes_num": fake3l.random_element(elements=[12, 24, 48, 52]),
            "integrated": fake3l.random_element(elements=[True, False]),
            "file_meta": {
                "name": fake3l.unique.text(max_nb_chars=10),
                "type": fake3l.random_element(elements=["TXT", "PDF", "EPUB"]),
                "size": fake3l.random_element(elements=[12434123, 2314, 124, 44325]),
            },
            "sharing_addresses": {
                "baidu_cloud": {
                    "url": fake3l.url(),
                    "password": fake3l.random_number(digits=4),
                },
                "ali_cloud": {
                    "url": fake3l.url(),
                    "password": fake3l.random_number(digits=4),
                },
            },
            "created_by": fake3l.random_element(elements=staff_ids),
            "updated_by": fake3l.random_element(elements=staff_ids),
            "comment": fake3l.paragraph(nb_sentences=3),
        }
        await novel_service.create(**data)


asyncio.run(main())
