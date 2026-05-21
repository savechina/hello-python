# 类型提示 (Type Hints)

## 导语

Python 是一门动态类型语言——变量不需要声明类型，同一个变量可以在运行时改变类型。这种灵活性带来便利的同时，也让大型项目的代码维护和团队协作变得困难。类型提示（Type Hints）是 Python 3.5 引入的可选语法，允许你为变量、函数参数和返回值标注期望的类型。IDE 可以据此提供智能补全，mypy 等静态检查工具可以在运行前发现类型错误，代码阅读者也能一目了然地理解数据流向。Python 的渐进式类型（gradual typing）哲学让类型提示既强大又灵活——你可以从零开始，逐步为项目添加类型标注。

## 学习目标

- 掌握函数参数和返回值的类型注解语法
- 熟练使用 `typing` 模块中的 `List`、`Dict`、`Optional`、`Union`、`TypeAlias` 等类型工具
- 理解 Python 3.10+ 的 `X | Y` 联合类型语法、`TypedDict` 和 `Protocol` 的高级用法

## 概念介绍

类型提示是 Python 中的可选类型标注系统，核心设计理念是**渐进式类型**（gradual typing）——你可以在现有代码中逐步添加类型注解，而不影响运行行为。Python 解释器在运行时**完全忽略**类型提示，它们仅服务于静态分析工具（mypy、pyright）和 IDE（自动补全、重构）。

1. **基本类型注解** — 函数参数使用 `name: type` 语法，返回值使用 `-> type` 语法。例如 `def greet(name: str) -> str:`。变量注解使用 `var: int = 0`。
2. **`typing` 模块** — Python 标准库提供 `List`、`Dict`、`Set`、`Tuple` 等泛型容器类型。`Optional[X]` 等价于 `X | None`，`Union[X, Y]` 表示"X 或 Y"。
3. **`X | Y` 联合语法** — Python 3.10 引入的管道符联合类型，比 `Union[X, Y]` 更简洁。`str | None` 比 `Optional[str]` 更直观。
4. **`TypeAlias`** — 为复杂类型创建可读的别名，提高代码可维护性。
5. **`TypedDict`** — 为字典定义结构化键值类型，比纯 `Dict[str, Any]` 更精准。
6. **`Protocol`** — Python 的"结构子类型"（structural subtyping）——定义接口契约，只要对象实现了所需的方法和属性，就视为兼容，不需要显式继承。
7. **mypy** — 最流行的 Python 静态类型检查器。安装后对文件运行 `mypy myfile.py`，即可在运行前捕获类型错误。

> [!TIP]
> Python 3.10 的 `X | Y` 语法已是官方推荐写法，新项目建议优先使用 `str | None` 而非 `Optional[str]`，`int | str` 而非 `Union[int, str]`。

## 代码示例

### Example 1: Basic function annotations + return types

```python
from typing import Optional


def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def calculate_total(price: float, quantity: int, discount: Optional[float] = None) -> float:
    """Calculate the total price with an optional discount."""
    total = price * quantity
    if discount is not None:
        total *= (1 - discount)
    return round(total, 2)


def find_user(users: list[tuple[int, str]], user_id: int) -> str | None:
    """Find a user name by ID. Returns None if not found."""
    for uid, name in users:
        if uid == user_id:
            return name
    return None


if __name__ == "__main__":
    print(greet("Alice"))  # Hello, Alice!

    result = calculate_total(9.99, 3, 0.1)
    print(f"Total: {result}")  # Total: 26.97

    user_list: list[tuple[int, str]] = [(1, "Alice"), (2, "Bob")]
    found = find_user(user_list, 2)
    print(f"Found: {found}")  # Found: Bob
```

> [!NOTE]
> 函数注解可通过 `greet.__annotations__` 在运行时访问：`{'name': <class 'str'>, 'return': <class 'str'>}`。但 Python 运行时不会检查传入值是否匹配注解的类型。

### Example 2: Complex types (`Optional`, `Union`, `list[dict[str, int]]`) and `X | Y` syntax

```python
from typing import TypeAlias


# Python 3.10+ union syntax
def process_value(value: str | int | float) -> str:
    """Process a value that can be string, int, or float."""
    match value:
        case str():
            return f"String: {value.upper()}"
        case int() | float():
            return f"Number: {value * 2}"


# TypeAlias for complex nested types
ScoreBoard: TypeAlias = dict[str, list[int]]


def get_top_student(scores: ScoreBoard) -> str | None:
    """Find the student with the highest average score."""
    if not scores:
        return None
    averages = {name: sum(s) / len(s) for name, s in scores.items()}
    top = max(averages, key=averages.get)
    return top


UserRecord: TypeAlias = dict[str, str | int | bool]


def format_user(record: UserRecord) -> str:
    """Format a user record into a readable string."""
    name: str = record.get("name", "Unknown")
    age: int = record.get("age", 0)
    active: bool = record.get("active", False)
    status = "active" if active else "inactive"
    return f"{name} (age {age}, {status})"


if __name__ == "__main__":
    print(process_value("hello"))  # String: HELLO
    print(process_value(42))       # Number: 84

    scores: ScoreBoard = {
        "Alice": [95, 87, 92],
        "Bob": [80, 78, 85],
        "Charlie": [90, 93, 91],
    }
    print(f"Top: {get_top_student(scores)}")  # Top: Charlie

    user: UserRecord = {"name": "Alice", "age": 30, "active": True}
    print(format_user(user))  # Alice (age 30, active)
```

> [!TIP]
> `TypeAlias` 不会创建新类型——它仅为复杂的类型表达式赋予可读的名称。mypy 仍然会按原类型严格检查。

### Example 3: TypedDict and Protocol (structural subtyping)

```python
from typing import Protocol, TypedDict


class UserDict(TypedDict):
    """Typed dictionary for user data."""
    name: str
    age: int
    email: str


def create_user(name: str, age: int, email: str) -> UserDict:
    """Create a typed user dictionary."""
    return {"name": name, "age": age, "email": email}


def describe_user(user: UserDict) -> str:
    """Describe a user from a typed dictionary."""
    return f"{user['name']}, age {user['age']}, email {user['email']}"


class Serializable(Protocol):
    """Protocol for objects that can be serialized to string."""

    def serialize(self) -> str: ...


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def serialize(self) -> str:
        return f"User({self.name}, {self.age})"


class Config:
    def __init__(self, data: dict):
        self.data = data

    def serialize(self) -> str:
        return str(self.data)


def serialize_any(obj: Serializable) -> str:
    """Accept any object that follows the Serializable protocol."""
    return obj.serialize()


if __name__ == "__main__":
    # TypedDict usage
    user = create_user("Alice", 30, "alice@example.com")
    print(describe_user(user))  # Alice, age 30, email alice@example.com

    # Protocol-based structural subtyping
    u = User("Bob", 25)
    c = Config({"debug": True})
    print(serialize_any(u))  # User(Bob, 25)
    print(serialize_any(c))  # {'debug': True}
```

> [!NOTE]
> `Protocol` 实现的是**结构子类型**——`User` 和 `Config` 不需要声明继承 `Serializable`，只要它们有 `serialize() -> str` 方法，就被认为兼容 `Serializable` 协议。这与 Java/C# 的接口（名义子类型）不同。

## 常见错误与解决

> [!WARNING]
> **错误 1：混淆运行时检查与静态检查**
>
> ```python
> def add(a: int, b: int) -> int:
>     return a + b
>
>
> result = add("hello", "world")  # 运行时不会报错！Python 不检查类型
> print(result)  # "helloworld" — 字符串拼接
> ```
>
> **原因**：类型提示在运行时完全被忽略。`add("hello", "world")` 不会抛出任何异常，因为 Python 解释器不执行类型检查。
>
> **解决**：在 CI/CD 流程中集成 `mypy`，在代码合并前自动检测类型错误。
>
> ```bash
> pip install mypy
> mypy myfile.py  # 会报告 add("hello", "world") 类型不匹配
> ```

> [!WARNING]
> **错误 2：过度注解（Over-annotating trivial code）**
>
> ```python
> def add(a: int, b: int) -> int:
>     """Add two numbers."""
>     return a + b
>
>
> x: int = 1
> y: int = 2
> z: int = add(x, y)
> ```
>
> **原因**：对于简单赋值和推导，Python 可以自行推断类型。过度注解会增加代码噪音，降低可读性。
>
> **解决**：只为函数签名（参数和返回值）和复杂类型添加注解。简单变量的赋值不需要显式注解。
>
> ```python
> def add(a: int, b: int) -> int:
>     return a + b
>
>
> x = 1       # inference: int
> z = add(x, 2)  # inference: int
> ```

## 最佳实践

1. **优先注解函数签名** — 函数参数和返回值是类型提示的核心价值所在。让 IDE 和 mypy 在函数调用点捕获错误，远比注解局部变量重要
2. **Python 3.10+ 使用 `X | Y` 而非 `Union[X, Y]`** — `|` 语法更简洁，是 PEP 604 的推荐写法。`Optional[X]` 可读性好可以保留，但 `X | None` 也完全可以
3. **在 CI 中集成 mypy** — 类型提示的价值在于工具链。在 GitHub Actions 中添加 `mypy` 检查步骤，确保类型注解不会被破坏

## 练习

1. 使用 `TypedDict` 定义一个 `Product` 类型，包含 `name: str`、`price: float`、`tags: list[str]`。编写函数 `discount(product: Product, rate: float) -> float`，返回打折后的价格。

<details>
<summary>查看答案</summary>

```python
from typing import TypedDict


class Product(TypedDict):
    name: str
    price: float
    tags: list[str]


def discount(product: Product, rate: float) -> float:
    """Return the discounted price."""
    return round(product["price"] * (1 - rate), 2)


if __name__ == "__main__":
    p: Product = {"name": "Laptop", "price": 999.99, "tags": ["electronics", "computer"]}
    print(discount(p, 0.2))  # 799.99
```

</details>

2. 定义 `Protocol` 名为 `Drawable`，包含方法 `draw(self) -> str`。创建 `Circle` 和 `Square` 两个类实现它，编写函数 `render(shape: Drawable) -> str` 调用 `shape.draw()` 并返回结果。

<details>
<summary>查看答案</summary>

```python
from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> str: ...


class Circle:
    def draw(self) -> str:
        return "Drawing a circle"


class Square:
    def draw(self) -> str:
        return "Drawing a square"


def render(shape: Drawable) -> str:
    return shape.draw()


if __name__ == "__main__":
    print(render(Circle()))  # Drawing a circle
    print(render(Square()))  # Drawing a square
```

</details>

## 知识检查

1. Python 的 type hints 在运行时会被执行吗？
    - A. 会，Python 会自动检查传入参数的类型
    - B. 不会，Python 解释器在运行时完全忽略类型提示
    - C. 仅在函数首次调用时检查一次
    - D. 取决于是否安装了 mypy

2. Python 3.10+ 中，`str | None` 等价于 `typing` 模块中的哪个类型？
    - A. `Union[str, None]`
    - B. `Optional[str]`
    - C. 两者都等价
    - D. 没有等价类型

3. `TypedDict` 和 `Protocol` 的核心区别是？
    - A. `TypedDict` 定义字典的键值类型，`Protocol` 定义对象的行为接口
    - B. `TypedDict` 用于类，`Protocol` 用于字典
    - C. `TypedDict` 在运行时被检查，`Protocol` 不被检查
    - D. 没有区别，可以互换使用

<details>
<summary>查看答案</summary>

1. B — Python 解释器运行时不执行类型检查，类型提示仅服务于静态分析工具和 IDE
2. C — `Optional[str]` 等价于 `Union[str, None]`，也等价于 `str | None`，三者语义相同
3. A — `TypedDict` 描述字典内部结构（键和对应的值类型），`Protocol` 描述对象的行为契约（方法和属性）

</details>

## 本章小结

- 类型提示是 Python 的可选语法，运行时不执行，由 mypy 等静态工具在运行前检查
- 函数参数使用 `name: type` 语法，返回值使用 `-> type` 语法
- `typing` 模块提供 `List`、`Dict`、`Optional`、`Union`、`TypeAlias`、`TypedDict`、`Protocol` 等丰富工具
- Python 3.10+ 的 `X | Y` 联合类型语法是官方推荐写法，更简洁直观
- 类型提示的价值依赖于工具链——IDE 自动补全、mypy 静态检查、CI 集成缺一不可

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| type hint | 类型提示 | Python 中为变量和函数标注期望类型的可选语法 |
| gradual typing | 渐进式类型 | 允许在动态类型语言中逐步添加类型标注的理念 |
| mypy | 静态类型检查器 | 检查 Python 代码类型一致性的工具 |
| Union | 联合类型 | 表示一个值可以是多种类型之一 |
| Optional | 可选类型 | 等价于 `X | None`，表示可有可无的类型 |
| TypeAlias | 类型别名 | 为复杂类型表达式创建可读名称 |
| TypedDict | 类型化字典 | 定义字典的键和对应值类型的结构化标注 |
| Protocol | 协议 | Python 的结构子类型机制，定义行为接口契约 |
| structural subtyping | 结构子类型 | 基于对象拥有的方法和属性判断类型兼容性，而非继承关系 |

## 下一步

- [Dataclasses 和 Pydantic](./dataclasses.md) → 学习现代 Python 数据建模工具

## 源码链接

- [type_hints_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/type_hints_sample.py)
