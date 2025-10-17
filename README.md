# 王祥的简历
[github下载pdf版本](https://raw.githubusercontent.com/ramwin/resume/master/王祥的简历-上海交通大学-全栈工程师-10年.pdf)  
[github访问](https://github.com/ramwin/resume/)  

[国内下载pdf版本](./王祥的简历-上海交通大学-全栈工程师-10年.pdf)  
[国内访问](http://resume.ramwin.com/README.html)  


##  基础信息
* 姓名: 王祥
* 性别: 男
* 电话: 18801903271
* 邮箱: [*ramwin@qq.com*](mailto:ramwin@qq.com)
* 出生年月: 1992.01
* [stackoverflow: 6333分](https://stackoverflow.com/users/3601654/ramwin)
* [github: 58 followers](https://github.com/ramwin)
* [pypi: 40个项目](https://pypi.org/user/ramwin/)

## 教育经历
时间 | 学校 | 专业
---------- | ----------- | -----------
2010.09 - 2014.07 | 上海交通大学 | *化学化工学院*

## 工作经历

时间 | 公司名称 | 岗位 | 技术挑战
------------ | ------------- | ------------- | ------
2021.07 至<br> 今 | 上海华为技术有限公司 | *全栈工程师* | 测试框架,每日自动化测试<br>上亿级别数据处理
2020.04 至<br> 2021.07 | 上海锐天投资管理有限公司 | *全栈工程师* | 几十TB交易数据处理<br> 数据并发处理分析框架
2017.08 至<br> 2020.04 | 上海小荐网络科技有限公司 | *全栈工程师* | 大量拆分模块项目<br>千万级数据计算,秒级计算
2016.08 至<br> 2017.07 | 上海希格斯智能科技有限公司 | *全栈工程师* | 深入理解DRF<br>完成会议室系统,招聘系统
2015.06 至<br> 2016.07 | 南京振古信息科技有限公司 | *全栈工程师* | 项目前后端开发部署运维<br>管理10人团队
2014.07 至<br> 2015.06 | 中天科技集团 | *工艺员* | 自学密码学,算法原理,linux运维

## 项目经验

### 上海华为技术有限公司

#### 无线网络产品设计部(2025.04~今)
* 个人职责: 无线芯片优化方案设计  
设计芯片内性能,功耗优化方案, 根据仿真日志推算收益对比各个方案的合理性.  
* 项目简介:  
无线基站产品芯片SOC的性能和功耗优化设计.  
* 项目难点:  
需要思维异常敏捷,能挑战一切不可能的约束,提出创新型的想法.  
需要快速验证的能力,能利用可用的资源和日志尽可能推算真实场景.  

#### LTE 4G无线产品部测试系统(2022.12~2025.04)
* 个人职责: 项目负责人, 全栈工程师, 负责产品方案设计, 任务流程规划, 技术选型, 新人指导
* 带队人数: 5人
* 项目简介:  
综合其他模块功能数据, 完成用例设计, 策略规划, 用例执行的完整流程.  
设计整个项目框架, 提供统一规范的API和适配流程给其他子系统  
* 项目难点:  
**千万级用例**方便用户随时筛选,各种模式匹配  
百万级任务如何分批调度**上千**台执行机**并发**测试. 合理规划升级路径, 执行流程.  
万物留痕, 方便复盘每个bug的出现.  

#### LTE 4G无线产品部性能网站(2021.07~2022.12)
* 个人职责: 项目负责人, 全栈工程师
* 项目简介:
实现每日版本的性能数据全自动测试,归档,对比分析.  
提供通用工具方便开发测试各种编译参数的性能(CPU占用率,IPC,内存占比,cache miss率)   
分析内存访问记录,提供优化指导  
* 项目难点:
流程非常长, 需要 申请虚拟机 -- 挂载磁盘 -- 同步代码仓 -- 适配编译工具 -- 清理缓存 -- 编译软件 -- 同步可执行文件 -- 下发执行任务 -- 同步性能测试结果 -- 保存对比数据 -- 访问日志分析  
    1. 代码仓巨大, 如何快速同步(使用共享磁盘挂载,并加锁避免多个虚拟机同时使用,编译后释放)  
    2. 编译很慢,如何快速测试(根据代码仓url生成hash保存到指定文件夹,以commit来保存二进制文件,避免重复编译. 保存编译状态, 小版本之间充分利用缓存)  
    3. 日志文件上百G, 光结构体信息和全局变量信息就占用了几十个G内存. 如何快速准确解析.(设计文件保存格式, 支持分批多进程解析, 尽量让每个进程只载入部分结构体和全局变量)  
    4. 任务流程非常长,执行可靠新差,容易报错怎么办(利用后端保存各个任务进度,支持每个任务的单独执行)

### 上海锐天投资管理有限公司
主要做公司内部OA系统和数据清洗对比工作  

* 基金调整项目
    对一个组内的多个同类基金进行资产判断,保证他们的收益曲线接近. 当持仓差异过大时生成可自定义的交易列表提醒交易员
    * 项目难点: 多个基金的数据联动变化,需要找到最小操作次数让多个基金的持仓误差小于执行范围

* 投资人合规审查系统  
    保存所有投资人的基础信息穿透信息,对不合规的投资人进行剔除

* 分红系统  
    根据分红方式,分红频率,分红基准,利用分红记录, 实现对每个客户/每个基金分红的计算
    * 难点
    每种分红的方式都不一致, 需要设计一套通用的分红框架给不同分红方式

* 打新系统  
    根据邮件推送,及时提醒运营人员满足条件,即将打新的股票
    根据交易策略,及时提醒运营人员确认打新份额,卖出时机
    根据交易员下发的打新价格,快速生成交易所的打新规范文件

* 数据清洗
    对不同券商上TB级别的tick数据和价格数据进行统一处理, 互相之间进行验证,确保数据的可靠性.  
    设计了一套批量任务处理框架, 利用ceph文件系统+redis部署任务, 利用公司k8s服务进行快速计算  
    设计了一套针对pandas处理的框架, 只用修改配置就能实现不同券商数据的归一化.  

### 上海小荐网络科技有限公司 -- 对上智能商汇
* 简介: 一款商务社交软件，用户可以在这里匹配到最适合的商业伙伴，轻松拓宽自己的人脉。
* 利用django-rest-framework做基本的crud接口
* 主要技术: django-rest-framework, python
* 个人职责:
    1. 全部的后台接口
    2. 利用websocket做了整套的聊天机制，和网页的实时互动系统
    3. **利用redis, celery, rabbitmq处理了四千万数量级的匹配数量的任务队列和查询机制。实现了系统的推荐机制**

### 上海希格斯智能科技有限公司 [内网系统](https://github.com/ramwin/resume/blob/master/higgs/)
* 简介: 给公司内部使用的系统
* 主要技术: django django-rest-framework vue
* 个人职责:
    1. 后台系统。包含论坛，周报，代办事项等模块
    2. 设计了公司的业务流程后台，从而能实现业务流程的自定义，设置流程的前置条件和后置任务
    3. 利用redis实现了网页上类似tower, teambition的代办事项功能。
    4. 前端页面, 主要用vue。做过会议室管理系统，做了时间表，可以通过图表一眼看到哪个会议室什么时候在被人使用. [图片链接](https://github.com/ramwin/resume/blob/master/higgs/img/会议室管理系统.png)
    5. **独立实现了公司的oauth系统, 接口格式照抄了微信公众号的登录认证模式** [图片链接](https://github.com/ramwin/resume/blob/master/higgs/img/oauth2.0认证系统_1.png)
    6. 和公司的exchange系统里的会议室功能联动，实现了在内网上查询预定会议室以及发送邮件通知的功能。

### 南京振古信息科技有限公司 [数据邦](https://github.com/ramwin/resume/blob/master/zettage/README.md)
* 简介: 一个云计算,云共享平台,用户可以把他们自己写的脚本,数据放入该平台,可以实现数据脚本共享,交易,在线分析等功能
* 主要技术: django, python, docker, mysql
* 个人职责:
    0. git服务器的搭建
    1. 数据库设计
    2. 后台逻辑业务的实现
    3. 部分前端页面。用递归写了文件的目录树以及对应的操作功能
    3. 调用底层docker的接口, 对相应的服务进行操作
    4. 利用redis, kafka, flask实现了一个提供了增删改查api接口的应用,让用户可以上传并查看他们的传感器数据/流式数据。
    5. 调用支付宝API,实现用户充值支付功能

### 其他项目
* 振古公司主页。
* 船舶管理平台。这个平台的接口太多了，所以我写了[django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md)代码，通过注册model，就能生成api接口
* 音乐管理项目。充分利用git，实现了用代码去写重复代码。
* 爬虫项目。用scrapy爬过十几种网站。最多只涉及cookie,header的模拟，没涉及过反验证码。

#### solana交易系统
实现solana交易数据的全监听, 归档流程.
* 项目难点
    1. 上TB级别的数据存储.
    2. 10+台服务器的规划
    3. 实现1000+qps的websocket推送
    4. 实现2000+qps的交易处理
    5. 实现ms级的交易触发

## 工作技能
* [python](https://github.com/ramwin/python-reference/)
    * [发布过40个项目](https://pypi.org/user/ramwin/)
    * 理解面向对象编程，编写易懂，可复用的代码
* [django](https://github.com/ramwin/django-reference/) & [django-rest-framework](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md)  
点击上面的django链接可以看我学习django的笔记，我是django开发学习群的群主（群号: 461214756）,欢迎您加入。
    * 深入了解了django-rest-framework的源码，了解里面的[serializer](https://github.com/ramwin/django-reference/blob/master/rest-framework/serializer.md), [view](https://github.com/ramwin/django-reference/blob/master/rest-framework/view.md), mixin的原理
    * 写了[django-rest-extensions](https://github.com/ramwin/django-rest-extensions),可以快速生成一个model的api
    * 写了[viewflow-rest](https://github.com/ramwin/viewflow-rest)
    * 能做到APP的充分隔离，APP复用
* [web前端](https://github.com/ramwin/html-reference) & [vue](https://github.com/ramwin/html-reference/blob/master/vue/README.md), [小程序](https://github.com/ramwin/mini-program-reference)
    * 喜欢flex布局，写代码时喜欢考虑自适应
    * 熟练运用vue。习惯于组件化页面代码。
    * 主导开发了对上智能商汇小程序。
    * 利用vue-router, ant-design做了音乐项目后台系统
* [redis](https://github.com/ramwin/linux-reference/blob/master/redis.md)
    * 处理过超过四千万的数据表，充分利用rabbitmq, redis, celery做了用户匹配后台的异步系统和缓存系统。
* [linux](https://github.com/ramwin/linux-reference/)
    * 一直负责公司的运维工作
    * 经常使用git, github
* 英语
    * 能无压力地看大部分英文文档。直接阅读了django, celery, redis, mysql的英文文档
    * 上很多coursera的英文课程
    * 一直在tutorabc(原vipabc)上英语课，当前等级level11
    * 大学过了四六级
* 算法
    * [leetcode链接](https://leetcode.com/ramwin/)
    * 录制过一些算法视频，都是现编的算法，无前期准备。[视频链接](https://space.bilibili.com/498198)
    * coursera上了算法课程, 斯坦福大学，纯英文授课。[课程链接](https://www.coursera.org/course/algo) [课程证书](https://github.com/ramwin/resume/blob/master/算法证书_algorithm_certificate.pdf)
* 密码学
    * coursera上了密码学的课程, 斯坦福大学，纯英文授课。[课程链接](https://www.coursera.org/learn/crypto/home/welcome) [课程证书](https://github.com/ramwin/resume/blob/master/密码学证书_crypto_certificate.pdf)
* 计算机证书
    * 2019年上半年考了计算机初级 - 程序员
    * 2019年下半年考了计算机中级 - 软件设计师
* JAVA  
不熟, 曾使用 [guacamole](http://guacamole.incubator.apache.org/) 的API制作过一个[servlet应用](https://github.com/ramwin/my_guacamole_sample/)，实现网页上远程操作局域网内部的电脑的功能。[图片链接](https://github.com/ramwin/resume/blob/master/zettage/img/工作台.png)

## 自学的课程
* [Linux](https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS101x.2+1T2015/info)
* [密码学](https://www.coursera.org/learn/crypto)
* [算法导论](https://www.coursera.org/learn/algorithm-design-analysis)
* [计算机导论与C语言基础](https://www.coursera.org/learn/jisuanji-biancheng)

## 贡献过的项目
* [hot redis](https://github.com/ramwin/hot-redis) 在redis基础上设计了python的缓存,实现数据的快速查询
* [django commands](https://github.com/ramwin/django-command) 常用的django命令框架,永久运行,指定时间,指定次数运行命令,支持软退出, 支持超大数据集合的分批获取
* [**wechatpy** python的微信API项目](https://github.com/jxtech/wechatpy/)
    * [修改文档: 引到用户在合适的场景下使用session storage](https://github.com/jxtech/wechatpy/pull/362)
    * [添加新功能: 获取用户列表的generator](https://github.com/jxtech/wechatpy/pull/387)
    * [修改生成二维码的文档](https://github.com/jxtech/wechatpy/pull/434)
    * [添加支付回调时获取appid的函数](https://github.com/jxtech/wechatpy/pull/494)
* [修复django的bug](https://github.com/django/django/pull/10497)
* [tldr](https://github.com/tldr-pages/tldr) 快速文档查看项目
    * [https://github.com/tldr-pages/tldr/pull/1063](https://github.com/tldr-pages/tldr/pull/1063)
    * [https://github.com/tldr-pages/tldr/pull/1289](https://github.com/tldr-pages/tldr/pull/1289)
    * [https://github.com/tldr-pages/tldr/pull/2101](https://github.com/tldr-pages/tldr/pull/2101)
* [https://github.com/stonebig/sqlite_bro](https://github.com/stonebig/sqlite_bro/pull/3)
* [https://github.com/Sopage/china-city](https://github.com/Sopage/china-city/pull/1)
* [https://github.com/joke2k/faker 模拟数据生成](https://github.com/joke2k/faker/pull/769#event-1701596869)
* [给javascript项目barrager(一个能在网页显示弹幕的项目)添加自定义字体大小功能](https://github.com/yaseng/jquery.barrager.js/pull/27)



## 自我评价
* 自学能力强(自学django, mysql, javascript);
* 热爱编程，善于动手;
* 英语不错，可以无障碍地看英文资料,文档;
* 冷静思考，善于沟通;
