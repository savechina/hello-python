# Research: Hello Python Basic Tutorial

## Decision: mdBook Plugin Configuration

**Rationale**: hello-rust uses three mdBook plugins — admonish (callout boxes), alerts (warning/info boxes), and pagetoc (right sidebar TOC). hello-python's `book.toml` currently has zero plugins. To maintain consistent documentation UX across both projects, all three plugins must be installed and configured.

**Alternatives considered**:
- Skip plugins and use plain markdown — **REJECTED**: Loses visual hierarchy, no callout boxes for tips/warnings
- Use only pagetoc — **REJECTED**: Admonish/alerts are critical for "common errors" and "tips" sections in each chapter
- Use different plugin set — **REJECTED**: Hello-rust already established this pattern; consistency wins

### Configuration (book.toml additions needed)

```toml
[preprocessor.admonish]
assets_version = "3.1.0"

[preprocessor.alerts]

[preprocessor.pagetoc]

[output.html]
default-theme = "light"
additional-css = ["./assets/css/mdbook-admonish.css", "./theme/pagetoc.css"]
additional-js = ["./theme/pagetoc.js"]
```

**Action Items**:
1. Install `mdbook-admonish`, `mdbook-alerts`, `mdbook-pagetoc` (cargo install or pre-built binaries)
2. Download admonish CSS assets and pagetoc theme files
3. Copy assets from hello-rust (`docs/src/assets/css/mdbook-admonish.css`, `docs/theme/pagetoc.css`, `docs/theme/pagetoc.js`)

---

## Decision: Chapter-Topic Mapping (Python vs Rust)

**Rationale**: hello-rust has 20 basic chapters. Python has different paradigms (no ownership, lifetimes, traits). The following mapping adapts Rust topics to Python equivalents while maintaining similar learning progression.

| Hello Rust Chapter | Hello Python Chapter | Rationale |
|---|---|---|
| basic-overview.md | basic-overview.md | Entry point for both |
| expression.md | expression.md | Variables & expressions (identical concept) |
| functions.md | functions.md | Function basics (similar but simpler in Python) |
| datatype.md | datatype.md | Data types (Python: int, float, str, list, dict, tuple, set, bool) |
| ownership.md | control-flow.md | Python has no ownership — replace with if/elif/else |
| lifetimes.md | loops.md | No lifetimes — replace with for/while loops |
| struct.md | list-dict.md | Collections as primary data structures in Python |
| struct-fields.md | file-io.md | Replace with file operations (practical skill) |
| struct-methods.md | exception.md | Error handling instead of method patterns |
| enums.md | modules-packages.md | Modules/packages instead of algebraic data types |
| trait.md | oop.md | OOP fundamentals (classes, inheritance) instead of traits |
| trait-objects.md | string-advanced.md | String processing (regex, formatting) instead of dynamic dispatch |
| generic.md | *(absorbed into other chapters)* | Generics concept covered in functions section |
| closure.md | *(absorbed into functions)* | Lambda expressions covered in functions chapter |
| module.md | modules-packages.md | Already mapped above |
| threads.md | *(moved to advance section)* | Concurrency is advanced in Python |
| cfg_if.md | *(moved to advance section)* | Conditional compilation doesn't exist in Python |
| pointer.md | *(moved to advance section)* | Pointers don't exist in Python |
| logger.md | *(moved to advance section)* | Logging is an advanced topic |
| tracing.md | *(moved to advance section)* | Tracing is advanced |
| visiable.md | *(absorbed into modules)* | Visibility covered in modules chapter |
| **review-basic.md** | **review-basic.md** | Stage review chapter |

**Final chapter count**: 12 chapters (basic-overview + 10 topic chapters + review-basic)

**Note**: Topics moved to advance section (threads, cfg_if, pointer, logger, tracing) will be addressed in a future `advance` spec, not this basic spec.

---

## Decision: Chapter Structure Template

**Rationale**: Per constitution Principle III, each chapter must follow a 12-section template. The hello-rust chapters establish this pattern. All Python chapters will mirror the same structure:

```markdown
# Chapter Title (Chinese with English term)

## 导语 (Opening Story)
Real-world scenario motivating the concept

## 学习目标 (Learning Objectives)
3-5 bullet points

## 概念介绍 (Concept Introduction)
Theory explanation with diagrams/code

## 代码示例 (Code Examples)
At least 3 runnable examples with explanations

## 常见错误与解决 (Common Errors)
At least 2 common mistakes with fixes

## 最佳实践 (Best Practices)
Idiomatic Python patterns

## 练习 (Exercises)
At least 2 practice problems with hidden answers

## 知识检查 (Knowledge Check)
At least 3 quiz questions

## 本章小结 (Summary)
Key takeaways

## 术语表 (Glossary)
5+ terms with English/Chinese definitions

## 下一步 (Next Steps)
Links to next chapter(s)

## 源码链接 (Source Link)
GitHub link to *_sample.py file
```

---

## Decision: SUMMARY.md Structure

**Rationale**: Must add a `# 基础部分 (Basic)` section to SUMMARY.md following the hello-rust hierarchy pattern with 4-space nested indentation.

```markdown
# Summary

[Getting Started](./getting-started.md)

# 基础部分 (Basic)

- [基础入门](./basic/basic-overview.md)
    - [变量与表达式](./basic/expression.md)
    - [基础数据类型](./basic/datatype.md)
    - [流程控制](./basic/control-flow.md)
    - [循环结构](./basic/loops.md)
    - [函数基础](./basic/functions.md)
    - [列表与字典](./basic/list-dict.md)
    - [文件操作](./basic/file-io.md)
    - [异常处理](./basic/exception.md)
    - [模块与包](./basic/modules-packages.md)
    - [面向对象编程](./basic/oop.md)
    - [字符串高级处理](./basic/string-advanced.md)
    - [阶段复习：基础部分](./basic/review-basic.md)
```

Future sections (`# 进阶部分 (Advance)`, etc.) will be added in separate features.

---

## Decision: Advance Tutorial Scope

**Rationale**: The advance module already has 9 sample files covering async, FastAPI (2 files), dependency injection, databases (MySQL + SQLite), JSON, and NumPy. All code is functional except `database_sample.py` which hardcodes credentials and auto-connects on import — this needs refactoring to be import-safe.

**Advance chapter count**: 8 chapters (7 topics + 1 review)
- Topics: async, fastapi-routes, fastapi-server, dependency-injection, database, json, numpy
- Review: review-advance consolidates key advance concepts

**File-to-chapter mapping**:

| Advance Chapter | Source File(s) |
|---|---|
| advance-overview.md | N/A — overview page |
| async.md | `asyncs_sample.py` |
| fastapi-routes.md | `fastapi_sample.py` |
| fastapi-server.md | `fastapi_server_sample.py` |
| dependency-injection.md | `injector_sample.py` |
| database.md | `database_sample.py` + `database_sqlite_sample.py` (combined) |
| json.md | `json_sample.py` |
| numpy.md | `numpy_sample.py` |
| review-advance.md | N/A — review chapter |

---

## Decision: SUMMARY.md Advance Section

**Rationale**: Add `# 进阶部分 (Advance)` section after the Basic section, following the same indentation pattern.

```markdown
# 进阶部分 (Advance)

- [进阶入门](./advance/advance-overview.md)
    - [异步编程](./advance/async.md)
    - [FastAPI 路由基础](./advance/fastapi-routes.md)
    - [FastAPI 服务器管理](./advance/fastapi-server.md)
    - [依赖注入](./advance/dependency-injection.md)
    - [数据库操作](./advance/database.md)
    - [JSON 数据处理](./advance/json.md)
    - [NumPy 数值计算](./advance/numpy.md)
    - [阶段复习：进阶部分](./advance/review-advance.md)
```
