# 数据类 (Data Classes)

## 导语

在 Python 中，我们常常需要创建仅用于存储数据的类——比如表示坐标的点、配置参数、API 响应模型等。一个典型的"数据容器"类往往充斥着重复的样板代码：`__init__` 赋值、`__repr__` 调试输出、`__eq__` 相等比较……这些工作乏味且容易出错。Python 3.7 引入的 `dataclasses` 模块通过 `@dataclass` 装饰器自动生成这些样板方法，让你用最少代码声明数据结构。数据类在概念上类似命名元组（namedtuple），但更灵活——支持类型注解、默认值、继承和自定义初始化逻辑，是现代 Python 项目中构建数据载体的首选方式。

## 学习目标

- 掌握 `@dataclass` 装饰器的基本用法，理解自动生成的 `__init__`、`__repr__`、`__eq__` 方法
- 学会使用 `field()` 配置默认值、`default_factory` 和 `frozen=True` 不可变语义
- 理解 `__post_init__` 钩子和数据类继承的用法与限制

## 概念介绍

`dataclasses` 模块的核心是 `@dataclass` 装饰器。它扫描类体中带类型注解的字段，自动生成一系列特殊方法：

1. **`__init__`** — 根据字段声明生成构造函数，支持默认值
2. **`__repr__`** — 生成可读的字符串表示，格式为 `ClassName(field1=value1, field2=value2)`
3. **`__eq__`** — 按字段值逐个比较，判断两个实例是否相等
4. **`__lt__`、`__le__`、`__gt__`、`__ge__`** — 比较运算（需设置 `order=True`）
5. **`__hash__`** — 哈希值（仅当 `frozen=True` 或 `unsafe_hash=True` 时生成）

`field()` 函数提供字段的细粒度控制，常用参数包括：`default`（默认值）、`default_factory`（无参工厂函数，生成可变默认值）、`init=False`（不参与构造函数）、`repr=False`（不在 `__repr__` 中展示）、`frozen=True`（该字段不可变）、`compare=False`（不参与 `__eq__` 比较）等。

> [!TIP]
> 数据类与命名元组（namedtuple）的关系：namedtuple 是不可变的 `tuple` 子类，侧重节省内存和向后兼容；dataclass 是普通 `class`，支持默认值、修改字段、继承和 `__post_init__`，适用范围更广。两者都可用 `_asdict()` / `dataclasses.asdict()` 转为字典。

## 代码示例

### 示例 1：基本 @dataclass — 自动生成常用方法

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Person:
    name: str
    age: int
    email: str = ""


# Auto-generated __init__: constructor with typed parameters
p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
p3 = Point(1.0, 2.0)

# Auto-generated __repr__: clean debug-friendly string representation
print(p1)  # Point(x=3.0, y=4.0)

# Auto-generated __eq__: field-by-field value comparison
print(p1 == p2)  # True
print(p1 == p3)  # False

# Person with optional default value
alice = Person("Alice", 30)
bob = Person("Bob", 25, "bob@example.com")
print(alice)  # Person(name='Alice', age=30, email='')
print(bob)    # Person(name='Bob', age=25, email='bob@example.com')

# Mutability: fields can be reassigned by default
p1.x = 10.0
print(p1)  # Point(x=10.0, y=4.0)
```

`@dataclass` 只处理带**类型注解**的类变量。没有类型注解的赋值不被视为数据字段。注意：先声明无默认值字段、再声明有默认值字段会引发 `SyntaxError`——因为 Python 无法判断构造函数中哪些参数是必传的。如果有默认值的字段放在前面，没有默认值的字段放在后面，调用时会导致参数位置混乱，这与 Python 函数参数的规则一致。

> [!WARNING]
> **字段声明顺序：没有默认值的字段必须排在有默认值的字段之前。**

```python
# BAD — raises dataclasses.SlotWrapperError / SyntaxError at call site
@dataclass
class Bad:
    name: str = "Alice"
    age: int  # ERROR: non-default argument follows default argument
```

### 示例 2：field() 配置 — default_factory 与 frozen=True

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Classroom:
    teacher: str
    students: List[str] = field(default_factory=list)
    max_size: int = field(default=30, repr=False)  # hidden from __repr__


# default_factory avoids shared mutable state between instances
room_a = Classroom("Ms. Wang")
room_a.students.append("Alice")

room_b = Classroom("Mr. Li")
# room_b.students is []. Without default_factory, it would incorrectly share the same list
print(room_a.students)  # ['Alice']
print(room_b.students)  # []
print(room_a)  # Classroom(teacher='Ms. Wang', students=['Alice']) — max_size hidden


@dataclass(frozen=True)
class Config:
    host: str
    port: int
    debug: bool = False


cfg = Config("localhost", 8080)
print(cfg)  # Config(host='localhost', port=8080, debug=False)

# Reassignment raises dataclasses.FrozenInstanceError — instance is now immutable
try:
    cfg.port = 9090
except dataclasses.FrozenInstanceError as e:
    print(f"FrozenInstanceError: {e}")
```

**为什么需要 `default_factory`？** 如果直接使用 `students: List[str] = []`，所有实例会共享同一个列表对象——这是 Python 中经典的"可变默认值坑"。`default_factory` 接受一个无参可调对象，每次实例化时调用它来生成独立的新对象。`list`、`dict`、`set` 以及任何无参工厂函数都可以作为 `default_factory` 的值。

> [!TIP]
> `frozen=True` 使实例变为不可变的——所有字段赋值都会触发 `FrozenInstanceError`。这让你可以用数据类安全地表示配置值、常量集合等不应被修改的数据。

### 示例 3：数据类继承与 \_\_post_init\_\_ 钩子

```python
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Shape:
    name: str
    color: str = "white"
    _area: Optional[float] = field(default=None, init=False)

    def area(self) -> Optional[float]:
        return self._area


@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def __post_init__(self):
        # Validation and computed field assignment after auto-generated __init__
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive")
        self._area = self.width * self.height


@dataclass
class Circle(Shape):
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")
        self._area = 3.14159 * self.radius ** 2


rect = Rectangle("Photo Frame", "blue", 10.0, 5.0)
print(rect)          # Rectangle(name='Photo Frame', color='blue', width=10.0, height=5.0)
print(rect.area())   # 50.0

circle = Circle("Coin", "gold", 3.0)
print(circle)        # Circle(name='Coin', color='gold', radius=3.0)
print(circle.area()) # 28.274309999999997

# Inheritance: parent fields come first, then child fields
# Shape(name, color, _area) → Rectangle(name, color, width, height)
# _area has init=False, so constructor is (name, color, width, height)
```

`__post_init__` 在自动生成的 `__init__` 的**末尾**被调用，适合做两件事：字段校验（确保数据合法性）和计算字段（根据其他字段推导值）。带 `init=False` 的字段不会出现在构造函数中，只能通过 `__post_init__` 或实例方法赋值。继承时，父类字段排在构造函数参数的前面，子类字段排在后面。

> [!NOTE]
> `dataclasses` 在 Python 3.10+ 支持 `kw_only=True`，允许将指定字段标记为仅关键字参数，进一步降低继承时参数顺序的问题。

## 常见错误与解决

> [!WARNING]
> **错误 1：可变默认值共享（mutable default argument）**
>
> ```python
> from dataclasses import dataclass
>
> @dataclass
> class BadClass:
>     items: list = []  # BAD — all instances share the same list
>
> a = BadClass()
> b = BadClass()
> a.items.append(1)
> print(b.items)  # [1] — unexpected! b sees a mutation
> ```
>
> **原因**：与函数参数的可变默认值问题同源——`[]` 在类定义时被创建一次，所有实例共享。
>
> **解决**：使用 `field(default_factory=list)`：
>
> ```python
> from dataclasses import dataclass, field
>
> @dataclass
> class GoodClass:
>     items: list = field(default_factory=list)
>
> a = GoodClass()
> b = GoodClass()
> a.items.append(1)
> print(b.items)  # [] — each instance gets its own independent list
> ```

> [!WARNING]
> **错误 2：比较 frozen dataclass 时混用类型**
>
> ```python
> from dataclasses import dataclass
>
> @dataclass(frozen=True)
> class A:
>     x: int
>
> @dataclass(frozen=True)
> class B(A):
>     y: int
>
> a = A(10)
> b = B(10, 20)
> print(a == b)  # False — type() is checked first
> ```
>
> **原因**：dataclass 的 `__eq__` 实现会先比较 `type(self) == type(other)`，再逐项比较字段值。即使子类包含父类的所有字段，不同类型的实例也永远不会相等。
>
> **解决**：这是正确行为——不同类型的实例本不应相等。需要值相同则显式提取所需字段比较，或不要将两个不同类做等同判断。

## 最佳实践

1. **数据容器优先使用 `@dataclass`** — 比手写 `__init__`、`__repr__` 更简洁，比 namedtuple 更灵活，是现代 Python 的标准实践
2. **可变默认值一律用 `default_factory`** — `list`、`dict`、`set` 等可变类型永远不要直接赋为默认值，始终用 `field(default_factory=...)`
3. **配置类和无共享状态对象用 `frozen=True`** — 不可变性消除意外修改的 bug，使实例可哈希（能放入 `set` 或作 `dict` 的键），也更利于类型检查工具推断

## 练习

1. 使用 `@dataclass` 定义一个 `Book` 类，包含字段：`title`（str）、`author`（str）、`isbn`（str）、`price`（float）、`tags`（List[str] 默认空列表）。创建一个实例并打印其字符串表示。

<details>
<summary>查看答案</summary>

```python
from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    price: float
    tags: List[str] = field(default_factory=list)


book = Book("Learning Python", "Mark Lutz", "978-1449355739", 59.99, ["Python", "Programming"])
print(book)
# Book(title='Learning Python', author='Mark Lutz', isbn='978-1449355739', price=59.99, tags=['Python', 'Programming'])
```

</details>

2. 定义一个不可变 dataclass `Vector2D`（`x: float`, `y: float`），实现 `__add__` 魔术方法使其支持 `v1 + v2` 返回新的 Vector2D 实例，并添加一个 `magnitude` 属性方法计算模长。

<details>
<summary>查看答案</summary>

```python
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Vector2D:
    x: float
    y: float

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


v1 = Vector2D(3.0, 4.0)
v2 = Vector2D(1.0, 1.0)
v3 = v1 + v2
print(v3)           # Vector2D(x=4.0, y=5.0)
print(v3.magnitude) # 6.4031242374328485
```

</details>

## 知识检查

1. `@dataclass` 装饰器默认**不**会生成以下哪个方法？
    - A. `__init__`
    - B. `__repr__`
    - C. `__hash__`
    - D. `__eq__`

2. 为 dataclass 字段设置可变类型（如 `list`）的默认值时，正确做法是？
    - A. `items: list = []`
    - B. `items: list = field(default=[])`
    - C. `items: list = field(default_factory=list)`
    - D. `items: list = field(init=False)`

3. 以下关于 `frozen=True` dataclass 的描述，**正确**的是？
    - A. 字段可以修改但无法添加新字段
    - B. 实例赋值任何字段都会触发 `FrozenInstanceError`
    - C. 只能通过 `__post_init__` 设置字段值，其他方法不行
    - D. `frozen=True` 不影响 `__eq__` 的比较行为

<details>
<summary>查看答案</summary>

1. C — `@dataclass` 默认生成 `__init__`、`__repr__`、`__eq__`；`__hash__` 仅在 `frozen=True` 或 `unsafe_hash=True` 时生成
2. C — `default_factory=list` 每次实例化调用 `list()` 创建独立新对象，避免共享可变默认值
3. B — `frozen=True` 使实例完全不可变，任何字段赋值（包括 `__post_init__` 之外的任何位置）都会触发 `FrozenInstanceError`

</details>

## 本章小结

- `@dataclass` 自动为带类型注解的类生成 `__init__`、`__repr__`、`__eq__` 等样板方法
- `field(default_factory=...)` 解决可变默认值共享问题，是每个 dataclass 使用者的必备知识
- `frozen=True` 创建不可变实例，消除意外修改并自动支持哈希
- `__post_init__` 钩子在自动 `__init__` 后执行，适合字段校验和计算字段赋值
- 数据类继承遵循"父类字段优先"规则，子类扩展父类的同时保留 auto-generated 方法

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| dataclass | 数据类 | 使用 `@dataclass` 装饰器自动样板方法的类 |
| boilerplate | 样板代码 | 大量重复的手写方法（`__init__`、`__repr__` 等） |
| `default_factory` | 默认工厂函数 | 用于生成可变默认值的无参可调对象 |
| `frozen=True` | 冻结/不可变 | 使 dataclass 实例不可修改字段的配置 |
| `__post_init__` | 后初始化钩子 | 在自动生成的 `__init__` 末尾执行的自定义逻辑 |
| named tuple | 命名元组 | 带字段名的不可变 `tuple` 子类 |

## 下一步

- [阶段复习：进阶部分](./review-advance.md) → 回顾整个进阶部分的知识，检验学习成果

## 源码链接

- 数据类是 Python 标准库模块，无需额外安装：`from dataclasses import dataclass, field`
