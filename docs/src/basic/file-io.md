# 文件操作 (File I/O)

## 导语

你每天都在和文件打交道——打开一篇文档、保存一张图片、读取配置文件。在编程中，文件 I/O（file input/output）是程序与外部世界交换数据的基本方式。Python 提供了简洁而强大的文件操作 API：简单的 `open()`、自动管理资源的上下文管理器（context manager）、以及面向对象的 `pathlib` 模块。学会文件操作，你的程序才能持久化数据、读取配置、处理日志。

## 学习目标

- 掌握 `open()` 三种基本模式：读取（r）、写入（w）、追加（a）
- 熟练使用 `with` 语句（上下文管理器）自动管理文件资源
- 学会使用 `pathlib.Path` 进行现代文件系统操作

## 概念介绍

文件操作的核心是 `open()` 函数——它打开一个文件并返回文件对象。打开文件时必须指定**模式**（mode）：`"r"` 只读、`"w"` 写入（覆盖已有内容）、`"a"` 追加（在末尾添加而不覆盖）。

Python 推荐始终使用 **with 语句**（with statement）来操作文件。`with` 背后是上下文管理器（context manager）协议——无论代码是否正常结束，`with` 都会确保文件被正确关闭，避免资源泄露。

读取大文件时，逐行读取（line-by-line）比一次性 `read()` 更高效——Python 的文件对象本身就是可迭代的，每次 `for` 循环只将一行加载到内存。

> [!NOTE]
> Python 3.4 引入的 `pathlib` 是目前官方推荐的**现代**路径操作方式。相比旧的 `os.path`，`pathlib.Path` 使用面向对象的链式调用，更直观、更 Pythonic。

## 代码示例

### 示例 1：open() 读写模式

```python
# 写入文件（w 模式）
with open("hello.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("你好，世界！\n")

# 读取文件（r 模式）
with open("hello.txt", "r") as f:
    content = f.read()
    print(f"file content:\n{content}")

# 追加内容（a 模式）
with open("hello.txt", "a") as f:
    f.write("Appended line.\n")
```

> [!NOTE]
> `"r"` 是默认模式，`open("file.txt")` 等价于 `open("file.txt", "r")`。`"w"` 模式会**清空**已有文件内容，小心使用。

### 示例 2：with 语句与逐行读取

```python
# 用 with 自动管理资源
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# 逐行读取——内存友好
with open("data.txt", "r") as f:
    for line in f:
        print(f"line: {line.strip()}")
# 输出:
# line: Line 1
# line: Line 2
```

> [!TIP]
> `for line in f:` 是读取文件的**最高效方式**。相比 `f.readlines()`（一次性加载全部行到列表），逐行读取只需维护一行内容的内存。

### 示例 3：pathlib.Path 现代操作

```python
from pathlib import Path

path = Path(".")

# 检查路径是否存在
print(f"current dir exists: {path.exists()}")

# 列出当前目录下的 .py 文件
py_files = [p.name for p in path.iterdir() if p.name.endswith(".py")]
print(f"Python files in current dir: {py_files}")

# 路径拼接与文件信息
readme = path / "README.md"
if readme.exists():
    print(f"README.md size: {readme.stat().st_size} bytes")

# 一步读写文件
readme_content = readme.read_text()
print(f"README length: {len(readme_content)} characters")
```

> [!TIP]
> `Path / "subdir"` 使用 `/` 运算符拼接路径，比 `os.path.join()` 更直观。`Path.read_text()` 和 `Path.write_text()` 可以一步完成整个文件的读写。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记关闭文件**
>
> ```python
> f = open("data.txt", "r")
> content = f.read()
> # 💥 忘记 f.close()，文件句柄泄露
> ```
>
> **解决**：始终使用 `with` 语句，让 Python 自动关闭文件：
> ```python
> with open("data.txt", "r") as f:
>     content = f.read()
> ```

> [!WARNING]
> **错误 2：写入中文时报 `UnicodeEncodeError`**
>
> 在 Windows 上，`open()` 默认编码可能是 `gbk`，遇到 UTF-8 字符会报错。
>
> **解决**：始终显式指定编码：`open("file.txt", "w", encoding="utf-8")`。

## 最佳实践

1. **永远用 `with` 打开文件**——自动关闭、异常安全，无需手动 `f.close()`
2. **大文件逐行读取**——`for line in f:` 比 `f.read()` 或 `f.readlines()` 更节省内存
3. **优先 `pathlib`**——`Path.read_text()` 一行完成读写，`/` 运算符拼接路径优雅清晰
4. **显式指定 `encoding`**——避免平台差异导致的编码问题

## 练习

1. 使用 pathlib 找出当前目录下所有 `.md` 文件，并打印它们的大小（字节）。

<details>
<summary>查看答案</summary>

```python
from pathlib import Path

for p in Path(".").iterdir():
    if p.suffix == ".md":
        print(f"{p.name}: {p.stat().st_size} bytes")
```

</details>

2. 读取一个日志文件 `app.log`，只打印包含 `"ERROR"` 的行。

<details>
<summary>查看答案</summary>

```python
with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
```

</details>

## 知识检查

1. `open("file.txt", "a")` 的作用是？
    - A. 清空文件重新写入
    - B. 在文件末尾追加内容
    - C. 只读模式打开
    - D. 删除文件

2. 关于 `with open(...)` 以下说法正确的是？
    - A. 需要手动调用 `.close()`
    - B. 只读取文件的一部分
    - C. 代码结束后自动关闭文件
    - D. 仅二进制文件需要

3. `Path(".").iterdir()` 返回什么？
    - A. 一个字符串列表
    - B. 当前目录下的 Path 对象迭代器
    - C. 布尔值
    - D. 文件内容

<details>
<summary>查看答案</summary>

1. B — `"a"` (append) 在文件末尾追加内容，不会清空已有内容
2. C — `with` 是上下文管理器，退出时自动调用 `.close()`
3. B — `iterdir()` 返回目录中每个条目的 `Path` 对象

</details>

## 本章小结

- `open()` 支持 `"r"`（读）、`"w"`（写）、`"a"`（追加）三种基本模式
- `with` 语句确保文件资源安全释放，是 Python 文件操作的标准写法
- `for line in f:` 是逐行读取的高效方式，内存友好
- `pathlib.Path` 提供面向对象的路径操作，`/` 运算符拼接路径、`.read_text()` 一步读写
- 始终显式指定 `encoding="utf-8"` 避免跨平台编码问题

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| file I/O | 文件 I/O | 文件的读写输入输出操作 |
| context manager | 上下文管理器 | 用 `with` 自动管理资源的协议 |
| with statement | with 语句 | 确保资源正确释放的代码块 |
| pathlib | pathlib | 面向对象的现代路径操作库 |
| file mode | 文件模式 | 打开文件的方式（r/w/a等） |

## 下一步

- [异常处理](./exception.md) → 学会优雅地处理运行错误

## 源码链接

- [file_io_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/file_io_sample.py)
