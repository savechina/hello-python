# 字符串进阶 (String Advanced)

## 导语

在真实项目中，字符串处理几乎无处不在：从日志文件中提取订单号、清洗用户输入的脏数据、验证邮箱和手机号格式……如果你只会 `+` 拼接和 `.split()`，那只能处理最简单的场景。Python 的字符串工具箱里还有更强大的武器——`re` 模块（regular expression，正则表达式）可以匹配复杂模式，`split()` / `join()` / `strip()` 可以精确操控字符串，以及 f-string 的高级格式化语法可以进行数字对齐、进制转换和精度控制。本节带你掌握 Python 字符串的高阶用法。

## 学习目标

- 掌握 `re` 模块的 `search()`、`findall()`、`sub()` 三大核心函数
- 熟练运用 `split()`、`join()`、`strip()` 等字符串方法
- 学会 f-string 的高级格式化（对齐、精度、进制）

## 概念介绍

正则表达式（regular expression，简称 regex）是一种用特定语法描述文本模式的语言。Python 通过内置的 `re` 模块提供支持。

三个最常用的 `re` 函数：
- `re.search(pattern, string)` — 在字符串中**搜索第一个匹配**，返回 match 对象或 `None`
- `re.findall(pattern, string)` — 找出字符串中**所有匹配**，返回列表
- `re.sub(pattern, repl, string)` — 将匹配的部分**替换**为指定字符串

字符串方法方面，`split()` 分割字符串、`join()` 合并序列、`strip()` 去除两端空白——这三个方法在日常数据处理中出场率最高。

f-string 除了基本的 `f"{value}"` 之外，还支持**格式说明符**（format specifier）：比如 `{number:.2f}` 控制小数位数、`{number:>10}` 控制对齐、`{number:b}` 转换进制。

> [!NOTE]
> 正则表达式的模式字符串建议用**原始字符串** `r"..."` 书写，避免反斜杠转义问题。

## 代码示例

### 示例 1：re 模块 — search / findall / sub

参考源码：[string_advanced_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/string_advanced_sample.py) 中的 `re_module_sample()`

```python
import re

text = "Order #1234, total: ¥89.50. Order #5678, total: ¥120.00"

# findall — 提取所有订单号
orders = re.findall(r"#(\d+)", text)
print(f"order ids: {orders}")
# 输出: order ids: ['1234', '5678']

# sub — 替换匹配内容（脱敏）
redacted = re.sub(r"¥\d+\.\d{2}", "***", text)
print(f"redacted: {redacted}")
# 输出: redacted: Order #1234, total: ***. Order #5678, total: ***

# search — 查找第一个匹配并分组提取
match = re.search(r"total: ¥(\d+\.\d{2})", text)
if match:
    print(f"first total: {match.group(1)}")
# 输出: first total: 89.50
```

正则模式解读：
- `#(\d+)`：匹配 `#` 后跟一个或多个数字，`()` 是捕获组（capturing group）
- `¥\d+\.\d{2}`：匹配 `¥` 后跟数字、小数点、两位小数（货币格式）

> [!TIP]
> `re.findall` 返回的是捕获组的内容而非完整匹配——`r"#(\d+)"` 中的 `()` 让它只返回数字部分 `['1234', '5678']`。

### 示例 2：字符串方法 — split / join / strip

参考源码：`string_advanced_sample.py` 中的 `string_methods_sample()`

```python
csv = "name,age,city\nAlice,30,Shanghai\nBob,25,Beijing"

# strip() 去除两端空白（换行符）
lines = csv.strip().split("\n")
for line in lines:
    # split(",") 按逗号分割每行
    fields = line.split(",")
    print(f"  fields: {fields}")
#   fields: ['name', 'age', 'city']
#   fields: ['Alice', '30', 'Shanghai']
#   fields: ['Bob', '25', 'Beijing']

# join() 合并序列——这里反序重新拼接
reversed_csv = "\n".join(line for line in reversed(lines))
print(f"reversed:\n{reversed_csv}")
```

> [!TIP]
> `str.join(iterable)` 的性能远优于 `+` 循环拼接——它在底层一次性分配内存，而非反复创建新字符串。

### 示例 3：f-string 高级格式化

参考源码：`string_advanced_sample.py` 中的 `fstring_advanced_sample()`

```python
name = "Alice"
score = 95.678
count = 42

# >10 右对齐，宽度 10
print(f"name: {name:>10}")
# 输出: name:      Alice

# 8.2f 总宽度 8，保留 2 位小数
print(f"score: {score:8.2f}")
# 输出: score:   95.68

# :b 二进制，:x 十六进制
print(f"count (binary): {count:b}")  # 101010
print(f"count (hex): {count:x}")     # 2a
```

f-string 格式说明符的通用语法：`{value:[fill]align;width.precision[type]}`。其中：
- `>` 右对齐，`<` 左对齐，`^` 居中
- `f` 浮点数，`b` 二进制，`x` 十六进制，`%` 百分比

> [!NOTE]
> f-string 的格式说明符在 `{}` 内用 `:` 分隔。`f"{score:8.2f}"` 中，`8` 是总宽度，`.2` 是小数位数，`f` 是浮点类型。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记用原始字符串 r"" 写正则**
>
> ```python
> re.search("\d+", "abc123")   # 在普通字符串中 \d 可能被视为转义
> re.search(r"\d+", "abc123")  # ✅ 正确：原始字符串保持 \d 原样
> ```
>
> **解决**：正则表达式模式始终用 `r"..."`（原始字符串）书写。

> [!WARNING]
> **错误 2：split() 不传参数 vs 传空字符串**
>
> ```python
> text = "  hello   world  \n"
> text.split("")      # 💥 ValueError: empty separator
> text.split()        # ✅ ['hello', 'world'] — 默认按任意空白分割并去除空串
> ```
>
> **解决**：按空白分割时无需传参，直接 `split()` 即可。

## 最佳实践

1. **正则表达式用 `r"..."` 原始字符串** — 避免反斜杠带来的转义陷阱
2. **字符串拼接优先 `join()`** — 比循环 `+` 性能更好
3. **善用 f-string 格式说明符** — 对齐、精度、进制转换一行搞定

## 练习

1. 用 `re.findall` 从文本 `"Call me at 138-1234-5678 or 139-8765-4321"` 中提取所有手机号（格式 `XXX-XXXX-XXXX`）。

<details>
<summary>查看答案</summary>

```python
import re
text = "Call me at 138-1234-5678 or 139-8765-4321"
phones = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(phones)  # ['138-1234-5678', '139-8765-4321']
```

</details>

2. 用 `join()` 和生成器表达式，将列表 `["apple", "banana", "cherry"]` 用 `" | "` 连接成大写字符串。

<details>
<summary>查看答案</summary>

```python
fruits = ["apple", "banana", "cherry"]
result = " | ".join(f.upper() for f in fruits)
print(result)  # APPLE | BANANA | CHERRY
```

</details>

## 知识检查

1. 以下哪个 `re` 函数返回所有匹配组成的列表？
    - A. `re.search()`
    - B. `re.findall()`
    - C. `re.sub()`
    - D. `re.match()`

2. `"  hello  world  ".split()` 的结果是？
    - A. `['', '', 'hello', '', 'world', '', '']`
    - B. `['hello', 'world']`
    - C. `['hello', '', 'world']`
    - D. 报错

3. `f"{42:b}"` 的输出是什么？
    - A. `42`
    - B. `0b42`
    - C. `101010`
    - D. `2a`

<details>
<summary>查看答案</summary>

1. B — `re.findall()` 返回列表，`re.search()` 返回单个 match 对象
2. B — `split()` 无参数时按任意连续空白分割并自动去除空串
3. C — `:b` 将整数转为二进制，42 的二进制是 `101010`

</details>

## 本章小结

- `re.search()` 查第一个匹配，`re.findall()` 查所有匹配，`re.sub()` 做替换
- 正则模式用 `r"..."` 原始字符串书写，`()` 定义捕获组
- `split()` / `join()` / `strip()` 是字符串处理三大高频方法
- f-string 支持高级格式说明符：对齐（`>`/`<`/`^`）、精度（`.2f`）、进制（`:b`/`:x`）
- 字符串不可变（immutable），所有字符串方法都返回新字符串

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| regular expression | 正则表达式 | 描述文本模式的语法 |
| re module | re 模块 | Python 内置的正则表达式库 |
| split | split | 按分隔符将字符串分割为列表 |
| join | join | 用分隔符将序列合并为字符串 |
| f-string formatting | f-string 格式化 | 使用 `{}` 和 `:` 控制输出格式 |

## 下一步

- [基础阶段复习](./review-basic.md) → 回顾并巩固基础知识

## 源码链接

- [string_advanced_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/string_advanced_sample.py)
