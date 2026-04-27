# 变量与表达式 (Variables & Expressions)

## 导语

想象你在超市结账——购物车里的商品数量、单价、折扣、最终金额，这些数字都需要通过变量存储和表达式计算。Python 编程的第一步，就是学会如何让计算机"记住"数据并对其进行计算。本节将带你掌握变量和表达式，这是所有 Python 程序的基石。

## 学习目标

- 了解 Python 中变量的概念和基本赋值方式
- 掌握常见算术运算符（`+`、`-`、`*`、`/`、`%`）
- 学会使用 f-string 进行字符串格式化

## 概念介绍

在 Python 中，你不需要声明变量类型。当你给一个变量赋值时，Python 会自动推断其类型。例如 `a = 1` — Python 知道 `a` 是整数。这种特性让 Python 非常适合快速原型开发。

表达式（expression）是由值和运算符组成的组合，计算机可以求值（evaluate）并返回结果。例如 `4 * 30` 是一个表达式，求值结果为 `120`。

> [!NOTE]
> Python 中的赋值使用 `=` 符号，而相等判断使用 `==`，初学者经常混淆两者。

## 代码示例

### 示例 1：基本算术运算

```python
a = 1
b = 2
c = a + b
print("c result:" + str(c))  # 输出: c result:3
```

加法运算直接对变量求值。注意 `print()` 中需要使用 `str()` 将数字转为字符串后再拼接。

### 示例 2：运算符速查

```python
sum_val = 5 + 10          # 加法
difference = 95.5 - 4.3   # 减法
product = 4 * 30          # 乘法
quotient = 56.7 / 32.2    # 除法（结果始终为浮点数）
remainder = 43 % 5        # 求余（取模）

print(
    f"sum: {sum_val}, diff: {difference}, product: {product}, quotient: {quotient}, remainder:{remainder}"
)
```

注意除法 `/` 在 Python 中始终返回浮点数（`4 / 2.0` 结果是 `2.0` 而非 `2`）。

### 示例 3：字符串格式化

```python
word = "World"
s2 = f"Format string, Hello {word}. 你好，世界。！"
print(s2)
```

f-string 是 Python 3.6+ 推荐的格式化方式。在字符串前加 `f`，用 `{}` 包裹变量或表达式，即可嵌入值。

## 常见错误与解决

> [!WARNING]
> **错误 1：类型混用导致报错**
>
> `"结果是" + 5` 会抛出 `TypeError`，因为字符串和整数不能直接拼接。
>
> **解决**：使用 `str(5)` 转字符串，或改用 f-string：`f"结果是 {5}"`。

> [!WARNING]
> **错误 2：除法结果类型不符合预期**
>
> `5 / 2` 在 Python 中返回 `2.5`（浮点数），而非 `2`（整数）。
>
> **解决**：如需整数除法，使用 `//`：`5 // 2` 返回 `2`。

## 最佳实践

1. **优先使用 f-string** 而非 `%` 或 `.format()` — 更易读且性能更好
2. **变量名要有意义** — 用 `total_price` 而非 `a`，用 `user_name` 而非 `n`
3. **除法要注意类型** — 用 `/` 得到浮点数，用 `//` 得到整数

## 练习

1. 写一个表达式，计算 1 到 100 的自然数之和。

<details>
<summary>查看答案</summary>

```python
total = (1 + 100) * 100 // 2
print(f"1-100 的和: {total}")  # 5050
```

</details>

2. 用 f-string 输出一段信息：`你今年 25 岁了`，其中 25 是变量。

<details>
<summary>查看答案</summary>

```python
age = 25
print(f"你今年 {age} 岁了")
```

</details>

## 知识检查

1. 以下哪段代码会抛出 `TypeError`？
   - A. `a = 1 + 2`
   - B. `"结果为:" + 5`
   - C. `b = 10 / 2`
   - D. `c = f"{5 + 3}"`

2. `5 // 2` 的结果是？
   - A. `2.5`
   - B. `2`
   - C. `3`
   - D. `5`

3. 在 Python 中，变量在使用前需要先声明吗？
   - A. 需要，用 `var` 声明
   - B. 需要，用 `let` 声明
   - C. 不需要，直接赋值即可
   - D. 不确定

<details>
<summary>查看答案</summary>

1. B — 字符串和整数不能直接拼接
2. B — `//` 是整数除法，结果为 `2`
3. C — Python 是动态类型语言，赋值即声明

</details>

## 本章小结

- 变量不需要声明类型，赋值即创建
- 算术运算符包括 `+`、`-`、`*`、`/`、`%`、`//`
- `/` 运算符始终返回浮点数
- f-string 是字符串格式化的推荐方式
- 变量命名要有意义，避免单字母名称

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| variable | 变量 | 存储数据的名称 |
| operator | 运算符 | 执行计算的符号 |
| expression | 表达式 | 由值和运算符组合的式子 |
| f-string | f-string | 字符串格式化方式 |
| literal | 字面量 | 直接写在代码中的值 |
| assignment | 赋值 | 用 `=` 给变量设定数值 |

## 下一步

- [基础数据类型](./datatype.md) → 了解 Python 的各种数据类型（字符串、列表、字典…）

## 源码链接

- [expression_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/expression_sample.py)
