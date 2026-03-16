# 第 1 周学习总表

## 本周主题

Python + Web 基础入门，完成从“能跑起来”到“能看懂、能调试、能自己写小接口”的过渡。

## 本周目标

- 能独立创建并使用 Python 虚拟环境
- 能启动 FastAPI 服务并访问接口
- 能理解 FastAPI 代码中的核心结构
- 能区分 query、path、body 三种常见参数形式
- 能使用命令行和 `curl` 调试接口
- 能完成一个小型 FastAPI API 练习项目

## 本周安排

| 天数 | 日期 | 学习主题 | 当日产出 | 状态 |
| --- | --- | --- | --- | --- |
| Day 1 | 2026-03-16 | 环境、HTTP/JSON、FastAPI Hello World | 跑通第一个 FastAPI 服务 | 已完成 |
| Day 2 | 2026-03-17 | 逐行理解 FastAPI 代码、query 参数、POST 请求 | 能看懂 `main.py` 的核心结构 | 待学习 |
| Day 3 | 2026-03-18 | path 参数、校验、状态码、异常处理 | 能理解 404、422、201 的含义 | 待学习 |
| Day 4 | 2026-03-19 | 项目结构、router、环境变量基础 | 能把单文件应用拆成多文件 | 待学习 |
| Day 5 | 2026-03-20 | Linux/Git/API 调试命令 | 能用命令行查看项目、调试接口、提交代码 | 待学习 |
| Day 6 | 2026-03-21 | 小型实战：Todo API | 完成一个最小 CRUD 风格 API | 待学习 |
| Day 7 | 2026-03-22 | 周复盘、自测、整理 | 完成第 1 周复盘和自测 | 待学习 |

## 本周学习入口

- [Day 1](../daily/2026-03-16.md)
- [Day 2](../daily/2026-03-17.md)
- [Day 3](../daily/2026-03-18.md)
- [Day 4](../daily/2026-03-19.md)
- [Day 5](../daily/2026-03-20.md)
- [Day 6](../daily/2026-03-21.md)
- [Day 7](../daily/2026-03-22.md)

## 本周练习目录建议

本周沿用仓库根目录下的 `dayX-*` 练习目录，避免一开始把结构搞得太复杂。

建议目录：

```text
aia/
├── day1-fastapi/
├── day2-fastapi/
├── day3-fastapi/
├── day4-fastapi-structure/
├── day6-todo-api/
└── notes/
```

## 本周通过标准

本周结束时，如果你能做到下面这些，就说明第 1 周学扎实了：

1. 能独立创建 FastAPI 项目并启动服务。
2. 能解释 `app = FastAPI()`、`@app.get()`、`@app.post()` 在做什么。
3. 能分清 query 参数、path 参数和 JSON body。
4. 知道 `BaseModel` 为什么有用。
5. 能看懂基本的校验错误和 404 错误。
6. 能用 `curl` 测一个 GET 和一个 POST 接口。
7. 能完成一次 Git 提交并 push 到 GitHub。
8. 能独立做出一个小型 Todo API。

## 本周自测题

周末时请尝试自己回答这些问题：

1. FastAPI 为什么要先创建 `app = FastAPI()`？
2. `@app.get("/hello")` 和 `def hello()` 是怎么关联起来的？
3. query 参数和 path 参数有什么区别？
4. 为什么 POST 请求经常和 JSON body 一起使用？
5. `BaseModel` 帮你解决了什么问题？
6. 为什么有时会返回 422？
7. `HTTPException` 是用来做什么的？
8. `uvicorn main:app --reload` 中的 `main:app` 是什么意思？
9. 为什么要有 `requirements.txt`？
10. 你这周做的小项目解决了什么最基础的问题？

## 本周提醒

- 不要追求一下子学很多框架。
- 重点是把最小后端应用看懂、改动、运行、测试清楚。
- 如果某个概念模糊，优先回到代码和请求流程里理解。
