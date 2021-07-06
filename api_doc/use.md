# 使用手册

## 部署

## 配置

api_data/logs/ 需要手动创建



## 指令

所有指令应当在项目根目录处执行

```shell
$ cd your/path/EDATRMS
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
        -mobile     联系电话
        -intr       自我介绍
        -comment    备注 
    ```

- 列出全部用户信息摘要： list_users

    ```shell
    Usage:          python -m api.manage user list_users [OPTIONS="VALUE"]
    Options:
        -staff_only	当该选项值为 y 时，仅列出 staff 用户的信息
    ```

- 列出单个用户详细信息： inspect_user

    ```shell
    Usage:          python -m api.manage user inspect_user [OPTIONS="VALUE"]
    Options:
        -id         所要查看的用户 id，值为整型，或可以转化为整型的字符串
    ```
    
- 为用户设置 staff 角色： set_staff

    ```shell
    Usage:          python -m api.manage user set_staff [OPTIONS="VALUE"]
    Options:
        -id         所要设置 staff 角色的用户 id，值为整型，或可以转化为整型的字符串
    ```

- 取消用户的 staff 角色： unset_staff

    ```shell
    Usage:          python -m api.manage user unset_staff [OPTIONS="VALUE"]
    Options:
        -id         所要取消 staff 的用户 id，值为整型，或可以转化为整型的字符串
    ```

