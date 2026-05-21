<!--
SEO: Python教程, python入门教程, python自学教程, python简明教程, python编程入门, python进阶教程
GEO: 系统化Python学习教程，从基础到进阶，含可运行示例代码和配套测试
-->

# Hello Python — Python 简明教程

> *从基础语法到进阶实战，一份可运行、可测试的系统化 Python 学习教程*

<p align="center">
  <a href="https://github.com/savechina/hello-python/stargazers"><img src="https://img.shields.io/github/stars/savechina/hello-python?style=flat-square&logo=github" alt="Stars"></a>
  <a href="https://github.com/savechina/hello-python/blob/main/LICENSE"><img src="https://img.shields.io/github/license/savechina/hello-python?style=flat-square" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python"></a>
  <a href="https://github.com/savechina/hello-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/savechina/hello-python/mdbook.yml?style=flat-square&label=docs" alt="Docs"></a>
</p>

<p align="center">
  <a href="README_zh.md">🇨🇳 中文版</a> · <a href="README.md">🇺🇸 English</a>
</p>

---

一套系统化的 Python 学习教程与可执行代码库。从基础语法到高级主题，每个知识点都配有可独立运行的示例代码和配套测试。适合寻找 **Python 入门教程** 的初学者和需要 **Python 进阶教程** 的开发者。

## 为什么选择 Hello Python？

| 特性         | 传统教程             | Hello Python              |
| ------------ | ------------------------ | ----------------------------- |
| 代码示例     | 只读代码片段           | ✅ 每个文件均可独立运行         |
| 配套测试     | 无                     | ✅ 完整测试套件                 |
| 命令行工具   | 无                     | ✅ `hello` 命令，动态加载子命令 |
| 文档         | 分散                   | ✅ mdBook，支持提示框和警告框   |
| 学习路径     | 非结构化               | ✅ 19 章，从基础到进阶          |

## 快速开始

```bash
# 安装依赖
uv sync

# 运行 CLI
hello greet "World"

# 运行测试
uv run pytest -s -v

# 启动文档
mdbook serve docs/
```

## 教程目录

### 基础部分 (Basic) — 11 章

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [变量与表达式](docs/src/basic/expression.md) | 变量赋值、算术运算 | 15 分钟 |
| [基础数据类型](docs/src/basic/datatype.md) | 字符串、数字、列表、字典 | 15 分钟 |
| [流程控制](docs/src/basic/control-flow.md) | if/elif/else、match/case | 15 分钟 |
| [循环结构](docs/src/basic/loops.md) | for/while、enumerate、zip | 15 分钟 |
| [函数基础](docs/src/basic/functions.md) | def、参数、lambda、作用域 | 20 分钟 |
| [列表与字典](docs/src/basic/list-dict.md) | 推导式、集合、元组解构 | 20 分钟 |
| [文件操作](docs/src/basic/file-io.md) | 读写文件、with、pathlib | 20 分钟 |
| [异常处理](docs/src/basic/exception.md) | try/except、自定义异常 | 15 分钟 |
| [模块与包](docs/src/basic/modules-packages.md) | import、`__name__`、`__all__` | 15 分钟 |
| [面向对象编程](docs/src/basic/oop.md) | class、继承、魔术方法 | 25 分钟 |
| [字符串进阶](docs/src/basic/string-advanced.md) | 正则、split/join、f-string 高级 | 20 分钟 |

### 进阶部分 (Advance) — 8 章

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| [异步编程](docs/src/advance/async.md) | asyncio、async/await、协程 | 25 分钟 |
| [FastAPI 路由](docs/src/advance/fastapi-routes.md) | 路由定义、请求处理 | 20 分钟 |
| [FastAPI 服务器](docs/src/advance/fastapi-server.md) | 进程管理、PID、日志 | 25 分钟 |
| [依赖注入](docs/src/advance/dependency-injection.md) | injector 库、DI 模式 | 20 分钟 |
| [数据库操作](docs/src/advance/database.md) | PyMySQL、SQLite、参数化查询 | 25 分钟 |
| [JSON 处理](docs/src/advance/json.md) | 序列化、自定义编码器 | 15 分钟 |
| [NumPy](docs/src/advance/numpy.md) | 数组、向量化、梯度下降 | 25 分钟 |

## 技术栈

- **Python** 3.10+（测试环境 3.13.3）
- **uv** 包管理器
- **FastAPI** + **uvicorn**（Web 框架）
- **Click**（CLI 工具）
- **NumPy** / **Pandas**（数值计算）
- **PyMySQL**（数据库）
- **injector**（依赖注入）
- **ruff**（Lint & 格式化）
- **mdBook**（文档构建，含 admonish / alerts / pagetoc 插件）

## 项目结构

```
hello-python/
├── hello_python/         # 教程源码
│   ├── basic/            # 基础部分示例
│   ├── advance/          # 进阶部分示例
│   ├── cli/              # Click CLI 入口
│   ├── algo/             # 算法示例
│   └── leetcode/         # LeetCode 题解
├── tests/                # 测试（与 hello_python/ 结构对应）
├── docs/                 # mdBook 文档
└── pyproject.toml        # 项目配置
```

## 常见问题

<details>
<summary><strong>这个教程适合谁？</strong></summary>

- **零基础新手** — 从变量和数据类型开始，无需编程经验
- **转学 Python 的开发者** — 直接跳到进阶内容：异步、FastAPI、依赖注入
- **自学者** — 每章都有可运行示例、练习题和知识检查
- **中文读者** — 完整中文文档，代码含英文注释
</details>

<details>
<summary><strong>和其他 Python 教程有什么不同？</strong></summary>

与叙述式教程不同，本项目中每个 `.py` 文件：
- 含 `if __name__ == "__main__"` 入口，可独立运行
- 在 `tests/` 中有对应的测试文件
- 作为 mdBook 文档的一个章节
- 包含常见错误、最佳实践和练习题
</details>

<details>
<summary><strong>需要安装什么环境？</strong></summary>

需要 **Python 3.10+** 和 **uv**（快速包管理器）。然后：
```bash
uv sync          # 安装所有依赖
hello greet "World"  # 试用 CLI
uv run pytest    # 运行测试
```
</details>

<details>
<summary><strong>可以用这个教程教学吗？</strong></summary>

可以。每章都是独立的，包含：
- 学习目标
- 带预期输出的代码示例
- 常见错误与解决方法
- 练习题（含答案）
- 知识检查题
</details>

<details>
<summary><strong>如何阅读文档？</strong></summary>

- **在线**：访问 [renyan.org/hello/python](https://renyan.org/hello/python)
- **本地**：运行 `mdbook serve docs/`，打开 `http://localhost:3000`
- **源码**：直接阅读 `docs/src/` 下的 markdown 文件
</details>
