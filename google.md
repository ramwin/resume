Here is the English translation of your résumé:

---

# Resume of Wang Xiang  
[Download PDF from GitHub](https://raw.githubusercontent.com/ramwin/resume/master/王祥的简历-上海交通大学-全栈工程师-10年.pdf)  
[Visit GitHub repository](https://github.com/ramwin/resume/)  

[Download PDF (China mirror)](./王祥的简历-上海交通大学-全栈工程师-10年.pdf)  
[Visit mirror site](http://resume.ramwin.com/README.html)  

## Basic Information  
* Name: Wang Xiang  
* Gender: Male  
* Phone: +86 188-0190-3271  
* Email: [ramwin@qq.com](mailto:ramwin@qq.com)  
* Date of Birth: January 1992  
* [Stack Overflow: 6,333 reputation](https://stackoverflow.com/users/3601654/ramwin)  
* [GitHub: 58 followers](https://github.com/ramwin)  
* [PyPI: 40 published packages](https://pypi.org/user/ramwin/)  

## Education  
Time | School | Major  
---------- | ----------- | -----------  
Sep 2010 – Jul 2014 | Shanghai Jiao Tong University | School of Chemistry & Chemical Engineering  

## Work Experience  
Time | Company | Position | Key Technical Challenges  
------------ | ------------- | ------------- | ------  
Jul 2021 – present | Huawei Technologies (Shanghai) | Full-Stack Engineer | Test framework, daily automated testing, billion-row data processing  
Apr 2020 – Jul 2021 | Shanghai Ruitian Investment Management | Full-Stack Engineer | Dozens of TB of trading data processing, high-concurrency data-analysis framework  
Aug 2017 – Apr 2020 | Shanghai Xiaojian Network Technology | Full-Stack Engineer | Highly modular project split, ten-million-row data computed in seconds  
Aug 2016 – Jul 2017 | Shanghai Higgs Intelligence Technology | Full-Stack Engineer | Deep understanding of DRF; built meeting-room & recruitment systems  
Jun 2015 – Jul 2016 | Nanjing Zhengu Information Technology | Full-Stack Engineer | End-to-end development, deployment & ops; managed 10-person team  
Jul 2014 – Jun 2015 | Zhongtian Technology Group | Process Engineer | Self-studied cryptography, algorithms, Linux operations  

## Project Experience  

### Huawei Technologies (Shanghai)  

#### Wireless Network Product Chip Design Dept. (Apr 2025 – present)  
* **Responsibility**: Wireless-chip optimization scheme design  
  Propose performance & power-saving solutions; estimate gains from simulation logs and compare rationality of each scheme.  
* **Introduction**: Performance & power optimization for wireless base-station SoC.  
* **Challenges**:  
  – Extremely agile thinking required to challenge impossible constraints and create innovative ideas.  
  – Rapid validation ability: leverage limited resources & logs to infer real scenarios.  

#### LTE 4G Wireless Product Test System (Dec 2022 – Apr 2025)  
* **Role**: Project owner & full-stack engineer; responsible for product design, task planning, tech selection, mentoring newcomers.  
* **Team size**: 5  
* **Introduction**: Integrate data from multiple modules; complete flow of test-case design, strategy planning & execution. Design overall framework, provide unified APIs and adaptation flow for sub-systems.  
* **Challenges**:  
  – **Ten-million test cases** must be filterable on demand with various pattern matches.  
  – Schedule **hundreds** of executors for **million-level tasks** concurrently; plan upgrade path & execution flow.  
  – Full traceability: every bug can be retraced.  

#### LTE 4G Wireless Product Performance Website (Jul 2021 – Dec 2022)  
* **Role**: Project owner & full-stack engineer  
* **Introduction**: Fully automated daily performance testing, archiving & comparative analysis for every nightly build. Provide generic tools for developers to test various compile flags (CPU usage, IPC, memory ratio, cache-miss rate). Analyze memory-access logs and give optimization guidance.  
* **Challenges**:  
  Very long pipeline: request VM → mount disk → sync huge repo → adapt build tools → clear cache → compile → sync binaries → dispatch tasks → sync results → save comparison data → analyze logs.  
  1. Repo is huge: how to sync quickly (shared disk + lock to prevent simultaneous use by multiple VMs; release after compile).  
  2. Compile is slow: how to test quickly (hash repo URL → folder; store binaries by commit to avoid re-compile; save build state & leverage cache between minor versions).  
  3. Log files >100 GB: struct & global-var info alone occupy tens of GB RAM. How to parse fast (custom file format, multi-process chunked parsing, each process loads only partial structs).  
  4. Long pipeline → low reliability & easy errors (backend saves progress per task; supports re-running any single task).  

### Shanghai Ruitian Investment Management  
Mainly built internal OA systems and data-cleaning/comparison tools.  

* **Fund Adjustment Project**  
  For multiple similar funds in a group, judge assets to keep their return curves close; when holdings diverge too much, generate customizable trade list to alert traders.  
  – **Challenge**: Multi-fund data linkage; find minimal operations so that holding errors of all funds are within tolerance.  

* **Investor Compliance Review System**  
  Store all investor basic &穿透 (penetration) info; filter out non-compliant investors.  

* **Dividend System**  
  According to dividend method, frequency & benchmark, use dividend records to calculate dividend for every client / fund.  
  – **Difficulty**: Each dividend method differs; design a universal dividend framework for various methods.  

* **IPO Subscription System**  
  According to email pushes, promptly remind ops staff of eligible upcoming IPO stocks.  
  According to trading strategies, remind ops staff to confirm IPO shares & selling timing.  
  According to traders’ IPO price, quickly generate exchange-compliant IPO files.  

* **Data Cleaning**  
  Uniformly process & cross-validate TB-level tick & price data from different brokers to ensure reliability.  
  Designed a batch-task framework using Ceph filesystem + Redis for job deployment and company K8s for fast computing.  
  Designed a pandas-oriented framework: change config only to normalize data from different brokers.  

### Shanghai Xiaojian Network Technology – “MatchU” Business Social App  
* **Introduction**: A business-social app where users can find the most suitable business partners and expand their network.  
* **Tech**: django-rest-framework for CRUD APIs; WebSocket for real-time chat; redis + celery + rabbitmq for 40-million-row match queue & query mechanism, realizing recommendation engine.  
* **Responsibility**: All backend APIs; entire WebSocket chat & real-time interaction; async & cache system for huge matching tasks.  

### Shanghai Higgs Intelligence Technology – Internal Systems  
* **Introduction**: Internal company system.  
* **Tech**: django, django-rest-framework, vue  
* **Responsibility**:  
  1. Backend: forum, weekly report, todo modules.  
  2. Designed customizable business-process backend with pre-/post-conditions.  
  3. Redis-based todo function similar to Tower/Teambition.  
  4. Frontend (vue): meeting-room management system with timetable chart to see room occupancy at a glance.  
  5. **Independently implemented company OAuth system**, API format copied from WeChat Official Account login.  
  6. Integrated with company Exchange meeting-room function: query/reserve rooms on intranet and send email notifications.  

### Nanjing Zettage Information Technology – “DataBond” Cloud Platform  
* **Introduction**: A cloud computing & sharing platform where users can upload their own scripts & data to share, trade, and analyze online.  
* **Tech**: django, python, docker, mysql  
* **Responsibility**:  
  0. Set up git server.  
  1. Database design.  
  2. Backend business logic.  
  3. Partial frontend: recursive file-tree directory & operations.  
  4. Called Docker APIs to manipulate services.  
  5. Used redis + kafka + flask to provide CRUD APIs for users to upload & view sensor / streaming data.  
  6. Called Alipay API to implement user top-up & payment.  

### Other Projects  
* Zettage company homepage.  
* Ship-management platform: too many APIs, so I wrote [django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md) to auto-generate APIs by registering models.  
* Music-management project: fully leveraged git to generate repetitive code.  
* Scrapy crawler: crawled >10 sites; only used cookie/header simulation, no captcha bypass.  

#### Solana Trading System  
Full listening & archiving pipeline for Solana trading data.  
* **Challenges**  
  1. Store TB-level data.  
  2. Plan 10+ servers.  
  3. 1,000+ QPS WebSocket push.  
  4. 2,000+ QPS trade processing.  
  5. ms-level trade triggering.  

## Skills  
* **Python** – [40 published packages](https://pypi.org/user/ramwin/); solid OOP, readable & reusable code.  
* **Django & Django-REST-Framework** – studied DRF source deeply ([serializer](https://github.com/ramwin/django-reference/blob/master/rest-framework/serializer.md), [view](https://github.com/ramwin/django-reference/blob/master/rest-framework/view.md), mixin); author of [django-rest-extensions](https://github.com/ramwin/django-rest-extensions) and [viewflow-rest](https://github.com/ramwin/viewflow-rest); good at app isolation & reuse.  
* **Web Front-end & Vue, Mini-Programs** – love flex layout & responsive design; proficient in Vue & componentization; led MatchU mini-program; built music-admin with vue-router & ant-design.  
* **Redis** – handled 40-million-row tables; built async & cache system with rabbitmq + celery.  
* **Linux** – responsible for company ops; daily git/GitHub user.  
* **English** – read English docs of django, celery, redis, mysql without pressure; took many Coursera courses in English; current level 11 at tutorabc; passed CET-4 & CET-6.  
* **Algorithms** – [LeetCode profile](https://leetcode.com/ramwin/); recorded impromptu algorithm videos ([Bilibili](https://space.bilibili.com/498198)); completed Stanford algorithm course on Coursera ([certificate](https://github.com/ramwin/resume/blob/master/算法证书_algorithm_certificate.pdf)).  
* **Cryptography** – completed Stanford crypto course on Coursera ([certificate](https://github.com/ramwin/resume/blob/master/密码学证书_crypto_certificate.pdf)).  
* **IT Certificates** –初级程序员 (2019 H1), 软件设计师 (2019 H2).  
* **Java** – basic; once used [guacamole](http://guacamole.incubator.apache.org/) API to build a servlet for remote desktop inside browser ([project](https://github.com/ramwin/my_guacamole_sample/)).  

## Self-Study Courses  
* [Linux](https://courses.edx.org/courses/course-v1:LinuxFoundationX+LFS101x.2+1T2015/info)  
* [Cryptography](https://www.coursera.org/learn/crypto)  
* [Algorithms](https://www.coursera.org/learn/algorithm-design-analysis)  
* [CS101 & C](https://www.coursera.org/learn/jisuanji-biancheng)  

## Open-Source Contributions  
* [hot-redis](https://github.com/ramwin/hot-redis) – pythonic cache layer over redis for fast query.  
* [django-command](https://github.com/ramwin/django-command) – reusable django command framework: long-running, scheduled, batch-fetch huge datasets, graceful shutdown.  
* [wechatpy](https://github.com/jxtech/wechatpy/) – python WeChat API  
  – Improved docs for session storage usage.  
  – Added generator for fetching user list.  
  – Fixed QR-code generation docs.  
  – Added function to obtain appid in pay callback.  
* [Fixed django bug](https://github.com/django/django/pull/10497)  
* [tldr-pages](https://github.com/tldr-pages/tldr) – concise man pages (multiple PRs).  
* And more PRs to sqlite_bro, china-city, faker, jquery.barrager.js, etc.  

## Self-Evaluation  
* Strong self-learning ability (self-taught django, mysql, javascript).  
* Passionate about coding and hands-on practice.  
* Good English; can read English documentation fluently.  
* Calm thinker and good communicator.
