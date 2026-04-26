# tests

**Purpose:** Test suite mirroring `hello_python/` structure. Mirrors source organization.

## STRUCTURE
```
tests/
├── test_sample.py           # Root-level sample (string operations)
├── basic/
│   ├── test_datatype_sample.py
│   └── test_expression_sample.py
├── advance/
│   ├── test_asyncs_sample.py
│   ├── test_injector_sample.py
│   └── test_numpy_sample.py
├── cli/
│   └── test_cli.py          # Click CLI tests with CliRunner + mock
└── advance/ and basic/      # Mirror hello_python/ subdirs
```

## WHERE TO LOOK
| Testing | File |
|---------|------|
| Basic module tests | `basic/test_*.py` |
| Async/DI/NumPy tests | `advance/test_*.py` |
| CLI tests | `cli/test_cli.py` (uses `CliRunner` + `patch`) |
| Sample test structure | `test_sample.py` (root-level) |

## CONVENTIONS
- **Framework**: `unittest.TestCase` (NOT pytest-style functions)
- **Test class naming**: `Test<Module>Sample` pattern
- **Test file naming**: `test_<module>_sample.py`
- **No conftest.py** — no shared fixtures
- **No pytest markers** — no `@pytest.mark.*` categorization
- Run via: `uv run pytest -s -v` or `uv run pytest tests/basic/`
- Tests use `if __name__ == "__main__": unittest.main()` for standalone execution

## ANTI-PATTERNS
- Many tests lack assertions — print-only verification ("tests that don't test")
- `try: ... except Exception: pass` silently swallows failures (e.g., in test_asyncs_sample.py)
- Test class name typo: `TestExpressioneSample` (extra 'e')
- No shared fixtures — each test case self-contained with duplicated setup
- Mix of `unittest` assertions and direct function calls without checking results
- CLI tests invoke commands but don't always assert on output
