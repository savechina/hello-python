# hello_python Package

**Purpose:** Main source package. Tutorial modules organized by difficulty level.

## STRUCTURE
```
hello_python/
├── basic/       # Foundational Python: datatypes, expressions
├── advance/     # Advanced topics: async, FastAPI, DI, numpy, DB, JSON
├── cli/         # Click CLI: entry point + dynamically loaded commands
├── algo/        # Algorithm examples
├── leetcode/    # LeetCode solutions
└── utils/       # Shared utilities
```

## WHERE TO LOOK
| Need | File |
|------|------|
| Basic Python tutorials | `basic/*.py` |
| Advanced patterns | `advance/*.py` |
| Add CLI subcommand | `cli/commands/*.py` |
| Logging config | `__init__.py` (root-level logging.basicConfig) |

## CONVENTIONS
- Tutorial modules named `<topic>_sample.py`
- Subpackages have EMPTY `__init__.py` — import via full paths (e.g., `from hello_python.advance import asyncs_sample`)
- No `__all__` exports defined anywhere
- Root `__init__.py` configures logging → file output to `hello.log`
- Each sample file is runnable standalone

## ANTI-PATTERNS
- Typo in file: `fastapi_server_sample.py` vs `fastapi_sample.py` — two separate FastAPI files
- No package-level re-exports — every module requires full import path
