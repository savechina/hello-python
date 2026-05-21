# 生成器与迭代 (Generators & Iteration)

## 导语

假设你需要处理一个包含 10 亿行日志的文件。如果用列表把所有行读入内存，你的程序会瞬间耗尽几 GB 内存然后崩溃。但如果逐行读取、处理完就丢弃，内存占用几乎为零——这就是**懒加载**（lazy evaluation）的力量。Python 的生成器正是实现懒加载的核心工具：它每次只生成一个值，用多少算多少，特别适合处理大数据流、无限序列和管道式数据处理。掌握生成器，你的程序既省内存又高效。

## 学习目标

- 理解迭代器协议（`__iter__` / `__next__`）和生成器函数的区别与联系
- 掌握 `yield` 关键字的工作原理、生成器表达式以及 `yield from` 的用法
- 学会使用 `.send()`、`.throw()`、`.close()` 实现生成器的双向通信

## 概念介绍

生成器是 Python 中一种特殊的迭代器，它通过 `yield` 关键字实现按需生产值。理解生成器需要先理解迭代器协议。

几个关键概念：

1. **迭代器协议（Iterator Protocol）** — 任何实现了 `__iter__()` 和 `__next__()` 方法的对象都是迭代器。`__iter__()` 返回迭代器自身，`__next__()` 返回下一个值，没有更多值时抛出 `StopIteration`。`for` 循环底层就是通过这个协议工作的。
2. **生成器函数（Generator Function）** — 用 `yield` 而非 `return` 返回值的函数。每次调用 `next()` 时，生成器函数从上次暂停的位置继续执行，保留了所有局部变量和调用栈。这种「暂停-恢复」机制使其内存效率极高。
3. **生成器表达式（Generator Expression）** — 类似列表推导式的语法，但用圆括号而非方括号。例如 `(x**2 for x in range(1000000))` 不创建完整列表，而是在需要时逐个产生值。
4. **`yield from`** — 将控制权委托给另一个生成器或可迭代对象。它等价于用 `for` 循环逐一 `yield` 子 iterable 的所有元素，但代码更简洁，且正确处理了 `send()`/`throw()` 等双向通信。
5. **双向通信（Two-way Communication）** — 生成器不仅是生产者，也是消费者。`.send(value)` 可以向生成器内部发送值（作为 `yield` 表达式的返回值），`.throw()` 可以在生成器内部抛入异常，`.close()` 可以提前关闭生成器。

> [!TIP]
> 判断一个对象是否可以迭代：只要它能用于 `for item in obj` 或传给 `iter(obj)` 而不报错，它就是可迭代的。生成器是迭代器的一种，所有生成器都是可迭代的。

## 代码示例

### 示例 1：基本生成器函数 — 斐波那契数列

```python
def fibonacci():
    """生成斐波那契数列的无限生成器。"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    # 创建生成器对象
    fib = fibonacci()

    # 使用 next() 逐个获取值
    print(next(fib))  # 0
    print(next(fib))  # 1
    print(next(fib))  # 1
    print(next(fib))  # 2
    print(next(fib))  # 3

    # 更常见的用法：结合 break 取前 N 项
    print("\nFirst 10 Fibonacci numbers:")
    for i, num in enumerate(fibonacci()):
        if i >= 10:
            break
        print(num, end=" ")
    print()


if __name__ == "__main__":
    main()
```

斐波那契数列是无限序列，用列表存储会无限增长。生成器让它成为可能——每次只计算并返回下一个值，内存中始终只保存 `a` 和 `b` 两个变量。注意第二次 `for` 循环创建了一个**新的**生成器实例，因为 `fibonacci()` 每次调用都返回独立的生成器对象。

> [!IMPORTANT]
> 生成器是**一次性**的。一旦迭代耗尽（抛出 `StopIteration`），无法重新迭代。如需重用，必须重新调用生成器函数创建新实例。

### 示例 2：生成器表达式 vs 列表推导式 — 内存对比

```python
import sys

def compare_memory():
    """对比列表推导式和生成器表达式的内存占用。"""
    # 列表推导式 — 一次性创建所有元素
    list_comp = [x ** 2 for x in range(1000000)]
    print(f"List comprehension: {sys.getsizeof(list_comp):,} bytes")
    # List comprehension: 8,906,504 bytes  (~8.9 MB)

    # 生成器表达式 — 不创建列表，只创建生成器对象
    gen_exp = (x ** 2 for x in range(1000000))
    print(f"Generator expression: {sys.getsizeof(gen_exp):,} bytes")
    # Generator expression: 112 bytes

    # 验证生成器的值与列表一致
    squares = list(gen_exp)
    print(f"Generated {len(squares)} squares")
    print(f"First 5: {squares[:5]}")
    print(f"Last 5: {squares[-5:]}")


def main():
    compare_memory()


if __name__ == "__main__":
    main()
```

生成器表达式只占用约 100 字节，而列表推导式需要近 9 MB。当数据量增大到 1 亿条时，列表方式会耗尽内存，而生成器依然只占 100 多字节。生成器的核心优势在于**空间复杂度从 O(N) 降到 O(1)**。

> [!TIP]
> 什么时候用列表推导式，什么时候用生成器表达式？答案是：如果只需要遍历一次（如传给 `sum()`、`max()`、`list()` 或用在 `for` 循环中），用生成器表达式；如果需要多次访问、索引或切片，用列表推导式。

### 示例 3：`yield from` 与双向通信 — `.send()`` 和 `.close()`

```python
def running_average():
    """计算运行平均值的生成器，演示 send/close 双向通信。"""
    total = 0
    count = 0
    average = 0

    while True:
        value = yield average
        if value is None:
            break
        total += value
        count += 1
        average = total / count


def flatten_nested(nested_list):
    """使用 yield from 展平嵌套列表。"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_nested(item)
        else:
            yield item


def main():
    print("--- Running Average with .send() ---")
    avg_gen = running_average()
    # 第一次必须用 next() 启动生成器，运行到第一个 yield
    initial = next(avg_gen)
    print(f"Initial average: {initial}")  # 0.0

    # 使用 send 发送值并获取新的平均值
    print(f"After 10: {avg_gen.send(10)}")    # 10.0
    print(f"After 20: {avg_gen.send(20)}")    # 15.0
    print(f"After 30: {avg_gen.send(30)}")    # 20.0
    print(f"After 40: {avg_gen.send(40)}")    # 25.0

    # 用 close() 关闭生成器
    avg_gen.close()
    print("Generator closed.")

    print("\n--- yield from: Flattening Nested Lists ---")
    nested = [[1, 2], [3, [4, 5]], [6]]
    flat = list(flatten_nested(nested))
    print(f"Flattened: {flat}")
    # Flattened: [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    main()
```

运行平均值生成器展示了双向通信的完整流程：`next()` 首次启动生成器并获取初始值，之后 `.send(value)` 将值传入生成器内部（作为 `yield` 表达式的返回值），同时获取新的计算结果。`.close()` 会向生成器内部抛出 `GeneratorExit`，安全终止生成器。

`yield from` 则是 Python 3.3 引入的语法糖，它将迭代任务委托给子可迭代对象，自动处理所有元素的逐一产出，包括递归结构的展平。相比手动写 `for ... yield ...`，代码更简洁且行为更正确。

## 常见错误与解决

> [!WARNING]
> **错误 1：重复使用耗尽的生成器**
>
> ```python
> def count_to_3():
>     for i in range(1, 4):
>         yield i
>
> gen = count_to_3()
> print(list(gen))  # [1, 2, 3]
> print(list(gen))  # 💥 [] — 生成器已耗尽！
> ```
>
> **原因**：生成器是**一次性使用的迭代器**。一旦迭代到末尾（抛出 `StopIteration`），所有后续迭代都直接返回空结果。
>
> **解决**：重新调用生成器函数创建新实例。
>
> ```python
> gen = count_to_3()
> print(list(gen))  # [1, 2, 3]
> gen = count_to_3()  # 创建新实例
> print(list(gen))    # ✅ [1, 2, 3]
> ```

> [!WARNING]
> **错误 2：自定义迭代器忘记在 `__next__` 中抛出 `StopIteration`**
>
> ```python
> class BadCounter:
>     def __init__(self, limit):
>         self.limit = limit
>         self.current = 0
>
>     def __iter__(self):
>         return self
>
>     def __next__(self):
>         if self.current < self.limit:
>             self.current += 1
>             return self.current
>         # 💥 忘记 return 或抛异常！Python 会隐式返回 None，导致 for 循环异常
>
> for x in BadCounter(3):
>     print(x)  # 抛出 TypeError 或死循环
> ```
>
> **原因**：迭代协议要求 `__next__` 在耗尽时**必须**抛出 `StopIteration`。不抛出则 `for` 循环无法正确终止。
>
> **解决**：明确抛出 `StopIteration`。
>
> ```python
> def __next__(self):
>     if self.current < self.limit:
>         self.current += 1
>         return self.current
>     raise StopIteration  # ✅ 正确
> ```

## 最佳实践

1. **大数据处理优先用生成器** — 读取大文件、处理流式数据时，用生成器逐条处理而非一次性加载，内存占用稳定在 O(1)
2. **用 `yield from` 替代嵌套的 `for-yield`** — `yield from sub_generator` 比 `for item in sub_generator: yield item` 更简洁，且正确传递 `send()`/`throw()` 信号
3. **生成器函数内不要混用 `return value`** — PEP 380 规定生成器中的 `return value` 等价于 `raise StopIteration(value)`，但容易引起误解。需要终止时直接用 `return` 或 `raise StopIteration`

## 练习

1. 编写一个生成器函数 `chunked(iterable, size)`，将可迭代对象按指定大小分块，每块返回一个列表。

<details>
<summary>查看答案</summary>

```python
def chunked(iterable, size):
    """将可迭代对象按指定大小分块。"""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


# 使用示例
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for batch in chunked(data, 3):
    print(batch)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
```

</details>

2. 编写一个生成器 `prime_generator()`，按需生成素数（无限序列），并用它打印前 10 个素数。

<details>
<summary>查看答案</summary>

```python
def prime_generator():
    """按需生成素数的无限生成器。"""
    yield 2
    candidate = 3
    while True:
        is_prime = True
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 2


# 打印前 10 个素数
count = 0
for prime in prime_generator():
    if count >= 10:
        break
    print(prime, end=" ")
    count += 1
# 2 3 5 7 11 13 17 19 23 29
```

</details>

## 知识检查

1. 生成器表达式 `(x for x in range(5))` 与列表推导式 `[x for x in range(5)]` 的主要区别是？
    - A. 语法不同，功能完全一样
    - B. 生成器表达式延迟求值，列表推导式立即求值
    - C. 生成器表达式支持索引访问
    - D. 列表推导式内存效率更高

2. 以下哪个方法可以将值发送到生成器内部？
    - A. `gen.push(value)`
    - B. `gen.send(value)`
    - C. `gen.write(value)`
    - D. `gen.input(value)`

3. `yield from [1, 2, 3]` 等价于以下哪段代码？
    - A. `yield [1, 2, 3]`
    - B. `yield 1, 2, 3`
    - C. `for x in [1, 2, 3]: yield x`
    - D. `return [1, 2, 3]`

<details>
<summary>查看答案</summary>

1. B — 生成器表达式只在迭代时逐个产生值（懒加载），列表推导式立即创建完整列表
2. B — `.send(value)` 是生成器的内置方法，用于向内部发送值并获取下一个产出值
3. C — `yield from` 将子可迭代对象的每个元素逐一产出，等价于 for 循环 + yield

</details>

## 本章小结

- 迭代器协议由 `__iter__()` 和 `__next__()` 组成，`for` 循环通过该协议工作
- 生成器函数使用 `yield` 实现暂停-恢复机制，每次只生成一个值，内存效率极高
- 生成器表达式 `(expr for var in iterable)` 语法与列表推导式相同但延迟求值，空间复杂度 O(1)
- `yield from` 将迭代任务委托给子可迭代对象，支持递归结构和双向通信
- 生成器是一次性的，耗尽后需重新创建；`.send()` 和 `.close()` 实现生成器的双向控制

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| generator | 生成器 | 使用 `yield` 的函数，按需产生值而非一次性返回所有结果 |
| iterator protocol | 迭代器协议 | 由 `__iter__()` 和 `__next__()` 组成的接口规范 |
| yield | 产出关键字 | 暂停函数执行并返回当前值，下次调用时从该位置恢复 |
| lazy evaluation | 懒加载/延迟求值 | 只在需要时才计算值，而非提前计算所有结果 |
| generator expression | 生成器表达式 | 用圆括号的推导式语法，返回生成器而非列表 |
| yield from | 委托产出 | 将迭代任务委托给子可迭代对象的语法糖 |
| coroutine | 协程 | 可通过 `.send()` 接收外部值的生成器，支持双向通信 |
| StopIteration | 迭代终止异常 | 迭代器耗尽时抛出的异常，`for` 循环捕获后会正常终止 |

## 下一步

- [上下文管理器](./context-managers.md) → 学习 `with` 语句和 `__enter__`/`__exit__` 协议

## 源码链接

- 本章无对应源码文件 — 示例代码可直接在文档中运行
