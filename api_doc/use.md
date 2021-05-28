# 使用手册

## 部署

## 配置

## 指令

所有指令应当在项目根目录处执行

```shell
$ cd your/path/EDATRMS
```



### 数据库表管理

- 列出已定义的全部模型

    ```shell
    $ python -m api.manage model list_models
    ```

- 列出已创建的全部库表

    ```shell
    $ python -m api.manage model list_tables
    ```

- 创建所有库表

    ```shell
    $ python -m api.manage model create_tables
    ```

- 删除所有库表

    ```shell
    $ python -m api.manage model drop_tables
    ```



### 用户管理

- 新增用户

    ```shell
    $ python -m api.manage user create_user -name="alice" -password="27182818"
    
    Usage:			python -m api.manage user create_user [OPTIONS="VALUE"]
    Options:
    	-name	   	用户名，该选项不可省略
    	-password	用户密码，该选项不可省略
        -mail		邮箱
        -mobile		联系电话
        -intro		自我介绍
        -comment	备注
    ```

- 列出全部用户信息摘要

    ```shell
    $ python -m api.manage user list_users
    
    Usage:			python -m api.manage user list_users [OPTIONS="VALUE"]
    Options:
    	-role		当该选项值为staff时，仅列出staff用户的信息
    ```

- 列出单个用户详细信息

    ```shell
    python -m api.manage user list_users -id=7
    
    Options:
    	-id			所要查看的用户id，值为整型，或可以转化为整型的字符串
    	-role		当该选项值为staff时，仅列出staff用户的信息
    ```

- 设置staff角色

    ```shell
    $ python -m api.manage user set_staff -id=7
    
    Options:
    	-id			所要设置staff角色的用户id，值为整型，或可以转化为整型的字符串
    ```

- 取消staff角色

    ```shell
    $ python -m api.manage user unset_staff -id=7
    
    Options:
    	-id			所要取消staff的用户id，值为整型，或可以转化为整型的字符串
    ```

