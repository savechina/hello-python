# 函数基础 (Functions)

## 导语

函数（function）是将代码"打包"的魔法——把一段可复用的逻辑封装起来，需要时调用即可。从 `print()` 到 `len()`，你每天用的内置函数都是别人写好的函数。现在，轮到你自己写了。Python 的函数系统相当强大：默认参数、`*args`/`**kwargs`、lambda 表达式、以及独特的 LEGB 变量作用域规则，掌握这些，你的代码就能从"脚本"进化为"工程"。

## 学习目标

- 使用 `def` 定义函数并传递参数
- 理解位置参数（positional）与关键字参数（keyword）
- 掌握 `*args` 和 `**kwargs` 处理任意参数
- 学会 lambda 匿名函数
- 理解 LEGB 变量作用域规则

## 概念介绍

函数是一段可重复调用的代码块。在 Python 中使用 `def`（define）关键字定义函数。函数可以接收参数（parameter）、也可以返回值。没有 `return` 语句的函数默认返回 `None`。

Python 的函数系统有几个独特之处：

1. **参数可以有默认值** — 调用时可以省略，提高了灵活性
2. **`*args` 接收任意数量的位置参数** — 打包为元组（tuple）
3. **`**kwargs` 接收任意数量的关键字参数** — 打包为字典（dict）
4. **变量作用域遵循 LEGB 规则** — Local → Enclosing → Global → Built-in

> [!NOTE]
> Python 中**一切皆对象**，函数也不例外。函数可以赋值给变量、作为参数传递、也可以从函数返回——这就是所谓的一等函数（first-class function）。

## 代码示例

### 示例 1：def 定义函数与参数

```python
def greet(name, greeting="Hello"):
    """带默认参数的函数。"""
    return f"{greeting}, {name}!"

print(greet("Python"))        # Hello, Python!
print(greet("Python", "你好")) # 你好, Python!
```

`greeting="Hello"` 是默认参数（default parameter）。调用时如果没传 `greeting`，就使用默认值。

> [!WARNING]
> 默认参数只能放在必选参数之后！`def greet(greeting="Hello", name):` 会报 `SyntaxError`。

### 示例 2：返回值

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Python 支持返回多个值（实际是返回元组）
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)  # 1 9
```

没有 `return` 的函数隐式返回 `None`。

### 示例 3：*args 与 **kwargs

```python
def show_info(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

show_info("Python", "3.13", version="3.13", type="tutorial")
# 位置参数: ('Python', '3.13')        ← args 是元组
# 关键字参数:
#   version = 3.13                    ← kwargs 是字典
#   type = tutorial
```

`*args` 将额外位置参数打包为**元组**，`**kwargs` 将额外关键字参数打包为**字典**。

> [!TIP]
> 参数顺序规则：`def func(positional, *args, default=value, **kwargs)` — 位置参数 → `*args` → 默认参数 → `**kwargs`。

### 示例 4：lambda 匿名函数

```python
# 普通函数
def square(x):
    return x * x

# 等价 lambda
square = lambda x: x * x
print(square(5))  # 25

# lambda 常见于排序 key
students = [("Bob", 90), ("Alice", 85), ("Charlie", 95)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)  # [('Charlie', 95), ('Bob', 90), ('Alice', 85)]
```

lambda 只能包含一个表达式，不能有语句。适合短小的、一次性的函数。

### 示例 5：LEGB 作用域规则

```python
x = "global"  # Global 作用域

def outer():
    x = "enclosing"  # Enclosing 作用域

    def inner():
        x = "local"  # Local 作用域
        print(f"inner: {x}")  # local

    inner()
    print(f"outer: {x}")  # enclosing

outer()
print(f"global: {x}")  # global

# Builtin 作用域：内置函数如 len(), print() 等
```

**LEGB 规则**：Python 查找变量时按 Local → Enclosing → Global → Built-in 的顺序逐层查找，找到即停。

> [!NOTE]
> 如果要在函数内修改全局变量，需要使用 `global` 关键字；修改 enclosing 作用域的变量，使用 `nonlocal`。

## 常见错误与解决

> [!WARNING]
> **错误 1：可变默认参数的陷阱**
>
> ```python
> def add_item(item, target=[]):
>     target.append(item)
>     return target
>
> print(add_item(1))  # [1]
> print(add_item(2))  # [1, 2]  💥 为什么不是 [2]？
> ```
>
> **原因**：默认参数的值在**函数定义时**求值一次，而非每次调用时创建。
>
> **解决**：使用 `None` 作为默认值。
>
> ```python
> def add_item(item, target=None):
>     if target is None:
>         target = []
>     target.append(item)
>     return target
> ```

> [!WARNING]
> **错误 2：忘记 return**
>
> ```python
> def add(a, b):
>     a + b  # 💥 没有 return！返回 None
>
> result = add(3, 5)
> print(result)  # None
> ```
>
> **解决**：确保需要返回值的函数有 `return` 语句。

> [!WARNING]
> **错误 3：关键字参数位置错误**
>
> ```python
> greet("Python", "Hello", name="World")  # 💥 error
> ```
>
> **解决**：位置参数必须在关键字参数之前。要么全部位置，要么全部关键字。

## 最佳实践

1. **函数职责单一** — 一个函数只做一件事，超过 30 行考虑拆分
2. **参数不要超过 5 个** — 参数太多时考虑用字典或 dataclass 传参
3. **避免可变默认参数** — 默认参数用 `None`，内部再创建空容器
4. **写 docstring** — 每个函数第一行用三引号字符串描述功能、参数、返回值
5. **优先具名函数** — lambda 适合简单场景，复杂逻辑用 `def` 更易维护

## 练习

1. 写一个函数 `calculate(a, b, operation="add")`，支持 `"add"`、`"subtract"`、`"multiply"`、`"divide"` 四种运算，默认加法。

<details>
<summary>查看答案</summary>

```python
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "除数不能为零"
    else:
        return f"未知操作: {operation}"

print(calculate(10, 5))              # 15
print(calculate(10, 5, "divide"))    # 2.0
```

</details>

2. 用 lambda 对列表 `["banana", "Apple", "cherry"]` 按忽略大小写字母排序。

<details>
<summary>查看答案</summary>

```python
words = ["banana", "Apple", "cherry"]
words.sort(key=lambda w: w.lower())
print(words)  # ['Apple', 'banana', 'cherry']
```

</details>

## 知识检查

1. 以下代码输出什么？
    ```python
    def f(x, y=[]):
        y.append(x)
        return y
    print(f(1))
    print(f(2))
    ```
    - A. `[1]`, `[2]`
    - B. `[1]`, `[1, 2]`
    - C. `[1]`, `[2, 1]`
    - D. 报错

2. `*args` 在函数内部是什么类型？
    - A. 列表（list）
    - B. 元组（tuple）
    - C. 字典（dict）
    - D. 集合（set）

3. 以下哪个是合法的 lambda 表达式？
    - A. `lambda x: x + 1`
    - B. `lambda x: return x + 1`
    - C. `lambda x: {return x + 1}`
    - D. `lambda (x): return x + 1`

<details>
<summary>查看答案</summary>

1. B — 可变默认参数被多次调用共享
2. B — `*args` 打包为元组
3. A — lambda 只能包含表达式，不能有 `return` 关键字

</details>

## 本章小结

- `def` 定义函数，可带位置参数、默认参数和返回值
- `*args` 接收任意位置参数（元组），`**kwargs` 接收任意关键字参数（字典）
- lambda 适合简单的一次性函数，语法 `lambda 参数: 表达式`
- LEGB 规则（Local → Enclosing → Global → Built-in）决定变量查找顺序
- 永远不要用可变对象（列表、字典）作为默认参数

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| function | 函数 | 封装可复用代码的块 |
| parameter | 参数 | 函数定义时的占位变量 |
| keyword argument | 关键字参数 | 用 `name=value` 传递的参数 |
| lambda | lambda | 匿名一行函数 |
| scope (LEGB rule) | 作用域 (LEGB 规则) | 变量查找顺序规则 |

## 下一步

- [列表与字典](./list-dict.md) → 掌握最常用的数据结构

## 源码链接

- [functions_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/functions_sample.py)
