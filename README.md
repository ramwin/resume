[中文版](./README.md)/[English](./README_eng.md)
## 王祥的简历
###  基础信息
* 姓名: **王祥**
* 性别: **男**
* 电话: **18801903271**
* 邮箱: [*ramwin@qq.com*](mailto:ramwin@qq.com)
* 出生年月: **1992.01**

### 教育经历
时间 | 学校 | 专业
---------- | ----------- | -----------
2010.09 - 2014.07 | **上海交通大学** | *化学化工学院*

### 工作技能
* [python](https://github.com/ramwin/python-tutorial/)
    * 遵循`PEP8`代码规范
    * 理解面向对象编程，编写易懂，可复用的代码
* [django](https://github.com/ramwin/django-reference/)
    * 可以使用django+Apache2+MySQL搭建网站
    * 充分利用 `classbaseview` 和 `models` 的方法快速写出精简的可重复利用的代码
    * 能做到APP的充分隔离，APP复用
    * [对上App](#sharengine)
    * [数据邦项目](#zettage)
    * [个人网站项目](https://github.com/ramwin/django-reference/)
* flask
	* [数据分析项目](#tv)
* git
    * 经常使用git, github
    * 能够搭建git仓库对项目的代码进行版本控制,分支管理
    * 会搭建git服务器
* [HTML, JS, CSS, jQuery](https://github.com/ramwin/javascript_tutorial/)
    * 会用JS, jQuery进行前后端交互
    * 能实现一些滚动条,轮播图的效果
    * [振古科技官网](#homepage)
* redis
    * 知道redis的数据结构,能利用redis的数据结构做消息队列,计数器
* docker
    * 会使用docker来启动服务,制作docker镜像,服务。以此可以减少对环境的依赖,有利于服务器的维护
* 数据库
    * MySQL
    * Redis
    * MongoDB
* 密码学
* 算法
* JAVA
	* 不熟。曾使用 [guacamole](http://guacamole.incubator.apache.org/) 的API制作过一个[servlet应用](https://github.com/ramwin/my_guacamole_sample/)，实现网页上远程操作局域网内部的电脑的功能
* 英语
    * 自学 django, 读完了 [tutorial](https://docs.djangoproject.com/en/1.8/)
    * 能无压力地看英文文档

### 自学的课程
* [Linux](https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS101x.2+1T2015/info)
* [密码学](https://www.coursera.org/learn/crypto)
* [算法导论](https://www.coursera.org/learn/algorithm-design-analysis)
* [计算机导论与C语言基础](https://www.coursera.org/learn/jisuanji-biancheng)

### 贡献过的项目
* [**wechatpy** python的微信API项目](https://github.com/jxtech/wechatpy/)
    * [修改文档: 引到用户在合适的场景下使用session storage](https://github.com/jxtech/wechatpy/pull/362)
    * [添加新功能: 获取用户列表的generator](https://github.com/jxtech/wechatpy/pull/387)
    * [修改生成二维码的文档](https://github.com/jxtech/wechatpy/pull/434)
    * [添加支付回调时获取appid的函数](https://github.com/jxtech/wechatpy/pull/494)
* [修复django的bug](https://github.com/django/django/pull/10497)
* [https://github.com/tldr-pages/tldr 快速文档查看项目]
    * [https://github.com/tldr-pages/tldr/pull/1063](https://github.com/tldr-pages/tldr/pull/1063)
    * [https://github.com/tldr-pages/tldr/pull/1289](https://github.com/tldr-pages/tldr/pull/1289)
    * [https://github.com/tldr-pages/tldr/pull/2101](https://github.com/tldr-pages/tldr/pull/2101)
* [https://github.com/stonebig/sqlite_bro](https://github.com/stonebig/sqlite_bro/pull/3)
* [https://github.com/Sopage/china-city](https://github.com/Sopage/china-city/pull/1)
* [https://github.com/joke2k/faker 模拟数据生成](https://github.com/joke2k/faker/pull/769#event-1701596869)
* [给javascript项目barrager(一个能在网页显示弹幕的项目)添加自定义字体大小功能](https://github.com/yaseng/jquery.barrager.js/pull/27)

### 工作经历

时间 | 公司名称 | 岗位
------------ | ------------- | -------------
2014.07 - 2015.06 | **中天科技集团** | *工艺员*
2015.06 - 2016.06 | **南京振古信息科技有限公司** | *django后端工程师*
2016.07 - 2016.07 | **上海小荐网络科技有限公司** | *django后端工程师*
2016.08 - 今 | **上海希格斯智能科技有限公司** | *全栈工程师*


### 项目经验

<div id="sharengine"></div>

#### 对上
* 简介: 一款商务社交软件，用户可以在这里匹配到最适合的商业伙伴，轻松拓宽自己的人脉。
* 主要技术: django, python, mongodb
* 个人职责:
    0. 后台部分功能的实现
    1. 在用户创建或者加入群的时候后台自动创建一条说说
    2. 用户的说说被评论的时候，用户能收到消息并打开列表进行查看
    3. 代码优化，遵循PEP8规范，把部分函数封装在 models 里面，便于代码复用和理解

<div id="zettage"></div>  

#### 数据邦
* 简介: 一个云计算,云共享平台,用户可以把他们自己写的脚本,数据放入该平台,可以实现数据脚本共享,交易,在线分析等功能
* 主要技术: django, python, docker, mysql
* 个人职责:
    0. git服务器的搭建
    1. 数据库设计
    2. 后台逻辑业务的实现
    3. 和前端的交互
    4. 调用底层docker的接口, 对相应的服务进行操作
    5. 利用redis, kafka, flask实现了一个提供了增删改查api接口的应用,让用户可以上传并查看他们的传感器数据/流式数据。
    6. 调用支付宝API,实现用户充值支付功能
* [查看详情](./zettage/README.md)

<div id="tv"></div>

#### 数据分析
* 简介: 根据客户提供的数据,提供对应的HTTP服务,让客户能够进行数据统计分析
* 主要技术: flask, python, e-charts, redis
* 个人职责:
    1. 网站后台服务搭建
    2. 数据库优化,利用redis加sqlite来加速数据查询的速度
    3. 提供前端获取数据的API
* [查看详情](./tv/README.md)

#### 爬虫脚本
* 简介: 利用 scrapy, beautifulsoup, mysql, cron 编写爬虫脚本爬取环境质量的数据
* 爬取网站: 
    * [PM25.in](http://pm25.in/);
    * [绿色呼吸网](http://www.pm25.com);
    * [国家地表水水质自动监测实时数据发布系统](http://58.68.130.147/);

<div id="homepage"></div>

#### 振古公司主页
* 简介: 南京振古信息科技有限公司主页，[浏览](https://github.com/ramwin/zettage_homepage/).
* 个人职责:
    * 这个主页是我一个人独立完成的项目，包括：
    * 阿里云服务器管理
    * 编写html页面
    * 用js, css美化页面(除了`jQuery.min.js`, 其余js,css都是我自己独立完成的)

### 自我评价
* 自学能力强(自学django, mysql, javascript);
* 热爱编程，善于动手;
* 英语6级，可以无障碍地看英文资料,文档;
* 冷静思考，善于沟通;


