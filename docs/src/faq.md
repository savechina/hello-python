# 常见问题 FAQ

本页面收集 Python 学习过程中最常见的问题。如果你有其他问题，欢迎[提交 Issue](https://github.com/savechina/hello-python/issues)。

## 入门相关

### Python 适合用来做什么？

Python 是一门通用编程语言，特别适合以下场景：
- **Web 后端开发**：FastAPI、Django、Flask 等框架
- **数据科学与 AI**：NumPy、Pandas、PyTorch、TensorFlow
- **自动化脚本**：文件处理、网络爬虫、系统管理
- **CLI 工具**：使用 Click 或 Typer 构建命令行工具

### Python 难学吗？

Python 以"语法简洁、接近自然语言"著称，是公认最适合初学者的语言之一。
- **优势**：无需手动管理内存，类型动态推断，生态系统丰富
- **挑战**：动态类型可能导致运行时错误（可通过类型提示缓解）

### 我应该学 Python 2 还是 Python 3？

**永远选择 Python 3**。Python 2 已于 2020 年停止维护。本教程基于 Python 3.10+ 编写。

---

## 环境与工具

### `uv` 和 `pip` 有什么区别？

| 特性 | `uv` | `pip` |
|------|------|-------|
| 速度 | 极快（Rust 编写，10-100x 提升） | 较慢 |
| 虚拟环境 | 内置管理 | 需配合 `venv` |
| 依赖解析 | 全局缓存，智能解析 | 每次重新解析 |
| 推荐场景 | 现代 Python 项目首选 | 遗留项目兼容 |

### 如何检查 Python 版本？

```bash
python --version
# 或
python3 --version
```

### 为什么推荐用 `uv` 而不是 `pip`？

`uv` 是新一代 Python 包管理器，解决了 `pip` + `venv` + `pip-tools` 的碎片化问题。
- 一条命令完成：`uv sync` = 创建虚拟环境 + 安装依赖
- 兼容 `pyproject.toml` 标准
- 速度更快，磁盘占用更小

---

## 代码与语法

### `list` 和 `tuple` 有什么区别？

- **list (`[]`)**：可变，可添加/删除/修改元素
- **tuple (`()`)**：不可变，创建后不能修改，适合存储固定数据

### 什么是"Pythonic"代码？

"Pythonic"指符合 Python 设计哲学的代码风格：
- 使用列表推导式而非循环
- 使用 `with` 管理资源
- 使用 `enumerate` 替代 `range(len())`
- 遵循 PEP 8 命名规范

### 如何处理中文编码问题？

Python 3 默认使用 UTF-8。如果读写文件时遇到乱码：
```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 进阶问题

### 什么时候用异步编程？

- **适合**：大量 I/O 操作（网络请求、数据库查询、文件读写）
- **不适合**：CPU 密集型任务（数学计算、图像处理）— 应使用多线程/多进程

### `*args` 和 `**kwargs` 是什么？

- `*args`：接收任意数量的位置参数，打包为元组
- `**kwargs`：接收任意数量的关键字参数，打包为字典

### 类型提示会影响运行性能吗？

**不会**。类型提示在运行时被忽略，仅用于静态检查（如 `mypy`）和 IDE 提示。

---

## 下一步

- 回到[教程首页](./about-hello.md)
- 查看[学习路径](./learning_path.md)
- 在[GitHub](https://github.com/savechina/hello-python)上报告问题
