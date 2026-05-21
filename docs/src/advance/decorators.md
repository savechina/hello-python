# 装饰器 (Decorators)

## 导语

装饰器是 Python 中一种极具表现力的设计模式，它允许你在不修改原始函数代码的前提下，为其增加额外的功能。想象你编写了一系列核心业务函数，现在需要为每个函数添加性能监控、日志记录、权限校验或缓存功能——如果不使用装饰器，你需要逐一修改每个函数的内部逻辑，这不仅繁琐而且容易出错。装饰器通过 `@` 语法糖，将这些"横切关注点"（cross-cutting concerns）以声明式的方式"包裹"在函数外部，让你的代码既保持纯净又功能丰富。在 FastAPI 路由定义、Flask 视图保护、Django 中间件、Celery 任务调度等主流框架中，装饰器都是不可或缺的核心机制。

## 学习目标

- 理解函数作为一等对象（first-class object）的含义及其在装饰器中的应用
- 掌握装饰器的语法糖 `@` 及其等价的手动包裹写法
- 学会使用 `functools.wraps` 保留被装饰函数的元数据，以及编写带参数的装饰器

## 概念介绍

理解装饰器需要先掌握一个核心前提：**Python 中函数是一等对象**。这意味着函数可以像普通变量一样被赋值、传递、作为参数传入、作为返回值返回，甚至存储在数据结构中。

1. **函数作为一等对象** — 函数没有"特权"，它和整数、字符串一样是对象。你可以把函数赋值给另一个变量（`f = my_func`），可以把函数作为参数传给另一个函数（`call_it(my_func)`），也可以从函数中返回另一个函数。这种灵活性是装饰器能工作的基础。
2. **`@` 语法糖** — `@decorator` 本质上是一种"语法糖"：

   ```python
   @decorator
   def func():
       pass
   # 等价于:
   def func():
       pass
   func = decorator(func)
   ```

   `@` 语法在函数定义后立即用装饰器对象重新绑定函数名，使得增强逻辑的意图一目了然。

3. **包装函数（Wrapper）** — 装饰器本质上是一个接收函数作为参数并返回函数的"高阶函数"。内部通常定义一个 `wrapper` 函数，在其中执行额外逻辑（如计时、日志），然后通过 `*args, **kwargs` 将参数透传给原始函数。
4. **`functools.wraps`** — 如果装饰器直接返回一个新的 `wrapper` 函数，原始函数的 `__name__`、`__doc__`、`__signature__` 等元数据将丢失。`@functools.wraps(original_func)` 装饰器会将原始函数的元数据复制到 `wrapper` 上，确保调试、文档生成、内省等操作正常工作。
5. **带参数的装饰器** — 当需要向装饰器传递配置参数（如 `@repeat(3)`），实际需要一个三层嵌套：最外层接收装饰器参数，中间层接收被装饰函数，最内层是执行逻辑的 `wrapper`。

> [!TIP]
> 判断装饰器层数的方法：如果 `@` 后面直接是函数名（如 `@timer`），是两层结构（装饰器函数 + wrapper）；如果 `@` 后面是函数调用（如 `@repeat(3)`），则需要三层结构。

## 代码示例

### 示例 1：基础装饰器 — 计时与日志

```python
import time


def timer(func):
    """测量函数执行时间的装饰器。"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.4f} seconds.")
        return result

    return wrapper


def log_call(func):
    """记录函数调用参数的装饰器。"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result

    return wrapper


@timer
def compute_sum(n):
    total = sum(range(n))
    return total


@log_call
def greet(name):
    return f"Hello, {name}!"


@timer
@log_call
def process_data(items):
    return [item * 2 for item in items]


if __name__ == "__main__":
    print(compute_sum(1_000_000))
    # [LOG] Calling compute_sum(args=(1000000,), kwargs={})
    # [TIMER] compute_sum took 0.0012 seconds.
    # 499999500000

    print(greet("Python"))
    # [LOG] Calling greet(args=('Python',), kwargs={})
    # [LOG] greet returned Hello, Python!
    # Hello, Python!

    print(process_data([1, 2, 3]))
    # [LOG] Calling process_data(args=([1, 2, 3],), kwargs={})
    # [LOG] process_data returned [2, 4, 6]
    # [TIMER] process_data took 0.0001 seconds.
    # [2, 4, 6]
```

`*args` 和 `**kwargs` 使得 wrapper 可以接收任意数量和类型的参数，并原封不动地转发给原始函数。多个装饰器可以叠加使用（stack），叠加顺序是从下往上：`@timer` 包裹 `@log_call` 包裹 `process_data`，执行时 `timer` 最先启动计时，`log_call` 随后记录日志，最后执行原始函数。

> [!TIP]
> 装饰器的叠加顺序会影响执行行为。`@A @B def f()` 等价于 `f = A(B(f))`，即 B 先包裹 f，然后 A 再包裹结果。调用时 A 的逻辑最先执行，B 的逻辑次之。

### 示例 2：使用 `functools.wraps` 保留函数元数据

```python
import functools


def sloppy_decorator(func):
    """未使用 wraps 的装饰器 — 元数据丢失。"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def proper_decorator(func):
    """使用了 wraps 的装饰器 — 元数据保留。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@sloppy_decorator
def bad_function():
    """This docstring will be lost."""
    pass


@proper_decorator
def good_function():
    """This docstring is preserved."""
    pass


if __name__ == "__main__":
    print(f"sloppy: name={bad_function.__name__}, doc={bad_function.__doc__}")
    # sloppy: name=wrapper, doc=None

    print(f"proper: name={good_function.__name__}, doc={good_function.__doc__}")
    # proper: name=good_function, doc=This docstring is preserved.
```

不使用 `@functools.wraps` 时，被装饰函数的 `__name__` 变成了 `"wrapper"`，`__doc__` 变成了 `None`。这会破坏依赖元数据的工具（如 Flask 路由系统用函数名生成端点名，或 Sphinx 自动生成文档）。

> [!WARNING]
> 永远不要在装饰器中遗漏 `@functools.wraps(func)`。缺少 wraps 会导致调试困难（堆栈跟踪显示错误的函数名）、文档工具失效，以及某些框架（如 Flask、FastAPI）的路由注册异常。

### 示例 3：带参数的装饰器 — 重复执行与超时配置

```python
import functools
import time


def repeat(times):
    """重复执行被装饰函数指定次数的装饰器工厂。"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"[REPEAT] Execution {i + 1}/{times}: calling {func.__name__}()")
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


def timeout(max_seconds):
    """为函数设置超时限制的装饰器工厂。
    注意：此实现使用信号（signal）仅支持 Unix 平台。"""
    import signal

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def raise_timeout(signum, frame):
                raise TimeoutError(f"Function {func.__name__} timed out ({max_seconds}s).")

            old_handler = signal.signal(signal.SIGALRM, raise_timeout)
            signal.alarm(max_seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def roll_dice():
    import random

    return random.randint(1, 6)


@timeout(max_seconds=2)
def slow_task():
    time.sleep(5)
    return "completed"


if __name__ == "__main__":
    print(f"Dice results: {roll_dice()}")
    # [REPEAT] Execution 1/3: calling roll_dice()
    # [REPEAT] Execution 2/3: calling roll_dice()
    # [REPEAT] Execution 3/3: calling roll_dice()
    # Dice results: [4, 2, 6]

    # slow_task()  # Uncomment on Unix to see: TimeoutError
    # TimeoutError: Function slow_task timed out (2s).
```

带参数的装饰器需要三层嵌套：最外层 `repeat(times)` 接收参数并返回装饰器函数，中间层 `decorator(func)` 接收被装饰函数，最内层 `wrapper` 是实际执行的代码。`@repeat(times=3)` 先执行 `repeat(3)` 得到一个装饰器，再将 `roll_dice` 传入。

> [!NOTE]
> `signal.alarm` 仅在 Unix/Linux/macOS 上可用（Windows 不支持 `SIGALRM`）。生产中更推荐使用 `concurrent.futures.TimeoutError` 或第三方库 `func-timeout` 实现跨平台超时控制。

## 常见错误与解决

> [!WARNING]
> **错误 1：遗漏 `@functools.wraps` 导致元数据丢失**
>
> ```python
> def my_decorator(func):
>     def wrapper(*args, **kwargs):
>         return func(*args, **kwargs)
>     return wrapper
>
> @my_decorator
> def my_function():
>     """Important documentation."""
>     pass
>
> print(my_function.__name__)  # wrapper — 不是 my_function！
> print(my_function.__doc__)   # None — 文档字符串丢失！
> ```
>
> **原因**：装饰器返回的 `wrapper` 是一个全新的函数对象，没有继承原始函数的元数据。
>
> **解决**：为 `wrapper` 添加 `@functools.wraps(func)` 装饰器，将原始函数的 `__name__`、`__doc__` 等属性复制到 `wrapper` 上。

> [!WARNING]
> **错误 2：忽略装饰器顺序导致行为不一致**
>
> ```python
> def uppercase(func):
>     def wrapper(*args, **kwargs):
>         return func(*args, **kwargs).upper()
>     return wrapper
>
> def exclamation(func):
>     def wrapper(*args, **kwargs):
>         result = func(*args, **kwargs)
>         return result + "!"
>     return wrapper
>
> @uppercase
> @exclamation
> def message():
>     return "hello"
>
> print(message())  # HELLO! — exclamation 先给 hello 加 !，uppercase 再把整个字符串转大写
>
> # 交换顺序后：
> @exclamation
> @uppercase
> def message():
>     return "hello"
>
> print(message())  # HELLO! — uppercase 先转大写，exclamation 再加 !
> ```
>
> **原因**：装饰器从下往上执行包裹过程，调用时从上往下执行 wrapper 逻辑。顺序不同，组合效果也不同。
>
> **解决**：理解装饰器执行流程——`@A @B def f()` 等价于 `A(B(f))`。B 先包裹 f（进入时 B 的逻辑先执行），A 再包裹结果（A 在 B 的外层）。对于幂等性不强的装饰器组合，务必仔细验证执行顺序。

## 最佳实践

1. **始终使用 `@functools.wraps`** — 在每个装饰器的 `wrapper` 函数上应用 `@functools.wraps(func)`，保留原始函数的元数据，确保调试和文档工具正常工作
2. **保持装饰器职责单一** — 每个装饰器只负责一个增强功能（计时、缓存、日志、鉴权等），通过组合多个装饰器实现复杂逻辑，而非在单个装饰器中堆砌功能
3. **注意闭包变量捕获** — 当在循环中创建装饰器或闭包时，使用默认参数（如 `def wrapper(_i=i)`）避免"延迟绑定"（late binding）问题，否则所有 wrapper 可能捕获到循环变量的最终值

## 练习

1. 编写一个 `@cache_result` 装饰器，使用字典缓存函数在特定参数下的返回值。如果相同参数再次调用，直接返回缓存结果而非重新执行函数。

<details>
<summary>查看答案</summary>

```python
import functools


def cache_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in wrapper._cache:
            wrapper._cache[key] = func(*args, **kwargs)
        return wrapper._cache[key]

    wrapper._cache = {}
    return wrapper


@cache_result
def expensive_computation(n):
    """模拟耗时计算。"""
    print(f"Computing for {n}...")
    result = 0
    for i in range(n):
        result += i * i
    return result


print(expensive_computation(100))
# Computing for 100...
# 328350

print(expensive_computation(100))
# (no output — cached result returned)
# 328350

print(expensive_computation(200))
# Computing for 200...
# 2653300
```

</details>

2. 编写一个 `@validate_types` 装饰器，利用函数的 `__annotations__` 检查传入参数类型是否匹配，不匹配时抛出 `TypeError`。

<details>
<summary>查看答案</summary>

```python
import functools


def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        params = func.__code__.co_varnames[: func.__code__.co_argcount]

        for param_name, value in zip(params, args):
            if param_name in hints and not isinstance(value, hints[param_name]):
                raise TypeError(
                    f"Argument '{param_name}': expected {hints[param_name].__name__}, "
                    f"got {type(value).__name__}"
                )

        for key, value in kwargs.items():
            if key in hints and not isinstance(value, hints[key]):
                raise TypeError(
                    f"Argument '{key}': expected {hints[key].__name__}, "
                    f"got {type(value).__name__}"
                )

        return func(*args, **kwargs)

    return wrapper


@validate_types
def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old."


print(greet("Alice", 30))  # OK
# Alice is 30 years old.

# greet("Alice", "thirty")
# TypeError: Argument 'age': expected int, got str
```

</details>

## 知识检查

1. 装饰器 `@decorator` 放在函数定义上方时，等价于以下哪种写法？
    - A. `decorator(func)`
    - B. `func = decorator(func)`
    - C. `func(decorator)`
    - D. `decorator = func`

2. `functools.wraps` 的主要作用是？
    - A. 加速函数执行
    - B. 自动注册函数到某个注册表
    - C. 保留被装饰函数的元数据（`__name__`、`__doc__` 等）
    - D. 为函数添加参数类型检查

3. 当使用 `@A @B def f(): pass` 时，函数的执行顺序是？
    - A. A 的 wrapper 先执行，B 的 wrapper 再执行，最后执行原始 f
    - B. B 的 wrapper 先执行，A 的 wrapper 再执行，最后执行原始 f
    - C. 原始 f 先执行，然后 B，最后 A
    - D. A 和 B 并行执行

<details>
<summary>查看答案</summary>

1. B — `@decorator` 等价于函数定义后执行 `func = decorator(func)`
2. C — `wraps` 将原始函数的 `__name__`、`__doc__`、`__module__`、`__qualname__`、`__annotations__`、`__dict__`、`__wrapped__` 复制到 wrapper 上
3. A — `@A @B def f()` 等价于 `f = A(B(f))`：B 先包裹 f，A 再包裹 B 的结果；调用时 A 的 wrapper 最外层先执行，进入后 B 的 wrapper 执行，最后才执行原始 f

</details>

## 本章小结

- 装饰器是接收函数并返回函数的高阶函数，核心前提是一等函数（函数可赋值、可传递、可返回）
- `@decorator` 语法糖等价于 `func = decorator(func)`，定义后立即生效
- `functools.wraps` 必须用于 wrapper 函数，以保留原始函数的元数据，避免调试和框架集成问题
- 带参数的装饰器需要三层嵌套：参数接收层 → 装饰器函数层 → wrapper 执行层
- 多个装饰器可以叠加（stack），执行遵循"包裹顺序从下往上、调用顺序从外到内"的规则

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| decorator | 装饰器 | 接收函数并返回函数的高阶函数，用于增强函数行为 |
| first-class function | 一等函数 | 在 Python 中，函数可以像普通变量一样被赋值、传递、作为参数或返回值 |
| wrapper function | 包装函数 | 装饰器内部定义的函数，包裹原始函数并添加额外逻辑 |
| `functools.wraps` | `wraps` 装饰器 | 将原始函数元数据复制到 wrapper 上的实用装饰器 |
| closure | 闭包 | 内层函数捕获外层函数变量的现象，是装饰器能记住被装饰函数的关键机制 |
| `*args` / `**kwargs` | 可变参数 | 用于将任意位置参数和关键字参数转发给原始函数的语法 |
| decorator factory | 装饰工厂 | 返回装饰器函数的函数，用于创建带参数的装饰器 |
| stacked decorators | 叠加装饰器 | 多个装饰器同时修饰一个函数，从下往上执行包裹 |

## 下一步

- [生成器 (Generators)](./generators.md) → 学习 `yield` 和迭代器协议，构建惰性计算管道

## 源码链接

- [decorators_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/decorators_sample.py)
