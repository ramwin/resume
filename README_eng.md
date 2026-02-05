# Xiang Wang's Resume

## Basic Information
* Name: Xiang Wang
* Gender: Male
* Phone: +86 18801903271
* Email: [ramwin@qq.com](mailto:ramwin@qq.com)
* Date of Birth: January 1992
* Education: Shanghai Jiao Tong University

## Work Experience

| Period | Company | Position |
|--------|---------|----------|
| 2021.07 -<br> Present | Shanghai Huawei<br>Technologies Co., Ltd. | System Designer |
| 2020.04 -<br> 2021.07 | Shanghai Ruitian<br>Investment Management Co., Ltd. | Full Stack Engineer |
| 2017.08 -<br> 2020.04 | Shanghai Sharegine<br>Network Technology Co., Ltd. | System Architect |
| 2016.08 -<br> 2017.07 | Shanghai Higgs<br>Technology Co., Ltd. | Full Stack Engineer |
| 2015.06 -<br> 2016.07 | Nanjing Zettage<br>Information Technology Co., Ltd. | Full Stack Engineer |

## Technical Impact & Open Source Contributions
* [StackOverflow: 6,343 reputation](https://stackoverflow.com/users/3601654/ramwin)
* [GitHub: 57 followers](https://github.com/ramwin)
* [PyPI: 42 published packages](https://pypi.org/user/ramwin/)
* [viewflow-rest, 27 stars](https://github.com/ramwin/viewflow-rest): Workflow authorization, validation, and logic diagram encapsulation for OA processes; enables DAG-like custom workflow definitions.
* [china-public-data, 116 stars](https://github.com/ramwin/china-public-data): Recursive parsing of domestic university and industry data.
* [django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md): Rapid API development scaffolding,register models to auto-generate REST CRUD interfaces.
* [hot-redis](https://github.com/ramwin/hot-redis): Python caching layer built on Redis for high-speed data querying.
* [django-commands](https://github.com/ramwin/django-command): Framework for Django management commands supporting permanent execution, scheduled runs, soft shutdowns, and batch processing of ultra-large datasets.
* [**wechatpy** (Python WeChat API)](https://github.com/jxtech/wechatpy/):
  * [Identified multi-process bug, guided users on session storage best practices](https://github.com/jxtech/wechatpy/pull/362)
  * [Added feature: User list generator](https://github.com/jxtech/wechatpy/pull/387)
  * [Improved QR code generation documentation](https://github.com/jxtech/wechatpy/pull/434)
  * [Added function to retrieve appid during payment callbacks](https://github.com/jxtech/wechatpy/pull/494)
* [Fixed Django bug](https://github.com/django/django/pull/10497)
* [tldr-pages](https://github.com/tldr-pages/tldr): Added documentation for [rdesktop](https://github.com/tldr-pages/tldr/pull/1063), [find](https://github.com/tldr-pages/tldr/pull/1289), and [unzip](https://github.com/tldr-pages/tldr/pull/2101).
* [china-city](https://github.com/Sopage/china-city/pull/1)
* [faker (Mock data generator)](https://github.com/joke2k/faker/pull/769#event-1701596869)
* [Added custom font size feature to barrager.js (JavaScript danmaku/barrage project)](https://github.com/yaseng/jquery.barrager.js/pull/27)

Total: Submitted 50+ PRs to various open source projects.

## Project Experience

### Solana Trading Monitoring System
Independently designed and delivered mission-critical data infrastructure for a Web3 quantitative trading team.

Technical Challenges:
1. **10+TB** database management and storage optimization using token-based sharding and hot/cold data hierarchy
2. automated task load balancing on 10+ high performance servers, with data redundancy backup
3. **1,000+ QPS** WebSocket push notifications
4. **2,000+ QPS** transaction query processing
5. Millisecond-level trading monitoring triggers (address tracking, price plummeted, high-quality user position building)

### Huawei Technologies Co., Ltd.

#### Performance Monitoring & Testing Platform
* Role: Project Lead, System Architect
* Overview:  
Responsible for Daily version monitoring, compiler parameter optimization and analyzing billions of CPU and SOC instruction logs to analyse CPU behavior and performance bottlenecks.  
Implemented fully automated daily performance testing, archiving, and comparative analysis.  
Memory access pattern analysis for optimization guidance.
* Key Challenges:
  1. Extremely long pipeline with **50+GB** product code repositories; needed to support hundreds of concurrent users while quickly pinpointing task issues and bottlenecks.
  2. Massive log volumes requiring custom data format designs for rapid analysis and retrieval.

#### RF Antenna Testing System
* Role: Project Leader, Full Stack Engineer—responsible for product design, task workflow planning, technical selection, and mentoring new team members
* Team Size: 6 people(include me)
* Overview:  
Integrated the system with other company platforms to complete test case design, strategy planning, and execution workflows.  
Designed the overall project framework, providing unified APIs and adaptation processes for subsystems.
* Key Challenges:
  1. **Million-level test cases** with real-time filtering and pattern matching for task distribution.
  2. How to batch-schedule millions of tasks across **thousands** of execution machines for concurrent testing; optimizing upgrade paths and execution workflows.
  3. Full traceability for bug reproduction and analysis.
  4. Up to **99.99%** availability through containerization, Nginx grayscale routing, Redis clustering, and compliance with company DevOps standards.

### Shanghai Ruitian Investment Management Co., Ltd.

Multi-Source Tick Data Cleaning and Analysis
* Unified processing of TB-level historical tick data and price data from different brokers, cross-validating to ensure data reliability.
* Designed a **batch task processing framework** using Ceph filesystem + Redis for task deployment, leveraging on company K8s services for fast parallel computing.
* Developed a **pandas processing framework** enabling data normalization across different brokers through configuration-only modifications.
* Created a **data comparison framework** allowing multi-source data comparison and monitoring through configurable rules (tolerance ranges, cross-frequency constraints, etc.).

### Shanghai Sharegine Network Technology Co., Ltd. — Duishang Business Social Platform

* Overview: A business social networking app enabling users to match with optimal business partners and expand their network.
* Tech Stack: Django REST Framework, Python
* Responsibilities:
  1. Complete backend API development
  2. Implemented full chat mechanism using WebSocket and real-time web interaction systems
  3. Utilized Redis, Celery, and RabbitMQ to handle **40 million-level** matching task queues and query mechanisms; implemented the system's recommendation engine
  4. Microservices architecture development with proper service isolation across layers

## Skills

### Expert-Level
* Python Ecosystem ([Reference](https://github.com/ramwin/python-reference/))
  * [Published 42 packages on PyPI](https://pypi.org/user/ramwin/)
  * Strong OOP principles; writes clean, reusable, and maintainable code
  * [Django](https://github.com/ramwin/django-reference/) & [Django REST Framework](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md):  
    Administrator of Django Learning QQ Group (ID: 461214756). Deep understanding of DRF source code including [serializers](https://github.com/ramwin/django-reference/blob/master/rest-framework/serializer.md), [views](https://github.com/ramwin/django-reference/blob/master/rest-framework/view.md), and mixins.
    * Developed [django-rest-extensions](https://github.com/ramwin/django-rest-extensions): Auto-generates REST APIs through model registration
    * Developed [viewflow-rest](https://github.com/ramwin/viewflow-rest): Workflow management with proper app isolation and reusability

* System Architecture Design (High Availability, High Concurrency, Distributed Systems)
  * [Linux](https://github.com/ramwin/linux-reference/): 10 years of operations experience; researched underlying OS principles, SOC memory access architectures, and C++ code optimization
  * Redis: Processed tables with 40+ million records; built async systems and caching layers using RabbitMQ, Redis, and Celery

* Database Design and Optimization

### Proficient
* Algorithms
  * [LeetCode Profile](https://leetcode.com/ramwin/)
  * Recorded algorithm videos (live coding without preparation): [Bilibili Channel](https://space.bilibili.com/498198)
  * Completed Stanford University's Algorithm course on Coursera (English): [Certificate](https://github.com/ramwin/resume/blob/master/算法证书_algorithm_certificate.pdf)

* Web Frontend ([Reference](https://github.com/ramwin/html-reference)) & [Vue.js](https://github.com/ramwin/html-reference/blob/master/vue/README.md), [Mini Programs](https://github.com/ramwin/mini-program-reference)
  * Proficient in flex layouts with adaptive/responsive design principles
  * Component-based development with Vue.js
  * Led development of Duishang mini program

* English
  * Proficiency in reading technical documentation (Django, Celery, Redis, MySQL docs)
  * Completed multiple Coursera courses in English
  * 2+ years of continuous English training at TutorABC (formerly VIPABC)
  * CET-4 and CET-6 certified

* Cryptography
  * Completed Stanford University's Cryptography course on Coursera (English): [Certificate](https://github.com/ramwin/resume/blob/master/密码学证书_crypto_certificate.pdf)

* Certifications
  * 2019 (First Half): Junior Computer Qualification—Programmer
  * 2019 (Second Half): Intermediate Computer Qualification—Software Designer

## Summary
* Strong self-learning ability (self-taught Django, MySQL, Vue.js, Cryptography)
* Passionate about programming and hands-on implementation
* Excellent English skills—capable of reading technical documents without barriers
* Calm thinker with strong communication skills
