# 数据库操作 (Database Operations)

## 导语

在现代 Web 应用中，数据几乎总是持久化存储在数据库中。无论是电商平台的商品库存、社交网络的用户关系，还是博客系统的文章档案，都离不开数据库的支撑。Python 提供了多种数据库交互方式：标准库内置的 `sqlite3` 适合轻量级场景和开发测试，而 `PyMySQL` 等第三方库则用于连接 MySQL 等生产级数据库。掌握数据库操作，意味着你的程序不再只是"一次性脚本"，而是能够存储、查询和管理真实数据的应用。

## 学习目标

- 掌握 SQLite 内存数据库的基本操作（建表、插入、查询、更新、删除）
- 理解 PyMySQL 连接 MySQL 数据库的完整流程与错误处理
- 学会使用参数化查询防止 SQL 注入攻击

## 概念介绍

数据库是结构化存储数据的系统。Python 与数据库交互的核心模式可以用"连接 → 游标 → 执行 → 获取"四个步骤概括：

1. **连接（Connection）** — 建立程序与数据库之间的通信通道。每个数据库驱动（如 `sqlite3`、`pymysql`）都有自己的连接函数，需要传入连接参数（主机、端口、用户名、密码、数据库名）。
2. **游标（Cursor）** — 连接创建后，通过 `cursor()` 获取游标对象。游标是执行 SQL 语句的"句柄"，所有 SQL 操作都通过游标的 `execute()` 方法完成。
3. **执行（Execute）** — 游标的 `execute()` 方法接受 SQL 字符串和参数元组，发送给数据库执行。对于修改数据的操作（INSERT/UPDATE/DELETE），还需要调用连接的 `commit()` 来提交事务。
4. **获取（Fetch）** — 对于查询操作（SELECT），用 `fetchone()` 获取一行、`fetchmany(n)` 获取 n 行、`fetchall()` 获取所有结果。

> [!NOTE]
> **SQLite vs MySQL**：SQLite 是嵌入式数据库，数据存储在单一文件中（或内存中），不需要额外服务器，非常适合原型开发和测试。MySQL 是独立的数据库服务器，支持多用户并发访问，是生产环境的常见选择。

## 代码示例

### 示例 1：SQLite 内存数据库 — 完整的 CRUD 操作

```python
import sqlite3

# 使用内存数据库（不需要磁盘文件，适合学习和测试）
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 创建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
""")

# 插入数据（使用参数化查询 ? 占位符）
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
    ("John Doe", "IT", 75000.00),
)
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
    ("Jane Smith", "HR", 65000.00),
)
conn.commit()  # 提交事务

# 查询全部
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: {row[3]}")

# 条件查询
cursor.execute("SELECT name, salary FROM employees WHERE salary > ?", (70000,))
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Salary: {row[1]}")

conn.close()
```

SQLite 使用 `?` 作为参数占位符。`fetchall()` 返回元组列表，每个元组代表一行数据，通过索引 `row[0]`、`row[1]` 访问列值。记住修改数据后调用 `conn.commit()`，否则更改不会生效。

> [!TIP]
> 使用 `with sqlite3.connect(...) as conn:` 上下文管理器可以自动处理事务提交和回滚，代码更简洁安全。

### 示例 2：PyMySQL 连接 MySQL 数据库

```python
import pymysql

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "test_db",
}

def connect_sample():
    """连接 MySQL 并获取数据库版本信息。"""
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print(f"Database version: {data}")
        cursor.close()
        db.close()
    except pymysql.Error as e:
        print(f"MySQL connection failed: {e}")

# 查询示例
def query_sample():
    """执行基本 SQL 操作。"""
    try:
        db = pymysql.connect(**DB_CONFIG)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM demo")
        rows = cursor.fetchall()
        for row in rows:
            print(f"row: {row}")
        cursor.close()
        db.close()
    except pymysql.Error as e:
        print(f"Query failed: {e}")
```

PyMySQL 使用方式与 `sqlite3` 类似：连接 → 游标 → 执行 → 获取。主要区别在于 PyMySQL 需要配置服务器连接参数（host、port、user 等），并且异常类型是 `pymysql.Error`。生产环境中应始终使用 try-except 包裹数据库操作。

> [!WARNING]
> 生产环境中不要把数据库密码硬编码在代码里！应该使用环境变量或配置文件：`os.environ.get("DB_PASSWORD")`。

### 示例 3：参数化查询 — 防止 SQL 注入

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

# ❌ 危险的拼接方式
user_input = "Alice'; DROP TABLE users; --"
# cursor.execute(f"INSERT INTO users (name) VALUES ('{user_input}')")  # 会删除整张表！

# ✅ 安全的参数化查询
cursor.execute("INSERT INTO users (name) VALUES (?)", (user_input,))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # [('Alice\'; DROP TABLE users; --',)] — 安全地作为数据存储

conn.close()
```

**永远不要**用 Python 字符串拼接（f-string、`%`、`+`）构建 SQL 语句。参数化查询将 SQL 模板和数据分开传输给数据库，数据库引擎会将参数值视为**纯数据**而非 SQL 命令的一部分，从根本上杜绝 SQL 注入。

> [!WARNING]
> **SQL 注入攻击**是最常见的 Web 安全漏洞之一。攻击者通过在输入中注入恶意 SQL 片段，可以读取、修改或删除数据库中的任何数据。参数化查询是唯一可靠的防御方式。

## 常见错误与解决

> [!WARNING]
> **错误 1：忘记 `commit()` 导致数据丢失**
>
> ```python
> cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
> # 忘记调用 conn.commit()
> cursor.execute("SELECT * FROM users")
> print(cursor.fetchall())  # [] — 查不到刚插入的数据！
> ```
>
> **原因**：SQLite 和 PyMySQL 默认开启事务模式，所有修改操作（INSERT/UPDATE/DELETE）都需要显式 `commit()` 才能持久化。
>
> **解决**：在每个修改操作后调用 `conn.commit()`，或使用上下文管理器 `with` 语句。

> [!WARNING]
> **错误 2：单参数元组忘记加逗号**
>
> ```python
> cursor.execute("SELECT * FROM users WHERE id = ?", (1))  # 💥 (1) 是整数 1，不是元组！
> # 应该写成：
> cursor.execute("SELECT * FROM users WHERE id = ?", (1,))  # ✅ 注意末尾的逗号
> ```
>
> **原因**：Python 中 `(1)` 等价于 `1`（括号只是数学分组），`(1,)` 才是包含一个元素的元组。
>
> **解决**：单个参数时务必在末尾加逗号。

## 最佳实践

1. **始终使用参数化查询** — 所有用户输入、外部数据都通过 `?` 或 `%s` 占位符传入，绝不用字符串拼接构建 SQL
2. **使用上下文管理器（`with`）** — `with sqlite3.connect(...) as conn:` 自动处理提交/回滚和连接关闭，避免资源泄漏

## 练习

1. 使用 SQLite 创建一个 `books` 表（字段：id、title、author、year），插入至少 3 本书，然后查询所有 2000 年以后出版的书籍。

<details>
<summary>查看答案</summary>

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER
    )
""")

books = [
    ("Python 编程从入门到精通", "张三", 2018),
    ("流畅的Python", "Luciano Ramalho", 2016),
    ("Effective Python", "Brett Slatkin", 2019),
]

for title, author, year in books:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year),
    )
conn.commit()

cursor.execute("SELECT * FROM books WHERE year > ?", (2000,))
for row in cursor.fetchall():
    print(row)

conn.close()
```

</details>

2. 编写一个函数 `search_user(cursor, name)`，使用参数化查询安全地搜索用户名中包含指定关键字的用户。

<details>
<summary>查看答案</summary>

```python
def search_user(cursor, name):
    """使用 LIKE 进行模糊查询，参数化防止注入。"""
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{name}%",))
    return cursor.fetchall()

# 使用示例
# results = search_user(cursor, "Al")  # 查找名字中包含 "Al" 的用户
```

</details>

## 知识检查

1. SQLite 中 `fetchone()` 的返回值类型是？
    - A. 列表
    - B. 字典
    - C. 元组
    - D. 字符串

2. 防止 SQL 注入的正确方式是？
    - A. 使用字符串格式化（f-string）
    - B. 对用户输入进行 HTML 转义
    - C. 使用参数化查询（占位符）
    - D. 限制输入长度

3. 以下哪个 SQL 操作不需要 `commit()`？
    - A. `INSERT`
    - B. `UPDATE`
    - C. `DELETE`
    - D. `SELECT`

<details>
<summary>查看答案</summary>

1. C — `fetchone()` 返回单个元组，代表一行数据
2. C — 参数化查询将 SQL 和数据分开传输，是防御 SQL 注入的唯一可靠方式
3. D — `SELECT` 是只读操作，不会修改数据，不需要 commit

</details>

## 本章小结

- 数据库操作遵循"连接 → 游标 → 执行 → 获取"的标准模式
- SQLite 无需服务器，适合学习和原型开发；MySQL 适合生产环境
- 修改数据后必须 `commit()` 才能持久化
- 参数化查询（`?` 或 `%s` 占位符）是防止 SQL 注入的唯一可靠方式
- 使用上下文管理器 `with` 可以自动管理事务和连接资源

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| database | 数据库 | 结构化存储和检索数据的系统 |
| connection | 数据库连接 | 程序与数据库之间的通信通道 |
| cursor | 游标 | 用于执行 SQL 语句和获取结果的对象 |
| parameterized query | 参数化查询 | 使用占位符传递参数，而非字符串拼接的查询方式 |
| SQL injection | SQL 注入 | 通过构造恶意输入篡改 SQL 语句的攻击方式 |

## 下一步

- [JSON 数据处理](./json.md) → 学习如何在 Python 中序列化/反序列化 JSON 数据

## 源码链接

- [database_sample.py (PyMySQL)](https://github.com/savechina/hello-python/blob/main/hello_python/advance/database_sample.py)
- [database_sqlite_sample.py (SQLite)](https://github.com/savechina/hello-python/blob/main/hello_python/advance/database_sqlite_sample.py)
