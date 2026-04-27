# Contract: Chapter Document Structure

Every tutorial chapter under `docs/src/basic/` and `docs/src/advance/` MUST conform to this contract.

## Chapter File Contract

**Location**: `docs/src/basic/<chapter-slug>.md` or `docs/src/advance/<chapter-slug>.md`
**Format**: Markdown compatible with mdBook 0.4.52+

### Required Sections (all 12 mandatory)

| # | Section | Header | Min Content |
|---|---|---|---|
| 1 | Opening Story | `## 导语` | ≥100 Chinese characters, real-world scenario |
| 2 | Learning Objectives | `## 学习目标` | ≥3 bullet points |
| 3 | Concept Introduction | `## 概念介绍` | ≥200 Chinese characters |
| 4 | Code Examples | `## 代码示例` | ≥3 code blocks, each with explanation |
| 5 | Common Errors | `## 常见错误与解决` | ≥2 error patterns with fixes |
| 6 | Best Practices | `## 最佳实践` | ≥2 idiomatic patterns |
| 7 | Exercises | `## 练习` | ≥2 problems with hidden answers |
| 8 | Knowledge Check | `## 知识检查` | ≥3 quiz questions (A/B/C/D) |
| 9 | Summary | `## 本章小结` | ≥5 key takeaways |
| 10 | Glossary | `## 术语表` | ≥5 terms (English + Chinese) |
| 11 | Next Steps | `## 下一步` | Link to next chapter |
| 12 | Source Link | `## 源码链接` | GitHub link to `*_sample.py` |

### Code Block Contract

```python
# Language tag MUST be "python"
# Each block MUST be runnable from the corresponding *_sample.py file
# Each block MUST include a comment or text explaining what it does
```

### Answer Hiding Contract

Answers for exercises and quizzes MUST use mdBook details/collapsible syntax:

```markdown
<details>
<summary>查看答案</summary>

Answer content here.

</details>
```

### Link Contract

- Internal chapter links: relative paths from current file to target (e.g., `./loops.md`)
- GitHub source links: full HTTPS URL to `hello_python/basic/<file>_sample.py`
- SUMMARY.md links: `./basic/<chapter-slug>.md`

---

# Contract: Sample File Structure

Every `*_sample.py` in `hello_python/basic/` MUST conform to this contract.

**Location**: `hello_python/basic/<topic>_sample.py`
**Naming**: `<topic>` matches chapter slug (e.g., `control_flow_sample.py`)

### Required Elements

1. **Module docstring** at top of file (triple-quote) describing the topic
2. **Standalone functions** (not classes) demonstrating the concept
3. **`if __name__ == "__main__":`** block calling all sample functions
4. **No bare `except`** — all exception handlers must catch specific exceptions
5. **Print statements** must use f-strings or `.format()` (no `%` operator)

### Sample File Template

```python
"""
<Topic ZH/EN> Sample.
Brief description of what this module demonstrates.
"""


def example_one():
    """Docstring explaining this example."""
    # code here
    print(f"output: {result}")


if __name__ == "__main__":
    example_one()
    # call more examples...
```

---

# Contract: Test File Structure

Every `test_*_sample.py` in `tests/basic/` MUST conform to this contract.

**Location**: `tests/basic/test_<topic>_sample.py`
**Naming**: `Test<Topic>Sample` (title case, no typo)

### Required Elements

1. **unittest.TestCase** class (not pytest-style)
2. **One test method** per function in the corresponding sample file
3. **Assertion** — test must verify actual behavior (not just print)
4. **`if __name__ == "__main__":`** block with `unittest.main()`

### Test File Template

```python
import unittest
from io import StringIO
import sys
from hello_python.basic import <topic>_sample


class Test<CapTopic>Sample(unittest.TestCase):
    def test_<function_name>(self):
        captured = StringIO()
        sys.stdout = captured
        <topic>_sample.<function_name>()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("<expected substring>", output)


if __name__ == "__main__":
    unittest.main()
```
