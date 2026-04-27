# JSON 数据处理 (JSON Data Processing)

## 导语

在互联网世界中，数据交换几乎都使用 JSON 格式。当你的前端页面通过 API 从后端获取用户信息时，当移动应用与服务器同步数据时，当配置文件被读取时——背后都是 JSON 在承载数据。JSON（JavaScript Object Notation）源自 JavaScript 的对象字面量语法，但因简洁、可读、语言无关，已成为跨语言数据传输的通用标准。Python 内置的 `json` 模块提供了完善的序列化和反序列化工具，让你轻松在 Python 对象与 JSON 文本之间来回转换。

## 学习目标

- 掌握 `json.dumps()` 和 `json.loads()` 的基本用法，包括中文支持和格式化输出
- 学会自定义 JSON 编码器处理 datetime 和自定义类对象
- 掌握 JSON 文件的读写操作

## 概念介绍

JSON 本质上是结构化的文本格式，它支持的数据类型有限但实用：字符串、数字、布尔值、null、对象（字典）和数组（列表）。Python 的 `json` 模块提供了四组核心函数：

1. **`json.dumps()`（序列化）** — 将 Python 对象转换为 JSON 字符串。`dump` 中的 `s` 代表 `string`。常用参数：`indent`（缩进空格数，美化输出）、`ensure_ascii=False`（允许输出中文字符）、`cls`（自定义编码器类）。
2. **`json.loads()`（反序列化）** — 将 JSON 字符串解析为 Python 对象。`loads` 中的 `s` 代表 `string`。
3. **`json.dump()`** — 将 Python 对象直接写入文件对象（File object），而非返回字符串。
4. **`json.load()`** — 从文件对象读取并解析 JSON 数据。

> [!NOTE]
> JSON 与 Python 数据类型的对应关系：`object` ↔ `dict`，`array` ↔ `list`，`string` ↔ `str`，`number` ↔ `int`/`float`，`true/false` ↔ `True/False`，`null` ↔ `None`。注意 Python 的 `True`/`False`/`None` 与 JSON 的 `true`/`false`/`null` 大小写不同。

## 代码示例

### 示例 1：基本序列化与反序列化

```python
import json

data = {
    "name": "辽宁产串红小番茄",
    "price": 12.8,
    "in_stock": True,
    "varieties": ["串红", "樱桃番茄", "黄珍珠"],
    "weight_grams": None,
    "harvest_date": "2023-10-15",
}

# 序列化为 JSON 字符串
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
# 输出:
# {
#   "name": "辽宁产串红小番茄",
#   "price": 12.8,
#   ...
# }

# 从 JSON 字符串反序列化
parsed_data = json.loads(json_str)
print(parsed_data["name"])  # 辽宁产串红小番茄
```

`ensure_ascii=False` 是关键参数——默认情况下 `dumps()` 会将非 ASCII 字符转义为 `\uXXXX` 形式，设置 `False` 后中文直接输出，可读性更好。`indent=2` 使输出具有 2 空格缩进，便于人类阅读（调试时推荐，生产环境为节省带宽通常省略）。

### 示例 2：自定义编码器 — 处理 datetime 和自定义对象

```python
import json
from datetime import datetime


class Product:
    def __init__(self, name: str, expiry_date: datetime):
        self.name = name
        self.expiry_date = expiry_date


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Product):
            return {"name": obj.name, "expiry_date": obj.expiry_date.isoformat()}
        return super().default(obj)


tomato = Product("辽宁串红番茄", datetime(2023, 12, 31))
product_list = {"product": tomato, "update_time": datetime.now()}

json_with_date = json.dumps(product_list, cls=CustomEncoder, indent=2)
print(json_with_date)
# 输出:
# {
#   "product": {
#     "name": "辽宁串红番茄",
#     "expiry_date": "2023-12-31T00:00:00"
#   },
#   "update_time": "2026-04-27T10:30:00.123456"
# }
```

`json` 模块默认只支持基本类型。遇到 `datetime`、自定义类等无法直接序列化的对象时会抛出 `TypeError`。通过继承 `json.JSONEncoder` 并重写 `default()` 方法，可以指定自定义类型的序列化规则。`default()` 方法在遇到未知类型时被调用，返回可序列化的 Python 基本类型。

> [!TIP]
> 如果只需临时处理一两个自定义类型，也可以用 `default` 参数而非定义完整类：`json.dumps(obj, default=lambda o: o.__dict__)`。

### 示例 3：JSON 文件读写

```python
import json

data = {
    "name": "辽宁产串红小番茄",
    "price": 12.8,
    "in_stock": True,
}

# 写入 JSON 文件
with open("data/tomato.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 从 JSON 文件读取
with open("data/tomato.json", "r", encoding="utf-8") as f:
    file_data = json.load(f)
print(file_data)  # {'name': '辽宁产串红小番茄', 'price': 12.8, 'in_stock': True}
```

注意 `dump()`/`load()` 与 `dumps()`/`loads()` 的区别：不带 `s` 的版本操作文件对象（File object），带 `s` 的版本操作字符串。两种 API 的参数基本相同。文件操作时务必指定 `encoding="utf-8"`，否则在某些系统上可能产生编码问题。

> [!NOTE]
> 对于追求极致性能的场景，可以考虑 `ujson`（UltraJSON）库——它是用 C 实现的超fast JSON 编解码器，API 与标准库 `json` 模块完全兼容，但速度可提升数倍。

## 常见错误与解决

> [!WARNING]
> **错误 1：未设置 `ensure_ascii=False` 导致中文乱码**
>
> ```python
> import json
> data = {"city": "大连"}
> print(json.dumps(data))
# 输出: {"city": "\u5927\u8fde"}  — 中文变成了 Unicode 转义序列
> ```
>
> **原因**：`json.dumps()` 默认 `ensure_ascii=True`，将所有非 ASCII 字符转义为 `\uXXXX` 格式。
>
> **解决**：显式设置 `ensure_ascii=False`。
>
> ```python
> json.dumps(data, ensure_ascii=False)  # {"city": "大连"}
> ```

> [!WARNING]
> **错误 2：尝试序列化不支持的类型（如 datetime）**
>
> ```python
> import json
> from datetime import datetime
>
> data = {"time": datetime.now()}
> json.dumps(data)  # 💥 TypeError: Object of type datetime is not JSON serializable
> ```
>
> **原因**：`json` 模块默认不支持 `datetime`、自定义类等复杂类型的序列化。
>
> **解决**：自定义编码器或使用 `default` 参数：
>
> ```python
> json.dumps(data, default=str)  # ✅ 将 datetime 转为字符串
> # 或定义完整的 CustomEncoder 类（见上方示例 2）
> ```

## 最佳实践

1. **写文件用 `encoding="utf-8"`** — JSON 文件读写时必须显式指定 UTF-8 编码，避免不同操作系统上的默认编码差异导致乱码
2. **对不可信输入使用 `try-except` 包裹 `json.loads()`** — 解析外部来源的 JSON 字符串时，格式可能不符合规范，捕获 `json.JSONDecodeError` 避免程序崩溃

## 练习

1. 编写一个函数 `save_config(config_dict, filepath)`，将配置字典保存为格式化的 JSON 文件，包含中文支持。

<details>
<summary>查看答案</summary>

```python
import json

def save_config(config_dict, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(config_dict, f, ensure_ascii=False, indent=2)
```

</details>

2. 编写一个自定义编码器，能将 Python `set` 类型序列化为 JSON 数组。

<details>
<summary>查看答案</summary>

```python
import json

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)  # 将 set 转为 list
        return super().default(obj)

data = {"tags": {"Python", "数据分析", "机器学习"}, "count": 3}
print(json.dumps(data, cls=SetEncoder, ensure_ascii=False))
```

</details>

## 知识检查

1. `json.dumps(data, ensure_ascii=False)` 中 `ensure_ascii=False` 的作用是？
    - A. 加快序列化速度
    - B. 允许非 ASCII 字符（如中文）直接输出
    - C. 跳过字典中的 Unicode 键
    - D. 启用 UTF-16 编码

2. 以下哪个是 `json` 模块将文件读取的正确方式？
    - A. `json.loads()`
    - B. `json.load()`
    - C. `json.read()`
    - D. `json.parse()`

3. Python 的 `None` 在 JSON 中等价于什么？
    - A. `"null"`
    - B. `null`
    - C. `undefined`
    - D. `empty`

<details>
<summary>查看答案</summary>

1. B — 默认 `ensure_ascii=True` 会将中文等转为 `\uXXXX` 转义序列
2. B — `load()` 从文件对象读取，`loads()` 从字符串解析
3. B — JSON 中的 `null`（小写，无引号）对应 Python 的 `None`

</details>

## 本章小结

- `json.dumps()`/`json.loads()` 处理字符串，`json.dump()`/`json.load()` 处理文件
- `ensure_ascii=False` 使中文正常输出，`indent=N` 美化排版
- 自定义 `JSONEncoder` 的 `default()` 方法可以处理 datetime、自定义类等复杂对象
- JSON 数据类型与 Python 类型一一映射：object→dict、array→list、null→None
- 解析外部 JSON 数据时务必处理 `JSONDecodeError` 异常

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| JSON | JavaScript 对象表示法 | 一种轻量级数据交换格式，易于人阅读和编写 |
| serialization | 序列化 | 将 Python 对象转换为 JSON 字符串（或字节）的过程 |
| deserialization | 反序列化 | 将 JSON 字符串解析为 Python 对象的过程 |
| JSONEncoder | JSON 编码器 | Python 中负责将对象序列化为 JSON 格式的基类 |
| custom encoder | 自定义编码器 | 继承 `JSONEncoder` 重写 `default()` 方法处理特殊类型的编码器 |

## 下一步

- [NumPy 数值计算](./numpy.md) → 学习使用 NumPy 进行高效的数值计算和数组操作

## 源码链接

- [json_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/json_sample.py)
