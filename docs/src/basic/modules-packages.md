# 模块与包 (Modules & Packages)

## 导语

当你的代码从几十行增长到几千行，把所有东西塞在一个文件里就变成了"维护噩梦"。Python 用**模块**（module）和**包**（package）来组织代码——每个 `.py` 文件就是一个模块，包含 `__init__.py` 的目录就是一个包。`import` 语句让你可以在不同模块之间共享代码，`if __name__ == "__main__"` 让模块既能被导入又能独立运行。掌握模块系统，你的代码就从"杂乱的脚本"升级为"结构化的项目"。

## 学习目标

- 掌握 `import` 和 `from...import` 两种导入方式
- 理解 `if __name__ == "__main__"` 守卫（guard）的作用
- 学会 `__all__` 控制模块公开接口

## 概念介绍

**模块**（module）就是单个 `.py` 文件。模块有自己的命名空间（namespace）——模块内的变量、函数、类不会污染全局空间。通过 `import` 语句，你可以访问另一个模块的内容。

`import` 有两种形式：
- `import math` — 导入整个模块，使用时需加前缀 `math.pi`
- `from math import pi` — 只导入特定对象，使用时直接写 `pi`

**`__name__` 守卫**是 Python 模块系统的精髓：当一个 `.py` 文件被**直接运行**时，它的 `__name__` 是 `"__main__"`；被**导入**时，`__name__` 是模块名。通过 `if __name__ == "__main__"` 可以区分这两种场景——测试代码、示例代码放在这个守卫内，被导入时不会执行。

**`__all__`** 是一个字符串列表，定义了模块的**公开 API**。当其他人写 `from module import *`（通配导入）时，只有 `__all__` 中列出的对象会被导入。这是模块化编程中"隐藏实现细节"的重要手段。

> [!TIP]
> Python 标准库中常用的模块：`math`（数学运算）、`datetime`（日期时间）、`json`（JSON 解析）、`os`/`pathlib`（文件系统）、`collections`（高级数据结构）。

## 代码示例

### 示例 1：import 与 from...import

```python
import math
from datetime import datetime

# 完整导入 — 需要模块前缀
print(f"pi = {math.pi:.4f}")
# 输出: pi = 3.1416

# 部分导入 — 直接使用
now = datetime.now()
print(f"now = {now.strftime('%Y-%m-%d %H:%M')}")
# 输出: now = 2024-01-15 14:30 （具体时间）
```

> [!NOTE]
> `import math` 和 `from datetime import datetime` 都是有效的导入方式。推荐后者——只导入你需要的东西，提高代码可读性。

### 示例 2：`__name__ == "__main__"` 守卫

```python
def name_check():
    if __name__ == "__main__":
        print("This module is run directly")
    else:
        print("This module is imported by another module")
```

> [!NOTE]
> 直接运行此文件（`python modules_packages_sample.py`）时，`__name__` 为 `"__main__"`，输出 "run directly"。被其他模块 `import` 时，`__name__` 为 `"modules_packages_sample"`，输出 "imported by another module"。

> [!TIP]
> 这是 Python 模块的**标准模式**——每个模块都可以在文件末尾加上 `if __name__ == "__main__":` 块，放入测试代码或示例用法，让模块既可被导入又可独立运行。

### 示例 3：`__all__` 控制公开接口

```python
# 模块顶部定义 __all__
__all__ = ["import_basics"]


def import_basics():
    """这个函数是公开 API，可通过 __all__ 被导入。"""
    print("import_basics is available")


def internal_helper():
    """这个函数是内部实现，不在 __all__ 中。"""
    return "internal"


# 其他模块写 `from modules_packages_sample import *` 时
# 只能导入 import_basics，不能导入 internal_helper
```

> [!WARNING]
> `__all__` **只影响** `from module import *`（通配导入）的行为。对于 `from module import internal_helper`（显式导入），`__all__` 不起限制作用。它是对公共 API 的声明，而非强制访问控制。

## 常见错误与解决

> [!WARNING]
> **错误 1：循环导入（circular import）**
>
> ```python
> # a.py
> from b import func_b
> def func_a(): pass
>
> # b.py
> from a import func_a  # 💥 ImportError: cannot import name
> def func_b(): func_a()
> ```
>
> **解决**：
> 1. 重构——将共享代码提取到第三个模块 c.py
> 2. 或使用**局部导入**：把 `import` 放在函数内部延迟加载

> [!WARNING]
> **错误 2：`from module import *` 污染命名空间**
>
> 通配导入会把模块的所有公共名称导入当前环境，容易产生命名冲突，且难以追踪名称来源。
>
> **解决**：始终显式导入需要的对象——`from module import a, b, c`，明确列出所需名称。

## 最佳实践

1. **显式导入优于通配导入** — `from module import specific_name` 而非 `from module import *`
2. **把测试代码放在 `if __name__ == "__main__"` 中** — 确保模块被导入时不会执行副作用
3. **用 `__all__` 声明公开 API** — 让使用者清楚哪些是稳定接口，哪些是内部实现
4. **模块按功能分组** — 相关函数放在一起，保持模块"职责单一"

## 练习

1. 假设有一个模块 `utils.py`，其中定义了 `helper()` 和 `_internal()` 两个函数。写一段代码，只导入 `helper()` 而不导入 `_internal()`。

<details>
<summary>查看答案</summary>

```python
from utils import helper

# _internal 不会被导入——即使不定义 __all__，
# 以 _ 开头的名称约定为"内部使用"，不会被通配导入
helper()
```

</details>

2. 写一个模块 `math_utils.py`，包含 `add(a, b)` 和 `multiply(a, b)`，并添加 `if __name__ == "__main__"` 块进行自测试。

<details>
<summary>查看答案</summary>

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


__all__ = ["add", "multiply"]


if __name__ == "__main__":
    assert add(2, 3) == 5
    assert multiply(3, 4) == 12
    print("All tests passed!")
```

</details>

## 知识检查

1. 当模块被直接运行时，`__name__` 的值是？
    - A. 模块文件名
    - B. `"__main__"`
    - C. `"__name__"`
    - D. `"__init__"`

2. `__all__` 控制的是？
    - A. `import module` 导入什么
    - B. `from module import *` 导入什么
    - C. 模块能否被导入
    - D. 模块内部的变量作用域

3. 以下哪种导入方式是推荐的？
    - A. `from math import *`
    - B. `import math` 或 `from math import pi`
    - C. `import *`
    - D. `include math`

<details>
<summary>查看答案</summary>

1. B — 直接运行时 `__name__` 为 `"__main__"`，被导入时为模块名
2. B — `__all__` 只控制通配导入 `from module import *` 的行为
3. B — 显式导入（完整模块或具体名称）是推荐的，通配导入应避免

</details>

## 本章小结

- 每个 `.py` 文件都是一个模块，模块有自己的命名空间
- `import module` 导入整个模块，`from module import name` 导入特定对象
- `if __name__ == "__main__"` 区分"直接运行"和"被导入"两种场景
- `__all__` 声明模块的公开 API，控制 `import *` 的行为
- 避免 `from module import *`，始终显式列出需要导入的名称

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| module | 模块 | 单个 .py 文件，有独立命名空间 |
| package | 包 | 包含 `__init__.py` 的目录 |
| import statement | 导入语句 | 引入其他模块内容的语句 |
| `__name__` | `__name__` | 模块名称的特殊变量 |
| `__all__` | `__all__` | 控制公开接口的列表 |

## 下一步

- [面向对象编程](./oop.md) → 学习用类和对象组织更复杂的代码

## 源码链接

- [modules_packages_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/modules_packages_sample.py)
