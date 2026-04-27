# 列表与字典 (Lists & Dicts)

## 导语

想象你在整理一张购物清单——你要不断添加新商品、删掉已买的、修改价格信息。这就是列表和字典的日常用途：它们是 Python 中最常用、最灵活的数据容器。列表（list）是有序的"排队"结构，字典（dict）是键值对应的"查表"结构。掌握它们，加上列表推导式（comprehension）和集合（set），你就能优雅地处理绝大多数数据组织问题。

## 学习目标

- 掌握列表推导式（list comprehension）的简单、条件、嵌套三种写法
- 学会字典的 `get()`、`items()`、`update()` 常用方法
- 理解集合（set）运算和元组（tuple）解包（unpacking）

## 概念介绍

列表推导式是一种用一行表达式生成列表的 Pythonic 写法。它的核心思想是：**把 for 循环和条件判断压缩为一个表达式**，同时避免显式的 `.append()` 调用。

字典是键值对映射（key-value mapping），通过键快速查找值，底层基于哈希表（hash table）实现，所以查找复杂度为 O(1)。

集合（set）是**无序不重复**元素的容器，天然支持数学集合运算：并集（union）、交集（intersection）、差集（difference）。元组（tuple）是不可变的有序序列，常用于**解包**（unpacking）——一次性把多个值赋给多个变量。

> [!TIP]
> 列表推导式比等效的 `for + append` 快约 20%–30%，因为它们在 C 层面优化了内存分配。

## 代码示例

### 示例 1：列表推导式（简单、条件、嵌套）

```python
# 简单推导式：生成 0-4 的平方
squares = [x * x for x in range(5)]
print(f"squares of 0-4: {squares}")
# 输出: squares of 0-4: [0, 1, 4, 9, 16]

# 带条件的推导式：筛选偶数
evens = [x for x in range(10) if x % 2 == 0]
print(f"evens 0-9: {evens}")
# 输出: evens 0-9: [0, 2, 4, 6, 8]

# 嵌套推导式：生成 3x3 乘法表矩阵
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 multiplication matrix: {matrix}")
# 输出: 3x3 multiplication matrix: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

> [!NOTE]
> 嵌套列表推导式的读法是**从外到内**：外层 `for i in range(1, 4)` 控制行，内层 `for j in range(1, 4)` 控制列。

### 示例 2：字典的 get()、items()、update()

```python
user = {"name": "Alice", "age": 30, "city": "Shanghai"}

# 安全访问：get() 找不到键时返回 None 而非 KeyError
print(f"name: {user.get('name')}")      # Alice
print(f"missing key (None): {user.get('phone')}")  # None

# 遍历所有键值对
for key, value in user.items():
    print(f"  {key}: {value}")

# 合并/更新：update() 就地修改字典
user.update({"email": "alice@example.com"})
print(f"after update: {user}")
```

> [!WARNING]
> 直接用 `user['phone']` 访问不存在的键会抛出 `KeyError`。不确定键是否存在时，始终优先使用 `.get()`。

### 示例 3：集合运算与元组解包

```python
# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
print(f"union: {a | b}")           # {1, 2, 3, 4, 5}
print(f"intersection: {a & b}")   # {3}
print(f"difference: {a - b}")     # {1, 2}

# 元组解包
point = (10, 20)
x, y = point
print(f"point ({x}, {y})")  # point (10, 20)
```

> [!TIP]
> 元组解包也可以用于交换变量：`a, b = b, a`——无需临时变量，这是 Python 独有的优雅写法。

## 常见错误与解决

> [!WARNING]
> **错误 1：推导式过度嵌套导致可读性下降**
>
> ```python
> # 三重嵌套——几乎无法理解
> result = [[i * j * k for k in range(3)] for j in range(3) for i in range(3)]
> ```
>
> **解决**：超过两层的推导式应该拆分为普通 `for` 循环。可读性永远优先于简洁性。

> [!WARNING]
> **错误 2：试图解包数量不匹配的元组**
>
> ```python
> point = (10, 20, 30)
> x, y = point  # 💥 ValueError: too many values to unpack
> ```
>
> **解决**：使用 `*` 收集多余值：`x, y, *rest = point`，或确保两边元素数量一致。

## 最佳实践

1. **简单的列表生成优先推导式**：`[x**2 for x in items]` 比 `for + append` 更 Pythonic
2. **字典访问优先 `.get()`**：避免因键不存在触发 `KeyError`；需要默认值时用 `.get(key, default)`
3. **集合用于去重和成员关系测试**：`"apple" in {"apple", "banana"}` 是 O(1) 操作
4. **元组解包处理多返回值**：`width, height = get_size()` 让代码意图清晰

## 练习

1. 用列表推导式生成 1 到 20 之间所有能被 3 整除的数的平方。

<details>
<summary>查看答案</summary>

```python
result = [x * x for x in range(1, 21) if x % 3 == 0]
print(result)  # [9, 36, 81, 144, 225, 324]
```

</details>

2. 有两个字典 `d1 = {"a": 1, "b": 2}` 和 `d2 = {"b": 3, "c": 4}`，合并它们使得 d2 的值覆盖 d1 的同名键。

<details>
<summary>查看答案</summary>

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# 方法 1: update()
merged = d1.copy()
merged.update(d2)

# 方法 2: Python 3.9+ 合并运算符
merged = d1 | d2

print(merged)  # {'a': 1, 'b': 3, 'c': 4}
```

</details>

## 知识检查

1. `[x for x in range(5) if x > 3]` 输出什么？
    - A. `[0, 1, 2, 3, 4]`
    - B. `[4]`
    - C. `[3, 4]`
    - D. `[]`

2. 字典 `d = {"a": 1}`，`d.get("b", 0)` 返回什么？
    - A. `KeyError`
    - B. `None`
    - C. `0`
    - D. `1`

3. 集合 `{1, 2} | {2, 3}` 的结果是？
    - A. `{1, 2, 2, 3}`
    - B. `{2}`
    - C. `{1, 2, 3}`
    - D. `{1, 3}`

<details>
<summary>查看答案</summary>

1. B — `range(5)` 生成 0-4，只有 4 大于 3
2. C — `.get(key, default)` 在键不存在时返回默认值
3. C — `|` 是集合的并集运算，自动去重

</details>

## 本章小结

- 列表推导式 `[expr for x in iterable if cond]` 是生成列表的首选方式
- 字典 `.get()` 安全访问值，`.items()` 遍历键值对，`.update()` 合并字典
- 集合支持 `|`（并集）、`&`（交集）、`-`（差集）运算
- 元组解包 `a, b = pair` 使多值赋值简洁优雅
- 推导式不是越复杂越好——超过两层嵌套时就拆成普通循环

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| list comprehension | 列表推导式 | 一行表达式生成列表 |
| dict comprehension | 字典推导式 | 一行表达式生成字典 |
| set | 集合 | 无序不重复元素容器 |
| tuple | 元组 | 不可变有序序列 |
| unpacking | 解包 | 将序列元素分别赋给多个变量 |

## 下一步

- [文件操作](./file-io.md) → 学会读写文件和路径管理

## 源码链接

- [list_dict_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/list_dict_sample.py)
