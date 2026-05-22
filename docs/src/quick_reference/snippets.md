# Python 常用操作速查

本章节提供 Python 开发中最常用操作的代码片段，方便快速查找和复制使用。每个类别包含 3-5 个实用示例。

---

## 字符串操作

### 创建与转换

```python
# 创建字符串
s1 = "hello"
s2 = 'world'
s3 = """多行
字符串"""

# 类型转换
num_str = str(42)
parsed = int("42")
float_val = float("3.14")
```

### 格式化

```python
name = "Alice"
age = 30

# f-string (推荐)
f"Name: {name}, Age: {age}"

# 对齐与精度
f"{name:>10}"      # 右对齐
f"{3.14159:.2f}"   # 保留 2 位小数
f"{42:b}"          # 二进制
```

### 常用方法

```python
text = "  Hello World  "
text.strip()        # 去除两端空白
text.lower()        # 转小写
text.upper()        # 转大写
text.split()        # 按空白分割
" ".join(["a", "b"]) # 合并
text.replace("H", "h") # 替换
text.find("World")  # 查找位置
```

---

## 列表操作

### 创建与初始化

```python
# 基本创建
nums = [1, 2, 3]
empty = []
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# 推导式
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

### 常用操作

```python
nums = [1, 2, 3]
nums.append(4)        # 末尾添加
nums.insert(0, 0)     # 指定位置插入
nums.extend([5, 6])   # 批量追加
nums.pop()            # 弹出末尾
nums.remove(2)        # 按值删除
nums.sort()           # 原地排序
sorted_nums = sorted(nums) # 返回新列表
nums.reverse()        # 原地反转
```

### 切片

```python
nums = [0, 1, 2, 3, 4, 5]
nums[0:3]    # [0, 1, 2]
nums[3:]     # [3, 4, 5]
nums[:3]     # [0, 1, 2]
nums[::2]    # [0, 2, 4] (步长 2)
nums[::-1]   # [5, 4, 3, 2, 1, 0] (反转)
```

---

## 字典操作

### 创建与初始化

```python
# 基本创建
user = {"name": "Alice", "age": 30}

# 推导式
squares = {x: x**2 for x in range(5)}

# 默认值
from collections import defaultdict
counts = defaultdict(int)
```

### 常用操作

```python
user = {"name": "Alice", "age": 30}
user.get("name")           # 安全访问
user.get("phone", "N/A")   # 默认值
user.keys()                # 所有键
user.values()              # 所有值
user.items()               # 键值对
user.update({"role": "admin"}) # 更新
user.pop("age")            # 删除并返回值
```

### 合并字典 (3.9+)

```python
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2  # {"a": 1, "b": 2}
```

---

## 文件操作

### 读取文件

```python
# 一次性读取
content = open("file.txt").read()

# 逐行读取
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# 读取所有行
lines = open("file.txt").readlines()
```

### 写入文件

```python
# 覆盖写入
with open("output.txt", "w") as f:
    f.write("Hello\n")

# 追加写入
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

### 路径操作 (pathlib)

```python
from pathlib import Path

path = Path("data/file.txt")
path.exists()         # 是否存在
path.is_file()        # 是否文件
path.parent           # 父目录
path.name             # 文件名
path.suffix           # 扩展名
path.read_text()      # 读取文本
path.write_text("...") # 写入文本
```

---

## 错误处理

### 基本结构

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No errors")
finally:
    print("Always runs")
```

### 自定义异常

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

raise ValidationError("email", "Invalid format")
```

---

## 函数与装饰器

### 参数类型

```python
def func(pos1, pos2, /, *, kw1, kw2):
    pass
# / 前为位置参数，* 后为关键字参数
```

### 常用装饰器

```python
from functools import lru_cache, wraps

@lru_cache(maxsize=128)
def expensive_computation(n):
    return n * n

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper
```

---

## 迭代工具

### enumerate 与 zip

```python
names = ["Alice", "Bob"]
for i, name in enumerate(names):
    print(f"{i}: {name}")

ages = [30, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### itertools 常用

```python
from itertools import chain, combinations

# 扁平化
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# 组合
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
```

---

## 完整示例代码

所有代码片段均可直接复制使用。更多完整示例请参考:

- [基础部分示例](../basic/)
- [进阶部分示例](../advance/)

---

**返回**: [目录](../SUMMARY.md)
