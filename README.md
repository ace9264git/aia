# all in ai

> 一个记录我学习 AI Agent、构建项目、准备投递 AI Agent 应用开发实习的成长型仓库。

## 项目简介

`all in ai` 用来记录我在 3 个月内系统学习 AI Agent 应用开发的全过程。

这不是一个只看理论的学习仓库，而是一个以“能做项目、能写简历、能参加面试”为目标的实战型作品集。整个学习周期按 **12 周、每天 4-6 小时** 设计，最终目标是完成可投递实习的项目作品和求职材料。

## 最终目标

3 个月结束时，我需要拿出下面 4 样东西：

1. 1 个基础 Agent 项目
2. 1 个 RAG 项目
3. 1 个业务型 Agent 项目
4. 1 份能投实习的简历 + GitHub + 项目 README

## 核心能力目标

学习完成后，我希望自己能够：

- 使用 Python 和 FastAPI 开发 AI 应用后端
- 调用大模型 API 并处理流式输出、异常和环境变量
- 使用 structured outputs 返回稳定 JSON
- 使用 function calling / tools 完成基础 Agent 能力
- 独立完成一个基础 RAG 项目
- 设计并实现 Agent workflow
- 部署 demo，并能清楚讲解项目设计

## 12 周学习路线概览

| 阶段 | 周数 | 重点 | 阶段目标 |
| --- | --- | --- | --- |
| 第 1 阶段 | 第 1-4 周 | Python、FastAPI、模型 API、structured outputs、function calling | 做出一个基础工具调用 Agent Demo |
| 第 2 阶段 | 第 5-8 周 | RAG、检索优化、Agent workflow、前后端联调 | 完成一个可演示的 RAG 文档问答 Agent |
| 第 3 阶段 | 第 9-12 周 | 业务型 Agent、工程化、部署、简历整理、投递准备 | 完成主项目并具备投递实习能力 |

详细时间安排见：[12 周学习时间表](docs/LEARNING_SCHEDULE.md)

## 项目产出规划

### 项目 1：基础工具调用 Agent

展示重点：

- function calling
- structured outputs
- 简单工具调度
- 基础对话状态管理

### 项目 2：RAG 文档问答 Agent

展示重点：

- 文档上传与切分
- 向量检索
- 基于上下文生成回答
- 引用来源展示
- 未命中兜底处理

### 项目 3：业务型 Agent

优先考虑方向：

1. SQL 数据分析 Agent
2. 简历筛选 Agent
3. 客服工单分流 Agent
4. 会议纪要 Agent

## 每天学习节奏

建议每天投入 4-6 小时：

1. 前 2 小时：学习新内容，阅读文档，跑 demo
2. 中间 2 小时：动手编码，完成接口、工具或联调
3. 最后 1-2 小时：提交 Git、写 README、记录问题和复盘

## 每周固定动作

每周至少完成以下事项：

- 提交 4-5 次 Git
- 完成一个可运行的小功能
- 更新 README 或学习记录
- 周末进行一次复盘

## 仓库规划

当前仓库将逐步扩展为以下结构：

```text
all in ai/
├── README.md
├── docs/
│   └── LEARNING_SCHEDULE.md
├── notes/
│   ├── README.md
│   ├── templates/
│   │   └── DAILY_CHECKIN_TEMPLATE.md
│   └── daily/
│       └── 2026-03-16.md
├── projects/
│   ├── basic-agent/
│   ├── rag-agent/
│   └── business-agent/
└── assets/
```

## 学习记录

从今天开始，这个仓库会持续记录每日学习打卡。

- 每日学习记录入口：[notes/README.md](notes/README.md)
- 今日打卡：[notes/daily/2026-03-16.md](notes/daily/2026-03-16.md)
- 每日模板：[notes/templates/DAILY_CHECKIN_TEMPLATE.md](notes/templates/DAILY_CHECKIN_TEMPLATE.md)

## 当前里程碑清单

- [ ] 完成基础工具调用 Agent
- [ ] 完成 RAG 文档问答 Agent
- [ ] 完成业务型 Agent 主项目
- [ ] 完成项目 README 和演示材料
- [ ] 完成简历初稿
- [ ] 开始投递 AI Agent 应用开发实习

## 使用方式

这个仓库将持续记录：

- 每周学习计划和完成情况
- 项目开发过程
- 遇到的问题与解决方案
- 面试准备内容
- 投递前的简历和项目整理过程

如果你也在学习 AI Agent，希望这份路线能成为一个清晰、务实、能落地的执行模板。
