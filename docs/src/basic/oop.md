# 面向对象编程 (Object-Oriented Programming)

## 导语

想象你在经营一家动物园——有狗、猫、鸟等各种动物。每种动物都有名字和种类，但叫声不同、技能不同。如果不用面向对象，你需要用一堆函数和字典来管理这些动物：`{"name": "旺财", "speak": "汪汪"}`……但当动物种类越来越多、属性越来越复杂时，这种函数式写法会变得难以维护。面向对象编程（OOP, Object-Oriented Programming）让你用**类**（class）来定义动物的模板，用**对象**（object）来创建具体的动物，用**继承**（inheritance）来共享共性、覆盖差异。本节带你走进 Python 的 OOP 世界。

## 学习目标

- 掌握 `class` 定义类和 `__init__` 初始化对象
- 学会继承（inheritance）与 `super()` 调用父类
- 理解方法重写（method overriding）和 `__str__` / `__repr__` 双下划线方法

## 概念介绍

面向对象编程（OOP）是一种编程范式（paradigm），核心思想是将**数据**和**行为**封装在同一个对象中。

在 Python 中：
- **类（class）**是对象的模板或蓝图
- **对象（object）**是根据类创建的具体实例（instance）
- **属性（attribute）**是对象上的数据成员（如 `dog.name`）
- **方法（method）**是对象上的函数（如 `dog.speak()`）

`__init__` 是类的**构造方法**（constructor），在创建对象时自动调用，用于初始化对象的属性。`self` 指向对象自身（类似于其他语言中的 `this`），所有实例方法第一个参数必须是 `self`。

继承允许一个子类（subclass）获取父类（ superclass）的属性和方法。`super()` 函数用于调用父类的方法，在子类的 `__init__` 中特别常用。

> [!NOTE]
> Python 所有类默认继承 `object`。`class Animal:` 等价于 `class Animal(object):`。

## 代码示例

### 示例 1：类定义与 `__init__` / `self`

参考源码：[oop_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/oop_sample.py) 中的 `class_definition_sample()`

```python
class Animal:
    """基础动物类。"""

    def __init__(self, name, species):
        self.name = name      # 实例属性
        self.species = species  # 实例属性

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.name} ({self.species})"


pet = Animal("Buddy", "Dog")
print(pet)  # 调用 __str__，输出: Buddy (Dog)
```

- `class Animal:` 定义一个类
- `__init__(self, name, species)` 是构造方法，`self` 指向新创建的对象
- `self.name = name` 将参数保存为实例属性
- `print(pet)` 自动调用 `__str__` 方法获取对象的字符串表示

> [!NOTE]
> `self` 不是 Python 关键字——你完全可以叫它 `this` 或其他名字，但 **PEP 8 强烈推荐 `self`**。

### 示例 2：继承与方法重写

参考源码：`oop_sample.py` 中的 `inheritance_sample()`

```python
class Dog(Animal):
    """Dog 继承 Animal。"""

    def __init__(self, name, breed):
        super().__init__(name, species="狗")  # 调用父类构造方法
        self.breed = breed

    def speak(self):
        return "汪汪！"


class Cat(Animal):
    """Cat 继承 Animal，只重写 speak。"""

    def speak(self):
        return "喵~"


dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "猫")

for animal in [dog, cat]:
    print(f"  {animal.name}: {animal.speak()}")
#   旺财: 汪汪！
#   咪咪: 喵~
```

- `class Dog(Animal):` 表示 Dog 是 Animal 的子类
- `super().__init__(name, species="狗")` 调用父类 Animal 的 `__init__`，复用了属性初始化逻辑
- `Dog.speak()` **重写**（override）了父类的 `speak()` 方法，返回 `"汪汪！"`
- 这就是**多态**（polymorphism）——不同子类对同一个方法有不同的实现

> [!TIP]
> `super()` 比直接用 `Animal.__init__(self, ...)` 更好，因为它支持**多继承**（multiple inheritance）的 MRO（Method Resolution Order）。

### 示例 3：`__str__` 与 `__repr__` 双下划线方法

参考源码：`oop_sample.py` 中的 `dunder_methods_sample()`

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="狗")
        self.breed = breed

    def speak(self):
        return "汪汪！"

    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}')"


dog = Dog("大黄", "田园犬")
print(f"str:  {dog}")         # 调用 __str__（继承自 Animal）: 大黄 (狗)
print(f"repr: {repr(dog)}")   # 调用 __repr__: Dog('大黄', '田园犬')
```

- `__str__` 用于**用户友好**的字符串表示（`print(obj)` 时使用）
- `__repr__` 用于**开发者友好**的字符串表示（REPL 交互、调试时使用），理想情况下应像有效的 Python 代码

> [!NOTE]
> 如果没有 `__str__`，`print(obj)` 会回退到 `__repr__`；但没有 `__repr__` 时会回退到默认的 `<Dog object at 0x...>`。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记写 `self` 参数**
>
> ```python
> class Person:
>     def greet():  # 💥 缺少 self
>         print("Hello")
>
> Person().greet()  # TypeError: greet() takes 0 positional arguments but 1 was given
> ```
>
> **解决**：所有实例方法的第一个参数必须是 `self`。

> [!WARNING]
> **错误 2：在子类 `__init__` 中没有调用 `super().__init__()`**
>
> ```python
> class Dog(Animal):
>     def __init__(self, name, breed):
>         self.breed = breed
>         # 💥 没调用 super().__init__()，self.name 不存在
> ```
>
> **解决**：子类的 `__init__` 中通常要以 `super().__init__(...)` 开头初始化父类。

## 最佳实践

1. **`__init__` 只做赋值** — 不要在构造方法中做复杂计算或 I/O 操作
2. **优先组合而非继承** — 能用"has-a"关系的组合解决的，不用"is-a"关系的继承
3. **善用 `__str__` 和 `__repr__`** — 让自定义对象在 print 和调试中可读

## 练习

1. 定义一个 `BankAccount` 类，包含 `balance` 属性、`deposit(amount)` 和 `withdraw(amount)` 方法，`withdraw` 时检查余额是否足够。

<details>
<summary>查看答案</summary>

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于零")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"余额不足：余额 {self.balance}，取 {amount}")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.holder}'s account: ¥{self.balance}"

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account)  # Alice's account: ¥1500
```

</details>

2. 定义一个 `Student` 类继承 `Person`，添加 `grades` 列表和一个 `average()` 方法返回平均分。

<details>
<summary>查看答案</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}岁"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"{super().__str__()} (学号: {self.student_id})"

s = Student("小明", 15, "S001")
s.add_grade(90)
s.add_grade(85)
print(s)           # 小明, 15岁 (学号: S001)
print(s.average()) # 87.5
```

</details>

## 知识检查

1. `self` 在 Python 类方法中代表什么？
    - A. 当前类本身
    - B. 当前实例对象
    - C. 父类对象
    - D. 无实际意义

2. 子类调用父类的方法应该使用什么？
    - A. `self.super()`
    - B. `super()`
    - C. `parent()`
    - D. `base()`

3. `__str__` 和 `__repr__` 的区别是什么？
    - A. 没有区别，只是命名不同
    - B. `__str__` 面向用户，`__repr__` 面向开发者
    - C. `__str__` 用于调试，`__repr__` 用于打印
    - D. `__str__` 在 Python 2 中使用，`__repr__` 在 Python 3 中使用

<details>
<summary>查看答案</summary>

1. B — `self` 指向调用该方法的实例对象
2. B — `super()` 返回父类的代理对象
3. B — `__str__` 可读性好，`__repr__` 信息完整（理想情况可 eval）

</details>

## 本章小结

- `class` 定义类，`__init__` 是构造方法，`self` 指向实例对象
- 继承用 `class SubClass(ParentClass):` 语法，`super()` 调用父类方法
- 方法重写（method overriding）让子类可以改变父类方法的行为
- `__str__` 提供用户友好的字符串表示，`__repr__` 提供开发者友好的表示
- OOP 的核心是**封装**（encapsulation）、**继承**（inheritance）、**多态**（polymorphism）

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| class | 类 | 创建对象的模板 |
| object | 对象 | 类的实例 |
| inheritance | 继承 | 子类获取父类属性和方法 |
| `__init__` | `__init__` | 类的构造方法 |
| method override | 方法重写 | 子类重新定义父类的方法 |

## 下一步

- [字符串进阶](./string-advanced.md) → 掌握正则表达式和高级字符串操作

## 源码链接

- [oop_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/oop_sample.py)
