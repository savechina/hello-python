# 异常处理 (Exception Handling)

## 导语

你的程序会在哪个环节出错？文件找不到、网络断开、用户输入了非法数据——程序的世界充满不确定性。Python 用 **异常**（exception）机制来优雅地处理这些"意外情况"。通过 `try`/`except`/`finally` 结构，你可以精准捕获特定错误、提供降级方案、并保证资源被正确清理。写好异常处理，你的程序就从"脆弱"变成了"坚韧"。

## 学习目标

- 掌握 `try`/`except`/`finally`/`else` 完整结构
- 学会使用多个 `except` 子句捕获不同类型的异常
- 掌握自定义异常类（custom exception）的定义与 `raise` 用法

## 概念介绍

异常（exception）是程序运行过程中发生的问题。每个异常都是一个 **Exception 的子类**——`ValueError`（值错误）、`KeyError`（键不存在）、`ZeroDivisionError`（除零）、`FileNotFoundError`（文件不存在）等等。

`try`/`except` 的核心思想：**把可能出错的代码放在 `try` 块中，用 `except` 捕获特定异常并处理**。Python 还支持 `else` 子句（无异常时执行）和 `finally` 子句（无论如何都会执行）——常用于清理资源。

对于业务逻辑中的非法状态，你可以继承 `Exception` 创建**自定义异常类**，然后用 `raise` 主动抛出。这是 Python 中"显式优于隐式"原则的典型体现。

> [!NOTE]
> Python 的异常层次是**树状结构**。`except Exception` 可以捕获大多数异常（但不包括 `SystemExit`、`KeyboardInterrupt` 等），而裸露的 `except:`（无类型）会捕获一切——包括那些你不应该捕获的系统级异常。

## 代码示例

### 示例 1：try/except — 捕获特定异常

```python
raw = "not a number"
try:
    value = int(raw)
    print(f"value: {value}")
except ValueError as e:
    print(f"ValueError: cannot convert '{raw}' to int — {e}")
# 输出: ValueError: cannot convert 'not a number' to int — invalid literal for int()
```

> [!NOTE]
> `except ValueError as e` 中的 `as e` 将异常对象绑定到变量 `e`，方便在错误处理中获取详情。

### 示例 2：try/except/else/finally — 完整结构

```python
numbers = [10, 2, 0]
for n in numbers:
    try:
        result = 100 / n
    except ZeroDivisionError:
        print(f"  n={n}: cannot divide by zero")
    else:
        print(f"  n={n}: 100 / {n} = {result}")
    finally:
        print(f"  n={n}: cleanup done")
# 输出:
#   n=10: 100 / 10 = 10.0     ← 成功，走 else
#   n=10: cleanup done        ← finally 总执行
#   n=2: 100 / 2 = 50.0
#   n=2: cleanup done
#   n=0: cannot divide by zero  ← 捕获零除异常
#   n=0: cleanup done           ← finally 仍然执行
```

> [!TIP]
> `else` 子句只在**没有异常**时执行，把"正常逻辑"和"异常处理"分开，提高可读性。

### 示例 3：自定义异常与 raise

```python
class InvalidAgeError(Exception):
    """自定义异常：年龄不合法。"""

    def __init__(self, age, message="年龄必须在 0-150 之间"):
        self.age = age
        self.message = f"{message}，当前值: {age}"
        super().__init__(self.message)


def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    print(f"  age {age}: valid")


ages = [25, -3, 200]
for age in ages:
    try:
        validate_age(age)
    except InvalidAgeError as e:
        print(f"  age {age}: {e}")
# 输出:
#   age 25: valid
#   age -3: 年龄必须在 0-150 之间，当前值: -3
#   age 200: 年龄必须在 0-150 之间，当前值: 200
```

> [!NOTE]
> 自定义异常类必须继承 `Exception`（或其子类），通过 `raise` 主动抛出。`raise` 可以单独使用（在 `except` 块中重新抛出），也可以带参数。

## 常见错误与解决

> [!WARNING]
> **错误 1：使用裸露的 `except:` 吞掉所有异常**
>
> ```python
> try:
>     do_something()
> except:  # 💥 捕获一切，包括 KeyboardInterrupt
>     pass
> ```
>
> **解决**：始终指定具体异常类型。至少要写 `except Exception:` 而非裸 `except:`。

> [!WARNING]
> **错误 2：在 `except` 中不做任何处理**
>
> ```python
> try:
>     value = int(user_input)
> except ValueError:
>     pass  # 💥 错误被静默吞掉，无法追踪
> ```
>
> **解决**：至少打印日志或记录错误信息：`logging.error(f"Invalid input: {user_input}")`。

## 最佳实践

1. **精确捕获** — 只捕获你知道如何处理的具体异常类型，别用 `except Exception:` 兜底一切
2. **善用 `finally` 清理资源** — 关闭文件、断开数据库连接等清理操作放 `finally`，确保异常时也能执行
3. **自定义异常要有意义** — 异常名要表达业务语义（如 `InvalidAgeError` 而非 `MyError`）
4. **异常信息要具体** — 在异常消息中包含出错值和上下文，方便调试

## 练习

1. 写一个函数 `divide(a, b)`，捕获 `ZeroDivisionError` 和 `TypeError`，分别返回友好提示。

<details>
<summary>查看答案</summary>

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：参数必须是数字"

print(divide(10, 3))   # 3.333...
print(divide(10, 0))   # 错误：除数不能为零
print(divide(10, "a")) # 错误：参数必须是数字
```

</details>

2. 定义一个 `InsufficientFundsError` 异常类（余额不足），在提款函数中使用 `raise` 抛出。

<details>
<summary>查看答案</summary>

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额 {balance} 不足，需提取 {amount}")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    result = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)  # 余额 100 不足，需提取 150
```

</details>

## 知识检查

1. 以下代码中 `finally` 块在什么情况下执行？
    ```python
    try:
        risky_operation()
    except ValueError:
        handle_error()
    finally:
        cleanup()
    ```
    - A. 只在没有异常时执行
    - B. 只在捕获到异常时执行
    - C. 无论是否有异常都执行
    - D. 永远不会执行

2. 自定义异常类应该继承：
    - A. `RuntimeError`
    - B. `Exception`
    - C. 任何内置类
    - D. 不需要继承

3. `raise` 的作用是：
    - A. 捕获异常
    - B. 抛出异常
    - C. 忽略异常
    - D. 定义异常类

<details>
<summary>查看答案</summary>

1. C — `finally` 块无论如何都会执行，无论是否有异常
2. B — 自定义异常应继承 `Exception`（不推荐直接继承 `BaseException`）
3. B — `raise` 用于主动抛出异常

</details>

## 本章小结

- `try`/`except` 捕获特定异常，`finally` 保证清理操作一定执行
- `else` 子句在无异常时执行，分离"正常路径"和"异常路径"
- 多个 `except` 子句可分别处理不同类型的异常
- 自定义异常通过继承 `Exception` 并实现 `__init__`，用 `raise` 抛出
- 永远不要使用裸 `except:`，始终指定具体的异常类型

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| exception | 异常 | 程序运行时的错误事件 |
| try/except | try/except | 捕获并处理异常的结构 |
| finally | finally | 无论异常与否都执行的代码块 |
| custom exception | 自定义异常 | 继承 Exception 的业务专用异常类 |
| raise | raise | 主动抛出异常的语句 |

## 下一步

- [模块与包](./modules-packages.md) → 学会组织和管理代码结构

## 源码链接

- [exception_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/exception_sample.py)
