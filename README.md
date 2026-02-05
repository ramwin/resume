# 王祥的简历

##  基础信息
* 姓名: 王祥
* 性别: 男
* 电话: 18801903271
* 邮箱: [*ramwin@qq.com*](mailto:ramwin@qq.com)
* 出生年月: 1992.01
* 毕业院校: 上海交通大学

## 工作经历

时间 | 公司名称 | 岗位 | 技术挑战
------------ | ------------- | ------------- | ------
2021.07 -<br> 今 | 上海华为技术有限公司 | 系统设计师 | 测试框架,每日自动化测试<br>上亿级别数据处理<br>上千台服务器设备并发通信和调度
2020.04 -<br> 2021.07 | 上海锐天投资管理有限公司 | 全栈工程师 | 几十TB交易数据处理<br> 数据并发处理分析框架
2017.08 -<br> 2020.04 | 上海小荐网络科技有限公司 | 系统架构师 | 大量拆分模块项目<br>千万级数据计算,秒级计算
2016.08 -<br> 2017.07 | 上海希格斯智能科技有限公司 | 全栈工程师 | 深入理解DRF<br>完成会议室系统,招聘系统
2015.06 -<br> 2016.07 | 南京振古信息科技有限公司 | 全栈工程师 | 项目前后端开发部署运维<br>管理10人团队

## 技术影响力
* [stackoverflow: 6343分](https://stackoverflow.com/users/3601654/ramwin)
* [github: 57 followers](https://github.com/ramwin)
* [pypi: 42个项目](https://pypi.org/user/ramwin/)
* [viewflow-rest, 27个star](https://github.com/ramwin/viewflow-rest), 在OA流程上,封装了授权,流程校验,逻辑图功能,可以像写dag一样自定义流程.  
* [china-public-data, 116个star](https://github.com/ramwin/china-public-data), 递归解析了国内高校,行业数据  
* [django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md)快速进行api开发的脚手架, 只要注册model，就能生成CRUD的rest接口.  
* [hot redis](https://github.com/ramwin/hot-redis) 在redis基础上设计了python的缓存,实现数据的快速查询
* [django commands](https://github.com/ramwin/django-command) 常用的django命令框架,永久运行,指定时间,指定次数运行命令,支持软退出, 支持超大数据集合的分批获取
* [**wechatpy** python的微信API项目](https://github.com/jxtech/wechatpy/)
    * [发现多进程bug, 引导用户在合适的场景下使用session storage](https://github.com/jxtech/wechatpy/pull/362)
    * [添加新功能: 获取用户列表的generator](https://github.com/jxtech/wechatpy/pull/387)
    * [修改生成二维码的文档](https://github.com/jxtech/wechatpy/pull/434)
    * [添加支付回调时获取appid的函数](https://github.com/jxtech/wechatpy/pull/494)
* [修复django的bug](https://github.com/django/django/pull/10497)
* [tldr](https://github.com/tldr-pages/tldr) 补充[rdesktop](https://github.com/tldr-pages/tldr/pull/1063), [find](https://github.com/tldr-pages/tldr/pull/1289), [unzip](https://github.com/tldr-pages/tldr/pull/2101)的语法
* [https://github.com/Sopage/china-city](https://github.com/Sopage/china-city/pull/1)
* [https://github.com/joke2k/faker 模拟数据生成](https://github.com/joke2k/faker/pull/769#event-1701596869)
* [给javascript项目barrager(一个能在网页显示弹幕的项目)添加自定义字体大小功能](https://github.com/yaseng/jquery.barrager.js/pull/27)  

累计向开源项目提交了50+个PR


## 项目经验

### solana交易监控系统
为某Web3量化团队设计并独立交付了核心数据基础设施  
* 技术挑战
    1. **10+TB**级别的数据库管理,设计冷热分层,根据token分数据库高并发存储策略  
    2. 10+节点集群的自动化运维与负载均衡
    3. 实现**1000+qps**的websocket推送  
    4. 实现**2000+qps**的交易查询处理  
    5. 实现ms级的交易监控(关注地址,价格异动,优质用户建仓)触发  

### 上海华为技术有限公司

* 性能监控测试网站
    * 个人职责: 项目负责人, 系统架构师  
    * 项目简介:  
    每天版本监控,编译参数寻优,根据CPU,SOC上亿条指令日志,分析反推CPU行为,性能差异点.  
    实现每日版本的性能数据全自动测试,归档,对比分析.  
    分析内存访问记录,提供优化指导  
    * 项目难点:
        1. 流程非常长,产品代码仓**50+GB**,需要能支撑上百人同时使用的同时快速定位每个任务的问题和卡顿点.  
        2. 日志超级多,需要设计各种数据格式方便快速分析查找.

* 射频天线测试系统
    * 个人职责: 项目负责人, 全栈工程师, 负责产品方案设计, 任务流程规划, 技术选型, 新人指导
    * 带队人数: 6人(含自己)
    * 项目简介:  
    与公司其他系统对接, 完成用例设计, 策略规划, 用例执行的完整流程.  
    设计整个项目框架, 提供统一规范的API和适配流程给其他子系统  
    * 项目难点:  
        1. **千万级用例**方便用户随时筛选,各种模式匹配下发任务  
        2. 百万级任务如何分批调度**上千**台执行机**并发**测试. 合理规划升级路径, 执行流程.  
        3. 万物留痕, 方便复盘每个bug的出现.  
        4. 业务需要, 服务容器化+nginx灰度路由+redis集群+公司运维规范做到了 **99.99%** 可用性. 

### 上海锐天投资管理有限公司
* 多来源的tick数据价格数据的清洗和分析.  
    * 对不同券商上TB级别的历史tick数据和价格数据进行统一处理, 互相之间进行验证,确保数据的可靠性.  
    * 设计了一套**批量任务处理框架**, 利用ceph文件系统+redis部署任务, 利用公司k8s服务进行快速并行计算  
    * 设计了一套针对**pandas处理的框架**, 只用修改配置就能实现不同券商数据的归一化.  
    * 设计了一套针对数据进行对比的框架, 通过配置规则(误差范围,交叉次数等逻辑约束)就能实现各数据源的对比和监控.  

### 上海小荐网络科技有限公司 -- 对上智能商汇
* 简介: 一款商务社交软件，用户可以在这里匹配到最适合的商业伙伴，轻松拓宽自己的人脉。
* 利用django-rest-framework做基本的crud接口
* 主要技术: django-rest-framework, python
* 个人职责:
    1. 全部的后台接口
    2. 利用websocket做了整套的聊天机制，和网页的实时互动系统
    3. 利用redis, celery, rabbitmq处理了 **四千万数量级**的匹配数量的任务队列和查询机制。实现了系统的推荐机制
    4. 微服务模式开发, 做到了各层服务隔离.  


## 工作技能
### 专家级
* [python](https://github.com/ramwin/python-reference/)生态
    * [发布过42个项目](https://pypi.org/user/ramwin/)
    * 理解面向对象编程，编写易懂，可复用的代码
    * [django](https://github.com/ramwin/django-reference/) & [django-rest-framework](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md)  
    点击上面的django链接可以看我学习django的笔记，我是django开发学习QQ群的群主（群号: 461214756）,欢迎您加入。
        * 深入了解了django-rest-framework的源码，了解里面的[serializer](https://github.com/ramwin/django-reference/blob/master/rest-framework/serializer.md), [view](https://github.com/ramwin/django-reference/blob/master/rest-framework/view.md), mixin的原理
        * 写了[django-rest-extensions](https://github.com/ramwin/django-rest-extensions),可以快速生成一个model的api
        * 写了[viewflow-rest](https://github.com/ramwin/viewflow-rest)
        * 能做到APP的充分隔离，APP复用
* 系统架构设计(高可用高并发,分布式系统设计)
    * [linux](https://github.com/ramwin/linux-reference/)10年运维经验 另外研究过各种底层操作系统原理,SOC访存结构,C++代码优化
    * redis
        * 处理过超过四千万的数据表，充分利用rabbitmq, redis, celery做了用户匹配后台的异步系统和缓存系统。
* 数据库设计与优化

### 熟练级
* 算法
    * [leetcode链接](https://leetcode.com/ramwin/)
    * 录制过一些算法视频，都是现编的算法，无前期准备。[视频链接](https://space.bilibili.com/498198)
    * coursera上了算法课程, 斯坦福大学，纯英文授课。[课程链接](https://www.coursera.org/course/algo) [课程证书](https://github.com/ramwin/resume/blob/master/算法证书_algorithm_certificate.pdf)

* [web前端](https://github.com/ramwin/html-reference) & [vue](https://github.com/ramwin/html-reference/blob/master/vue/README.md), [小程序](https://github.com/ramwin/mini-program-reference)
    * 喜欢flex布局，写代码时喜欢考虑自适应
    * 熟练运用vue。习惯于组件化页面代码。
    * 主导开发了对上智能商汇小程序。
* 英语
    * 能无压力地看大部分英文文档。直接阅读了django, celery, redis, mysql的英文文档
    * 上很多coursera的英文课程
    * 持续在tutorabc(原vipabc)上了2年多英语课
    * 大学过了四六级
* 密码学
    * coursera上了密码学的课程, 斯坦福大学，纯英文授课。[课程链接](https://www.coursera.org/learn/crypto/home/welcome) [课程证书](https://github.com/ramwin/resume/blob/master/密码学证书_crypto_certificate.pdf)
* 计算机证书
    * 2019年上半年考了计算机初级 - 程序员
    * 2019年下半年考了计算机中级 - 软件设计师

## 自我评价
* 自学能力强(自学django, mysql, vue, 密码学);
* 热爱编程，善于动手;
* 英语不错，可以无障碍地看英文资料,文档;
* 冷静思考，善于沟通;
