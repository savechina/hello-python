# Getting Started

## 安装 Python

首先，你需要安装 Python。Hello Python 项目使用 Python 3.10+ 开发（推荐 3.13+）。

### macOS

使用 Homebrew 安装：

```bash
$ brew install python@3.13
$ python3 --version
Python 3.13.x
```

### Linux

使用系统包管理器安装：

```bash
# Ubuntu/Debian
$ sudo apt-get install python3 python3-pip python3-venv

# CentOS/RHEL
$ sudo yum install python3 python3-pip
```

### Windows

从 [Python 官方网站](https://www.python.org/downloads/) 下载并安装。安装时记得勾选 "Add Python to PATH"。

## 安装 uv 包管理器

Hello Python 使用 [uv](https://github.com/astral-sh/uv) 作为包管理器，它比 pip + venv 更快更简洁。

```bash
# 安装 uv
$ curl -LsSf https://astral.sh/uv/install.sh | sh

# 验证安装
$ uv --version
uv x.x.x
```

## 克隆项目

```bash
$ git clone https://github.com/savechina/hello-python.git
$ cd hello-python
```

## 安装依赖

```bash
# 同步项目依赖
$ uv sync

# 验证 Python 版本
$ python --version
Python 3.13.x
```

## 运行示例

```bash
# 运行任意示例文件
$ python -m hello_python.basic.datatype_sample
$ python -m hello_python.advance.json_sample

# 或通过 CLI 入口
$ uv run hello greet "World"
```

## 运行测试

```bash
# 运行所有基础教程测试
$ uv run pytest tests/basic/ -s -v

# 运行特定模块测试
$ uv run pytest tests/basic/test_datatype_sample.py -s -v
```

## Lint 和格式化

```bash
# 代码检查
$ uv run ruff check .

# 代码格式化
$ uv run ruff format .
```

## 构建文档

Hello Python 使用 mdBook 构建文档。你可以本地预览教程：

```bash
# 构建文档
$ mdbook build docs

# 本地启动文档服务
$ mdbook serve docs
```

文档将在 `http://localhost:3000` 打开。

## 项目结构

```
hello-python/
├── hello_python/        # 教程源码
│   ├── basic/           # 基础教程（变量、数据类型、循环、函数…）
│   ├── advance/         # 进阶教程（异步、FastAPI、数据库、NumPy…）
│   ├── cli/             # Click CLI 入口
│   ├── algo/            # 算法示例
│   └── leetcode/        # LeetCode 解题
├── tests/               # 测试代码（镜像 hello_python 结构）
├── docs/                # mdBook 文档
│   └── src/             # 文档源文件
│       ├── basic/       # 基础教程章节
│       └── advance/     # 进阶教程章节
├── pyproject.toml       # 项目配置和依赖
└── Makefile             # 快捷命令
```

## 运行 Makefile 快捷命令

```bash
$ make install   # uv sync
$ make test      # pytest -s -v
$ make lint      # ruff check .
$ make format    # ruff format .
$ make build     # uv build
```

## 下一步

完成环境配置后，你可以进入 [介绍](introduction.md) 了解更多关于 Python 的信息，或者直接开始 [基础入门](basic/basic-overview.md) 的学习之旅。
