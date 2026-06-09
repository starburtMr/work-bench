# Project Rescue Intake

> 用于开始诊断前收集最少必要上下文。未知项不要编造，填 `Unknown`。

## 1. 项目基本信息

| 字段 | 内容 |
|---|---|
| 项目名称 |  |
| 项目根目录 |  |
| Run ID |  |
| 报告目录 |  |
| 诊断触发原因 |  |
| 当前业务目标 |  |
| 当前开发阶段 | 概念 / 原型 / MVP / 内测 / 生产 / 交付验收 / Unknown |
| 主要用户/客户 |  |
| 是否有生产数据 | Yes / No / Unknown |
| 是否涉及支付/权限/隐私/敏感数据 | Yes / No / Unknown |
| 是否允许运行命令 | No / Read-only only / Local verification / Unknown |
| 是否落盘报告 | Yes / No，默认 Yes |

## 2. 当前痛点

| 痛点 | 观察到的证据 | 影响 | 紧急程度 |
|---|---|---|---|
|  |  |  |  |

## 3. 已知真源

| 真源类型 | 位置 | 更新时间 | 可信度 | 备注 |
|---|---|---|---|---|
| 产品范围 |  |  | High / Medium / Low |  |
| 技术选型 |  |  | High / Medium / Low |  |
| 数据模型 |  |  | High / Medium / Low |  |
| API 契约 |  |  | High / Medium / Low |  |
| 前端规则 |  |  | High / Medium / Low |  |
| 后端规则 |  |  | High / Medium / Low |  |
| 任务计划 |  |  | High / Medium / Low |  |
| 发布/回滚 |  |  | High / Medium / Low |  |

## 4. 权限与限制

- 不可读取的目录/文件：
- 不可执行的命令：
- 不可触碰的环境：
- 必须遵守的项目规则：
- 必须保护的数据或密钥：

## 5. 本轮诊断目标

- 只做风险分诊：Yes / No
- 输出完整报告：Yes / No
- 需要落盘到 `docs/rescue/runs/<run-id>/`：Yes / No，默认 Yes
- 需要判断继续/冻结/终止：Yes / No
