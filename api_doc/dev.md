# 开发文档

## 需求分析

### 系统目标

本项目旨在建立一个较为完善的英配资源数据库，将各种EXCEL文档或其他信息整理进数据方便查询调用。

本项目主要有三种应用场景：

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

    就是设置不同用户权限，有的可以修改，有的只能查询，这类功能。

4. 日志功能

    记录数据库修改信息，方便纠错。

5. 报表功能

    能够输出年度总结

## 总体设计

### 数据层设计

1. ip

    | Filed         | Type | Nullable | PK   | FK   | Comment      |
    | ------------- | ---- | -------- | ---- | ---- | ------------ |
    | id            | int  | n        | y    |      |              |
    | name          | str  | n        |      |      | 标识名       |
    | reversed_name | str  | y        |      |      | 备用名       |
    | jp_name       | str  | y        |      |      | 日文名       |
    | cn_name       | str  | y        |      |      | 中文名       |
    | en_name       | str  | y        |      |      | 英文名       |
    | rm_name       | str  | y        |      |      | 罗马音名     |
    |               |      |          |      |      |              |
    |               |      |          |      |      |              |
    | created_by    | str  | n        |      |      | 创建人       |
    | created_at    | date | n        |      |      | 创建日期     |
    | updated_by    | str  | n        |      |      | 最近编辑人   |
    | updated_at    | date | n        |      |      | 最近编辑日期 |
    | comment       | str  | y        |      |      | 备注         |

2. animation

    | Filed               | Type | Nullable | PK   | FK    | Comment             |
    | ------------------- | ---- | -------- | ---- | ----- | ------------------- |
    | id                  | int  | n        | y    |       |                     |
    | ip_id               | int  | y        |      | ip.id |                     |
    | name                | str  | n        |      |       | 标识名              |
    | jp_name             | str  | y        |      |       | 日文名              |
    | cn_name             | str  | y        |      |       | 中文名              |
    | en_name             | str  | y        |      |       | 英文名              |
    | rm_name             | str  | y        |      |       | 罗马音名            |
    | studio              | str  | n        |      |       | 出品公司            |
    | written_by          | str  | y        |      |       | 原著作者            |
    | type                | str  | n        |      |       | TV/movie/SP/OVA/OAD |
    | eps_num             | int  | n        |      |       | 集数                |
    | en_intro            | str  | y        |      |       | 中文简介            |
    | cn_intro            | str  | y        |      |       | 英文简介            |
    | horizontal_image_id | id   | y        |      |       | 图片列表            |
    | vertical_image_id   |      |          |      |       |                     |
    | reversed_image_id   |      |          |      |       |                     |

3. video

    | Filed         | Type | Nullable | PK   | FK           | Comment           |
    | ------------- | ---- | -------- | ---- | ------------ | ----------------- |
    | id            | int  | n        | y    |              |                   |
    | animation_id  | int  | n        |      | animation.id |                   |
    | video_url     | str  | n        |      |              | 视频链接          |
    | video_size    | int  | n        |      |              | 视频大小          |
    | video_quality | str  | n        |      |              | 分辨率（720/原画/ |
    | video_format  | str  | n        |      |              | 格式（mp4/        |

4. caption

    | Filed        | Type | Nullable | PK   | FK           | Comment         |
    | ------------ | ---- | -------- | ---- | ------------ | --------------- |
    | id           | int  |          | y    |              |                 |
    | animation_id | int  | n        |      | animation.id |                 |
    | caption_url  | str  | n        |      |              | 字幕链接        |
    | integrity    | bool | n        |      |              | 完整性          |
    | status       | str  | n        |      |              | doing/todo/done |
    | done_at      | date | n        |      |              | 完成日          |

5. novel

    | Filed       | Type | Nullable | PK   | FK    | Comment        |
    | ----------- | ---- | -------- | ---- | ----- | -------------- |
    | id          | int  | n        | y    |       |                |
    | ip_id       | int  | n        |      | ip.id | 参照ip的id     |
    | name        | str  | n        |      |       | 名字+正篇/番外 |
    | written_by  | str  | n        |      |       | 作者           |
    | volume_num  | int  | n        |      |       | 卷数           |
    | file_format | str  | n        |      |       | 格式/txt/pdf   |
    | file_size   | int  | n        |      |       | 文件大小       |
    | file_url    | json | n        |      |       | 文件链接       |
    | en_intro    | str  | y        |      |       | 中文简介       |
    | cn_intro    | str  | y        |      |       | 英文简介       |
    | image_id    | int  |          |      |       |                |

6. file

    | Filed  | Type | Nullable | PK   | FK   | Comment            |
    | ------ | ---- | -------- | ---- | ---- | ------------------ |
    | id     | int  | n        | y    |      |                    |
    | region | str  | n        |      |      | 区域（本地/oss     |
    | bucket | str  | n        |      |      | 文件桶             |
    | path   | str  | n        |      |      | 具体路径，包括名字 |
    | meta   | json | n        |      |      | 文件信息           |

7. tag

    | Filed | Type | Nullable | PK   | FK   | Comment |
    | ----- | ---- | -------- | ---- | ---- | ------- |
    | id    | int  | n        | y    |      |         |
    | name  | str  | n        |      |      |         |

8. tag_ip

    | Filed  | Type | Nullable | PK   | FK   | Comment |
    | ------ | ---- | -------- | ---- | ---- | ------- |
    | id     | int  | n        | y    |      |         |
    | tag_id | int  | n        |      |      |         |
    | ip_id  | int  | n        |      |      |         |

9. contributor

    | Filed     | Type | Nullable | PK   | FK   | Comment |
    | --------- | ---- | -------- | ---- | ---- | ------- |
    | id        | int  | n        | y    |      |         |
    | name      | str  | n        |      |      |         |
    | password  | str  | n        |      |      |         |
    | salt      | str  | n        |      |      |         |
    | email     | str  | y        |      |      |         |
    | mobile    | str  | y        |      |      |         |
    | intro     | text | y        |      |      |         |
    | avatar_id | int  | y        |      |      |         |

10. contributor_caption

    | Filed          | Type | Nullable | PK   | FK   | Comment |
    | -------------- | ---- | -------- | ---- | ---- | ------- |
    | id             | int  | n        | y    |      |         |
    | contributor_id | int  | n        |      |      |         |
    | caption_id     | int  | n        |      |      |         |

11. staff

    | Filed          | Type | Nullable | PK   | FK   | Comment |
    | -------------- | ---- | -------- | ---- | ---- | ------- |
    | id             | int  | n        | y    |      |         |
    | contributor_id | int  | n        |      |      |         |

    

