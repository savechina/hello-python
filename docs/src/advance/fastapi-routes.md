# FastAPI 路由基础 (FastAPI Routes)

## 导语

你每天使用的各种 App 都在通过 API 与服务器交换数据：发一条消息、搜索商品、下单支付——背后都是 HTTP 接口在运作。FastAPI 是 Python 生态中最高效的 Web 框架之一，它让你用几行代码就能写出高性能的 REST API。本节带你迈出 Web 开发的第一步。

## 学习目标

- 了解 FastAPI 框架的基本概念和使用场景
- 学会定义路由（`@app.get()`）和返回 JSON 数据
- 掌握使用 uvicorn 启动开发服务器

## 概念介绍

FastAPI 是一个现代 Python Web 框架，基于 Starlette 和 Pydantic 构建。它的特点包括：
- **自动文档**：自动生成交互式 Swagger UI 和 ReDoc
- **类型提示**：利用 Python 类型注解实现请求/响应验证
- **异步支持**：原生 async/await
- **高性能**：接近 Node.js 和 Go 的水平

> [!NOTE]
> 本节使用 `fastapi_sample.py`（125 行）展示基本路由定义。`fastapi_server_sample.py`（332 行）将在下一章节讲解更高级的服务器管理。

## 代码示例

### 示例 1：基本应用定义

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, FastAPI!"}
```

`FastAPI()` 实例化应用，`@app.get("/")` 是一个**装饰器**，将 `hello()` 函数注册为处理 GET `/` 路由的请求处理器。返回的字典会自动序列化为 JSON。

### 示例 2：启动服务器

```python
import uvicorn

# 启动开发服务器
uvicorn.run(app, host="0.0.0.0", port=8000)
```

`uvicorn` 是 ASGI 服务器，负责接收 HTTP 请求并转发给 FastAPI 应用。`host="0.0.0.0"` 允许外部访问。

### 示例 3：带参数的路由

```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

路径参数通过 `{param_name}` 定义，查询参数通过函数参数定义。FastAPI 会自动进行类型验证。

> [!TIP]
> 启动服务器后访问 `http://localhost:8000/docs` 可以看到自动生成的交互式 API 文档。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记启动 ASGI 服务器**
>
> 直接运行 `python app.py` 不会启动服务器——FastAPI 本身不包含 Web 服务器。
>
> **解决**：必须使用 `uvicorn.run(app)` 或在命令行运行 `uvicorn app:app`。

> [!WARNING]
> **错误 2：路径参数类型不匹配**
>
> 访问 `/users/abc` 会返回 422 验证错误——`user_id` 声明为 `int` 类型。
>
> **解决**：这正是 FastAPI 的优势——自动类型验证阻止了无效请求。

## 最佳实践

1. **始终使用 async def** 对于 I/O 密集型路由
2. **利用类型提示** — FastAPI 用它来生成文档和验证请求
3. **先写好模型** — 用 Pydantic BaseModel 定义请求/响应数据结构

## 练习

1. 定义一个路由 `GET /greet/{name}`，返回 `{"greeting": "Hello, <name>!"}`.

<details>
<summary>查看答案</summary>

```python
@app.get("/greet/{name}")
async def greet(name: str):
    return {"greeting": f"Hello, {name}!"}
```

</details>

2. 定义一个路由 `GET /search`，接受查询参数 `q`（字符串，默认值为 `None`），返回搜索结果的占位符。

<details>
<summary>查看答案</summary>

```python
@app.get("/search")
async def search(q: str = None):
    if q:
        return {"query": q, "results": []}
    return {"error": "Please provide a search query"}
```

</details>

## 知识检查

1. FastAPI 自动生成的 API 文档可以通过哪个路径访问？
   - A. `/api`
   - B. `/docs`
   - C. `/swagger`
   - D. `/admin`

2. `@app.post("/users")` 路由可以处理哪种 HTTP 请求？
   - A. GET
   - B. POST
   - C. PUT
   - D. DELETE

3. FastAPI 的路径参数 `{user_id}` 支持类型注解吗？
   - A. 不支持，所有路径参数都是字符串
   - B. 支持，可以在函数参数上标注类型
   - C. 只有整数类型支持
   - D. 只支持可选参数

<details>
<summary>查看答案</summary>

1. B — FastAPI 自动生成 `/docs` (Swagger UI) 和 `/redoc`
2. B — `@app.post()` 处理 POST 请求
3. B — FastAPI 支持所有 Python 类型注解进行自动验证

</details>

## 本章小结

- FastAPI 是基于 ASGI 的现代 Python Web 框架
- `@app.get()` 等装饰器注册路由处理器
- 返回值字典自动序列化为 JSON
- uvicorn 是推荐的生产级 ASGI 服务器
- FastAPI 自动生成交互式 API 文档（/docs）
- 路径参数和查询参数都支持类型注解和自动验证

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| route | 路由 | HTTP 路径与处理函数的映射 |
| decorator | 装饰器 | Python 修饰函数的语法特性 |
| ASGI | ASGI | 异步服务器网关接口 |
| endpoint | 端点 | API 的具体 URL 路径 |
| serialization | 序列化 | Python 对象转换为 JSON 格式 |

## 下一步

- [FastAPI 服务器管理](./fastapi-server.md) → 学会管理服务进程、PID 和日志

## 源码链接

- [fastapi_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/fastapi_sample.py)
