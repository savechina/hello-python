# 循环结构 (Loops)

## 导语

重复是程序员最强大的美德之一——但不是让你手动复制粘贴代码。Python 提供了 `for` 循环和 `while` 循环来处理重复任务，配合 `enumerate()`、`zip()` 和列表推导式（comprehension），能让循环代码既简洁又优雅。学会循环，你就掌握了自动化的第一步。

## 学习目标

- 掌握 `for` 循环遍历可迭代对象
- 学会 `while` 循环及其适用场景
- 理解 `break`、`continue` 和 `else` 子句
- 熟练使用 `enumerate()` 和 `zip()` 增强循环
- 了解列表推导式基础

## 概念介绍

循环（loop）让程序可以重复执行一段代码块，直到满足退出条件。Python 中最常用的是 **for 循环**（for loop）——它遍历一个可迭代对象（iterable），每次取出一个元素执行循环体。

**while 循环**（while loop）则在条件为 `True` 时持续执行，适合"不知道要循环多少次"的场景。循环体中可以嵌套 `if` 判断，实现更复杂的逻辑。

Python 的循环有一个独特特性：循环可以带 `else` 子句——只有循环**正常结束**（没有遇到 `break`）时才会执行 `else` 块。这为"遍历未找到"的场景提供了优雅的写法。

> [!TIP]
> 如果你熟悉 C/Java 的 `for (int i = 0; i < n; i++)`，Python 的 `for i in range(n)` 是等价写法，但更直观——"对于 `range(n)` 中的每一个 `i`"。

## 代码示例

### 示例 1：for 循环 — range() 与列表遍历

```python
# 使用 range() 控制循环次数
for i in range(3):
    print(f"第 {i} 次循环")
# 输出: 第 0 次循环, 第 1 次循环, 第 2 次循环

# 直接遍历列表
fruits = ["苹果", "香蕉", "樱桃"]
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")
# 输出: 我喜欢吃 苹果, 我喜欢吃 香蕉, 我喜欢吃 樱桃
```

`range(n)` 生成 0 到 n-1 的整数序列。`range(start, stop, step)` 可以指定起始、结束和步长。

### 示例 2：while 循环与 break/continue

```python
# while + break：找到目标就退出
numbers = [1, 3, 7, 4, 8]
target = 7
for num in numbers:
    if num == target:
        print(f"找到了 {target}！")
        break
    print(f"检查 {num}，不是目标")

# continue：跳过偶数
for i in range(6):
    if i % 2 == 0:
        continue  # 跳过本次循环剩余代码
    print(f"奇数: {i}")
# 输出: 奇数: 1, 奇数: 3, 奇数: 5
```

> [!NOTE]
> `break` 跳出整个循环，`continue` 跳过当前迭代进入下一次循环。不要把两者混淆。

### 示例 3：循环 else 子句

```python
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"找到了 {target}")
        break
else:
    print(f"{target} 不在列表中")
# 输出: 4 不在列表中
```

只有循环**没有被 `break` 中断**时，`else` 块才执行。这在"搜索"场景中非常有用——找到了用 `break` 退出，没找到走 `else`。

### 示例 4：enumerate() 与 zip()

```python
# enumerate：同时获取索引和值
colors = ["红色", "绿色", "蓝色"]
for index, color in enumerate(colors):
    print(f"第 {index} 个颜色: {color}")

# zip：并行遍历多个序列
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} {age} 岁")
# 输出: Alice 30 岁, Bob 25 岁, Charlie 35 岁
```

`enumerate(iterable)` 返回 `(索引, 值)` 的迭代器。`zip(a, b)` 将多个序列"拉链式"配对。

> [!TIP]
> `zip()` 在序列长度不同时，会以最短的为准截断。如需完整遍历，使用 `itertools.zip_longest()`。

### 示例 5：列表推导式基础

```python
# 传统写法
squares = []
for x in range(5):
    squares.append(x ** 2)

# 列表推导式（推荐）
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 带条件的推导式
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

列表推导式（list comprehension）将 `for` + `append` 压缩为一行，同时保持可读性。

## 常见错误与解决

> [!WARNING]
> **错误 1：在循环中修改正在遍历的列表**
>
> ```python
> nums = [1, 2, 3, 4]
> for n in nums:
>     if n == 2:
>         nums.remove(n)  # 💥 会跳过下一个元素
> ```
>
> **解决**：遍历副本 `for n in nums[:]` 或使用列表推导式 `[n for n in nums if n != 2]`。

> [!WARNING]
> **错误 2：无限循环**
>
> ```python
> while True:
>     print("停不下来")  # 💥 永远不会停
> ```
>
> **解决**：确保 `while` 条件最终能变为 `False`，或内部有 `break`。

> [!WARNING]
> **错误 3：range() 边界搞错**
>
> `range(5)` 生成 0 到 4（不含 5），不是 1 到 5。这是新手最常犯的错误。
>
> **解决**：从 1 开始用 `range(1, 6)`。

## 最佳实践

1. **优先 for 循环** 遍历可迭代对象，需要条件控制再用 while
2. **善用 enumerate()** 替代手动维护计数器 `i = 0; for ...; i += 1`
3. **用列表推导式** 替代简单的 for + append，保持代码简洁
4. **避免嵌套超过 2 层** 的循环——考虑提取函数或使用生成器
5. **循环 else 子句** 适合搜索场景，但不要滥用——可读性优先

## 练习

1. 写一个 for 循环，打印 1 到 10 之间所有能被 3 整除的数字。

<details>
<summary>查看答案</summary>

```python
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
# 输出: 3, 6, 9
```

</details>

2. 使用 `enumerate()` 找出列表 `["a", "b", "c", "b", "d"]` 中 `"b"` 出现的所有索引位置。

<details>
<summary>查看答案</summary>

```python
items = ["a", "b", "c", "b", "d"]
indices = [i for i, val in enumerate(items) if val == "b"]
print(indices)  # [1, 3]
```

</details>

## 知识检查

1. `range(2, 8, 2)` 生成哪些数字？
    - A. `2, 4, 6, 8`
    - B. `2, 4, 6`
    - C. `2, 3, 4, 5, 6, 7`
    - D. `2, 4, 6, 7`

2. 以下代码输出什么？
    ```python
    for i in range(3):
        if i == 2:
            break
    else:
        print("loop complete")
    ```
    - A. `loop complete`
    - B. 无输出
    - C. 报错
    - D. `loop complete` 打印 3 次

3. `zip([1, 2], ['a', 'b', 'c'])` 返回几个配对？
    - A. 3 个 — `(1, 'a'), (2, 'b'), (None, 'c')`
    - B. 2 个 — `(1, 'a'), (2, 'b')`
    - C. 报错
    - D. 1 个

<details>
<summary>查看答案</summary>

1. B — `range(start, stop, step)` 不包含 stop，步长为 2
2. B — `break` 中断了循环，`else` 子句不执行
3. B — `zip()` 以最短序列为准

</details>

## 本章小结

- `for` 循环遍历可迭代对象，`while` 基于条件重复执行
- `break` 跳出循环，`continue` 跳过当前迭代
- 循环 `else` 子句在循环正常结束时执行（未被 `break`）
- `enumerate()` 提供索引-值对，`zip()` 并行配对多个序列
- 列表推导式 `[expr for x in iterable if cond]` 是 Pythonic 写法

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| for loop | for 循环 | 遍历可迭代对象的循环 |
| while loop | while 循环 | 基于条件判断的循环 |
| break | break | 跳出整个循环 |
| enumerate | enumerate | 同时获取索引和值的内置函数 |
| zip | zip | 并行遍历多个序列的内置函数 |

## 下一步

- [函数基础](./functions.md) → 学会封装可复用代码块

## 源码链接

- [loops_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/loops_sample.py)
