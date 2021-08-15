# Use

## 系统指令

### 备注

所有指令应当在项目根目录处执行

```shell
$ cd your/path/EDATRMS
```

在指令执行时，所有的参数遵循如下解析方式：

```python
import fire
fire.Fire(lambda obj: type(obj).__name__)
```

```shell
$ python example.py 10
int
$ python example.py 10.0
float
$ python example.py "10"
int
$ python example.py '"10"'
str
$ python example.py "'10'"
str
$ python example.py \"10\"
str
$ python example.py hello
str
$ python example.py '(1,2)'
tuple
$ python example.py [1,2]
list
$ python example.py True
bool
$ python example.py {name:David}
dict
```

当要传入字典参数时，其行为如下：

```shell
$ python example.py '{"name": "David Bieber"}'  # Good! Do this.
dict
$ python example.py {"name":'"David Bieber"'}  # Okay.
dict
$ python example.py {"name":"David Bieber"}  # Wrong. This is parsed as a string.
str
$ python example.py {"name": "David Bieber"}  # Wrong. This isn't even treated as a single argument.
<error>
$ python example.py '{"name": "Justin Bieber"}'  # Wrong. This is not the Bieber you're looking for. (The syntax is fine though :))
dict
```



### 数据库表管理： model

- 列出已定义的全部模型： list_models

    ```shell
     Usage:         python -m api.manage model list_models
    ```

- 列出已创建的全部库表： list_tables

    ```shell
     Usage:         python -m api.manage model list_tables
    ```

- 创建所有库表： create_tables

    ```shell
     Usage:         python -m api.manage model create_tables
    ```

- 删除所有库表： drop_tables

    ```shell
     Usage:         python -m api.manage model drop_tables
    ```



### 用户管理： user

- 新增用户： create_user

    ```shell
    Usage:          python -m api.manage user create_user [OPTIONS="VALUE"]
    Options:
        -name       用户名，该选项不可省略
        -password   用户密码，该选项不可省略
        -mail       邮箱
        -qq     	qq账号
        -intr       自我介绍
        -comment    备注 
    ```

- 列出全部用户信息摘要： list_users

    ```shell
    Usage:          python -m api.manage user list_users [OPTIONS="VALUE"]
    Options:
        -staff_only	当该选项值为 true 时，仅列出 staff 用户的信息
    ```

- 列出单个用户详细信息： inspect_user

    ```shell
    Usage:          python -m api.manage user inspect_user [OPTIONS="VALUE"]
    Options:
        -id         所要查看的用户 id，值为整型，或可以转化为整型的字符串
    ```
    
- 为用户设置 staff 权限： set_staff

    ```shell
    Usage:          python -m api.manage user set_staff [OPTIONS="VALUE"]
    Options:
        -id         所要设置 staff 角色的用户 id，值为整型，或可以转化为整型的字符串
    ```

- 取消用户的 staff 权限： unset_staff

    ```shell
    Usage:          python -m api.manage user unset_staff [OPTIONS="VALUE"]
    Options:
        -id         所要取消 staff 的用户 id，值为整型，或可以转化为整型的字符串
    ```
    
- 新增角色：create_role

    ```shell
    Usage:              python -m api.manage user create_role [OPTIONS="VALUE"]
    Options:
        -id             角色id，将用于展示时的排序
        -name           角色名，该选项不可省略
        -reservedNames  角色别名，该选项为json对象，格式为：{"cn":"名称","en":"name"}
        -style          角色徽章风格，该选项为json对象，格式为：{"icon":"face","color":"red-7"}
    ```

- 列出全部角色信息摘要： list_roles

  ```shell
  Usage:          python -m api.manage user list_roles
  ```

- 列出单个角色的详细信息： inspect_role

  ```shell
  Usage:          python -m api.manage user inspect_role [OPTIONS="VALUE"]
  Options:
      -id         所要查看的角色 id，值为整型，或可以转化为整型的字符串
  ```

- 删除角色：delete_role

  ```shell
  Usage:          python -m api.manage user delete_role [OPTIONS="VALUE"]
  Options:
      -id         所要删除的角色 id，值为整型，或可以转化为整型的字符串
  ```

- 为用户分配角色：assign_role

  ```shell
  Usage:          python -m api.manage user assign_role [OPTIONS="VALUE"]
  Options:
      -userId.    所要分配的用户 id，值为整型，或可以转化为整型的字符串
      -roleId.    所要分配的角色 id，值为整型，或可以转化为整型的字符串
  ```

- 为取消用户的角色：cancel_role

  ```shell
  Usage:          python -m api.manage user cancel_role [OPTIONS="VALUE"]
  Options:
      -userId.    所要取消的用户 id，值为整型，或可以转化为整型的字符串
      -roleId.    所要取消的角色 id，值为整型，或可以转化为整型的字符串
  ```



### 附录

cancel_role命令举例：

```shell
python -u -m src.manage user create_role -id=1 -name=Leader -reservedNames='{"cn":"站长","en":"LEADER"}' -style='{"icon":"face","color":"red-7"}'

python -u -m src.manage user create_role -id=11 -name=sub_producer -reservedNames='{"cn":"字幕监制","en":"Subt. Producer"}' -style='{"icon":"subtitles","color":"primary"}'

python -u -m src.manage user create_role -id=21 -name=sub_proofreader -reservedNames='{"cn":"字幕校对","en":"Subt. Proofreader"}' -style='{"icon":"subtitles","color":"primary"}'

python -u -m src.manage user create_role -id=31 -name=animation_reuploader -reservedNames='{"cn":"动漫搬运","en":"Animation Reuploader"}' -style='{"icon":"local_shipping","color":"primary"}'

python -u -m src.manage user create_role -id=41 -name=novel_reuploader -reservedNames='{"cn":"小说搬运","en":"Novel Reuploader"}' -style='{"icon":"local_shipping","color":"secondary"}'

python -u -m src.manage user create_role -id=51 -name=tech_support -reservedNames='{"cn":"技术支持","en":"Tech Support"}' -style='{"icon":"settings","color":"purple-14"}'

python -u -m src.manage user create_role -id=61 -name=accountant -reservedNames='{"cn":"会计","en":"Accountant"}' -style='{"icon":"calculate","color":"purple-14"}'

python -u -m src.manage user create_role -id=71 -name=editor -reservedNames='{"cn":"编辑","en":"Editor"}' -style='{"icon":"history_edu","color":"purple-14"}'

python -u -m src.manage user create_role -id=81 -name=top_sponsor -reservedNames='{"cn":"赞助","en":"Top Sponsor"}' -style='{"icon":"attach_money","color":"orange-9"}'

python -u -m src.manage user create_role -id=91 -name=mascot -reservedNames='{"cn":"吉祥物","en":"Mascot"}' -style='{"icon":"emoji_emotions","color":"yellow-6"}'

python -u -m src.manage user create_role -id=111 -name=retired -reservedNames='{"cn":"退休干部","en":"Retired"}' -style='{"icon":"emoji_food_beverage","color":"white"}'
```



### 

