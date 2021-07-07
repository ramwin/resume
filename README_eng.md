[Chinese](./README.md)/[English](./README_eng.md)

## PERSONAL RESUME
###  Personal Information
* Name: **Xiang Wang**
* Gender: **Male**
* Cell Phone: **18801903271**
* E-mail Address: [*ramwin@qq.com*](mailto:ramwin@qq.com)
* Date of Birth: **1992.01**
* [stackoverflow's reputation: 4083](https://stackoverflow.com/users/3601654/ramwin)
* [github: 31 followers](https://github.com/ramwin)
* [pypi: 7 projects](https://pypi.org/user/ramwin/)

### Education
Time | School | Major
---------- | ----------- | -----------
2010.09 - 2014.07 | **Shanghai Jiaotong University** | *Chemistry and Chemical Engineering*

### Skill
* [python](https://github.com/ramwin/python_tutorial/)
    * follow the PEP8 standard, write readable and reusable code
* [django](https://github.com/ramwin/django-reference/)
    * able to establish an website using django
    * use classbaseview, encapsulate the models to develop quickly
    * write standalone, resuable app
    * [Match up app](#sharengine)
    * [zettage daas project](#zettage)
    * [personal website](https://github.com/ramwin/django-reference/)
* flask
	* [order data analysis](#tv)
* git
    * used to control the version and branch of my project using git and github
* [HTML, JS, CSS, jQuery](https://github.com/ramwin/javascript_tutorial/)
    * interaction using javascript, jQuery
    * can realize some effects such as toggle or slide
    * [zettage.com](#homepage)
* redis
    * know the basic structure of redis (I like to use the list as a message queue).
* docker
    * be used to use docker to run different service on my computer
* database
    * MySQL
    * Redis
    * MongoDB
* cryptography
* algorithm
* JAVA
	* not familiar. Once following the tutorial of [guacamole](http://guacamole.incubator.apache.org/) to build a [servlet app](https://github.com/ramwin/my_guacamole_sample/), which can be used to control the computers inside the local lan.
* English
    * learn django by myself, finish reading the [tutorial](https://docs.djangoproject.com/en/1.8/)
    * able to read English documentation easily

### lessons
* [Introduction to Linux](https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS101x.2+1T2015/info)
* [Cryptography](https://www.coursera.org/learn/crypto)
* [Algorithms: Design and Analysis](https://www.coursera.org/learn/algorithm-design-analysis)
* [Introduction to computing with C language](https://www.coursera.org/learn/jisuanji-bianchen)

### My Contribution to some Open Source Repository
* [**wechatpy** python API for wechat](https://github.com/jxtech/wechatpy/)
    * [modify documents: encourage user to use session storage in proper situation](https://github.com/jxtech/wechatpy/pull/362)
    * [new function: create a generator to iterate user's openid](https://github.com/jxtech/wechatpy/pull/387)
    * [modify documents: the usage of creating wechat qrcode](https://github.com/jxtech/wechatpy/pull/434)
    * [add function to read the appid from wechat pay callback](https://github.com/jxtech/wechatpy/pull/494)
* [https://github.com/tldr-pages/tldr]
    * [https://github.com/tldr-pages/tldr/pull/1063](https://github.com/tldr-pages/tldr/pull/1063)
    * [https://github.com/tldr-pages/tldr/pull/1289](https://github.com/tldr-pages/tldr/pull/1289)
    * [https://github.com/tldr-pages/tldr/pull/2101](https://github.com/tldr-pages/tldr/pull/2101)
* [Fix Django bug](https://github.com/django/django/pull/10497)
* [https://github.com/stonebig/sqlite_bro](https://github.com/stonebig/sqlite_bro/pull/3)
* [https://github.com/Sopage/china-city](https://github.com/Sopage/china-city/pull/1)
* [https://github.com/joke2k/faker](https://github.com/joke2k/faker/pull/769#event-1701596869)
* [enbale customer fontsize in the barrager project(which can show barrage in the website)](https://github.com/yaseng/jquery.barrager.js/pull/27)

### Working Experience

Time | Company | Position
------------ | ------------- | -------------
2014.07 - 2015.06 | **ZTT** | *Technologist*
2015.06 - 2016.06 | **Nanjing Zettage Information Technology Co., Ltd** | *Full stack Developer*
2016.08 - 2017.07 | **Shanghai Higgs Technology Co., Ltd** | *Full Stack Developer*
2017.07 - 2020.04 | **Shanghai Sharegine Network Technology Co., Ltd** | *Full Stack Developer*
2020.04 - now | **Shanghai Ruitian Investment Management Co., Ltd** | *Full Stack Developer*


### Project Experience
<div id="sharengine"></div>

#### Match up app
* Introduction: Match up is a commercial social software where people can find their ideal partner, broaden their connection.
* Technology: django, python, mongodb
* Responsibility:
    0. realize some back-end's feature
    1. create a dynamic at the back-end whenever a people create a group or join in a group
    2. create a message when uses' dynamic was replied, show the reply list to users
    3. optimize the code, follow the PEP8 standard, encapsulate some function to models to make it readable and reusable


<div id="zettage"></div>  

#### Zettage daas
* Introduction:  a cloud computing, sharing platform where uses can share their script, tool, data and purchase other's script, tool, data and analysis online.
* Technology: django, python, docker, mysql
* Responsibility:
    0. establish the git server and control the branch, version of project
    1. design the structure of database in a clear and week coupling way
    2. the backend logic
    3. interacting with the front end engineer and discuss the api
    4. invoke the restful api to create different service for user
    5. use redis, kafka, flask to build an application for users so that they can invoke the api to upload, delete, modify their streaming data/sensor data.
    6. read the alipay documentation and implement the function of charge and pay.
* [See details](./zettage/README.md)

<div id="tv"></div>

#### Order data analysis
* Introduction: Use the order provided by the customer, build a website for data analysis
* Technology: flask, python, e-charts, redis
* Responsibility:
    0. the back end service of the website
    1. optimize the database, use memory database (redis) to accelerate the query performance
    3. provide the API for front end engineer
* [See details](./tv/README.md)

#### Spider script
* Introduction: crawl the environmental data using scrpy, mysql, cron
* Data sources: 
    * [PM25.in](http://pm25.in/);
    * [green breathe](http://www.pm25.com);
    * [The national surface water quality automatic detection in real time data publishing system](http://58.68.130.147/);

<div id="homepage"></div>

#### Zettage homepage
* Introduction: Homepage of Zettage company, [visit it](https://github.com/ramwin/zettage_homepage/).
* Responsibility:
    * the website is set up all by myself, including:
    * manage the ubuntu server
    * write the basic html
    * beautify the website using javascript and css (all the javascript and css code is written by myself except the `jQuery.min.js`).

### Self-judgement
* strong self-learning ability (taught myself django, mysql, javascript) and practical ability;
* love programming;
* Chinese English Test level 6, can read the English material or documentation without difficulty;
* calm with good communication skills;
