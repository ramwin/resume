# Xiang Wang · AI Agent Engineering / AI Full Stack

> 11+ years of backend and full-stack engineering (ten-million-scale test cases, 100M+ log lines,
> TB-level data, 99.99% availability). Since September 2026 I have been working on **AI Agent engineering**:
> agent platform architecture, agent quality evaluation, multi-model collaboration with a human in the loop,
> and an agent toolchain that I build, release and ship myself.

## Basic Information

| Item | Detail |
| --- | --- |
| Name | Xiang Wang (male, born Jan 1992, Shanghai) |
| Phone | +86 18801903271 |
| Email | [ramwin@qq.com](mailto:ramwin@qq.com) |
| Education | Shanghai Jiao Tong University · Chemical Engineering & Technology · B.Eng (2010.09 – 2014.07) |
| Target roles | AI Agent Engineer / LLM application engineering / Agent evaluation & platform engineering / AI full stack |
| Presence | GitHub [57 followers](https://github.com/ramwin) · PyPI [42 packages](https://pypi.org/user/ramwin/) · Stack Overflow [6,343 reputation](https://stackoverflow.com/users/3601654/ramwin) |

## Core Strengths

* **I can design an agent system from scratch**: turning "let the AI do this" into stages with decidable
  acceptance criteria, passing only structured contracts between them, and measuring every AI step with an
  evaluation set instead of dumping uncertainty on the user.
* **I can make agent quality hold up**: I lead the design of a multi-agent testing platform
  (seven-stage contracts + golden evaluation set + failure-to-test-case feedback loop), turning
  "is the AI right?" into something that can be re-run, versioned and rolled out gradually.
* **I build and ship my own tooling**: four DSH (DeepSeek Harness, a coding-agent host similar to Claude Code)
  plugins, two of them open-sourced and published on npm, going through the full chain of
  source → unit tests → npm release → marketplace PR.
* **Deep engineering base**: expert-level Python/Django; I have carried ten-million-scale test cases,
  1,000+ execution machines, 100M+ log lines and TB-level tick data. High availability, gradual rollout,
  containerization and message queues are things I have delivered, not buzzwords.

## Work Experience

| Period | Company | Role | Focus |
| --- | --- | --- | --- |
| 2021.07 – present | Huawei Technologies (Shanghai) | System Designer | **AI Agent & testing intelligence since 2026.09**: multi-agent testing platform, evaluation of test-AI capabilities; 2021.07 – 2026.08: test frameworks and daily automation, 100M+ log analysis, scheduling across 1,000+ executors |
| 2020.04 – 2021.07 | Ruitian Investment Management | Full Stack Engineer | Tens of TB of trading-data cleaning and cross-validation, concurrent task framework |
| 2017.08 – 2020.04 | Sharegine Network Technology | System Architect | Ten-million-scale data computed in seconds; 40-million-scale matching task queue |
| 2016.08 – 2017.07 | Higgs Intelligence Technology | Full Stack Engineer | Deep dive into DRF; delivered meeting-room and recruiting systems |
| 2015.06 – 2016.07 | Nanjing Zettage Information Technology | Full Stack Engineer | End-to-end development, deployment and ops; managed a team of 10 |
| 2014.07 – 2015.06 | Zhongtian Technology Group | Process Engineer | First job after a chemistry degree; self-taught programming in parallel to switch careers |

## AI Agent Engineering Practice

### 1. Multi-Agent Testing Platform (Huawei, since 2026.09, acceptance side, design lead)

**Problem**: the team wanted AI to take part in testing, but nobody could judge whether the AI-generated
test cases were good. Change the model or the prompt and everything regressed at once.

**Approach**: a platform that only does **acceptance**, never **provisioning** — not yet another agent builder,
but a way to measure an agent's capability boundary.

* **Seven stages, contracts between them**: requirement understanding → case generation → case review →
  script generation → execution → verdict → report. Every stage has a structured input/output contract, so
  swapping a model or an implementation never breaks its neighbours.
* **Golden evaluation set**: every AI step has baseline cases and pass criteria (contract compliance,
  diff size, defect interception rate, cost per task). Prompts, models and parameters are only changed after
  the evaluation set has been re-run.
* **Learning from failures**: failed samples are clustered and fed back as new cases and evaluation assets,
  so the platform gets sharper with use instead of drifting.
* **Agent versioning**: one version of one agent is defined as six behaviour factors plus evaluation-set
  coordinates, with a manifest, quality gates, gradual rollout and rollback — "an agent deserves a
  rollback-able version number too".
* **Human in the loop**: critical verdicts keep a manual review entry point; model conclusions and human
  conclusions are recorded separately for later attribution.

**Output**: the design and its companion articles are published as an open knowledge base
([multi-agent testing platform](https://linux-reference.ramwin.com/ai/testing/agent-testing-platform/):
architecture, versioning, self-evolution, external landscape), cross-checked point by point with external
models, with unverified claims kept on a separate "pending evidence" list.

### 2. DSH Plugin Suite (open source, on npm, marketplace submission)

DSH (DeepSeek Harness, a coding-agent host similar to Claude Code) is what I work with every day,
so when something is missing I write the plugin myself:

| Plugin | What it does | Status |
| --- | --- | --- |
| [dsh-workspace-tree-status](https://github.com/ramwin/dsh-workspace-tree-status) | Aggregated session status (waiting / running / finished) on workspace tree rows, bubbling up from nested sessions | npm `0.1.0` published, marketplace PR submitted |
| [dsh-turn-music](https://github.com/ramwin/dsh-turn-music) | Reminder when a turn finishes; custom audio, upload, per-device volume memory | npm `0.4.0` published |
| dsh-hide-left-sidebar | Collapse the whole sidebar like the desktop client, keeping a way to bring it back | Personal use, release in progress |
| dsh-branch-cleaner | Find branches already merged / rebased / PR-merged, delete them safely with backup refs | Personal use |

Engineering notes (each one learned the hard way):

* Client plugins run inside the host page, so **anything without an official slot has to be decorated at
  runtime**: inject a status dot into workspace tree rows, rewrite `grid-template-columns` on the AppFrame,
  and use a watchdog to take over nodes the host replaces.
* `exports.inject` is the activation gate (`dsh.client.inject` only orders loading). Confusing the two gives
  you "installed but no effect".
* Every plugin ships **unit tests that need no browser** (hand-rolled DOM / React / slot stubs, `node --test`);
  tests run first, then hot-reload is verified against the `rev` hash.

### 3. Cross-Model Review Room (multi-agent collaboration, human in the loop)

**Problem**: having one model review its own output is self-congratulation, but letting an external model
review it risks runaway feedback that nobody can stop.

**Approach**: a "room" built with Django + HTTP + WebSocket broadcasting, where my model, external models
(Kimi / Claude / DeepSeek) and the human share **one replayable record**:

* Each artefact (plan / code diff / command output / evaluation verdict) is sent into the room and reviewed
  by the external models **in parallel**.
* Sending opens a **10-second human window**; the human can interrupt at any time
  (`timeout` / `resumed` / `suggested` / `paused`), and a human suggestion outranks every model opinion.
* Every model has to `approve`; any `revise` means another round after fixing. If a model errors out, the
  record explicitly says "this vote is missing" instead of silently counting as a pass.

**Value**: "the AI said it's fine" becomes a signed, attributable review record, and model weaknesses surface
where they can be controlled.

### 4. Persistent Memory and Context Engineering

* **Two-layer memory**: a rules layer (hand-written `AGENTS.md` / knowledge base) and a facts layer
  (markdown facts extracted by a plugin and synced through git). The plugin extracts, deduplicates and evicts;
  the index is trimmed against a **byte budget** so that remembering too much does not end up injecting nothing.
* **Context engineering in practice**: prompts split into role / tool spec / safety boundary / task management
  modules; history summarised on demand; retrieval, budgeting and failure feedback written down as reusable
  docs rather than personal intuition.
* Published notes: [context engineering](https://linux-reference.ramwin.com/ai/agent-engineering/context-engineering.html),
  [DAG orchestration](https://linux-reference.ramwin.com/ai/agent-engineering/dag.html),
  [model routing](https://linux-reference.ramwin.com/ai/agent-engineering/model-routing.html),
  [layered architecture for weak models](https://linux-reference.ramwin.com/ai/agent-engineering/weak-model-layered-architecture.html).
* I also built **model-gateway adaptation and probing tools** for DSH on the intranet (mock gateway, request
  probe, request summariser), solving the problem that only an internal model was reachable and could not be
  compared against external ones.

## Engineering Background

### Huawei Technologies (Shanghai)

* **LTE 4G wireless product test system** (2022.12 – 2025.04 · project owner / full stack, team of 6)
    * Connected test-case design, strategy planning and execution into one flow, with unified APIs and an
      adaptation layer for other subsystems.
    * **Ten-million-scale test cases** filtered by any condition and dispatched by several matching modes.
    * Millions of tasks scheduled in batches across **1,000+ executors**; planned the upgrade path and
      execution flow.
    * Full traceability: every bug can be traced back to the task and the logs.
    * Containerization + Nginx gradual routing + Redis cluster + company ops standards for **99.99%** availability.

* **LTE performance monitoring platform** (2021.07 – 2022.12 · project owner / system architect)
    * Fully automated daily performance testing, archiving and comparison; analysed **100M+** CPU/SoC
      instruction log lines to infer CPU behaviour and performance deltas.
    * Challenge 1: a very long pipeline (request VM → mount disk → sync a **50+GB** repo → build → dispatch →
      collect → analyse) with hundreds of concurrent users, while still locating the stall point of any task;
      solved with a shared disk plus lock, per-commit artefact cache and task-level resume.
    * Challenge 2: **100GB+** logs per run; a custom file format plus multi-process chunked parsing, where each
      process loads only the structs it needs, brought parsing down to an acceptable time.

* **Wireless base-station SoC performance/power optimisation** (2025.04 – 2026.08 · solution design)
    * Estimated performance and power gains of optimisation options from simulation logs and compared their
      reasonableness to support the trade-off decisions.

### Ruitian Investment Management

* Cleaning, validation and analysis of multi-broker tick and price data (TB level, cross-validated).
* Designed a **batch task framework**: Ceph filesystem + Redis for task deployment, parallelised on company K8s.
* Designed a **pandas processing framework**: normalising data from different brokers by changing config only.
* Designed a **data comparison framework**: tolerance ranges and cross-check counts configured per rule to get
  multi-source comparison and monitoring.

### Sharegine Network Technology (Duishang business social app)

* Business social product; owned all backend APIs and real-time interaction.
* WebSocket-based chat and real-time web interaction.
* Redis + Celery + RabbitMQ behind a **40-million-scale** matching queue and the recommendation mechanism.
* Microservice development with layer isolation.

### Other

* **Solana trading system**: full market-data listening and archiving; TB-level storage, 1,000+ QPS WebSocket
  push, 2,000+ QPS trade processing, millisecond-level triggering, planning for 10+ servers.

## Open Source & Technical Influence

* **50+ PRs** to open-source projects; [42 packages published on PyPI](https://pypi.org/user/ramwin/).
* Agent tooling: [dsh-workspace-tree-status](https://github.com/ramwin/dsh-workspace-tree-status),
  [dsh-turn-music](https://github.com/ramwin/dsh-turn-music) (both released).
* [viewflow-rest](https://github.com/ramwin/viewflow-rest) (27 stars): authorisation, validation and logic
  diagrams for OA workflows — define a custom process like writing a DAG.
* [china-public-data](https://github.com/ramwin/china-public-data) (116 stars): recursive parsing of domestic
  university and industry data.
* [django-rest-extensions](https://github.com/ramwin/django-reference/blob/master/rest-framework/README.md):
  register a model, get CRUD REST endpoints.
* [hot-redis](https://github.com/ramwin/hot-redis): a Python cache layer on top of Redis.
* [django-command](https://github.com/ramwin/django-command): run commands permanently / on a schedule /
  a fixed number of times, with graceful shutdown and batched fetching of huge datasets.
* Upstream: [wechatpy](https://github.com/jxtech/wechatpy/) (multi-process bug diagnosis, generator for the
  user list, appid in pay callbacks — 4 PRs), [django](https://github.com/django/django/pull/10497),
  [tldr-pages](https://github.com/tldr-pages/tldr), [faker](https://github.com/joke2k/faker/pull/769),
  [jquery.barrager.js](https://github.com/yaseng/jquery.barrager.js/pull/27) and more.
* Maintain a DSH and agent-engineering notes site:
  [linux-reference](https://github.com/ramwin/linux-reference) (agent engineering, multi-agent testing platform).

## Skills

**AI Agent Engineering**

* Orchestration: single-agent loops, DAG orchestration, multi-agent role split with dependency graphs,
  contract design between stages
* Context: layered prompts (role / tools / safety / task), retrieval augmentation, history compression,
  persistent memory with budget trimming
* Tools and protocols: tool granularity and response trimming, permission allow-lists, MCP-style interfaces,
  plugin-based runtime extension
* Evaluation and operations: golden evaluation sets, contract compliance and interception rate, trace
  observation, versioning + gates + gradual rollback, human in the loop
* Model side: multi-model routing and fallback, cost/latency trade-offs, intranet model-gateway adaptation

**Backend & Architecture (expert)**

* Python ecosystem, 10+ years: [42 PyPI packages](https://pypi.org/user/ramwin/); OOP and reusable code
* [Django](https://github.com/ramwin/django-reference/) / DRF: read the source of serializers, views and
  mixins; admin of the Django learning QQ group (461214756); authored django-rest-extensions and viewflow-rest
* High availability / high concurrency / distributed systems: Redis, Celery, RabbitMQ, K8s, Ceph,
  Nginx gradual routing, containerization
* Database design, slow-query and index optimisation

**Frontend & others (proficient)**

* JS/TS plugin development (host slot injection, runtime DOM decoration, `node --test` unit tests)
* Vue componentisation, flex/responsive layouts, mini programs (led the Duishang mini program)
* 10 years of Linux operations; algorithms ([LeetCode](https://leetcode.com/ramwin/),
  [live-coded algorithm videos](https://space.bilibili.com/498198),
  [Stanford algorithms certificate](./算法证书_algorithm_certificate.pdf));
  cryptography ([Stanford cryptography certificate](./密码学证书_crypto_certificate.pdf))
* English: reads documentation and papers without friction, multiple Coursera courses in English, CET-4/6

**Certificates**

* 2019 H1 Computer Technology and Software Professional Qualification (Junior) · Programmer
* 2019 H2 Computer Technology and Software Professional Qualification (Intermediate) · Software Designer

## Education

| Period | School | Major |
| --- | --- | --- |
| 2010.09 – 2014.07 | Shanghai Jiao Tong University | Chemical Engineering & Technology (B.Eng) |

Not a computer-science graduate: I switched careers by self-teaching after graduation — Coursera courses in
algorithms, cryptography, Linux and C, then projects and open source to build real engineering depth
(continuously since 2014).

## Summary

* **I like turning the uncertain into the certain**: the value of an agent is not a demo that works once but
  something that can be re-run, rolled back and costed.
* **Hands-on**: if the tool is missing I write it and release it; I have delivered everything from database to
  frontend, from test frameworks to agent toolchains.
* **I can explain a design in writing**: proposals, docs and retrospectives are a habit; I maintain a public
  technical notes site.
* **Calm and communicative**: led teams of 6 and 10, and done plenty of cross-system integration work.
