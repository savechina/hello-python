# 上下文管理器 (Context Managers)

## 导语

想象你去自助餐厅吃饭：拿起餐盘→取菜→用餐→归还餐盘。这个流程中，"归还餐盘"不能忘，否则餐厅会多收押金。Python 编程中也经常遇到类似场景：打开文件后必须关闭、获取锁后必须释放、建立连接后必须断开。上下文管理器（Context Manager）就是 Python 提供的"自动归还餐盘"机制——它确保资源在使用完毕后一定被正确清理，即使中间发生异常也不会遗漏。`with` 语句是上下文管理器的语法入口，理解它不仅能写出更安全的代码，还能让你自定义优雅的资源管理工具。

## 学习目标

- 掌握 `with` 语句的工作机制和 `__enter__`/`__exit__` 协议
- 学会使用 `@contextmanager` 装饰器以生成器方式定义上下文管理器
- 掌握 `contextlib.suppress`、`contextlib.redirect_stdout` 等实用工具

## 概念介绍

上下文管理器的核心是**资源生命周期管理**——在进入代码块时获取资源，在离开代码块时释放资源。Python 通过 `with` 语句和上下文管理器协议来实现这一模式。

1. **`with` 语句** — 语法糖，底层调用上下文管理器的 `__enter__()` 获取资源，代码块执行完毕后（无论正常结束还是异常退出）调用 `__exit__()` 释放资源。
2. **`__enter__` 和 `__exit__` 协议** — 上下文管理器类必须实现这两个魔术方法。`__enter__()` 在进入 `with` 块时调用，返回值可通过 `as` 绑定；`__exit__(exc_type, exc_val, exc_tb)` 在离开时调用，三个参数分别描述异常的类型、值和追踪信息，如果没有异常则全部为 `None`。
3. **`contextlib.contextmanager` 装饰器** — 用生成器（`yield`）替代类来定义上下文管理器。`yield` 之前的代码相当于 `__enter__`，`yield` 之后的代码相当于 `__exit__`。适合简单场景，代码更简洁。
4. **`contextlib.suppress`** — 忽略指定异常类型的上下文管理器，等价于 `try-except` 但更简洁。
5. **嵌套上下文管理器** — `with` 语句支持嵌套（或使用同一行多对象），内层资源在外层之前释放，遵循"后分配先释放"的栈式顺序。

> [!NOTE]
> Python 内置的 `open()` 函数返回的文件对象就是一个上下文管理器——这就是为什么推荐用 `with open(...) as f` 而非手动 `f.close()`。

## 代码示例

### 示例 1：自定义上下文管理器类 — Timer

```python
import time


class Timer:
    """A context manager that measures execution time."""

    def __enter__(self):
        self.start = time.perf_counter()
        print("Timer started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Timer stopped. Elapsed: {self.elapsed:.4f} seconds")
        return False  # Do not suppress exceptions


# Usage
with Timer() as t:
    time.sleep(0.5)
    print(f"Inside: elapsed so far = {time.perf_counter() - t.start:.4f}s")
# 输出:
# Timer started.
# Inside: elapsed so far = 0.5012s
# Timer stopped. Elapsed: 0.5034s
```

`__enter__()` 返回 `self`，使得 `as t` 能访问 `Timer` 实例的属性（如 `elapsed`）。\_\_exit\_\_() 返回 `False` 表示不吞掉异常——如果 `with` 块内发生异常，异常会继续向外传播。

> [!TIP]
> `time.perf_counter()` 比 `time.time()` 更精确，专用于测量短时间间隔，不受系统时钟更新影响。

### 示例 2：@contextmanager 装饰器 — 临时工作目录

```python
import os
from contextlib import contextmanager


@contextmanager
def temporary_dir():
    """Create a temp directory and clean up on exit."""
    original_cwd = os.getcwd()
    temp_path = "tmp_temp_workspace"
    os.makedirs(temp_path, exist_ok=True)
    os.chdir(temp_path)
    print(f"Changed to: {os.getcwd()}")
    try:
        yield temp_path
    finally:
        os.chdir(original_cwd)
        os.rmdir(temp_path)
        print(f"Restored to: {os.getcwd()}")


# Usage
print(f"Before: {os.getcwd()}")
with temporary_dir() as td:
    print(f"Inside: creating file in {td}")
    with open("temp_data.txt", "w") as f:
        f.write("temporary data")
print(f"After: {os.getcwd()}")
# 输出:
# Before: /path/to/project
# Changed to: /path/to/project/tmp_temp_workspace
# Inside: creating file in tmp_temp_workspace
# Restored to: /path/to/project
# After: /path/to/project
```

`@contextmanager` 将生成器函数转换为上下文管理器。`yield` 之前的代码在 `__enter__` 阶段执行，`yield` 的值通过 `as` 绑定，`yield` 之后的代码在 `__exit__` 阶段（放在 `finally` 中确保即使异常也执行）。

> [!WARNING]
> 使用 `@contextmanager` 时，**必须用 `try...finally` 包裹清理逻辑**。如果忘记 `finally`，当 `with` 块内抛出异常时，清理代码可能不会执行，导致资源泄漏。

### 示例 3：contextlib.suppress 和 contextlib.redirect_stdout

```python
import os
from contextlib import suppress, redirect_stdout
from io import StringIO

# suppress: ignore specific exceptions
print("--- suppress example ---")
with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")
print("No error raised, program continues.")

print("")

# redirect_stdout: capture stdout output
print("--- redirect_stdout example ---")
buffer = StringIO()
with redirect_stdout(buffer):
    print("Hello, captured world!")
    print("This goes to buffer, not console.")

captured = buffer.getvalue()
print(f"Captured output: {captured.strip()}")
# 输出:
# --- suppress example ---
# No error raised, program continues.
#
# --- redirect_stdout example ---
# Captured output: Hello, captured world!
# This goes to buffer, not console.
```

`suppress(FileNotFoundError)` 等价于：
```python
try:
    os.remove("non_existent_file.txt")
except FileNotFoundError:
    pass
```
当需要忽略一两个特定异常时，`suppress` 比 `try-except` 更声明式。

`redirect_stdout(f)` 将 `print()` 等写入 `sys.stdout` 的输出重定向到文件对象 `f`。配合 `StringIO` 可以捕获输出用于测试验证。

> [!NOTE]
> `suppress()` 也可以传入多个异常类型：`suppress(FileNotFoundError, PermissionError)`。

## 常见错误与解决

> [!WARNING]
> **错误 1：在 `__exit__` 中吞掉异常而不传播**
>
> ```python
> class BadManager:
>     def __enter__(self):
>         return self
>
>     def __exit__(self, exc_type, exc_val, exc_tb):
>         print(f"Cleanup done")
>         return True  # 💥 所有异常都被吞掉了！
>
> with BadManager():
>     raise ValueError("Something went wrong")
> print("This prints — exception was silently swallowed!")
> ```
>
> **原因**：`__exit__()` 返回 `True` 表示"异常已处理"，会阻止异常继续传播。除非你**明确想要**忽略异常，否则不应返回 `True`。
>
> **解决**：默认返回 `False`，或者不写 return（Python 默认返回 `None`，等价于 `False`）。仅在 `exc_type is not None` 且确实需要时返回 `True`。

> [!WARNING]
> **错误 2：在 `@contextmanager` 中遗漏 `finally` 导致异常时资源未释放**
>
> ```python
> from contextlib import contextmanager
>
> @contextmanager
> def leaky_resource():
>     resource = open("data.txt", "w")  # acquired
>     yield resource
>     resource.close()  # 💥 如果 with 块内抛异常，这行不会执行！
> ```
>
> **原因**：当 `with` 块内抛出异常时，生成器在 `yield` 处被中断，`yield` 之后的清理代码不会执行。
>
> **解决**：始终用 `try...finally` 包裹：
>
> ```python
> @contextmanager
> def safe_resource():
>     resource = open("data.txt", "w")
>     try:
>         yield resource
>     finally:
>         resource.close()  # ✅ 无论如何都会执行
> ```

## 最佳实践

1. **优先使用 `with` 语句管理资源** — 文件、网络连接、锁等同步资源都应用 `with` 语句包裹，即使对象本身支持手动 close/释放，`with` 也能保证异常路径下的正确清理
2. **简单场景用 `@contextmanager`，复杂场景用类** — 如果上下文管理器需要维护多个状态、或需要除 `with` 之外调用方法（如示例 1 中的 `.elapsed`），用类实现；如果只是清理一个资源，`@contextmanager` 代码更简洁
3. **`__exit__` 中不要吞掉非预期异常** — `__exit__()` 默认返回 `False`，仅在明确需要忽略特定异常时返回 `True`，并在日志中记录被忽略的异常信息

## 练习

1. 实现一个 `Transaction` 上下文管理器，模拟数据库事务的提交与回滚。`with` 块正常结束时打印 `"Transaction committed."`，抛出异常时打印 `"Transaction rolled back."` 并重新抛出异常。

<details>
<summary>查看答案</summary>

```python
class Transaction:
    def __enter__(self):
        print("Transaction started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Transaction committed.")
        else:
            print("Transaction rolled back.")
        return False

with Transaction():
    print("Doing work...")
    raise RuntimeError("Something failed")
# 输出:
# Transaction started.
# Doing work...
# Transaction rolled back.
# (RuntimeError propagated)
```

</details>

2. 使用 `@contextmanager` 实现一个 `changed_env(key, value)` 上下文管理器，在 `with` 块内临时修改环境变量，离开后自动恢复原值。

<details>
<summary>查看答案</summary>

```python
import os
from contextlib import contextmanager


@contextmanager
def changed_env(key, value):
    original = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original

print(f"Before: {os.environ.get('MY_VAR', 'NOT_SET')}")
with changed_env("MY_VAR", "temporary"):
    print(f"Inside: {os.environ['MY_VAR']}")
print(f"After: {os.environ.get('MY_VAR', 'NOT_SET')}")
# 输出:
# Before: NOT_SET
# Inside: temporary
# After: NOT_SET
```

</details>

## 知识检查

1. `__exit__(exc_type, exc_val, exc_tb)` 返回 `True` 的效果是什么？
    - A. 重新抛出异常
    - B. 吞掉异常，阻止其继续传播
    - C. 忽略返回值，不影响异常流
    - D. 触发二次异常

2. `@contextmanager` 装饰器要求被装饰函数是什么类型？
    - A. 普通函数（返回 None）
    - B. 异步函数（`async def`）
    - C. 生成器函数（包含 `yield`）
    - D. Lambda 函数

3. `contextlib.suppress(ValueError)` 等价于以下哪种写法？
    - A. `try: ... except Exception: pass`
    - B. `try: ... except ValueError: pass`
    - C. `try: ... finally: pass`
    - D. `if ValueError: continue`

<details>
<summary>查看答案</summary>

1. B — 返回 `True` 会让 Python 认为异常已被处理，不再向外传播
2. C — `@contextmanager` 将包含 `yield` 的生成器函数转换为上下文管理器
3. B — `suppress(ValueError)` 只忽略 `ValueError` 及其子类，其他异常正常传播

</details>

## 本章小结

- `with` 语句通过调用 `__enter__()` 和 `__exit__()` 实现自动资源管理，即使异常也不会泄漏资源
- `__exit__()` 接收异常三要素 `(exc_type, exc_val, exc_tb)`，返回 `False`（默认）让异常继续传播，返回 `True` 吞掉异常
- `@contextmanager` 用生成器 + `yield` 简化上下文管理器定义，但清理逻辑必须放在 `try...finally` 中
- `contextlib.suppress()` 优雅地忽略指定异常，比 `try-except-pass` 更声明式
- `contextlib.redirect_stdout()` 可将 `print()` 输出重定向到任意文件对象，常用于测试和日志

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| context manager | 上下文管理器 | 实现 `__enter__`/`__exit__` 协议、用于资源管理的对象 |
| `with` statement | with 语句 | Python 中用于自动管理资源的语法结构 |
| `__enter__` | 进入方法 | 上下文管理器在进入 `with` 块时调用的方法 |
| `__exit__` | 退出方法 | 上下文管理器在离开 `with` 块时调用的方法，负责清理资源 |
| `@contextmanager` | 上下文装饰器 | `contextlib` 模块提供的装饰器，用生成器定义上下文管理器 |
| `contextlib.suppress` | 异常抑制器 | 忽略指定异常类型而不传播的上下文管理器 |

## 下一步

- [类型注解 (Type Hints)](./type-hints.md) → 学习 Python 的类型提示系统，让代码更可读、更可维护

## 源码链接

- 本章暂无对应的独立源码文件
