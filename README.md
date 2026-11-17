# 王祥 · AI Agent 工程 / AI 全栈

> 11 年后端与全栈工程底子（千万级用例调度、上亿日志、TB 级数据、99.99% 可用性），
> 2026 年 9 月起内部转做 **AI Agent 工程**：从 Agent 平台架构、Agent 质量评测，到多模型协作与人机协同，
> 以及自己写、自己发版、自己上架的 Agent 工具链。

## 基础信息

| 项目 | 内容 |
| --- | --- |
| 姓名 | 王祥（男，1992.01，上海） |
| 电话 | 18801903271 |
| 邮箱 | [ramwin@qq.com](mailto:ramwin@qq.com) |
| 教育 | 上海交通大学 · 化学工程与工艺 · 本科（2010.09 – 2014.07） |
| 求职方向 | AI Agent 工程 / 大模型应用落地 / Agent 评测与平台工程 / AI 全栈 |
| 技术影响力 | GitHub [57 followers](https://github.com/ramwin) · PyPI [42 个包](https://pypi.org/user/ramwin/) · Stack Overflow [6343 分](https://stackoverflow.com/users/3601654/ramwin) |

## 核心优势

* **Agent 系统能从零设计**：擅长把"让 AI 干这件事"拆成可判定的阶段、阶段间只传结构化契约，
  再用评测集度量每个 AI 环节的好坏——而不是把不确定性甩给用户。
* **Agent 质量能兜住**：主导多智能体测试平台设计（七阶段契约 + golden 评测集 + 失败样本回流），
  把"AI 做得对不对"变成可回归、可版本化、可灰度的工程问题。
* **工具链自己写自己发**：自研 4 个 DSH（DeepSeek Harness，类 Claude Code 的编码 Agent 宿主）插件，
  其中 2 个已开源并在 npm 发版，走完"源码 → 单元测试 → npm 发版 → 官方插件市场 PR"全链路。
* **底子够厚**：Python/Django 专家级，千万级用例、上千台执行机、上亿条日志、TB 级 tick 数据都扛过；
  高可用、灰度、容器化、消息队列不是概念，是交付过的东西。

## 工作经历

| 时间 | 公司 | 岗位 | 主线 |
| --- | --- | --- | --- |
| 2021.07 – 今 | 上海华为技术有限公司 | 系统设计师 | **2026.09 起转做 AI Agent 与测试智能化**：多智能体测试平台、测试 AI 能力评测；2021.07 – 2026.08 负责测试框架与每日自动化测试、上亿级日志分析、上千台执行机调度 |
| 2020.04 – 2021.07 | 上海锐天投资管理有限公司 | 全栈工程师 | 几十 TB 交易数据清洗比对，任务并发框架 |
| 2017.08 – 2020.04 | 上海小荐网络科技有限公司 | 系统架构师 | 千万级数据秒级计算、四千万级匹配任务队列 |
| 2016.08 – 2017.07 | 上海希格斯智能科技有限公司 | 全栈工程师 | 深入 DRF，交付会议室系统、招聘系统 |
| 2015.06 – 2016.07 | 南京振古信息技术有限公司 | 全栈工程师 | 前后端开发部署运维，管理 10 人团队 |
| 2014.07 – 2015.06 | 中天科技集团 | 工艺工程师 | 化学专业毕业后的第一份工作，同期自学编程完成转行 |

## AI Agent 工程实践

### 一、多智能体测试平台（华为 · 2026.09 起 · 验收端平台 · 设计主导）

**问题**：团队要让 AI 参与测试，但"AI 生成的用例好不好"没人能判定，模型一换、提示词一改就全面回归。

**方案**：一个只做**验收**、不做**供给**的平台——不做又一个 Agent 构建器，而是度量 Agent 的能力边界。

* **七阶段流水线，阶段间只传契约**：需求理解 → 用例生成 → 用例评审 → 脚本生成 → 执行 → 判定 → 报告；
  每个阶段输入输出是结构化契约，任何一环换模型/换实现都不影响上下游。
* **golden 评测集**：每个 AI 环节都有基准用例与通过标准（契约合规率、diff 幅度、缺陷拦截率、单任务成本），
  改提示词、换模型、调参数一律先跑评测集再上线。
* **从失败里自我进化**：失败样本聚类 → 回流成新用例与评测集资产，平台越用越准，而不是越用越飘。
* **Agent 版本化**：把"一个 Agent 的一个版本"定义为六个行为因子 + 评测集坐标，
  配套 manifest、门禁、灰度与回滚——即"Agent 也要有可回滚的版本号"。
* **人在环路**：关键判定环节保留人工复核入口，人工结论与模型结论分别记账，便于事后归因。

**产出**：平台方案与专题文档已整理为公开知识库
（[多智能体测试平台专题](https://linux-reference.ramwin.com/ai/testing/agent-testing-platform/) 含架构、版本化、自进化、外部横评），
与外部模型逐条交叉校对，未证实的结论单独挂"待验证"清单。

### 二、DSH 插件体系（开源 · npm 已发布 · 插件市场上架）

DSH（DeepSeek Harness，类 Claude Code 的编码 Agent 宿主，我日常靠它干活）缺什么就自己写插件补：

| 插件 | 作用 | 状态 |
| --- | --- | --- |
| [dsh-workspace-tree-status](https://github.com/ramwin/dsh-workspace-tree-status) | 工作区目录树显示会话聚合状态（等待/运行/完成），嵌套会话向上冒泡 | npm `0.1.0` 已发布，已提插件市场 PR |
| [dsh-turn-music](https://github.com/ramwin/dsh-turn-music) | 回合结束提醒，支持自定义音频/上传/按设备记忆音量 | npm `0.4.0` 已发布 |
| dsh-hide-left-sidebar | 像桌面端那样整栏收起侧栏并保留唤起入口 | 自用，发版准备中 |
| dsh-branch-cleaner | 识别已合并/已变基/PR 已合的分支，安全清理并留备份 ref | 自用 |

技术要点（都是踩过坑才写对的）：

* 客户端插件运行在宿主页面里，**没有官方插槽的位置只能靠运行时装饰**：给工作区树行插入状态点、
  给 AppFrame 改写 `grid-template-columns`，再用看门狗接管宿主替换节点；
* `exports.inject` 是激活门（`dsh.client.inject` 只排加载顺序），搞混就是"插件装了但没效果"；
* 每个插件都带**不依赖浏览器的单测**（自建 DOM / React / 插槽桩，`node --test`），
  改完先跑测试再热更新核对 `rev` 哈希。

### 三、多模型交叉评审房间（人在环路的多 Agent 协作）

**问题**：只让一个模型评审自己的产出，等于自说自话；让外部模型评，又怕它跑偏没人拦。

**做法**：用 Django + HTTP + WebSocket 广播做了一个"房间"——本模型、外部异模型（Kimi / Claude / DeepSeek）、
人，三方在**同一份可回放的记录**里：

* 每一步产物（计划 / 代码 diff / 执行输出 / 评价结论）送进房间，外部模型**并行**评审；
* 送审时自动开一个 **10 秒人工窗口**，人可以随时打断（`timeout` / `resumed` / `suggested` / `paused` 四态），
  人工建议的优先级高于所有模型意见；
* 所有模型都要 `approve` 才算过，有 `revise` 就改完再审一轮；某个模型报错就明确记"这一票缺失"，
  不偷偷当通过。

**价值**：把"AI 说行"变成"有签名、可追责的评审记录"，也让模型能力的短板暴露在可控的位置。

### 四、持久记忆层与上下文工程

* **记忆分两层**：规则层（人写的 `AGENTS.md` / 知识库）与事实层（插件自动沉淀的 markdown 事实，随 git 同步）；
  插件负责提取、去重、淘汰，索引按**字节预算**裁剪，避免"记住太多反而什么都没注入"。
* **上下文工程落地**：提示词按角色/工具规范/安全边界/任务管理拆模块；历史按需摘要压缩；
  检索、预算、失败样本回流都写成可复用文档，而不是个人手感。
* 沉淀的公开笔记：[上下文工程](https://linux-reference.ramwin.com/ai/agent-engineering/context-engineering.html)、
  [DAG 编排](https://linux-reference.ramwin.com/ai/agent-engineering/dag.html)、
  [模型路由](https://linux-reference.ramwin.com/ai/agent-engineering/model-routing.html)、
  [弱模型分层架构](https://linux-reference.ramwin.com/ai/agent-engineering/weak-model-layered-architecture.html)。
* 还在内网做了 DSH 的**模型网关适配与探测工具**（mock gateway、请求探针、请求汇总），
  解决"内网只有内部模型、无法直接对比外部模型"的问题。

## 项目经验（工程底子）

### 上海华为技术有限公司

* **LTE 4G 无线产品测试系统**（2022.12 – 2025.04 · 项目负责人 / 全栈，带队 6 人）
    * 打通用例设计、策略规划、用例执行的完整流程，为其他子系统提供统一 API 与适配层。
    * **千万级用例**按任意条件筛选、按多种模式匹配下发任务。
    * 百万级任务分批调度 **上千台**执行机并发测试，规划升级路径与执行流。
    * 万物留痕，每个 bug 都能复盘到具体任务与日志。
    * 容器化 + Nginx 灰度路由 + Redis 集群 + 公司运维规范，做到 **99.99%** 可用性。

* **LTE 性能监控测试平台**（2021.07 – 2022.12 · 项目负责人 / 系统架构师）
    * 每日版本全自动性能测试、归档、对比分析；分析 CPU/SoC **上亿条**指令日志，反推 CPU 行为与性能差异点。
    * 难点一：流程极长（申请虚机 → 挂盘 → 同步 **50+GB** 代码仓 → 编译 → 派发 → 回收 → 分析），
      上百人并发使用还要能定位每个任务的卡顿点；用共享盘加锁 + 按 commit 缓存产物 + 任务级断点续跑解决。
    * 难点二：单次日志 **100GB+**，自建文件格式 + 多进程分块解析（每进程只加载局部结构体）把解析压到可接受时间。

* **无线基站 SoC 性能与功耗优化方案**（2025.04 – 2026.08 · 方案设计）
    * 用仿真日志估算各类优化方案的性能/功耗收益，横向对比方案合理性，为取舍提供依据。

### 上海锐天投资管理有限公司

* 多来源 tick 与价格数据的清洗、校验和分析（TB 级、多券商互验）。
* 设计**批量任务处理框架**：Ceph 文件系统 + Redis 部署任务，借助公司 K8s 并行计算。
* 设计**pandas 处理框架**：只改配置即可完成不同券商数据的归一化。
* 设计**数据对比框架**：配置误差范围、交叉次数等约束，即可实现多数据源对比与监控。

### 上海小荐网络科技有限公司（对上智能商汇）

* 商务社交产品，负责全部后端接口与实时互动系统。
* WebSocket 实现整套聊天与网页实时互动。
* Redis + Celery + RabbitMQ 承载 **四千万数量级**匹配任务队列与推荐机制。
* 微服务模式开发，各层服务隔离。

### 其他

* **Solana 交易系统**：行情全量监听与归档，TB 级存储，1000+ QPS WebSocket 推送、2000+ QPS 成交处理、毫秒级触发，10+ 台服务器规划。

## 开源与技术影响力

* 累计向开源项目提交 **50+ 个 PR**，[PyPI 发布 42 个包](https://pypi.org/user/ramwin/)。
* Agent 工具链：[dsh-workspace-tree-status](https://github.com/ramwin/dsh-workspace-tree-status)、
  [dsh-turn-music](https://github.com/ramwin/dsh-turn-music)（均已发版）。
* [viewflow-rest](https://github.com/ramwin/viewflow-rest)（27 star）：OA 流程封装授权、流程校验、逻辑图，可像写 DAG 一样自定义流程。
* [china-public-data](https://github.com/ramwin/china-public-data)（116 star）：递归解析国内高校与行业数据。
* [django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md)：注册 model 即生成 CRUD REST 接口的脚手架。
* [hot-redis](https://github.com/ramwin/hot-redis)：在 Redis 之上做的 Python 缓存层。
* [django-command](https://github.com/ramwin/django-command)：常驻/定时/指定次数运行命令，支持软退出与超大数据集分批。
* 上游贡献：[wechatpy](https://github.com/jxtech/wechatpy/)（多进程 bug 定位、generator 取用户列表、支付回调取 appid 等 4 个 PR）、
  [django](https://github.com/django/django/pull/10497)、[tldr-pages](https://github.com/tldr-pages/tldr)、
  [faker](https://github.com/joke2k/faker/pull/769)、[jquery.barrager.js](https://github.com/yaseng/jquery.barrager.js/pull/27) 等。
* 维护 DSH 使用与 Agent 工程笔记站：[linux-reference](https://github.com/ramwin/linux-reference)（含 Agent 工程、多智能体测试平台专题）。

## 技能栈

**AI Agent 工程**

* 编排：单 Agent 循环、DAG 编排、多 Agent 角色分工与依赖图、阶段间契约设计
* 上下文：提示词分层（角色/工具/安全/任务）、检索增强、历史压缩、记忆持久化与预算裁剪
* 工具与协议：工具粒度与返回裁剪、权限白名单、MCP 思路、插件化运行时扩展
* 评测与运营：golden 评测集、契约合规与拦截率、轨迹观测、版本化 + 门禁 + 灰度回滚、人在环路
* 模型侧：多模型路由与降级、成本/延迟权衡、内网模型网关适配

**后端与架构（专家级）**

* Python 生态 10 年 +：[42 个 PyPI 包](https://pypi.org/user/ramwin/)；面向对象与可复用代码
* [Django](https://github.com/ramwin/django-reference/) / DRF：读过 serializer、view、mixin 源码；
  Django 学习 QQ 群群主（群号 461214756）；写过 django-rest-extensions、viewflow-rest
* 高可用高并发 / 分布式：Redis、Celery、RabbitMQ、K8s、Ceph、Nginx 灰度、容器化
* 数据库设计、慢查询与索引优化

**前端与其他（熟练）**

* JS / TS 插件开发（宿主插槽注入、运行时 DOM 装饰、`node --test` 单测）
* Vue 组件化、flex 自适应布局、小程序（主导对上智能商汇小程序）
* Linux 10 年运维；算法（[LeetCode](https://leetcode.com/ramwin/)、[B 站现编算法视频](https://space.bilibili.com/498198)、
  [斯坦福算法课证书](./算法证书_algorithm_certificate.pdf)）；密码学（[斯坦福密码学课证书](./密码学证书_crypto_certificate.pdf)）
* 英语：可无障碍阅读英文文档与论文，Coursera 多门英文课，CET-4/6

**证书**

* 2019 上半年 计算机技术与软件专业技术资格（初级）· 程序员
* 2019 下半年 计算机技术与软件专业技术资格（中级）· 软件设计师

## 教育经历

| 时间 | 学校 | 专业 |
| --- | --- | --- |
| 2010.09 – 2014.07 | 上海交通大学 | 化学工程与工艺（本科） |

非科班出身，毕业后自学编程转行：Coursera 补齐算法、密码学、Linux、C 语言等基础课，
靠项目和开源把工程能力补齐（2014 年起持续至今）。

## 自我评价

* **喜欢把不确定的东西做确定**：Agent 这种概率性组件，价值不在演示跑通，而在能回归、能回滚、能算清成本。
* **动手能力强**：缺工具就自己写、写完就发版；从数据库到前端、从测试框架到 Agent 工具链都自己落地过。
* **能用文字把方案讲清楚**：写方案、写文档、写复盘是习惯，公开技术笔记站长期维护。
* **冷静、可沟通**：带过 6 人、10 人团队，跨系统对接的活儿做过很多次。
