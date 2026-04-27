# 阶段复习：进阶部分 (Review: Advanced Python)

恭喜到达进阶部分的最后一站！在本章中，我们将回顾进阶阶段涉及的全部知识领域，通过综合练习和自测题检验你的学习成果。

## 导语

进阶部分涵盖了 Python 中最实用的几个高级主题：异步编程让你能同时处理大量并发任务，FastAPI 帮助你快速构建现代 Web API，依赖注入让你的代码更可测试和可维护，数据库操作让你的程序具备数据持久化能力，JSON 是网络数据交换的通用语言，NumPy 则是科学计算和数据分析的基石。这七个主题看似独立，但在实际项目中常常**组合使用**——例如一个 FastAPI API 可能需要异步连接数据库、序列化 JSON 响应、甚至调用 NumPy 做数据处理。复习的目的不是"再看一遍"，而是帮你**建立知识之间的连接**，形成完整的认知地图。

## 学习目标

- 系统回顾进阶部分的 7 个知识领域，查漏补缺
- 通过综合练习将多个知识点融会贯通
- 通过自测题检验理解深度，为后续学习奠定基础

## 知识回顾清单

对照以下清单，确认你对每个知识点有清晰的理解。如果某个条目让你犹豫，请回到对应章节重新学习。

### 1. 异步编程 (asyncio)

- [ ] `async`/`await` 语法的工作机制
- [ ] `asyncio.gather()` 并发运行多个协程
- [ ] `asyncio.create_task()` 后台调度任务
- [ ] `asyncio.wait_for()` 超时控制
- [ ] `ThreadPoolExecutor` 处理 CPU 密集型任务
- [ ] 避免在异步代码中使用阻塞调用

### 2. FastAPI 路由与请求处理 (FastAPI Routes)

- [ ] 定义 GET/POST/PUT/DELETE 路由
- [ ] 路径参数（Path Parameters）和查询参数（Query Parameters）
- [ ] 请求体（Request Body）与 Pydantic 模型验证
- [ ] 响应模型（Response Model）和数据过滤

### 3. FastAPI 服务器 (FastAPI Server)

- [ ] 完整的 FastAPI 应用生命周期
- [ ] 中间件（Middleware）和异常处理（Exception Handlers）
- [ ] APIRouter 模块化路由组织
- [ ] 异步 API 端点的实现

### 4. 依赖注入 (Dependency Injection)

- [ ] DI（依赖注入）的核心思想：控制反转
- [ ] FastAPI 的 `Depends()` 机制
- [ ] injector 库的基本使用
- [ ] 依赖注入如何提高代码的可测试性

### 5. 数据库操作 (Database)

- [ ] SQLite 内存数据库的 CRUD 操作
- [ ] PyMySQL 连接 MySQL 数据库的流程
- [ ] 游标（cursor）的作用和使用方式
- [ ] 参数化查询防止 SQL 注入
- [ ] `commit()` 和事务管理

### 6. JSON 数据处理 (JSON)

- [ ] `json.dumps()`/`json.loads()` 序列化与反序列化
- [ ] `ensure_ascii=False` 的中文字符处理
- [ ] 自定义 `JSONEncoder` 处理特殊类型（datetime、自定义类）
- [ ] JSON 文件的读写（`json.dump()`/`json.load()`）

### 7. NumPy 数值计算 (NumPy)

- [ ] ndarray 与 Python 列表的区别
- [ ] 向量化运算和广播（broadcasting）
- [ ] 矩阵乘法 `@` vs 逐元素乘 `*`
- [ ] 梯度下降算法的基本原理
- [ ] 学习率对收敛的影响

## 综合练习

### 练习 1：异步 FastAPI API + SQLite 数据库

编写一个 FastAPI 应用，实现以下功能：

1. 连接 SQLite 内存数据库，创建一个 `todos` 表（id, title, completed）
2. `GET /todos` — 获取所有待办事项，以 JSON 格式返回
3. `POST /todos` — 创建新的待办事项，接收 JSON 请求体 `{title: "..."}`
4. 所有数据库操作使用参数化查询

<details>
<summary>查看答案</summary>

```python
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


def get_connection():
    """获取数据库连接（内存）。"""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    return conn


class TodoCreate(BaseModel):
    title: str


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.get("/todos", response_model=List[Todo])
async def get_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM todos")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "title": r[1], "completed": bool(r[2])} for r in rows]


@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (title) VALUES (?)", (todo.title,)
    )
    conn.commit()
    todo_id = cursor.lastrowid
    conn.close()
    return {"id": todo_id, "title": todo.title, "completed": False}
```

</details>

### 练习 2：NumPy 数据处理 + JSON 序列化

给定一个学生成绩数组，使用 NumPy 计算：每个学生各科平均分、各科最高分、成绩标准差。将结果序列化为 JSON 格式（包含中文），保存到文件。

<details>
<summary>查看答案</summary>

```python
import numpy as np
import json

# 5个学生3门课程的成绩矩阵
scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [76, 82, 80],
    [95, 91, 88],
    [88, 75, 82],
])

# NumPy 计算
student_avg = scores.mean(axis=1)  # 每个学生平均分
subject_max = scores.max(axis=0)   # 每科最高分
std = scores.std()                  # 全部成绩标准差

# 汇总结果
results = {
    "学生平均分": [float(x) for x in student_avg],
    "各科最高分": [int(x) for x in subject_max],
    "成绩标准差": float(std),
}

# JSON 序列化
json_str = json.dumps(results, ensure_ascii=False, indent=2)
print(json_str)

# 保存文件
with open("data/scores_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
```

</details>

## 自测题

### 1. 以下哪个场景最适合使用 `asyncio`？

A. 需要大量 CPU 计算的科学模拟
B. 同时发起 1000 个 HTTP 请求获取数据
C. 排序一个包含 100 万个元素的列表
D. 在本地计算文件哈希值

### 2. 在 FastAPI 中，路径参数和查询参数的区别是什么？

A. 路径参数在 URL 路径中（如 `/users/{id}`），查询参数在 URL 末尾（如 `?skip=0&limit=10`）
B. 路径参数更安全，查询参数更灵活
C. 两者完全等价，只是写法不同
D. 路径参数只能是字符串，查询参数可以是任意类型

### 3. 以下哪个选项**不是**数据库参数化查询的好处？

A. 防止 SQL 注入攻击
B. 自动优化查询执行计划
C. 数据库驱动正确处理数据类型转义
D. 代码更易读和维护

### 4. NumPy 数组 `a = np.array([[1, 2], [3, 4]])` 与 `b = np.array([10, 20])` 执行 `a + b` 后，结果是？

A. 广播失败，抛出 ValueError
B. `[[11, 22], [23, 24]]`
C. `[[11, 12], [23, 24]]`
D. `[[11, 22], [13, 24]]`

### 5. `json.dumps({"data": datetime.now()}, default=str)` 的作用是什么？

A. 将 datetime 转为特定格式
B. 用 `str()` 函数将 datetime 序列化为字符串
C. 跳过 datetime 字段不序列化
D. 使用默认的 JSON 编码器

<details>
<summary>查看答案</summary>

1. **B** — asyncio 适合 I/O 密集型并发（大量网络请求），不适合 CPU 密集型任务
2. **A** — 路径参数是 URL 路径的一部分（`/users/{user_id}`），查询参数以 `?` 开头附加在 URL 末尾
3. **B** — 参数化查询主要好处是安全性和类型安全，执行计划优化由数据库自行决定，不是参数化的直接好处
4. **D** — `b = [10, 20]` 广播到 `a` 的每一行：`[[1,2]+[10,20], [3,4]+[10,20]] = [[11,22],[13,24]]`
5. **B** — `default=str` 是 `json.dumps()` 的参数，当遇到无法直接序列化的对象时调用 `str()` 转换

</details>

## 下一步

你已经完成了进阶部分的全部学习！以下是继续深入的建议路径：

**回顾与巩固：**
- [异步编程](./async.md) — 重温协程与事件循环
- [FastAPI 路由与请求处理](./fastapi-routes.md) — 回顾 Web API 路由设计
- [FastAPI 服务器](./fastapi-server.md) — 回顾完整 API 服务器构建
- [依赖注入](./dependency-injection.md) — 回顾 DI 模式
- [数据库操作](./database.md) — 重温 SQLite 和 PyMySQL
- [JSON 数据处理](./json.md) — 回顾序列化与自定义编码器
- [NumPy 数值计算](./numpy.md) — 重温向量化与数值算法

**进阶方向：**
- 探索 FastAPI 的认证与授权（JWT、OAuth2）
- 学习 SQLAlchemy ORM 进行更高级的数据库操作
- 尝试异步数据库驱动（如 `asyncpg`、`aiomysql`）
- 深入 NumPy 和 Pandas 进行数据分析实战
