from ..services import UserService
import asyncio

import schema
from rich.theme import Theme
from rich.console import Console
from rich.table import Table


class User:
    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

        self.user_service = UserService(config, db, cache)

        self.theme = Theme({
            "info": "green_yellow",
            "warning": "orange1",
            "danger": "red"
        })
        self.console = Console(theme=self.theme)

        self.user_validator = schema.Schema(
            {
                schema.Optional("id"): schema.Use(int, error="请检查用户id：整型数字"),
                schema.Optional("name"): schema.Regex(
                    r"^[a-zA-Z][a-zA-Z0-9_]{0,29}$",
                    error="请检查用户名：字母开头，可包含字母、数字、下划线，长度不超过30位"
                ),
                schema.Optional("password"): schema.And(
                    schema.Use(str),
                    schema.Regex(
                        r"[a-zA-Z0-9_]{6,18}$"
                    ),
                    error="请检查密码：可包含字母、数字、下划线，长度为6-18位"
                ),
                schema.Optional("email"): schema.Regex(
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
        )

    def _print_info_detail(self, row):
        table = Table(show_header=False)
        table.add_column("field", style="bold medium_orchid1")
        table.add_column("value", overflow="fold")

        for key, value in row.items():
            table.add_row(
                str(key),
                str(value)
            )

        self.console.print(table)

    def _print_infos_table(self, *rows):
        table = Table(show_header=True, header_style="bold medium_orchid1")

        table.add_column("id")
        table.add_column("name")
        table.add_column("email")
        table.add_column("mobile")
        table.add_column("created_at")
        table.add_column("updatedd_at")
        table.add_column("staff")

        for row in rows:
            style = "green_yellow" if row.get("staff") else ""

            table.add_row(
                str(row.get("id")),
                str(row.get("name")),
                str(row.get("email")),
                str(row.get("mobile")),
                row.get("created_at").tzinfo.fromutc(
                    row.get("created_at")).strftime("%Y-%m-%d %H:%M:%S"),
                row.get("updated_at").tzinfo.fromutc(
                    row.get("updated_at")).strftime("%Y-%m-%d %H:%M:%S"),
                str(row.get("staff")),
                style=style
            )

        self.console.print(table)

    def list_users(self, **kwargs):
        try:
            rows, total = asyncio.get_event_loop().run_until_complete(
                self.user_service.list_users()
            )

            staffs = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_ids([r['id'] for r in rows])
            )
            for row, staff in zip(rows, staffs):
                row['staff'] = staff

            if kwargs.get("role") == "staff":
                rows = list(filter(lambda x: x.get("staff"), rows))

            self._print_infos_table(*rows)

        except Exception as err:
            self.console.print(err, style="danger")
            return

    def inspect_user(self, **kwargs):
        try:
            data = self.user_validator.validate(kwargs)
            if data.get("id") == None:
                self.console.print("请指定用户id", style="danger")
                return

            id = data.get("id")
            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.info(id)
            )
            staff = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_id(id)
            )
            row['staff'] = staff

            self._print_info_detail(row)

        except Exception as err:
            self.console.print(err, style="danger")
            return

    def create_user(self, **kwargs):
        try:
            data = self.user_validator.validate(kwargs)
            if data.get("name") == None or data.get("password") == None:
                self.console.print("用户名或密码不能为空", style="danger")
                return

            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.create(**data)
            )
            id = row.get("id")
            staff = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_id(id)
            )
            row['staff'] = staff

            self._print_info_detail(row)

        except Exception as err:
            self.console.print(err, style="danger")
            return

    def set_staff(self, **kwargs):
        try:
            data = self.user_validator.validate(kwargs)
            if data.get("id") == None:
                self.console.print("请指定用户id", style="danger")
                return
            id = data.get("id")

            asyncio.get_event_loop().run_until_complete(
                self.user_service.set_staff(id)
            )

            self.inspect_user(id=id)

        except Exception as err:
            self.console.print(err, style="danger")
            return

    def unset_staff(self, **kwargs):
        try:
            data = self.user_validator.validate(kwargs)
            if data.get("id") == None:
                self.console.print("请指定用户id", style="danger")
                return
            id = data.get("id")

            asyncio.get_event_loop().run_until_complete(
                self.user_service.unset_staff(id)
            )

            self.inspect_user(id=id)

        except Exception as err:
            self.console.print(err, style="danger")
            return
