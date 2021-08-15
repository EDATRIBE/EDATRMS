# ToD0 List



### 最优先

重构存储

- data
  - runtime
    - bucket1
    - bucket2
    - ...
  - semi_static
    - announcemt
  - logs
  - database_backup

半静态定义：可以手动修改的静态文件，系统自动扫描生成目录



- [ ] 整理文档

在info endpoint中更新

三表的，都导出到中间表为止，第三表要么前端构建，要么后端查询

### 后端

-   [ ] 在程序启动前添加初始化配置文件中的文件夹的功能
-   [ ] 添加tag判断是否修改的逻辑
-   [ ] 设计api端点
    - [ ] 搜索
    - [ ] 检查可展示的字段
- [ ] 检查有关时间的类型转换
- [x] 设计唯一性索引
- [ ] 设计统计与日志模块
- [ ] 设计索引
- [ ] 以同步方式重构命令模块
- [ ] 规范命名
- [ ] dump性能优化
- [ ] 手工排序模型的字段

### 前端

统一field的颜色

修改password confirm 到外侧，免去删除操作

- [ ] 打印必要信息
- [ ] 构建消息翻译模型

-   [ ] 统一一下灰色有多灰
-   [x] 将index部分改成路由，由vuex存储
-   [x] 开发新增ip功能
-   [ ] 浏览器兼容性测试



搬运：porter

吉祥物：mascot

主要赞助人：top sponsor

字幕校对：caption corrector ？

字幕监制：caption inspector ？

检查：checker ？

编辑：editor

技术支持：tech support

退休干部：retired

会计：accounting



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





```json
import math
a = 0
t = 0
n = int(input())
while a < n:
    l = [int(x) for x in input().split()]
    t = t + ((l[0]*l[0] + l[1]*l[1])**0.5)/25 + 1.5*l[2]
    a = a + 1
T = math.ceil(t)
print(T)

{
    "code": "success",
    "message": "",
    "data": {
        "ips": [
            {
                "id": 1,
                "name": "ip name",
                "reservedNames": {
                    "jp": "N/A",
                    "cn": "刀剑神域",
                    "en": "sao",
                    "rm": "N/A",
                    "misc": "N/A"
                },
                "region": "CN",
                "writtenBy": "AAAAACHAN----",
                "createdBy": 1,
                "createdAt": "2021-07-30T05:16:45+08:00",
                "updateBy": 1,
                "updateAt": "2021-08-01T12:56:57+08:00",
                "comment": "THE COMMENT OF IP",
                "tagIds": [
                    17,
                    18,
                    19
                ],
                "animations": [
                    {
                        "id": 1,
                        "ipId": 1,
                        "name": "sao session 1",
                        "reservedNames": {
                            "jp": "ソードアート・オンライン s1",
                            "cn": "刀剑神域 s1",
                            "en": "sao s1",
                            "rm": "rmname sao s1",
                            "misc": "miscname sao s1"
                        },
                        "intros": {
                            "cn": "2011年10月宣佈將由A-1 Pictures改編成動畫的消息，於2012年7月起放映第1期电视動畫，並在隨後放映特別編動畫時宣佈啟動第2期电视動畫項目，其後自2014年7月起放映。[2]2015年10月4日宣布製作動畫劇場版《刀劍神域劇場版：序列爭戰》[3]，已於2017年2月18日於日本上映，臺灣則在2017年2月24日上映。2017年3月5日台灣代理木棉花宣布，動畫《刀劍神域劇場版：序列爭戰》4Dx版本於2017年3月16日上映。2017年10月宣佈第3期電視動畫製作[4]，於2018年10月6日開始播放。2019年3月30日放送完前半部（24集），後半部在2019年10月繼續放送，在播放前，後半部又再拆上下兩季，上半部分12集，下半部分11集原預計在2020年4月播放，但受2019冠狀病毒病日本疫情乃至东京都疫情的影响下，延至同年7月12日播放。[5][6]",
                            "en": "Sword Art Online is a science fantasy anime series adapted from the light novel series of the same title written by Reki Kawahara and illustrated by abec. It was produced by A-1 Pictures and directed by Tomohiko Itō.[1] It is divided into the \"Aincrad\" and \"Fairy Dance\" arcs, respectively adapted from volumes 1, 2 and one story of 8, and 3&4 from the original material. The story of the first season follows the adventures of Kazuto \"Kirito\" Kirigaya and Asuna Yuuki, two players who are trapped in the virtual world of \"Sword Art Online\" (SAO). They are tasked to clear all 100 Floors and defeat the final boss in order to be freed from the game.[2][3] Three months after the death game, Kazuto discovers that Asuna is being held captive in \"ALfheim Online\" (ALO), a spiritual successor to SAO, where the players assume the roles of fairies. Kazuto enters the game and allies himself with his sister Suguha \"Leafa\" Kirigaya to rescue Asuna from captivity.[4]"
                        },
                        "imageIds": {
                            "horizontal": 75,
                            "vertical": 76
                        },
                        "producedBy": "A-1 Pictures",
                        "releasedAt": "2014-01-31T12:12:12+08:00",
                        "type": "TV",
                        "episodesNum": 12,
                        "sharingAddresses": {
                            "baiduCloud": {
                                "url": "uuurrrlll",
                                "password": "123456"
                            },
                            "aliCloud": {
                                "url": "uuurrrlll",
                                "password": "123456"
                            }
                        },
                        "createdBy": 1,
                        "createdAt": "2021-07-30T05:27:19+08:00",
                        "updateBy": 1,
                        "updateAt": "2021-07-30T05:27:19+08:00",
                        "comment": "",
                        "images": {
                            "vertical": {
                                "id": 76,
                                "region": "local",
                                "bucket": "animation",
                                "path": "1/2eywCYaANPoNaqXQ.jpg",
                                "fileMeta": {
                                    "name": "aniimgs1.jpg",
                                    "type": "image/jpeg",
                                    "size": 123245
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:27:19+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:27:19+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/animation/1/2eywCYaANPoNaqXQ.jpg"
                            },
                            "horizontal": {
                                "id": 75,
                                "region": "local",
                                "bucket": "animation",
                                "path": "1/FmjAMkcUTovoQuXC.jpg",
                                "fileMeta": {
                                    "name": "aniimgs1.jpg",
                                    "type": "image/jpeg",
                                    "size": 123245
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:27:19+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:27:19+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/animation/1/FmjAMkcUTovoQuXC.jpg"
                            }
                        },
                        "videos": [
                            {
                                "id": 1,
                                "animationId": 1,
                                "fileMeta": {
                                    "name": "video3 animation1 ip1",
                                    "type": "AV1",
                                    "size": 1500,
                                    "quality": "720P"
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:39:18+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:39:18+08:00",
                                "comment": ""
                            }
                        ],
                        "captions": [
                            {
                                "id": 1,
                                "animationId": 1,
                                "integrated": true,
                                "state": "DOING",
                                "releasedAt": "2021-06-05T04:18:39+08:00",
                                "fileMeta": {
                                    "name": "caption3 animation1 ip1",
                                    "type": "ASS",
                                    "size": 1500
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:39:39+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:39:39+08:00",
                                "comment": "",
                                "userIds": [
                                    1,
                                    2
                                ]
                            }
                        ]
                    }
                ],
                "novels": [
                    {
                        "id": 1,
                        "ipId": 1,
                        "name": "sao v1",
                        "reservedNames": {
                            "jp": "ソードアート・オンライン v1",
                            "cn": "刀剑神域v1",
                            "en": "sao v1",
                            "rm": "rmname sao v1",
                            "misc": "miscname sao v1"
                        },
                        "intros": {
                            "cn": "原本是川原礫為了參加2002年電擊遊戲小說大獎而寫的長篇小說，但由於文章過長而無法參加，後改為在網路上以「九里史生」名義連載。連載時間是2002年11月－2008年7月，2004年開始受到大量關注，2005年開始連載最長的故事「Alicization篇」。在為了轉換心情而寫的《加速世界》獲得第15回電擊小說大獎大賞後，讀過本作的責任編輯就提議將本作在電擊文庫正式出版[註 1]。文庫版本是將網路版本的內容加以潤色或重寫而成。[註 2]在決定出版後，作者將網站上本系列已連載結束的章節刪除，並在網站上發佈「通知」[4]，將出版經過告知讀者。",
                            "en": "Sword Art Online (Japanese: ソードアート・オンライン, Hepburn: Sōdo Āto Onrain) is a Japanese light novel series written by Reki Kawahara and illustrated by abec. The series takes place in the near future and focuses on protagonist Kazuto \"Kirito\" Kirigaya and Asuna Yuuki as they play through various virtual reality MMORPG worlds. Kawahara originally wrote the series as a web novel on his website from 2002 to 2008. The light novels began publication on ASCII Media Works' Dengeki Bunko imprint from April 10, 2009, with a spin-off series launching in October 2012. The series has spawned twelve manga adaptations published by ASCII Media Works and Kadokawa. The novels and the manga adaptations have been licensed for release in North America by Yen Press."
                        },
                        "imageIds": {
                            "horizontal": 77,
                            "vertical": 78
                        },
                        "volumesNum": 25,
                        "integrated": true,
                        "fileMeta": {
                            "name": "novelname3345344",
                            "type": "TXT",
                            "size": 1500
                        },
                        "sharingAddresses": {
                            "baiduCloud": {
                                "url": "uuurrrlll",
                                "password": "123456"
                            },
                            "aliCloud": {
                                "url": "uuurrrlll",
                                "password": "123456"
                            }
                        },
                        "createdBy": 1,
                        "createdAt": "2021-07-30T05:38:28+08:00",
                        "updateBy": 1,
                        "updateAt": "2021-07-30T05:38:28+08:00",
                        "comment": "123",
                        "images": {
                            "vertical": {
                                "id": 78,
                                "region": "local",
                                "bucket": "novel",
                                "path": "1/Ycjsza2wn8FaSGZL.jpg",
                                "fileMeta": {
                                    "name": "aniimgs1.jpg",
                                    "type": "image/jpeg",
                                    "size": 123245
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:38:28+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:38:28+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/novel/1/Ycjsza2wn8FaSGZL.jpg"
                            },
                            "horizontal": {
                                "id": 77,
                                "region": "local",
                                "bucket": "novel",
                                "path": "1/vRQdt9qIUzUUyk9F.jpg",
                                "fileMeta": {
                                    "name": "aniimgs1.jpg",
                                    "type": "image/jpeg",
                                    "size": 123245
                                },
                                "createdBy": 1,
                                "createdAt": "2021-07-30T05:38:28+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-07-30T05:38:28+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/novel/1/vRQdt9qIUzUUyk9F.jpg"
                            }
                        }
                    }
                ]
            },
            {
                "id": 2,
                "name": "test2",
                "reservedNames": {
                    "jp": "xxx",
                    "cn": "测试IP",
                    "en": "test 2nd",
                    "rm": "xxxx",
                    "misc": "xxx"
                },
                "region": "CN",
                "writtenBy": "me",
                "createdBy": 1,
                "createdAt": "2021-07-30T05:47:28+08:00",
                "updateBy": 1,
                "updateAt": "2021-08-01T12:57:08+08:00",
                "comment": "xxxx",
                "tagIds": [
                    18,
                    21,
                    25
                ],
                "animations": [
                    {
                        "id": 4,
                        "ipId": 2,
                        "name": "What Do You Do at the End of the World? Are You Busy? Will You Save Us?",
                        "reservedNames": {
                            "jp": "",
                            "cn": "",
                            "en": "",
                            "rm": "",
                            "misc": ""
                        },
                        "intros": {
                            "cn": "",
                            "en": "test"
                        },
                        "imageIds": {
                            "vertical": 84
                        },
                        "producedBy": "test",
                        "releasedAt": "2021-08-20T00:00:00+08:00",
                        "type": "MOVIE",
                        "episodesNum": 12,
                        "sharingAddresses": {
                            "baiduCloud": {
                                "url": "url",
                                "password": "1234"
                            },
                            "aliCloud": {
                                "url": "urp",
                                "password": "1234"
                            }
                        },
                        "createdBy": 1,
                        "createdAt": "2021-08-01T11:50:30+08:00",
                        "updateBy": 1,
                        "updateAt": "2021-08-03T06:00:35+08:00",
                        "comment": "csfa",
                        "images": {
                            "vertical": {
                                "id": 84,
                                "region": "local",
                                "bucket": "animation",
                                "path": "4/L8BcoyCGoWmf3lYJ.jpg",
                                "fileMeta": {
                                    "name": "-56222bc4cc52e3aa.jpg",
                                    "type": "image/jpeg",
                                    "size": 218767
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-01T11:51:04+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-01T11:51:04+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/animation/4/L8BcoyCGoWmf3lYJ.jpg"
                            }
                        },
                        "videos": [
                            {
                                "id": 2,
                                "animationId": 4,
                                "fileMeta": {
                                    "name": "video editeddddd",
                                    "type": "OGG",
                                    "size": 312,
                                    "quality": "360p"
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-01T12:11:54+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T09:11:35+08:00",
                                "comment": "321"
                            },
                            {
                                "id": 6,
                                "animationId": 4,
                                "fileMeta": {
                                    "name": "",
                                    "type": "MP4",
                                    "size": 123,
                                    "quality": "1080P"
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-02T09:41:19+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T09:41:19+08:00",
                                "comment": ""
                            }
                        ],
                        "captions": [
                            {
                                "id": 2,
                                "animationId": 4,
                                "integrated": false,
                                "state": "DONE",
                                "releasedAt": "2021-08-31T00:00:00+08:00",
                                "fileMeta": {
                                    "name": "filename editeddddddd",
                                    "type": "SSA",
                                    "size": 321
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-01T11:53:55+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T09:01:10+08:00",
                                "comment": "321",
                                "userIds": []
                            },
                            {
                                "id": 3,
                                "animationId": 4,
                                "integrated": true,
                                "state": "TODO",
                                "releasedAt": "2021-08-19T00:00:00+08:00",
                                "fileMeta": {
                                    "name": "1123",
                                    "type": "ASS",
                                    "size": 12321
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-01T12:24:54+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-01T12:24:54+08:00",
                                "comment": "12321",
                                "userIds": []
                            },
                            {
                                "id": 4,
                                "animationId": 4,
                                "integrated": true,
                                "state": "TODO",
                                "releasedAt": "2021-08-21T00:00:00+08:00",
                                "fileMeta": {
                                    "name": "",
                                    "type": "SRT",
                                    "size": 123
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-01T13:40:39+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-01T13:40:39+08:00",
                                "comment": "123",
                                "userIds": []
                            }
                        ]
                    },
                    {
                        "id": 5,
                        "ipId": 2,
                        "name": "cessh",
                        "reservedNames": {
                            "jp": "",
                            "cn": "",
                            "en": "",
                            "rm": "",
                            "misc": ""
                        },
                        "intros": {
                            "cn": "",
                            "en": ""
                        },
                        "imageIds": {
                            "vertical": 87
                        },
                        "producedBy": "cesfc",
                        "releasedAt": "2021-08-20T00:00:00+08:00",
                        "type": "TV",
                        "episodesNum": 12,
                        "sharingAddresses": {
                            "baiduCloud": {
                                "url": "url",
                                "password": "123"
                            },
                            "aliCloud": {
                                "url": "url",
                                "password": "123"
                            }
                        },
                        "createdBy": 1,
                        "createdAt": "2021-08-02T00:50:59+08:00",
                        "updateBy": 1,
                        "updateAt": "2021-08-03T06:00:46+08:00",
                        "comment": "cmo",
                        "images": {
                            "vertical": {
                                "id": 87,
                                "region": "local",
                                "bucket": "animation",
                                "path": "5/5tYOHtmkc3A9IG0p.jpg",
                                "fileMeta": {
                                    "name": "IMG_0720.jpg",
                                    "type": "image/jpeg",
                                    "size": 62823
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-02T16:35:25+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T16:35:25+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/animation/5/5tYOHtmkc3A9IG0p.jpg"
                            }
                        },
                        "videos": [
                            {
                                "id": 3,
                                "animationId": 5,
                                "fileMeta": {
                                    "name": "cess",
                                    "type": "MP4",
                                    "size": 123,
                                    "quality": "1080P"
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-02T00:51:32+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T00:51:32+08:00",
                                "comment": ""
                            },
                            {
                                "id": 4,
                                "animationId": 5,
                                "fileMeta": {
                                    "name": "",
                                    "type": "MP4",
                                    "size": 21,
                                    "quality": "1080P"
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-02T00:52:01+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T00:52:01+08:00",
                                "comment": ""
                            }
                        ],
                        "captions": [
                            {
                                "id": 5,
                                "animationId": 5,
                                "integrated": true,
                                "state": "TODO",
                                "releasedAt": "2021-08-26T00:00:00+08:00",
                                "fileMeta": {
                                    "name": "",
                                    "type": "SRT",
                                    "size": 12
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-02T00:52:15+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-02T00:52:15+08:00",
                                "comment": "",
                                "userIds": []
                            },
                            {
                                "id": 8,
                                "animationId": 5,
                                "integrated": true,
                                "state": "TODO",
                                "releasedAt": "2021-08-19T00:00:00+08:00",
                                "fileMeta": {
                                    "name": "",
                                    "type": "SRT",
                                    "size": 123
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-06T01:32:42+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-06T01:32:42+08:00",
                                "comment": "",
                                "userIds": []
                            },
                            {
                                "id": 9,
                                "animationId": 5,
                                "integrated": true,
                                "state": "TODO",
                                "releasedAt": "2021-08-28T05:19:00+08:00",
                                "fileMeta": {
                                    "name": "321",
                                    "type": "SRT",
                                    "size": 123
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-06T01:35:21+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-06T01:35:21+08:00",
                                "comment": "123",
                                "userIds": [
                                    1
                                ]
                            }
                        ]
                    }
                ],
                "novels": [
                    {
                        "id": 2,
                        "ipId": 2,
                        "name": "test novel edited",
                        "reservedNames": {
                            "jp": "edited",
                            "cn": "测试 轻小说 编辑",
                            "en": "test novel edited",
                            "rm": "edited",
                            "misc": "edited"
                        },
                        "intros": {
                            "cn": "简介 edited",
                            "en": "intro  edited"
                        },
                        "imageIds": {
                            "horizontal": 94,
                            "vertical": 95
                        },
                        "volumesNum": 122,
                        "integrated": false,
                        "fileMeta": {
                            "name": "edited",
                            "type": "EPUB",
                            "size": 122
                        },
                        "sharingAddresses": {
                            "baiduCloud": {
                                "url": "url",
                                "password": "123"
                            },
                            "aliCloud": {
                                "url": "url",
                                "password": "123"
                            }
                        },
                        "createdBy": 1,
                        "createdAt": "2021-08-03T05:58:32+08:00",
                        "updateBy": 1,
                        "updateAt": "2021-08-03T07:22:05+08:00",
                        "comment": "edited",
                        "images": {
                            "vertical": {
                                "id": 95,
                                "region": "local",
                                "bucket": "novel",
                                "path": "2/TlRIssUX4DlGOfEm.jpg",
                                "fileMeta": {
                                    "name": "-3ae06371b26708d9.jpg",
                                    "type": "image/jpeg",
                                    "size": 140989
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-03T07:22:05+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-03T07:22:05+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/novel/2/TlRIssUX4DlGOfEm.jpg"
                            },
                            "horizontal": {
                                "id": 94,
                                "region": "local",
                                "bucket": "novel",
                                "path": "2/m1XACncNKXZaXGs7.jpg",
                                "fileMeta": {
                                    "name": "-4qiozQ5-g743ZhT3cShs-hs.jpg",
                                    "type": "image/jpeg",
                                    "size": 30462
                                },
                                "createdBy": 1,
                                "createdAt": "2021-08-03T07:22:05+08:00",
                                "updateBy": 1,
                                "updateAt": "2021-08-03T07:22:05+08:00",
                                "comment": "",
                                "url": "http://localhost:7000/local/novel/2/m1XACncNKXZaXGs7.jpg"
                            }
                        }
                    }
                ]
            },
            {
                "id": 3,
                "name": "test",
                "reservedNames": {
                    "jp": "",
                    "cn": "",
                    "en": "",
                    "rm": "",
                    "misc": ""
                },
                "region": "CN",
                "writtenBy": "123",
                "createdBy": 1,
                "createdAt": "2021-08-05T00:48:57+08:00",
                "updateBy": 1,
                "updateAt": "2021-08-05T00:48:57+08:00",
                "comment": "",
                "tagIds": [
                    17,
                    18,
                    26
                ],
                "animations": [],
                "novels": []
            }
        ],
        "total": 3
    }
}
```

