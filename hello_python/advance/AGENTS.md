# hello_python.advance

**Purpose:** Advanced Python concepts — async, FastAPI, dependency injection, numpy, database, JSON. Largest module (9 files, ~800+ lines total).

## STRUCTURE
```
advance/
├── asyncs_sample.py           # asyncio, async/await, scheduler
├── fastapi_sample.py          # FastAPI basic app (125 lines)
├── fastapi_server_sample.py   # FastAPI server with more features (332 lines)
├── injector_sample.py         # Dependency injection with injector (109 lines)
├── database_sample.py         # PyMySQL database operations
├── database_sqlite_sample.py  # SQLite operations (73 lines)
├── json_sample.py             # JSON processing (156 lines)
└── numpy_sample.py            # NumPy + gradient descent
```

## WHERE TO LOOK
| Feature | File |
|---------|------|
| Async/await patterns | `asyncs_sample.py` |
| Web API | `fastapi_*.py` (two files — pick simpler or full) |
| Dependency injection | `injector_sample.py` |
| SQL (MySQL) | `database_sample.py` |
| SQL (SQLite) | `database_sqlite_sample.py` |
| JSON handling | `json_sample.py` |
| Math/ML basics | `numpy_sample.py` |

## CONVENTIONS
- Each file is self-contained: runnable as `python advance/<file>.py`
- Async code uses `asyncio.run()` in `if __name__ == "__main__"` blocks
- FastAPI examples include `uvicorn.run()` for standalone server

## ANTI-PATTERNS
- Two FastAPI files with unclear boundary — `fastapi_sample.py` vs `fastapi_server_sample.py`
- `schedule_main()` in asyncs_sample has try/except that silently swallows errors (in tests)
