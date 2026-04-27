# 异步编程 (Asynchronous Programming)

## 导语

想象你在开一家咖啡店：如果只有一位服务员，每个客户点单后服务员必须站在柜台等待咖啡做好才能接待下一位，那队伍早就排到街角了。正确的做法是：服务员接单后把订单交给咖啡师，然后立刻去接待下一位客户——咖啡做好后再通知客户取餐。Python 的异步编程正是这个逻辑：让程序在等待 I/O（网络请求、数据库查询、文件读写）时不阻塞，可以去处理其他任务。当你需要并发处理大量网络请求、构建高并发 Web 服务、或编写定时任务调度器时，异步编程能显著提升效率和响应速度。

## 学习目标

- 理解 `async`/`await` 语法和协程（coroutine）的工作原理
- 掌握 `asyncio.gather()`、`asyncio.create_task()`、`asyncio.wait_for()` 等核心并发模式
- 学会在异步环境中使用 `ThreadPoolExecutor` 处理 CPU 密集型任务

## 概念介绍

异步编程的核心思想是**单线程并发**——一个线程通过协作式多任务（cooperative multitasking）同时执行多个操作。Python 通过 `asyncio` 模块提供支持。

几个关键概念：

1. **协程（Coroutine）** — 用 `async def` 定义的函数，执行到 `await` 时会主动让出控制权，等等待的内容完成后恢复执行。协程是异步编程的基本单元。
2. **事件循环（Event Loop）** — 异步程序的"调度中心"，负责在协程之间切换：当某个协程在等待 I/O 时，事件循环切换到其他就绪的协程继续执行。
3. **`await` 关键字** — 告诉事件循环"这件事我需要等待，你去执行别的任务吧"。只有 `await` 后面的操作才是真正"异步"的。
4. **GIL（全局解释器锁）** — Python 的 GIL 使得**多线程**无法真正实现并行计算，但 `asyncio` 是**单线程**的，不存在 GIL 竞争问题。不过，纯 CPU 密集计算仍会阻塞事件循环，需要配合 `ThreadPoolExecutor` 或 `ProcessPoolExecutor` 来解决。

> [!NOTE]
> `asyncio` 特别适合 **I/O 密集型**场景（网络请求、数据库查询、文件读写），因为等待的时间可以被其他任务利用。对于 **CPU 密集型**任务，`asyncio` 无法绕过 GIL，需要借助线程池或进程池。

## 代码示例

### 示例 1：`asyncio.gather()` — 并发执行多个任务

```python
import asyncio

async def fetch_data(task_id, delay):
    """模拟一个异步 I/O 操作，例如从网络获取数据。"""
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)  # 模拟 I/O 操作的延迟
    print(f"Task {task_id} completed.")
    return f"Data from task {task_id}"

async def once_main():
    # 创建多个异步任务
    tasks = [fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1)]

    # 并发运行所有任务，并等待它们完成
    results = await asyncio.gather(*tasks)

    # 打印所有任务的返回结果
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(once_main())
```

`asyncio.gather(*tasks)` 并发运行所有协程，并按传入顺序返回结果列表。注意 `tasks` 中存放的是**协程对象**（调用 `fetch_data()` 但未 `await`），而 `gather` 会并发调度它们。三个任务总耗时等于最长的单个任务耗时（3秒），而非累加（6秒）。

> [!TIP]
> `gather` 的特点是「等所有人到齐再出发」——它会在所有任务完成后一次性返回结果列表。如果某个任务抛出异常，异常会传播给 `gather` 的调用者。

### 示例 2：`asyncio.create_task()` + `asyncio.wait_for()` — 任务管理与超时控制

```python
import asyncio

async def fetch_data(task_id, delay):
    """模拟一个异步 I/O 操作。"""
    print(f"Task {task_id} started, will take {delay} seconds.")
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed.")
    return f"Data from task {task_id}"

async def task_main():
    # 使用 create_task 创建独立的调度任务
    tasks = [
        asyncio.create_task(fetch_data(1, 2)),
        asyncio.create_task(fetch_data(2, 4)),
        asyncio.create_task(fetch_data(3, 1)),
    ]

    try:
        # 设置一个超时时间，假设我们希望所有任务在3秒内完成
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=3)
    except asyncio.TimeoutError:
        print("Some tasks took too long and were cancelled.")

    # 处理任务结果
    for task in tasks:
        if not task.cancelled():
            try:
                result = task.result()
                print(f"Task result: {result}")
            except Exception as e:
                print(f"Task raised an exception: {e}")

if __name__ == "__main__":
    asyncio.run(task_main())
```

`asyncio.create_task()` 将协程封装为 `Task` 对象并立即调度。与直接传入协程的区别在于：`Task` 是独立调度的实体，可以在外部控制它的生命周期（取消、检查状态等）。`asyncio.wait_for(coro, timeout=N)` 为整个操作设置超时边界，超时后抛出 `asyncio.TimeoutError`。

> [!WARNING]
> `wait_for` 超时会取消内部的所有任务，但 `Task` 对象本身仍存在。处理结果前务必用 `task.cancelled()` 检查取消状态，否则访问 `task.result()` 会抛出 `CancelledError`。

### 示例 3：`ThreadPoolExecutor` — 在异步中处理 CPU 密集型任务

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def cpu_bound_task():
    """模拟 CPU 密集型任务。"""
    total = 0
    for i in range(10000000):
        total += i
    print(f"CPU task finished, sum: {total}")

async def io_bound_task():
    """模拟 I/O 密集型任务。"""
    await asyncio.sleep(1)
    print("I/O task finished")

async def thread_pool_task():
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        # 将 CPU 密集型任务提交到线程池，避免阻塞事件循环
        future = loop.run_in_executor(executor, cpu_bound_task)
        # 同时执行 I/O 密集型任务
        await io_bound_task()
        # 等待 CPU 任务完成
        await future

def thread_main():
    asyncio.run(thread_pool_task())

if __name__ == "__main__":
    thread_main()
```

`loop.run_in_executor()` 把阻塞操作放到线程池中执行，事件循环不会被卡住。I/O 任务和 CPU 任务在此可以**并行运行**——`io_bound_task` 不会等待 `cpu_bound_task` 完成。

> [!NOTE]
> 为什么用线程池而不是进程池？因为 `run_in_executor` 默认使用线程池。对于 Python，由于 GIL 的存在，线程池对 CPU 密集型的加速效果有限。如果确实需要 CPU 并行，可以改用 `ProcessPoolExecutor`：`loop.run_in_executor(ProcessPoolExecutor(), func)`。

## 常见错误与解决

> [!WARNING]
> **错误 1：在异步代码中使用阻塞 I/O**
>
> ```python
> import asyncio
> import time  # 💥 阻塞式睡眠！
>
> async def bad_example():
>     time.sleep(2)  # 阻塞整个事件循环，其他协程全部卡住
>     print("done")
>
> asyncio.run(bad_example())
> ```
>
> **原因**：`time.sleep()` 是同步阻塞的，会冻结事件循环，所有其他协程都无法执行。
>
> **解决**：使用异步替代方案。
>
> ```python
> async def good_example():
>     await asyncio.sleep(2)  # ✅ 让出控制权，事件循环继续调度其他协程
>     print("done")
> ```

> [!WARNING]
> **错误 2：忘记 `await` 协程**
>
> ```python
> async def fetch():
>     return "data"
>
> async def main():
>     result = fetch()  # 💥 没有 await！返回的是协程对象，而非 "data"
>     print(result)     # <coroutine object fetch at 0x...>
>
> asyncio.run(main())
> ```
>
> **原因**：调用 `async def` 函数不会立即执行函数体，而是返回一个协程对象。必须用 `await` 才能真正执行。
>
> **解决**：对每个协程都要 `await`。
>
> ```python
> async def main():
>     result = await fetch()  # ✅ 正确
>     print(result)           # data
> ```

## 最佳实践

1. **永远用 `await` 而非阻塞调用** — `time.sleep()` → `asyncio.sleep()`，`requests.get()` → `httpx.get()` 或 `aiohttp`，同步数据库驱动 → async 驱动（如 `aiomysql`）

2. **合理选择并发原语** — `gather()` 适合"收集所有结果"，`create_task()` 适合"后台调度"，`wait_for()` 适合"设置超时"，`as_completed()` 适合"谁先完成先处理谁"

## 练习

1. 编写一个异步爬虫函数 `fetch_urls(urls)`，并发获取多个 URL 的内容（可用 `asyncio.sleep` 模拟），并打印每个 URL 的结果。

<details>
<summary>查看答案</summary>

```python
import asyncio

async def fetch_url(url):
    """模拟网络请求。"""
    await asyncio.sleep(1)  # 模拟延迟
    return f"Content of {url}"

async def fetch_urls(urls):
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, content in zip(urls, results):
        print(f"{url}: {content}")

asyncio.run(fetch_urls([
    "https://example.com/api/users",
    "https://example.com/api/posts",
    "https://example.com/api/comments",
]))
```

</details>

2. 实现一个带超时的异步函数 `safe_fetch(task_id, delay, timeout)`，如果任务超时则返回 `"Timeout"`，否则返回实际结果。

<details>
<summary>查看答案</summary>

```python
import asyncio

async def safe_fetch(task_id, delay, timeout):
    try:
        await asyncio.sleep(delay)
        return f"Data from task {task_id}"
    except asyncio.TimeoutError:
        return "Timeout"

async def main():
    # 方式一：在外部用 wait_for 控制
    result = await asyncio.wait_for(
        safe_fetch(1, 2, 3), timeout=3
    )
    print(result)  # Data from task 1

    # 方式二：内部处理超时
    result = await asyncio.wait_for(
        safe_fetch(2, 5, 3), timeout=3
    )
    print(result)

asyncio.run(main())
```

</details>

## 知识检查

1. 以下哪个函数是 `asyncio` 中正确的非阻塞延迟调用？
   - A. `time.sleep(1)`
   - B. `asyncio.sleep(1)`
   - C. `await sleep(1)`
   - D. `async sleep(1)`

2. `asyncio.gather()` 的返回值顺序与什么有关？
   - A. 任务完成的先后顺序
   - B. 传入任务的顺序
   - C. 随机顺序
   - D. 按任务耗时排序

3. 在 Python 异步编程中，GIL 对以下哪种场景影响最大？
   - A. 大量并发网络请求（I/O 密集型）
   - B. 大量并发文件读写（I/O 密集型）
   - C. 大规模数值计算（CPU 密集型）
   - D. 定时器调度（CPU 密集型）

<details>
<summary>查看答案</summary>

1. B — `asyncio.sleep(1)` 是协程，必须用 `await` 调用
2. B — `gather()` 按传入顺序返回结果，与完成时间无关
3. C — GIL 限制多线程/单线程中的 CPU 并行计算，I/O 密集型不受影响

</details>

## 本章小结

- `async`/`await` 是 Python 异步编程的核心语法，`async def` 定义协程，`await` 挂起等待
- `asyncio.gather()` 并发执行多个协程并按传入顺序返回结果
- `asyncio.create_task()` 创建独立调度任务，`asyncio.wait_for()` 为任务设置超时
- I/O 密集型场景用 `asyncio` 效果最好，CPU 密集型任务需配合 `ThreadPoolExecutor` 或 `ProcessPoolExecutor`
- 永远不要在 `async def` 中使用阻塞调用（如 `time.sleep()`），要用异步替代方案

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| coroutine | 协程 | 用 `async def` 定义的异步函数，可被 `await` 挂起和恢复 |
| await | 等待关键字 | 挂起当前协程，等待异步操作完成后恢复 |
| event loop | 事件循环 | 异步程序的调度中心，负责在协程之间切换执行 |
| asyncio | 异步 I/O 模块 | Python 标准库中的异步编程框架，提供事件循环和协程工具 |
| GIL | 全局解释器锁 | Python 解释器级别的锁，限制多线程并行执行字节码 |

## 下一步

- [FastAPI 路由与请求处理](./fastapi-routes.md) → 将异步编程应用到 Web 开发

## 源码链接

- [asyncs_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/asyncs_sample.py)
