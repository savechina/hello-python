# 流程控制 (Control Flow)

## 导语

生活中无时无刻在做决定：如果下雨，我就带伞；如果迟到，我就打车。程序也一样——没有流程控制的代码只是一条直线。Python 提供了 `if`/`elif`/`else` 分支、三元运算符（ternary operator）、以及 Python 3.10+ 引入的 `match`/`case` 结构模式匹配。掌握这些，你的程序才能"思考"。

## 学习目标

- 掌握 `if`/`elif`/`else` 条件分支
- 学会使用 Python 三元运算符简化代码
- 了解 `match`/`case` 模式匹配语法（Python 3.10+）

## 概念介绍

流程控制（control flow）决定了代码的执行路径。Python 最常见的流程控制是条件分支：根据某个条件的真假（`True` 或 `False`），决定执行哪一段代码。

Python 中 falsy（假值）包括：`False`、`None`、`0`、`""`（空字符串）、`[]`（空列表）、`{}`（空字典）。其余值均为 truthy（真值）。

## 代码示例

### 示例 1：if/elif/else 分支

```python
score = 85

if score >= 90:
    grade = "A (优秀)"
elif score >= 80:
    grade = "B (良好)"
elif score >= 70:
    grade = "C (及格)"
elif score >= 60:
    grade = "D (待提高)"
else:
    grade = "F (不及格)"

print(f"分数 {score} 对应的等级: {grade}")
# 输出: 分数 85 对应的等级: B (良好)
```

注意 Python 中没有 `switch` 语句——在 3.10 之前，`elif` 链就是多路分支的标准写法。

### 示例 2：三元运算符

```python
temperature = 35
weather = "炎热" if temperature > 30 else "舒适"
print(f"温度 {temperature}°C, 感觉: {weather}")
# 输出: 温度 35°C, 感觉: 炎热
```

Python 的三元运算符格式为 `value_if_true if condition else value_if_false`，可读性优于传统 `? :`。

### 示例 3：match/case（Python 3.10+）

```python
status_code = 404
match status_code:
    case 200:
        message = "OK - 请求成功"
    case 301 | 302:
        message = "重定向 (Redirect)"
    case 404:
        message = "Not Found - 页面未找到"
    case 500:
        message = "Server Error - 服务器错误"
    case _:
        message = f"Unknown status code: {status_code}"

print(f"HTTP {status_code}: {message}")
# 输出: HTTP 404: Not Found - 页面未找到
```

`case _` 是通配匹配，相当于 `else` 或 `default`。

> [!NOTE]
> `match`/`case` 不仅仅是 switch 的替代品——它支持结构模式匹配（structural pattern matching），可以匹配数据类型、解构列表/字典等。详见 Python 官方文档。

## 常见错误与解决

> [!WARNING]
> **错误 1：混淆 `=` 和 `==`**
>
> `if a = 1:` 会报 `SyntaxError`，因为 `=` 是赋值而非比较。
>
> **解决**：使用 `==` 做相等判断。

> [!WARNING]
> **错误 2：`if x == True` 冗余**
>
> 不需要写 `if x == True:` ——直接写 `if x:` 即可。同理 `if x == False:` 应写为 `if not x:`。

## 最佳实践

1. **优先三元运算符** 替代简单的 `if/else` 赋值
2. **`match`/`case` 适合多路分支**（3 个以上条件），比 `elif` 链更清晰
3. **避免深层嵌套** — 超过 3 层嵌套时考虑提前 return 或提取函数

## 练习

1. 写一个函数，判断一个数字是正数、负数还是零，返回对应字符串。

<details>
<summary>查看答案</summary>

```python
def check_number(n):
    if n > 0:
        return "正数"
    elif n < 0:
        return "负数"
    else:
        return "零"

print(check_number(-5))  # 负数
```

</details>

2. 用三元运算符判断一个字符串是否为空（空字符串返回 `"空"`，否则返回 `"非空"`）。

<details>
<summary>查看答案</summary>

```python
text = ""
result = "空" if not text else "非空"
print(result)  # 空
```

</details>

## 知识检查

1. 以下代码输出什么？
   ```python
   x = 0
   if x:
       print("truthy")
   else:
       print("falsy")
   ```
   - A. `truthy`
   - B. `falsy`
   - C. 报错
   - D. 无输出

2. `match`/`case` 从哪个 Python 版本开始提供？
   - A. 3.6
   - B. 3.8
   - C. 3.10
   - D. 3.12

3. 三元运算符 `a if cond else b` 中，当 `cond` 为 `True` 时，返回？
   - A. `a`
   - B. `b`
   - C. `cond`
   - D. `True`

<details>
<summary>查看答案</summary>

1. B — `0` 是 falsy，进入 `else` 分支
2. C — Python 3.10 引入 `match`/`case`
3. A — 条件为真时返回 `a`

</details>

## 本章小结

- `if`/`elif`/`else` 是 Python 最基础的条件分支
- Python 没有传统 `switch`——用 `elif` 链或 `match`/`case`
- 三元运算符 `a if cond else b` 适合简单分支赋值
- `match`/`case` 支持类型匹配和模式解构
-  falsy 值包括 `False`、`None`、`0`、`""`、`[]`、`{}`

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| conditional | 条件 | 控制程序分支的判断 |
| if statement | if 语句 | 最基本条件分支 |
| elif | elif | else if 的缩写 |
| else | else | 默认分支 |
| ternary operator | 三元运算符 | 一行条件表达式 |
| match/case | match/case | 结构模式匹配 |

## 下一步

- [循环结构](./loops.md) → 学会重复执行代码块

## 源码链接

- [control_flow_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/control_flow_sample.py)
