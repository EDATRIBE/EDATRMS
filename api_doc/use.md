# 使用手册

## 部署

## 配置

## 指令

所有指令应当在项目根目录处执行

```shell
cd your/path/EDATRMS
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
    python -m api.manage user create_user -name="alice" -password="27182818" [-OPTION]
    ```

- 列出已创建的全部库表

    ```shell
    python -m api.manage model list_tables
    ```

- 创建所有库表

    ```she
    python -m api.manage model create_tables
    ```

- 删除所有库表

    ```shell
    python -m api.manage model drop_tables
    ```

