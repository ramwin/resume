**Author**: *[Xiang Wang](../README.md)* @   2016-05-30 15:47:42  
**e-mail**: [*ramwin@qq.com*](mailto:ramwin@qq.com)  

# 数据邦项目简介

**数据邦**是我在 *南京振古信息科技有限公司* 全程参与的一个产品项目。  

* 项目名称: 数据邦
* 项目描述: 一个云计算,云共享平台,用户可以把他们自己脚本,数据放入该平台,可以实现数据脚本共享,交易,在线分析等功能
* 职责范围: web后端，数据库设计使用，页面渲染部分，部分前端js代码。
* 相关技术: `python`, `django`, `MySQL`, `git`, `javascript`, `redis`, `tomcat`, `flask`等

### 用户注册登录模块
![注册登录](./img/注册登录.png)  
利用所学的密码学知识，实现了一个网页的`RSA`基础加密功能。  
[javascript加密代码](https://github.com/ramwin/javascript_tutorial/blob/master/ramwin1_convert.js)  
[python解密代码](https://github.com/ramwin/javascript_tutorial/blob/master/xor_crypto.py)

### 大数据上传模块  
![大数据上传](./img/大数据上传.png)  
根据我的基础代码，其他人实现了数据邦的网页大文件上传功能，实现上传文件的同时对每块代码进行md5校验以及断点续传功能  
[javascript上传文件片段的基础代码](https://github.com/ramwin/django_tutorial/blob/master/chunk_upload/templates/chunk_upload/index.html)  
[django处理](https://github.com/ramwin/django_tutorial/blob/master/chunk_upload/views.py)  

### 工作台
![工作台](./img/工作台.png)  
使用 [guacamole](http://guacamole.incubator.apache.org/) 制作过一个`tomcat`应用，让用户能够直接打开网页操作他的云主机。  
[我的项目地址](https://github.com/ramwin/my_guacamole_sample)  
[JAVA代码](https://github.com/ramwin/my_guacamole_sample/tree/master/src/main/java/net/sourceforge/guacamole/net/example)  
后台由我的同事使用`docker`来创建各种应用，并提供`restful api`。我根据前端传递的参数来调用后台接口。  
但是我也能够使用`docker`的基础命令，创建保存镜像，实现各个应用之间的环境隔离。  
[我使用过的docker镜像](https://hub.docker.com/u/ramwin/starred/)  

### 充值交易模块
![输入金额](./img/输入金额.png)  
![支付宝扫码付款](./img/支付宝扫码付款.png)
调用支付宝提供的API接口，实现付款功能。处理支付宝发送的付款结果。

### 传感器模块
![实时数据](./img/实时数据.png)  
利用`redis`，`kafka`，`flask`实现大数据的增删改查功能。让用户能够自定义传感器，上传传感器数据，查看传感器数据。 配合工作台的工具，用户可以实时监控设备运行状况

### 工具模块
![工具发布](./img/工具发布.png)
调用同事提供的`restful api`接口，实现工具上传，发布服务等功能。

[查看完整简历](../README.md)
