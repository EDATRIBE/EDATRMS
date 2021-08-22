import asyncio

from api.src.models import init_db
from api.src.services import AnimationService, UserService, VideoService

from .common import config, fake3l

NEW_ROWS = 600


async def main():
    db = await init_db(config)
    user_service = UserService(config, db, None)
    animation_service = AnimationService(config, db, None)
    video_service = VideoService(config, db, None)

    users, _ = await user_service.list_()
    user_ids = [user["id"] for user in users]
    is_staffs = await user_service.is_staff_by_ids(user_ids)
    staff_ids = [user["id"] for user, is_staff in zip(users, is_staffs) if is_staff]

    animations, _ = await animation_service.list_()
    animation_ids = [animation["id"] for animation in animations]

    for _ in range(NEW_ROWS):
        data = {
            "animation_id": fake3l.random_element(elements=animation_ids),
            "file_meta": {
                "name": fake3l.unique.text(max_nb_chars=10),
                "type": fake3l.random_element(elements=["MP4", "MKV", "AV1", "OGG"]),
                "size": fake3l.random_element(elements=[12434123, 2314, 124, 44325]),
                "quality": fake3l.random_element(
                    elements=["360P", "640P", "720P", "960P", "1080P"]
                ),
            },
            "created_by": fake3l.random_element(elements=staff_ids),
            "updated_by": fake3l.random_element(elements=staff_ids),
            "comment": fake3l.paragraph(nb_sentences=3),
        }
        await video_service.create(**data)


asyncio.run(main())
