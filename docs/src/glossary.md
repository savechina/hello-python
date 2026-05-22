# 术语表 (Glossary)

**Purpose**: Bilingual terminology reference (中文 ↔ English) for consistent translation across all documentation chapters.

**Usage**: Reference this glossary when writing chapters to ensure terminology consistency.

---

## 核心概念 (Core Concepts)

| English | 中文 | 说明 |
|---------|------|------|
| Variable | 变量 | 存储数据的名称 |
| Data Type | 数据类型 | 数据的分类（如 int, str, list） |
| Expression | 表达式 | 产生值的代码组合 |
| Statement | 语句 | 执行操作的代码行 |
| Function | 函数 | 可复用的代码块 |
| Method | 方法 | 与对象关联的函数 |
| Parameter | 参数 | 函数定义中的输入变量 |
| Argument | 实参 | 调用函数时传入的实际值 |
| Scope | 作用域 | 变量可访问的代码范围 |
| Module | 模块 | 包含 Python 代码的 `.py` 文件 |
| Package | 包 | 包含 `__init__.py` 的模块目录 |
| Namespace | 命名空间 | 名称到对象的映射 |

---

## 数据类型 (Data Types)

| English | 中文 | 说明 |
|---------|------|------|
| Integer (int) | 整数 | 不带小数点的数字 |
| Float (float) | 浮点数 | 带小数点的数字 |
| String (str) | 字符串 | 文本数据类型 |
| Boolean (bool) | 布尔值 | `True` 或 `False` |
| List | 列表 | 有序可变集合 |
| Tuple | 元组 | 有序不可变集合 |
| Dictionary (dict) | 字典 | 键值对映射 |
| Set | 集合 | 无序不重复元素容器 |
| NoneType | 空类型 | 表示"无值" |
| Mutable | 可变 | 创建后可修改 |
| Immutable | 不可变 | 创建后不可修改 |

---

## 控制流 (Control Flow)

| English | 中文 | 说明 |
|---------|------|------|
| Conditional | 条件语句 | if/elif/else 分支 |
| Loop | 循环 | for/while 重复执行 |
| Iteration | 迭代 | 逐个访问集合元素 |
| Break | 中断 | 跳出循环 |
| Continue | 继续 | 跳过当前循环剩余代码 |
| Match/Case | 模式匹配 | Python 3.10+ 的结构化匹配 |

---

## 面向对象 (OOP)

| English | 中文 | 说明 |
|---------|------|------|
| Class | 类 | 对象的蓝图 |
| Object/Instance | 对象/实例 | 类的具体实例 |
| Attribute | 属性 | 对象的数据成员 |
| Method | 方法 | 对象的函数成员 |
| Inheritance | 继承 | 子类获取父类特性 |
| Polymorphism | 多态 | 同一接口不同实现 |
| Encapsulation | 封装 | 隐藏内部实现细节 |
| Dunder Method | 魔术方法 | `__init__`, `__str__` 等特殊方法 |

---

## 函数式编程 (Functional)

| English | 中文 | 说明 |
|---------|------|------|
| Lambda | Lambda 函数 | 匿名单行函数 |
| Closure | 闭包 | 捕获外部变量的函数 |
| Decorator | 装饰器 | 修改函数行为的函数 |
| Generator | 生成器 | 使用 `yield` 的惰性迭代器 |
| Comprehension | 推导式 | 简洁创建集合的语法 |
| Higher-order Function | 高阶函数 | 接收或返回函数的函数 |

---

## 错误与异常 (Errors & Exceptions)

| English | 中文 | 说明 |
|---------|------|------|
| Exception | 异常 | 运行时错误对象 |
| Try/Except | 异常捕获 | 处理错误的结构 |
| Raise | 抛出 | 主动触发异常 |
| Traceback | 追踪信息 | 错误调用栈信息 |
| Assertion | 断言 | 调试用条件检查 |

---

## 异步与并发 (Async & Concurrency)

| English | 中文 | 说明 |
|---------|------|------|
| Async/Await | 异步/等待 | 异步编程语法 |
| Coroutine | 协程 | 可暂停/恢复的函数 |
| Event Loop | 事件循环 | 异步任务调度器 |
| Thread | 线程 | 操作系统级并发单元 |
| Process | 进程 | 独立执行的程序 |
| GIL | 全局解释器锁 | CPython 的线程限制机制 |

---

## 工具与生态 (Tools & Ecosystem)

| English | 中文 | 说明 |
|---------|------|------|
| Virtual Environment | 虚拟环境 | 隔离的 Python 运行环境 |
| Package Manager | 包管理器 | 安装/管理第三方库的工具 |
| Dependency | 依赖 | 项目所需的外部库 |
| Interpreter | 解释器 | 执行 Python 代码的程序 |
| REPL | 交互式环境 | Read-Eval-Print Loop |
| Linter | 代码检查工具 | 静态分析代码质量 |
| Formatter | 格式化工具 | 自动整理代码风格 |

---

## 常用短语 (Common Phrases)

| English | 中文 | 使用场景 |
|---------|------|----------|
| Runtime | 运行时 | 代码执行期间 |
| Compile time | 编译时 | 代码转换为字节码期间 |
| Type hint | 类型提示 | 标注变量/函数类型 |
| Dynamic typing | 动态类型 | 运行时确定类型 |
| Duck typing | 鸭子类型 | "像鸭子就是鸭子"的类型哲学 |
| Standard library | 标准库 | Python 内置模块集合 |
| Third-party library | 第三方库 | 通过 pip/uv 安装的外部库 |

---

## 维护指南

**更新外部链接**:
- 每季度检查一次官方文档链接
- Python 版本更新时同步更新术语

**添加新术语**:
- 新章节引入新概念时同步添加到对应分类
- 保持中英文对照一致性

---

**最后更新**: 2026-05-22  
**维护者**: Hello Python Documentation Team
