import sqlalchemy as sa
from ..services import UserService
import asyncio

import schema

class User:
    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

        # self.engine = sa.create_engine(
        #     'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        #         config['MYSQL_USER'],
        #         config['MYSQL_PASSWORD'],
        #         config['MYSQL_HOST'],
        #         config['MYSQL_PORT'],
        #         config['MYSQL_DB'])
        # )

        self.user_service = UserService(config, db, cache)

    def list_users(self):
        l = asyncio.get_event_loop().run_until_complete(
            self.user_service.list_(
            )
        )
        print(l)

    def create_user(self,**kwargs):
        try:
            date = schema.Schema(
                {
                    # "id": schema.Use(int,error="请检查用户id：整型数字"),
                    "name": schema.Regex(
                        r"^[a-zA-Z][a-zA-Z0-9_]{0,29}$",
                        error="请检查用户名：字母开头，可包含字母、数字、下划线，长度不超过30位"
                    ),
                    "password": schema.And(
                        schema.Use(str),
                        schema.Regex(
                            r"[a-zA-Z0-9_]{6,18}$"
                        ),
                        error="请检查密码：可包含字母、数字、下划线，长度为6-18位"
                    ),
                    schema.Optional("email"):schema.Regex(
                        r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
                        error="请检查邮箱格式"
                    ),
                    schema.Optional("mobile"): schema.And(
                        schema.Use(str),
                        schema.Regex(
                            r"^\d{11}$"
                        ),
                        error="请检查手机号码：11位数字"
                    ),
                    schema.Optional("intro"): schema.Use(str, error="请检查自我介绍"),
                    schema.Optional("comment"): schema.Use(str, error="请检查备注")
                },
                ignore_extra_keys=True
            ).validate(kwargs)
        except schema.SchemaError as err:
            print(err)
            return
        print(date)

        re = asyncio.get_event_loop().run_until_complete(
            self.user_service.create(**date)
        )

        print(re)

    def inspect_user(self,**kwargs):
        print(kwargs)

    def list_staffs(self,id):
        print(id)

    def set_staff(self):
        pass

    def unset_staff(self):
        pass
