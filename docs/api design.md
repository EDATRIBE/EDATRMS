# API Design

## Model

### 准则

#### 何时在库表中使用json字段？

- 数量不确定的同类字段（如名字与简介的多语言版本）、可变性强的字段（如文件的元信息，角色徽章的style信息）。

- 需要外键约束的字段不应使用json类型。

#### 那些字段不该为空？

- 所有字符串与json类型的字段都不应该为空。系统在插入数据时应提供空字符串或空字典作为默认值。
- 逻辑上存在合法值的字段不应为空（如animation的集数）
- （目前唯一可空的字段为用户的头像id）

### 设计

#### ip table

* **Column:**

  | Filed                        | Type           | Nullable | Comment      |
  | ---------------------------- | -------------- | -------- | ------------ |
  | id                           | integer        | PK       |              |
  | name                         | varchar(300)   | False    | 标识名       |
  | reserved_names               | json           | False    | 别名         |
  | [ reserved_names.jp_name ]   | json.attr: str | Optional | 日文名       |
  | [ reserved_names.cn_name ]   | json.attr: str | Optional | 中文名       |
  | [ reserved_names.en_name ]   | json.attr: str | Optional | 英文名       |
  | [ reserved_names.rm_name ]   | json.attr: str | Optional | 罗马音名     |
  | [ reserved_names.misc_name ] | json.attr: str | Optional | 混合关键字   |
  | region                       | varchar(300)   | False    | 地区         |
  | written_by                   | varchar(300)   | False    | 原著作者     |
  |                              |                |          |              |
  | created_by                   | integer        | False    | 创建者       |
  | created_at                   | datetime       | False    | 创建日期     |
  | updated_by                   | integer        | False    | 最近编辑者   |
  | updated_at                   | datetime       | False    | 最近编辑日期 |
  | comment                      | varchar(300)   | False    | 备注         |

* **Foreign Key Constraint:**

  * (created_by, user.id, ondelete='SET NULL', onupdate='CASCADE')
  * (created_by, user.id, ondelete='SET NULL', onupdate='CASCADE')

* **Index**:

  - (name, unique=True)

#### animation table

* **Column:**

  | Filed                               | Type           | Nullable  | Comment             |
  | ----------------------------------- | -------------- | --------- | ------------------- |
  | id                                  | integer        | PK        |                     |
  | ip_id                               | integer        | False     | 所属ip的id          |
  | name                                | varchar(300)   | False     | 标识名              |
  | reserved_names                      | json           | False     | 别名                |
  | [ reserved_names.jp_name ]          | json.attr: str | Optional  | 日文名              |
  | [ reserved_names.cn_name ]          | json.attr: str | Optional  | 中文名              |
  | [ reserved_names.en_name ]          | json.attr: str | Optional  | 英文名              |
  | [ reserved_names.rm_name ]          | json.attr: str | Optional  | 罗马音名            |
  | [ reserved_names.misc_name ]        | json.attr: str | Optional  | 混合关键词          |
  | intros                              | json           | False     | 简介                |
  | [ en_intro ]                        | json.attr: str | Optional  | 中文简介            |
  | [ cn_intro ]                        | json.attr: str | Optional  | 英文简介            |
  | image_ids                           | json           | False     | 展示图id            |
  | [ image_ids.horizontal_image_id ]   | json.attr: int | Necessary | 横向图id            |
  | [ image_ids.vertical_image_id ]     | json.attr: int | Necessary | 竖向图id            |
  | produced_by                         | varchar(300)   | False     | 出品公司            |
  | released_at                         | datetime       | False     | 上映时间            |
  | type                                | varchar(300)   | False     | TV/movie/SP/OVA/OAD |
  | episodes_num                        | integer        | False     | 集数                |
  | sharing_address                     | json           | False     | 分享地址            |
  | [ sharing_addresses.baidu.url ]     | json.attr: str | Necessary |                     |
  | [ sharing_addresses.baidu.password] | json.attr: str | Optional  |                     |
  | [ sharing_addresses.ali.url ]       | json.attr: str | Necessary |                     |
  | [ sharing_addresses.ali.password]   | json.attr: str | Optional  |                     |

* **Enum:**

  - type: (TV, MOVIE, SP, OVA, OAD)

* **Foreign Key Constraint:**

  * (ip_id, ip.id, ondelete='CASCADE', onupdate='CASCADE')

#### video table


* **Column:**

  | Filed                 | Type           | Nullable | Comment           |
  | --------------------- | -------------- | -------- | ----------------- |
  | id                    | integer        | PK       |                   |
  | animation_id          | integer        | False    |                   |
  | file_meta             | json           | False    | 视频元信息        |
  | [ file_meta.name ]    | json.attr: str | Optional | 文件原名          |
  | [ file_meta.type ]    | json.attr: str | Optional | 格式（mp4/        |
  | [ file_meta.size ]    | json.attr: int | Optional | 视频大小          |
  | [ file_meta.quality ] | json.attr: str | Optional | 分辨率（720/原画/ |

* **Enum:**

  - file_meta.format: (MP4, MKV, AV1, OGG)
  - file_meta.quality: (360P, 640P, 720P, 960P, 1080P)

* **Foreign Key Constraint:**

  * (animation_id, animation.id, ondelete='CASCADE', onupdate='CASCADE')

#### caption table


* **Column:**

  | Filed              | Type           | Nullable | Comment           |
  | ------------------ | -------------- | -------- | ----------------- |
  | id                 | integer        | PK       |                   |
  | animation_id       | integer        | False    | 所属animation的id |
  | integrated         | bool           | False    | 完整1，不完整0    |
  | state              | varchar(300)   | False    | doing/todo/done   |
  | released_at        | datetime       | True     | 完成于            |
  | file_meta          | json           | False    | 文件元信息        |
  | [ file_meta.name ] | json.attr: str | Optional | 文件原名          |
  | [ file_meta.type ] | json.attr: str | Optional | 格式/txt/pdf      |
  | [ file_meta.size ] | json.attr: int | Optional | 文件大小          |

* **Enum:**

  - state: (TODO, DOING, DONE)

  - file_meta.format: (SRT, ASS, VTT, SUP, SSA)

* **Foreign Key Constraint:**

  * (animation_id, animation.id, ondelete='CASCADE', onupdate='CASCADE')


#### novel table


* **Column:**

  | Filed                               | Type           | Nullable  | Comment      |
  | ----------------------------------- | -------------- | --------- | ------------ |
  | id                                  | integer        | PK        |              |
  | ip_id                               | integer        | False     | 参照ip的id   |
  | name                                | varchar(300)   | False     | 标识名       |
  | reserved_names                      | json           | False     | 别名         |
  | [ reserved_names.jp_name ]          | json.attr: str | Optional  | 日文名       |
  | [ reserved_names.cn_name ]          | json.attr: str | Optional  | 中文名       |
  | [ reserved_names.en_name ]          | json.attr: str | Optional  | 英文名       |
  | [ reserved_names.rm_name ]          | json.attr: str | Optional  | 罗马音名     |
  | [ reserved_names.misc_name ]        | json.attr: str | Optional  | 混合关键字   |
  | intros                              | json           | False     | 简介         |
  | [ intro.cn_intro ]                  | json.attr: str | Optional  | 中文简介     |
  | [ intro.en_intro ]                  | json.attr: str | Optional  | 英文简介     |
  | image_ids                           | json           | True      |              |
  | [ image_ids.horizontal_image_id ]   | json.attr: int | Necessary | 横向图id     |
  | [ image_ids.vertical_image_id ]     | json.attr: int | Necessary | 竖向图id     |
  | volumes_num                         | integer        | False     | 卷数         |
  | integrated                          | bool           | False     | 完整性       |
  | file_meta                           | json           | False     | 文件元信息   |
  | [ file_meta.name ]                  | json.attr: str | Optional  | 文件原名     |
  | [ file_meta.type ]                  | json.attr: str | Optional  | 格式/txt/pdf |
  | [ file_meta.size ]                  | json.attr: int | Optional  | 文件大小     |
  | sharing_address                     | json           | False     | 分享地址     |
  | [ sharing_addresses.baidu.url ]     | json.attr: str | Necessary |              |
  | [ sharing_addresses.baidu.password] | json.attr: str | Optional  |              |
  | [ sharing_addresses.ali.url ]       | json.attr: str | Necessary |              |
  | [ sharing_addresses.ali.password]   | json.attr: str | Optional  |              |

* **Enum:**

  - file_meta.format: (TXT, PDF, EPUB)

* **Foreign Key Constraint**:

  * (ip_id, ip.id, ondelete='CASCADE', onupdate='CASCADE')


#### file table


* **Column:**

  | Filed              | Type           | Nullable | Comment            |
  | ------------------ | -------------- | -------- | ------------------ |
  | id                 | integer        | PK       |                    |
  | region             | varchar(300)   | False    | 区域（本地/oss     |
  | bucket             | varchar(300)   | False    | 文件桶             |
  | path               | varchar(300)   | False    | 具体路径，包括名字 |
  | file_meta          | json           | False    | 文件信息           |
  | [ file_meta.name ] | json.attr: str | Optional | 文件名             |
  | [ file_meta.type ] | json.attr: str | Optional | 文件类型           |
  | [ file_meta.size ] | json.attr: int | Optional | 文件大小           |

#### tag table


* **Column:**

  | Filed                      | Type           | Nullable | Comment |
  | -------------------------- | -------------- | -------- | ------- |
  | id                         | integer        | PK       |         |
  | name                       | varchar(300)   | False    |         |
  | reserved_names             | json           | False    | 别名    |
  | [ reserved_names.cn_name ] | json.attr: str | Optional | 中文名  |
  | [ reserved_names.en_name ] | json.attr: str | Optional | 英文名  |

#### ip_tag table


* **Column:**

  | Filed  | Type    | Nullable | Comment |
  | ------ | ------- | -------- | ------- |
  | id     | integer | PK       |         |
  | ip_id  | integer | False    |         |
  | tag_id | integer | False    |         |

#### user table


* **Column:**

  | Filed      | Type         | Nullable | Comment  |
  | ---------- | ------------ | -------- | -------- |
  | id         | integer      | PK       |          |
  | name       | varchar(300) | False    |          |
  | password   | char(64)     | False    |          |
  | salt       | char(64)     | False    |          |
  | email      | varchar(300) | False    |          |
  | mobile     | varchar(300) | False    |          |
  | intro      | varchar(300) | False    |          |
  | avatar_id  | integer      | True     |          |
  |            |              |          |          |
  | created_at | datetime     | False    | 创建日期 |
  | comment    | varchar(300) | False    | 备注     |

#### caption_user table


* **Column:**

  | Filed      | Type   | Nullable | Comment |
  | ---------- | ------ | -------- | ------- |
  | id         | intger | PK       |         |
  | caption_id | intger | False    |         |
  | user_id    | intger | False    |         |

#### role table


* **Column:**

  | Filed                      | Type           | Nullable | Comment      |
  | -------------------------- | -------------- | -------- | ------------ |
  | id                         | intger         | PK       |              |
  | name                       | varchar(300)   | False    | 角色名       |
  | reserved_names             | json           | False    | 别名         |
  | [ reserved_names.cn_name ] | json.attr: str | Optional | 中文名       |
  | [ reserved_names.en_name ] | json.attr: str | Optional | 英文名       |
  | style                      | json           | False    | 样式         |
  | [ style.icon ]             | json.attr: str | Optional | 角色徽章图标 |
  | [ style.color ]            | json.attr: str | Optional | 角色徽章颜色 |
  |                            |                |          |              |
  | created_at                 | date           | False    | 创建日期     |
  | comment                    | varchar(300)   | False    | 备注         |

#### user_role table


* **Column:**

  | Filed   | Type   | Nullable | Comment |
  | ------- | ------ | -------- | ------- |
  | id      | intger | PK       |         |
  | user_id | intger | False    |         |
  | role_id | intger | False    |         |



## Service

### 准则

#### 是否对传入数据做检验？

不做格式上的检验。仅在有必要时做类型上的检验。传入数据的合法性应由调用方保证。

### 设计

#### BaseService

所有service的基类，该类不应直接被实例化。

实现了基础的增、删、改以及可指定数量与偏移量的列出功能。其属性与方法如下：

- attritubes: config, db, cache, model

- methods:

  - create

    接收由model对应的字段组成的关键字参数，返回info的调用结构

  - edit

    接收由model对应的字段组成的关键字参数，返回info的调用结构

  - info

    接收整数参数id，返回对应的数据库行对应的的字典对象

  - infos

    接收id列表，返回对应的数据库行对应的的字典对象列表，顺序与id列表一一对应

    例如:

    ```
    infos([1,2,3])
    #[dict1,dict2,dict3]
    ```
  
  - list
  
    接收limit与offset参数，返回数据库表中[ offset, offset+limit )之间，所有行对应的字典对象组成的列表

#### SearchKeywordInNameMixin

用于提供名字与别名的关键词搜索方法的混入类，该类不应直接被实例化。

- methods：

  - search_keyword_in_names

    接收字符串参数keyword，返回名称或别名中包含该关键字的行对应的字段对象组成的列表



#### IPService(BaseService,SearchKeywordInNameMixin)

继承自BaseService与SearchKeywordInNameMixin

在实例化时，model属性会被设为ip model

#### AnimationService(BaseService,SearchKeywordInNameMixin)

继承自BaseService与SearchKeywordInNameMixin

在实例化时，model属性会被设为animation model

- methods:

  - infos_by_ip_id

    接收ip_id参数，返回该ip下所有animation对应的列表

    例如：

    ```
    infos_by_animation_id(1)
    #[1,2,3]
    ```

  - infos_list_by_ip_ids

    接收一个由ip_id组成的列表作为参数，返回一个列表。该列表的元素为传入的ip_id列表中每个ip下所有的animation组成的列表

    例如：

    ```
    infos_list_by_animation_ids([1,2,3])
    #[[1,2,3],[4,5,6],[7,8,9]]
    ```

#### VideoService(BaseService)

继承自BaseService

在实例化时，model属性会被设为video model

- methods:

  - infos_by_animation_id

    接收animation_id参数，返回该animation下所有video对应的列表

    例如：

    ```
    infos_by_animation_id(1)
    #[1,2,3]
    ```
  
  - infos_list_by_animation_ids
  
    接收一个由animation_id组成的列表作为参数，返回一个列表。该列表的元素为传入的animation_id列表中每个animation下所有的video组成的列表。
    
    例如：
    
    ```
    infos_list_by_animation_ids([1,2,3])
    #[[1,2,3],[4,5,6],[7,8,9]]
    ```
    
    





## Endpoint

### 准则

对用户传入的数据进行如下处理：

-   格式检验
-   必要参数是否为空

编辑对象时，如果编辑的字段未知，则需要sift_dict_by_key。若编辑的字段已知(如创建时)，则逐一填写。

### 设计

#### account

-   account/login



## Data

```
api_data
├── logs
│   ├── access.log
│   └── app.log
├── region: (local,remote,...)
│  └── buckets: (limbo,user,animation,novel,...)
│       └── path: (user.id,animation.id,...)
│           └── file: (random_string16.ext)
├── region
│  └── ...
...
```



