# 依赖注入 (Dependency Injection)

## 导语

大型 Python 项目中，对象之间的依赖关系错综复杂：用户服务需要数据库连接，数据库连接需要配置，配置需要环境变量。手动管理这些依赖不仅繁琐，而且难以测试。依赖注入（DI）是一种将"创建依赖"与"使用依赖"解耦的模式——让组件只关注自己的职责，依赖由外部容器提供。本节带你使用 `injector` 库体验 Python 中的依赖注入。

## 学习目标

- 了解依赖注入（DI）的基本概念和优势
- 学会使用 `injector` 库定义模块和绑定
- 掌握 `@inject` 装饰器和 `@provider` 方法的使用

## 概念介绍

依赖注入的核心思想是：一个对象不需要知道如何创建它依赖的对象——它只需要声明需要什么，由外部容器（Injector）负责创建和注入。

`injector` 库提供了三个关键概念：
- **Module** — 定义一组绑定（什么类型映射到什么实现）
- **`@inject`** — 标注构造函数参数需要注入
- **`@provider`** — 方法返回一个实例，Injector 会自动调用

这种模式在大型应用中尤其有用——单元测试可以替换依赖为 mock 对象。

## 代码示例

### 示例 1：基本类型绑定

```python
from injector import Binder, Injector, Module, inject
from typing import NewType

Name = NewType("Name", str)
Description = NewType("Description", str)

class User:
    @inject
    def __init__(self, name: Name, description: Description):
        self.name = name
        self.description = Description

class UserModule(Module):
    def configure(self, binder: Binder):
        binder.bind(User)

class UserAttributeModule(Module):
    def configure(self, binder: Binder):
        binder.bind(Name, to="Sherlock")

    @provider
    def describe(self, name: Name) -> Description:
        return f"{name} is a man of astounding insight"

# 创建 Injector 并注入依赖
injector = Injector([UserModule(), UserAttributeModule()])
user = injector.get(User)
print(f"User: {user.name}")
print(f"Description: {user.description}")
```

### 示例 2：Provider 方法

```python
@provider
def describe(self, name: Name) -> Description:
    return f"{name} is a man of astounding insight"
```

`@provider` 装饰器告诉 Injector：当需要 `Description` 类型时，调用这个方法。Injector 会自动解析 `describe` 的参数 `name: Name`。

### 示例 3：获取注入实例

```python
injector = Injector([UserModule(), UserAttributeModule()])
user = injector.get(User)
```

`injector.get(User)` 触发整个依赖图：Injector 查看 User 的 `@inject` 标注的构造函数，发现需要 `Name` 和 `Description`，然后查找对应模块的绑定和 provider 方法。

> [!NOTE]
> `NewType` 创建了一个类型别名——这在 DI 中很实用：`Name = NewType("Name", str)` 让 Injector 区分 `Name` 和普通的 `str`。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记 `@inject` 装饰器**
>
> 构造函数参数没有 `@inject`，Injector 不知道哪些参数需要注入。
>
> **解决**：所有需要注入依赖的构造函数必须用 `@inject` 装饰。

> [!WARNING]
> **错误 2：绑定循环**
>
> A 依赖 B，B 依赖 A——Injector 无法解析循环依赖。
>
> **解决**：重新设计依赖关系，或使用延迟注入（Lazy Injection）。

## 最佳实践

1. **使用 NewType 创建类型标识** — 避免同类型不同含义的冲突
2. **分模块组织绑定** — 相关依赖放在同一个 Module 类中
3. **优先构造函数注入** — 避免属性注入导致的隐式依赖

## 练习

1. 定义一个 `APIUrl = NewType("APIUrl", str)` 类型，绑定到 `"https://api.example.com"`，注入到一个 `APIClient` 类中。

<details>
<summary>查看答案</summary>

```python
from injector import Binder, Injector, Module, inject
from typing import NewType

APIUrl = NewType("APIUrl", str)

class APIClient:
    @inject
    def __init__(self, url: APIUrl):
        self.url = url

class ConfigModule(Module):
    def configure(self, binder: Binder):
        binder.bind(APIUrl, to="https://api.example.com")
        binder.bind(APIClient)

injector = Injector([ConfigModule()])
client = injector.get(APIClient)
print(f"API URL: {client.url}")
```

</details>

2. 用 `@provider` 方法创建一个 `DatabaseConnection` 实例，依赖 `APIUrl`。

<details>
<summary>查看答案</summary>

```python
class DatabaseModule(Module):
    @provider
    def db_connection(self, url: APIUrl) -> DatabaseConnection:
        return DatabaseConnection(url)
```

</details>

## 知识检查

1. `@inject` 装饰器的作用是：
   - A. 标记函数为异步
   - B. 标注构造函数参数需要依赖注入
   - C. 自动记录函数调用日志
   - D. 创建类的单例实例

2. `@provider` 方法返回的值会被 Injector 如何处理？
   - A. 忽略
   - B. 缓存并注入到依赖该类型的对象中
   - C. 仅当第一次调用时缓存，后续重新计算
   - D. 直接丢弃

3. `NewType("Name", str)` 的用途是？
   - A. 创建 str 的子类
   - B. 在类型层面区分同名但不同含义的类型
   - C. 提升运行时性能
   - D. 替代 dataclass

<details>
<summary>查看答案</summary>

1. B — `@inject` 告诉 Injector 需要注入构造函数参数
2. B — provider 返回值被缓存并在依赖图中分发
3. B — NewType 创建一个新类型，仅在类型检查时区分，运行时等价于原类型

</details>

## 本章小结

- 依赖注入将"创建依赖"与"使用依赖"解耦
- `injector` 库提供 Module、`@inject`、`@provider` 三件套
- Module 定义绑定，Injector 解析依赖图并注入
- NewType 是创建类型标识的好方法
- DI 使单元测试更容易——可以替换依赖为 mock 对象

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| dependency injection | 依赖注入 | 将依赖从外部注入对象，而非内部创建 |
| module | 模块 | 一组依赖绑定的集合 |
| binder | 绑定器 | 负责注册类型映射 |
| provider | 提供者 | 返回特定类型实例的方法 |
| NewType | 新类型 | Python 类型别名机制，用于类型检查 |

## 下一步

- [数据库操作](./database.md) → 学会使用 PyMySQL 和 SQLite 操作数据库

## 源码链接

- [injector_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/injector_sample.py)
