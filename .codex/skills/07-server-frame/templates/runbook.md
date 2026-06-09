# 后端运行手册 Runbook

## 1. 环境要求

- 语言版本：
- 包管理器：
- 数据库：
- 端口：

## 2. 环境变量

复制 `.env.example` 为 `.env`，填入本地开发配置。

| 变量名 | 必填 | 示例 | 说明 | 是否敏感 |
|---|---|---|---|---|
| APP_ENV | 是 | development | 运行环境 | 否 |
| PORT | 是 | 3000 | 服务端口 | 否 |
| DATABASE_URL | 视项目而定 | postgres://... | 数据库连接 | 是 |

## 3. 安装依赖

```bash
# 填写项目实际命令
```

## 4. 启动项目

```bash
# 填写项目实际命令
```

## 5. 健康检查

```bash
curl http://localhost:<PORT>/health
```

预期返回：

```json
{
  "success": true
}
```

## 6. 数据库连接验证

```bash
# 填写项目实际命令
```

## 7. 最小 API 验证

### 成功请求

```bash
curl http://localhost:<PORT>/api/v1/_example/ping
```

### 参数错误请求

```bash
curl -X POST http://localhost:<PORT>/api/v1/_example/validate -H "Content-Type: application/json" -d '{}'
```

### 系统错误请求

```bash
curl http://localhost:<PORT>/api/v1/_example/error
```

## 8. 日志检查

- 请求日志位置：
- 错误日志位置：
- requestId / traceId 字段：

## 9. 常见问题

| 问题 | 可能原因 | 处理方式 |
|---|---|---|
| 启动失败 | 缺少环境变量 | 检查 `.env` 与 `.env.example` |
| health 失败 | 服务未启动/端口错误 | 检查启动日志 |
| DB 连接失败 | 连接串错误/数据库未启动 | 检查 `DATABASE_URL` |
