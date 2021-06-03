import asyncio

from marshmallow import Schema, ValidationError, fields
from pymysql.err import DatabaseError
from rich.console import Console
from rich.table import Table
from rich.theme import Theme

from ..models import UserSchema
from ..services import UserService


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
        for c in ["id","name","email","mobile","created_at","staff"]:
            table.add_column(c)

        for row in rows:
            style = "green_yellow" if row.get("staff") else ""
            table.add_row(
                str(row.get("id")),
                str(row.get("name")),
                str(row.get("email")),
                str(row.get("mobile")),
                row.get("created_at"). \
                    tzinfo. \
                    fromutc(row.get("created_at")). \
                    strftime("%Y-%m-%d %H:%M:%S"),
                str(row.get("staff")),
                style=style
            )

        self.console.print(table)

    def list_users(self, **kwargs):
        for k,v in kwargs.items():
            kwargs[k]= str(v)
        try:
            rows, total = asyncio.get_event_loop().run_until_complete(
                self.user_service.list_users()
            )
            staffs = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_ids([r['id'] for r in rows])
            )
        except Exception as err:
            self.console.print(err, style="danger")
            return

        for row, staff in zip(rows, staffs):
            row['staff'] = staff
        if kwargs.get("staff_only") in ['y','Y',"yes", "YES"]:
            rows = list(filter(lambda x: x.get("staff"), rows))

        self._print_infos_table(*rows)


    def inspect_user(self, **kwargs):
        for k,v in kwargs.items():
            kwargs[k]= str(v)
        try:
            data = UserSchema().load(kwargs)
            if data.get("id") is None:
                raise ValidationError("请指定用户id")
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data.get("id")
        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.info(id)
            )
            staff = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_id(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return
        row['staff'] = staff

        self._print_info_detail(row)


    def create_user(self, **kwargs):
        for k,v in kwargs.items():
            kwargs[k]= str(v)
        try:
            data = UserSchema().load(kwargs)
            if data.get("name") is None or data.get("password") is None:
                raise ValidationError("用户名或密码不能为空")
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.create(**data)
            )
            id = row.get("id")
            staff = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_id(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return
        row['staff'] = staff

        self._print_info_detail(row)

    def set_staff(self, **kwargs):
        for k,v in kwargs.items():
            kwargs[k]= str(v)
        try:
            data = UserSchema().load(kwargs)
            if data.get("id") is None:
                raise ValidationError("请指定用户id")
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data.get("id")
        try:
            asyncio.get_event_loop().run_until_complete(
                self.user_service.set_staff(id)
            )
            asyncio.get_event_loop().run_until_complete(
                self.user_service.force_logout(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=id)

    def unset_staff(self, **kwargs):
        for k,v in kwargs.items():
            kwargs[k]= str(v)
        try:
            data = UserSchema().load(kwargs)
            if data.get("id") is None:
                raise ValidationError("请指定用户id")
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data.get("id")
        try:
            asyncio.get_event_loop().run_until_complete(
                self.user_service.unset_staff(id)
            )
            asyncio.get_event_loop().run_until_complete(
                self.user_service.force_logout(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=id)
