# 基础数据类型 (Data Types)

## 导语

在编程世界里，数据是一切的基础——而数据类型决定了你可以对数据做什么、不能做什么。Python 提供了丰富的内置数据类型：文本有字符串（string），整数有整型（int），小数有浮点型（float），真/假有布尔型（bool），还有强大的列表（list）和字典（dict）。本节带你逐一认识它们。

## 学习目标

- 掌握 Python 最常见的几种数据类型
- 学会使用字符串的常用方法（拼接、格式化、大小写转换）
- 了解 f-string 和 `.format()` 的区别

## 概念介绍

Python 是强类型语言（strongly typed）——每个值都有明确的类型，你不能随意混用不同类型的值。但同时它也是动态类型语言（dynamically typed）——你无需提前声明变量类型，Python 会在赋值时自动推断。

常见内置类型包括：
- `str`：字符串
- `int`：整数
- `float`：浮点数
- `bool`：布尔值
- `list`：有序集合
- `dict`：键值对映射

## 代码示例

### 示例 1：字符串定义与使用

```python
text = "hello world. sample"
print(text)  # 输出: hello world. sample
```

字符串可以使用单引号 `'hello'`、双引号 `"hello"` 甚至三引号 `'''多行字符串'''` 来定义。

### 示例 2：字符串格式化

```python
word = "World"
s2 = f"Format string, Hello {word}. 你好，世界。！"
print(s2)

s3 = "The sum of 1 + 2 is {0}".format(1 + 2)
print(s3)
```

> [!TIP]
> f-string（Python 3.6+）是推荐方式。`.format()` 适用于动态模板场景。旧式 `%` 格式化已不推荐。

### 示例 3：字符串方法

```python
fo = "foo"
print("foo capitalize:" + fo.capitalize())  # Foo capitalize: Foo
```

字符串提供了大量内置方法：`.upper()`、`.lower()`、`.strip()`、`.split()`、`.replace()` 等等，是日常编程中使用频率最高的 API 之一。

## 常见错误与解决

> [!WARNING]
> **错误 1：用 `+` 拼接大量字符串导致性能问题**
>
> 在循环中反复用 `+` 拼接字符串会产生大量中间对象。
>
> **解决**：使用 `''.join(list_of_strings)`，或者用 f-string 一次性构建。

> [!WARNING]
> **错误 2：字符串和数字混用**
>
> `"价格是" + 100` 会报错。
>
> **解决**：`f"价格是 {100}"` 或 `"价格是" + str(100)`。

## 最佳实践

1. **统一使用双引号** 定义字符串（项目已配置 ruff 规则）
2. **优先 f-string** 进行格式化
3. **善用内置方法** 而非自己造轮子（如 `title()`、`strip()`）

## 练习

1. 将字符串 `"hello world"` 中的每个单词首字母大写。

<details>
<summary>查看答案</summary>

```python
text = "hello world"
print(text.title())  # Hello World
```

</details>

2. 提取文件名 `"report_2024_final.pdf"` 的扩展名（不含 `.`）。

<details>
<summary>查看答案</summary>

```python
filename = "report_2024_final.pdf"
extension = filename.rsplit(".", 1)[1]
print(extension)  # pdf
```

</details>

## 知识检查

1. `"hello".capitalize()` 返回？
   - A. `HELLO`
   - B. `Hello`
   - C. `hello`
   - D. `HELLO WORLD`

2. 以下哪种字符串格式化方式性能最好？
   - A. `"Name: %s" % name`
   - B. `"Name: {}".format(name)`
   - C. `f"Name: {name}"`
   - D. 性能没有差异

3. Python 中如何定义多行字符串？
   - A. 使用 `//`
   - B. 使用三引号 `"""..."""`
   - C. 使用 `\n` 拼接
   - D. 无法定义

<details>
<summary>查看答案</summary>

1. B — `.capitalize()` 将首字母大写
2. C — f-string 是编译期优化，性能最佳
3. B — 三引号保留换行

</details>

## 本章小结

- Python 是强类型但动态类型语言
- 字符串可以用单引号、双引号或多引号定义
- f-string 是最推荐的格式化方式
- 字符串内置方法丰富，善用 `.split()`、`.join()`、`.strip()` 等
- 注意类型混用会抛出 `TypeError`

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| string (str) | 字符串 | 文本数据类型 |
| integer (int) | 整数 | 不带小数点的数字 |
| float | 浮点数 | 带小数点的数字 |
| boolean (bool) | 布尔值 | `True` 或 `False` |
| list | 列表 | 有序可变集合 |
| dict | 字典 | 键值对映射 |

## 下一步

- [流程控制](./control-flow.md) → 学会根据条件做出不同的程序分支

## 源码链接

- [datatype_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/basic/datatype_sample.py)
