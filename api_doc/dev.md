# 开发文档

## 需求分析

### 系统目标

本项目旨在建立一个用于管理视频、字幕以及轻小说资源的系统。

系统功能主要包含三个方面：

1. 整理资源

    目前部落拥有的资源包括，英配动画、未加工的CC字幕、已加工的CC字幕、已压制的英配动画、英配轻小说。目前这些资源都是分别整理记录。并且单英配动画的信息就有很多，比如季数、中文名、英文名、罗马音名、剧场版等。之前资源少时，下载资源时就是无脑下载，因为大多数动画都没有收录。但现在以及收录的动画超过了800部，资源网上发布新资源时很难分辨这个番是否已经收录。需要根据罗马音名或英文名搜中文名，然后再与已有资源对比然后再确认下载，这个过程已经严重拖慢了效率。如果将已有的资源建立一个数据库，里面包含需要的信息，这些信息可以去网上爬下来。这样有新资源时就很快知道是否已经收录，而且资源网站还有RSS功能，也可以实现有新资源时自动提示下载，或者再进一步实现自动下载。

2. 分享资源

    目前部落分享资源主要通过 list.edatribe.com 网址分享资源，这就是一个静态网页，里面的信息很少，而且需要手动更新。如果连接此数据库就可以自动更新信息，而且可以显示更多信息，包括大小，集数，视频质量等等。下载资源的体验会更好。

3. 网站调用

    目前网站更新动画时，动画信息都是手工录入，如果能和此数据库连接，就可以直接调用数据库里的信息，减少工作量。

此数据库主要是一个后端程序，通过API可以让不同程序调用。其实本质上有些类似学生管理系统或者图书馆管理系统。

### 具体功能

1. 信息录入功能

    当有新资源时需要录入到数据库，有些信息需要手工操作，有些信息可以直接爬其他网站。比如：https://anidb.net/（英文数据库）、https://bangumi.tv/（中文数据库）https://reelgood.com/。录入时可以调用爬取的资源，如果信息不对也可以手动修改。

2. 信息查询功能

    这也是这个数据库的核心功能，可以根据已知的信息查询想要的信息。例如：根据一个番剧名（英文名、罗马音名、中文名、日文名等）查询出这个番的其他信息。或者查询这个数据库的某些信息，集数最多的番是哪部、2020年上架的番有哪些、搞笑的番有哪些、参与制作字幕最多人是谁（肯定是子弹啦，Ahhh）类似这种功能。

3. 用户权限管理

    设置不同用户权限，有的可以修改，有的只能查询，这类功能。

4. 日志功能

    记录数据库修改信息，方便纠错。

5. 报表功能

    能够输出年度总结

## 总体设计

### 技术架构

![fram](dev.assets/tec_fram.png)



### 数据层

#### 设计准则：

将可变的同类型字段（如各种语言的名字，各种语言的简介，文件的元信息）使用json存储。

所有的字符串类型不可为null，默认值为空字符串。

#### 逻辑层设计：

1. ip

    | Filed                        | Type      | Nullable | PK      | FK   | Comment      |
    | ---------------------------- | --------- | -------- | ------- | ---- | ------------ |
    | id                           | int       |          | y       |      |              |
    | name                         | str       | n        |         |      | 标识名       |
    | reserved_names               | json      | y        |         |      | 别名         |
    | [ reserved_names.jp_name ]   | json.attr |          |         |      | 日文名       |
    | [ reserved_names.cn_name ]   | json.attr |          |         |      | 中文名       |
    | [ reserved_names.en_name ]   | json.attr |          |         |      | 英文名       |
    | [ reserved_names.rm_name ]   | json.attr |          |         |      | 罗马音名     |
    | [ reserved_names.misc_name ] | json.attr |          |         |      | 混合关键字   |
    | intros                       | json      | y        |         |      | 简介         |
    | [ intro.cn_intro ]           | json.attr |          |         |      | 中文简介     |
    | [ intro.en_intro ]           | json.attr |          |         |      | 英文简介     |
    |                              |           |          |         |      |              |
    | created_by                   | str       | n        | user.id |      | 创建者       |
    | created_at                   | date      | n        |         |      | 创建日期     |
    | updated_by                   | str       | n        | user.id |      | 最近编辑者   |
    | updated_at                   | date      | n        |         |      | 最近编辑日期 |
    | comment                      | str       | y        |         |      | 备注         |
    
2. animation

    | Filed               | Type | Nullable | PK   | FK    | Comment             |
    | ------------------- | ---- | -------- | ---- | ----- | ------------------- |
    | id              | int |     | y |       |                     |
    | ip_id           | int | n   |      | ip.id |                     |
    | name            | str | n    |      |       | 标识名         |
    | reserved_names | json | y | | | 别名 |
    | [ reserved_names.jp_name ] | json.attr |         |      |       | 日文名             |
    | [ reserved_names.cn_name ] | json.attr |         |      |       | 中文名             |
    | [ reserved_names.en_name ] | json.attr |         |      |       | 英文名             |
    | [ reserved_names.rm_name ] | json.attr |         |      |       | 罗马音名           |
    | [ reserved_names.misc_name ] | json.attr | | | |  |
    | intros | json | y | | |  |
    | [ en_intro ]        | json.attr |         |      |       | 中文简介            |
    | [ cn_intro ]        | json.attr |         |      |       | 英文简介            |
    | image_ids | json | y | | |  |
    | [ image_ids.horizontal_image_id ] | json.attr |         |      |       | 横向图id       |
    | [ image_ids.vertical_image_id ] | json.attr |  |      |       | 竖向图id |
    | [ image_ids.reversed_image_id ] | json.attr |  |      |       | 备用图id |
    | produced_by | str | n    |      |       | 出品公司       |
    | released_at | dt | n | | | 上映时间 |
    | written_by      | str | n |      |       | 原著作者       |
    | type            | str | n    |      |       | TV/movie/SP/OVA/OAD |
    | episodes_num    | int | n    |      |       | 集数            |


3. video

    | Filed                 | Type      | Nullable | PK   | FK           | Comment           |
    | --------------------- | --------- | -------- | ---- | ------------ | ----------------- |
    | id                    | int       |          | y    |              |                   |
    | animation_id          | int       | n        |      | animation.id |                   |
    | file_url              | str       | n        |      |              | 视频链接          |
    | file_meta             | json      | n        |      |              | 视频元信息        |
    | [ file_meta.size ]    | json.attr |          |      |              | 视频大小          |
    | [ file_meta.quality ] | json.attr |          |      |              | 分辨率（720/原画/ |
    | [ file_meta.format ]  | json.attr |          |      |              | 格式（mp4/        |


4. caption

    | Filed        | Type | Nullable | PK   | FK           | Comment         |
    | ------------ | ---- | -------- | ---- | ------------ | --------------- |
    | id       | int |          | y |              |                 |
    | animation_id | int | n    |      | animation.id |                 |
    | integrated | bool | n    |      |              | 完整性      |
    | status   | str | n    |      |              | doing/todo/done |
    | finished_at | date | y |      |              | 完成于     |
    | file_url | str | y |      |              | 字幕文件链接 |
    | file_meta    | json  | y |      |       | 文件元信息 |
    | [ file_meta.name ] | json.attr |         |      |       | 文件原名       |
    | [ file_meta.format ] | json.attr |          |      |       | 格式/txt/pdf   |
    | [ file_meta.size ] | json.attr |         |      |       | 文件大小       |
    
5. novel

    | Filed            | Type      | Nullable | PK   | FK    | Comment        |
    | ---------------- | --------- | -------- | ---- | ----- | -------------- |
    | id           | int   |     | y |       |                |
    | ip_id        | int   | n    |      | ip.id | 参照ip的id |
    | name                | str   | n    |      |      | 标识名   |
    | reserved_names | json  | y    |      |      | 别名     |
    | [ reserved_names.jp_name ] | json.attr |         |      |      | 日文名       |
    | [ reserved_names.cn_name ] | json.attr |         |      |      | 中文名       |
    | [ reserved_names.en_name ] | json.attr |         |      |      | 英文名       |
    | [ reserved_names.rm_name ] | json.attr |         |      |      | 罗马音名     |
    | [ reserved_names.misc_name ] | json.attr |          |      |      | 混合关键字   |
    | intros              | json  | y |      |      | 简介     |
    | [ intro.cn_intro ]    | json.attr |          |      |      | 中文简介     |
    | [ intro.en_intro ]    | json.attr |          |      |      | 英文简介     |
    | image_ids | json | y | | |  |
    | [ image_ids.horizontal_image_id ] | json.attr |         |      |       | 横向图id       |
    | [ image_ids.vertical_image_id ] | json.attr |  |      |       | 竖向图id |
    | [ image_ids.reversed_image_id ] | json.attr |  |      |       | 备用图id |
    | written_by   | str   | n    |      |       | 作者       |
    | volumes_num  | int   | n    |      |       | 卷数       |
    | integrated | bool | n | | | 完整性 |
    | file_url     | str   | n    |      |       | 文件链接   |
    | file_meta    | json  | n    |      |       | 文件元信息 |
    | [ file_meta.name ] | json.attr |          |      |       | 文件原名       |
    | [ file_meta.format ] | json.attr |          |      |       | 格式/txt/pdf   |
    | [ file_meta.size ] | json.attr |          |      |       | 文件大小       |
    
6. file

    | Filed  | Type | Nullable | PK   | FK   | Comment            |
    | ------ | ---- | -------- | ---- | ---- | ------------------ |
    | id | int |     | y |      |                    |
    | region | str | n    |      |      | 区域（本地/oss |
    | bucket | str | n    |      |      | 文件桶         |
    | path | str | n    |      |      | 具体路径，包括名字 |
    | file_meta | json | n    |      |      | 文件信息       |
    | [ file_meta.name ] | json.attr |        |      |      | 文件名 |
    | [ file_meta.type ] | json.attr |        |      |      | 文件类型 |
    | [ file_meta.size ] | json.attr |  | | | 文件大小 |
    
7. tag

    | Filed | Type | Nullable | PK   | FK   | Comment |
    | ----- | ---- | -------- | ---- | ---- | ------- |
    | id    | int  |          | y    |      |         |
    | name  | str  | n        |      |      |         |

8. ip_tag

    | Filed  | Type | Nullable | PK   | FK   | Comment |
    | ------ | ---- | -------- | ---- | ---- | ------- |
    | id     | int  |          | y    |      |         |
    | ip_id  | int  | n        |      |      |         |
    | tag_id | int  | n        |      |      |         |

9. user

    | Filed         | Type    | Nullable | PK    | FK   | Comment |
    | ------------- | ------- | -------- | ----- | ---- | ------- |
    | id        | int |          | y |      |         |
    | name      | str | n    |       |      |         |
    | password  | str | n    |       |      |         |
    | salt      | str | n    |       |      |         |
    | email     | str | n    |       |      |         |
    | mobile    | str | n    |       |      |         |
    | intro     | str | n    |       |      |         |
    | avatar_id | int | y    |       |      |         |
    |            |      |          |      |      |          |
    | created_at          | date  | n    |       |      | 创建日期     |
    | comment             | str   | y    |       |      | 备注         |
    
10. caption_user

    | Filed      | Type | Nullable | PK   | FK   | Comment |
    | ---------- | ---- | -------- | ---- | ---- | ------- |
    | id         | int  |          | y    |      |         |
    | caption_id | int  | n        |      |      |         |
    | user_id    | int  | n        |      |      |         |

11. staff

    | Filed       | Type    | Nullable | PK    | FK   | Comment |
    | ----------- | ------- | -------- | ----- | ---- | ------- |
    | id      | int |          | y |      |         |
    | user_id | int | n    |       |      |         |
    |            |      |          |      |      |          |
    | created_at          | date  | n    |       |      | 创建日期     |
    | comment             | str   | y    |       |      | 备注         |
    
      

### 业务功能模块

## TODO

实现模型

重构开发文档

规范类型值域

检查是否可空

检查外键约束以及修改时的行为

设计索引

规范表comment

规范枚举值

