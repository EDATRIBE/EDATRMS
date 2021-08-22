import asyncio

from marshmallow import Schema, ValidationError, fields
from pymysql.err import DatabaseError
from rich import box
from rich.console import Console
from rich.table import Table
from rich.theme import Theme

from ..blueprints.common import required_field_validation
from ..models import RoleSchema, UserRoleSchema, UserSchema
from ..services import RoleService, UserRoleService, UserService


class User:
    def __init__(self, config, db, cache):
        self.config = config
        self.db = db
        self.cache = cache

        self.user_service = UserService(config, db, cache)
        self.role_service = RoleService(config, db, cache)
        self.user_role_service = UserRoleService(config, db, cache)

        self.theme = Theme(
            {
                "info": "turquoise2",
                "warning": "orange1",
                "danger": "red",
                "table header": "bold medium_spring_green",
            }
        )
        self.console = Console(theme=self.theme)

    def _print_dicts_as_table(self, rows):
        if len(rows) == 0:
            self.console.print("[ NULL! ]", style="info")
            return

        table = Table(show_header=True, header_style="table header", box=box.ROUNDED)
        for key in rows[0].keys():
            table.add_column(str(key))

        for row in rows:
            values = [
                str(value) if value is not None else "" for key, value in row.items()
            ]
            table.add_row(*values)

        self.console.print(table)

    def _print_dict_as_table(self, row):
        if not row:
            self.console.print("[ NULL! ]", style="info")
            return

        table = Table(show_header=True, header_style="table header", box=box.ROUNDED)
        table.add_column("key")
        table.add_column("value", overflow="fold")

        for key, value in row.items():
            table.add_row(str(key), str(value) if value is not None else "")

        self.console.print(table)

    def list_users(self, **kwargs):
        try:
            rows, total = asyncio.get_event_loop().run_until_complete(
                self.user_service.list_()
            )
            staffs = asyncio.get_event_loop().run_until_complete(
                self.user_service.is_staff_by_ids([r["id"] for r in rows])
            )
            role_ids_list = asyncio.get_event_loop().run_until_complete(
                self.user_role_service.role_ids_list_by_user_ids(
                    [r["id"] for r in rows]
                )
            )
        except Exception as err:
            self.console.print(err, style="danger")
            return

        for row, staff, role_ids in zip(rows, staffs, role_ids_list):
            row["staff"] = staff
            roles = asyncio.get_event_loop().run_until_complete(
                self.role_service.infos(role_ids)
            )
            row["roles"] = roles

        if kwargs.get("staff_only") is True:
            rows = list(filter(lambda x: x.get("staff"), rows))

        visible_field = ["id", "name", "staff", "roles", "comment"]
        users = [UserSchema(only=visible_field).dump(v) for v in rows]
        for user in users:
            roles = ["{}:{}".format(role["id"], role["name"]) for role in user["roles"]]
            user["roles"] = " | ".join(roles)

        self._print_dicts_as_table(users)

    def inspect_user(self, **kwargs):
        try:
            data = UserSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id"])
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
            role_ids = asyncio.get_event_loop().run_until_complete(
                self.user_role_service.role_ids_by_user_id(
                    user_id=data["id"],
                )
            )
            roles = asyncio.get_event_loop().run_until_complete(
                self.role_service.infos(role_ids)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return
        row["staff"] = staff
        row["roles"] = roles

        user = UserSchema().dump(row)
        roles = ["{}:{}".format(role["id"], role["name"]) for role in user["roles"]]
        user["roles"] = " | ".join(roles)
        self._print_dict_as_table(user)

    def comment_user(self, **kwargs):
        try:
            data = UserSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id", "comment"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.edit(id=data["id"], comment=data["comment"])
            )
            id = row.get("id")
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=id)

    def create_user(self, **kwargs):
        try:
            data = UserSchema().load(kwargs)
            required_field_validation(
                data=data, required_field=["name", "password", "email"]
            )
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.user_service.create(
                    name=data["name"],
                    password=data["password"],
                    email=data["email"],
                    comment=data.get("comment", ""),
                )
            )
            id = row.get("id")
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=id)

    def set_staff(self, **kwargs):
        try:
            data = UserSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data["id"]
        try:
            asyncio.get_event_loop().run_until_complete(self.user_service.set_staff(id))
            asyncio.get_event_loop().run_until_complete(
                self.user_service.force_logout(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=id)

    def unset_staff(self, **kwargs):
        try:
            data = UserSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id"])
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

    def list_roles(self):
        try:
            rows, total = asyncio.get_event_loop().run_until_complete(
                self.role_service.list_()
            )
        except Exception as err:
            self.console.print(err, style="danger")
            return

        visible_field = ["id", "name"]
        roles = [RoleSchema(only=visible_field).dump(v) for v in rows]
        self._print_dicts_as_table(roles)

    def inspect_role(self, **kwargs):
        try:
            data = RoleSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data.get("id")
        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.role_service.info(id)
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        role = RoleSchema().dump(row)
        self._print_dict_as_table(role)

    def create_role(self, **kwargs):
        print(kwargs)
        try:
            data = RoleSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id", "name"])

        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            row = asyncio.get_event_loop().run_until_complete(
                self.role_service.create(
                    id=data["id"],
                    name=data["name"],
                    reserved_names=data.get("reserved_names", {}),
                    style=data.get("style", {}),
                    comment=data.get("comment", ""),
                )
            )
            id = row.get("id")
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_role(id=id)

    def delete_role(self, **kwargs):
        try:
            data = RoleSchema().load(kwargs)
            required_field_validation(data=data, required_field=["id"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        id = data.get("id")
        try:
            asyncio.get_event_loop().run_until_complete(self.role_service.delete(id))
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.list_roles()

    def assign_role(self, **kwargs):
        try:
            data = UserRoleSchema().load(kwargs)
            required_field_validation(data=data, required_field=["user_id", "role_id"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            asyncio.get_event_loop().run_until_complete(
                self.user_role_service.create(
                    user_id=data["user_id"], role_id=data["role_id"]
                )
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=data["user_id"])

    def cancel_role(self, **kwargs):
        try:
            data = UserRoleSchema().load(kwargs)
            required_field_validation(data=data, required_field=["user_id", "role_id"])
        except ValidationError as err:
            self.console.print(err.messages, style="danger")
            return

        try:
            asyncio.get_event_loop().run_until_complete(
                self.user_role_service.delete_by_user_id_and_role_id(
                    user_id=data["user_id"], role_id=data["role_id"]
                )
            )
        except DatabaseError as err:
            self.console.print(err, style="danger")
            return

        self.inspect_user(id=data["user_id"])
