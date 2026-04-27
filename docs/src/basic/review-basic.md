# 阶段复习：基础部分 (Review Basic)

恭喜你完成了 Python 基础教程的全部 11 个章节。本节将帮助你巩固关键概念、检验学习成果。

## 知识清单

以下 11 个项目涵盖了基础部分的核心知识点。逐项自检，确保你对每个主题都有清晰理解：

- [ ] **变量与表达式** — 能用 `=` 赋值、使用算术运算符（`+`、`-`、`*`、`/`、`%`、`//`）、使用 f-string 格式化
- [ ] **基础数据类型** — 能区分 str、int、float、bool、list、dict，并知道它们的基本操作
- [ ] **流程控制** — 能使用 `if`/`elif`/`else` 分支、三元运算符、`match`/`case` 模式匹配
- [ ] **循环结构** — 能使用 `for`/`while` 循环、`break`/`continue`、`enumerate()`、`zip()`
- [ ] **函数基础** — 能定义函数（`def`）、使用参数和返回值、理解 `*args`/`**kwargs`、lambda 表达式、LEGB 作用域规则
- [ ] **列表与字典** — 能使用列表推导式、字典操作（get/items/update）、集合运算、元组解构
- [ ] **文件操作** — 能使用 `open()` 读写文件、`with` 上下文管理器、`pathlib` 操作文件系统
- [ ] **异常处理** — 能使用 `try`/`except`/`finally`、自定义异常类、`raise` 抛出异常
- [ ] **模块与包** — 能使用 `import`/`from...import`、理解 `__name__` guard、`__all__` 导出控制
- [ ] **面向对象编程** — 能定义类（`class`）、使用 `__init__`/`self`、实现继承和方法重写、理解 `__str__`/`__repr__`
- [ ] **字符串高级处理** — 能使用 `re` 模块正则匹配、常用字符串方法（split/join/strip）、f-string 高级格式

## 综合练习

### 练习 1：成绩管理系统

编写一个程序，接收学生姓名和成绩（0-100），存储到字典中。输入 "done" 结束。然后：
- 计算平均分
- 找出最高分和最低分的学生
- 按分数从高到低排序输出

<details>
<summary>查看答案</summary>

```python
scores = {}
while True:
    name = input("输入学生姓名 (done 结束): ")
    if name == "done":
        break
    score = int(input(f"输入 {name} 的成绩: "))
    scores[name] = score

if scores:
    avg = sum(scores.values()) / len(scores)
    best = max(scores, key=scores.get)
    worst = min(scores, key=scores.get)
    print(f"平均分: {avg:.1f}")
    print(f"最高分: {best} ({scores[best]})")
    print(f"最低分: {worst} ({scores[worst]})")
    print("排名:")
    for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name}: {score}")
```

</details>

### 练习 2：文件分析器

读取一个文本文件，统计：
- 总行数
- 总词数
- 出现频率最高的 5 个单词

<details>
<summary>查看答案</summary>

```python
from collections import Counter
from pathlib import Path

text = Path("sample.txt").read_text()
lines = text.strip().split("\n")
words = text.lower().split()

print(f"总行数: {len(lines)}")
print(f"总词数: {len(words)}")

top5 = Counter(words).most_common(5)
print("频率 Top 5:")
for word, count in top5:
    print(f"  {word}: {count}")
```

</details>

### 练习 3：自定义异常 + 类

创建一个 `ValidationError` 自定义异常类。再创建一个 `User` 类，包含 name 和 email 属性——如果 email 不包含 `@` 则抛出 `ValidationError`。

<details>
<summary>查看答案</summary>

```python
class ValidationError(Exception):
    def __init__(self, field, value):
        super().__init__(f"{field} 验证失败: {value}")

class User:
    def __init__(self, name, email):
        self.name = name
        if "@" not in email:
            raise ValidationError("email", email)
        self.email = email

    def __str__(self):
        return f"User({self.name}, {self.email})"

try:
    u = User("Alice", "alice@example.com")
    print(u)
    u2 = User("Bob", "invalid")
except ValidationError as e:
    print(f"验证失败: {e}")
```

</details>

## 自测题库

1. `"Python"[1:4]` 的结果是？
   - A. `Pyt`
   - B. `yth`
   - C. `Pyth`
   - D. `ytho`

2. 以下哪个语句可以遍历字典的键值对？
   - A. `for k in d:`
   - B. `for k, v in d.items():`
   - C. `for v in d.values():`
   - D. `for i in range(len(d)):`

3. `with open("f.txt") as f:` 中 `with` 的作用是？
   - A. 提高读取速度
   - B. 自动关闭文件
   - C. 检查文件是否存在
   - D. 加密文件内容

4. `try...except...else...finally` 中，`else` 块在什么时候执行？
   - A. 无论是否异常都执行
   - B. 只在发生异常时执行
   - C. 只在没有异常时执行
   - D. 在 finally 之后执行

5. `class Dog(Animal):` 表示？
   - A. Dog 是 Animal 的父类
   - B. Dog 继承了 Animal
   - C. Dog 和 Animal 没有关系
   - D. Animal 是一个方法

<details>
<summary>查看答案</summary>

1. B — 切片 `[1:4]` 取索引 1,2,3 → `yth`
2. B — `.items()` 返回 (key, value) 元组
3. B — `with` 是上下文管理器，确保文件自动关闭
4. C — `else` 在无异常时执行
5. B — 括号内是父类，Dog 继承 Animal

</details>

## 回顾章节链接

遇到不熟悉的主题，可回到对应章节复习：

- [变量与表达式](./expression.md)
- [基础数据类型](./datatype.md)
- [流程控制](./control-flow.md)
- [循环结构](./loops.md)
- [函数基础](./functions.md)
- [列表与字典](./list-dict.md)
- [文件操作](./file-io.md)
- [异常处理](./exception.md)
- [模块与包](./modules-packages.md)
- [面向对象编程](./oop.md)
- [字符串高级处理](./string-advanced.md)

祝学习顺利！进入进阶部分后，你会接触到异步编程、Web 框架、数据库等更强大的内容。
