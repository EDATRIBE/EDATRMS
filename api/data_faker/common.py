from faker import Faker

from api.src.config import config

locale_list = ["en-US", "zh_CN", "ja_JP"]
fake3l = Faker(locale_list)
