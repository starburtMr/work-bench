# External Source Map

> 本文件记录 v2 设计时参考的外部方法。使用这些来源时只取其方法论映射，不把它们当成项目事实。

| 来源 | 关键思想 | 在本 skill 中的映射 |
|---|---|---|
| PMI, “Rescue My Project™” — https://www.pmi.org/learning/library/project-failure-recovery-positive-outcome-6550 | 对 troubled project 先评估现状，再决定救援或终止 | `Release / Continuation Decision`、继续/冻结/终止候选结论 |
| DORA metrics — https://dora.dev/guides/dora-metrics/ | 用交付吞吐和不稳定性衡量软件交付能力 | `delivery_health_checklist` 中的交付健康代理指标 |
| Scrum.org Evidence-Based Management — https://www.scrum.org/resources/evidence-based-management | 用当前价值、未实现价值、上市时间、创新能力观察价值交付 | 产品/交付横向健康扫描 |
| NIST SSDF SP 800-218 — https://csrc.nist.gov/pubs/sp/800/218/final | 把安全开发实践纳入 SDLC | 安全与供应链检查表、STOP 信号 |
| OWASP SAMM — https://owaspsamm.org/model/ | 从 Governance、Design、Implementation、Verification、Operations 看安全成熟度 | 安全横向维度和安全补救 playbook |
| OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/ | 应用安全验证要求 | 鉴权、输入校验、敏感数据、错误响应检查方向 |
| OpenAPI Specification — https://swagger.io/specification/ | 用标准、语言无关的接口描述统一 HTTP API | `talk-link` 缺口判断、API 契约真源 |
| C4 model — https://c4model.com/ | 为现有代码建立不同层级的架构地图 | 大项目子系统拆分、架构与边界扫描 |
| Twelve-Factor App — https://12factor.net/ | 配置、构建、发布、运行分离等 SaaS 可运维原则 | 环境变量、部署、配置漂移检查 |
| OpenSSF Scorecard — https://scorecard.dev/ | 自动化评估开源项目安全风险信号 | 依赖与供应链健康扫描 |
| SLSA — https://slsa.dev/ | 用 source/build/provenance 等层级提升软件供应链可信度 | 构建来源、CI、发布产物可追溯检查 |
| Google SRE Postmortem Culture — https://sre.google/sre-book/postmortem-culture/ | 事故复盘记录影响、缓解、根因、后续动作，并建立复盘文化 | 交付/运维健康、事故证据、blameless 复盘检查 |
| Martin Fowler, Technical Debt Quadrant — https://martinfowler.com/bliki/TechnicalDebtQuadrant.html | 区分 deliberate/inadvertent、prudent/reckless 技术债 | 风险登记和“可后补/必须补/阻塞”的债务分级 |
| Thoughtworks, Fitness Function Driven Development — https://www.thoughtworks.com/en-us/insights/articles/fitness-function-driven-development | 用可持续反馈约束架构质量 | 质量门禁、架构漂移复查条件 |

## 使用注意

- 外部方法只提供诊断视角，不替代项目真实证据。
- 如果用户要求当前工具、依赖、法规、漏洞等最新信息，运行本 skill 时应重新查官方来源。
- 不要把行业最佳实践强塞到不适用项目；必须结合项目阶段、风险、团队能力和交付目标。
