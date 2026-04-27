# Implementation Plan: Hello Python Basic + Advance Tutorial

**Branch**: `001-python-basic-tutorial` | **Date**: 2026-04-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/docs/specs/001-python-basic-tutorial/spec.md`

## Summary

Two-phase documentation project:

**Phase A (Basic — IMPLEMENTED)**: 12 mdBook chapters (basic-overview + 11 topic chapters + review-basic), 11 sample files in `hello_python/basic/`, 11 test files in `tests/basic/`. All 67 tasks completed. 26 tests pass. mdBook builds successfully.

**Phase B (Advance — NEW)**: 8 mdBook chapters (7 topics + review) referencing existing `hello_python/advance/*_sample.py` files. Refactor `database_sample.py` to be safe for import. Create `docs/src/advance/` directory with 8 chapter files. Update `docs/src/SUMMARY.md` to include `# 进阶部分 (Advance)` section.

## Technical Context

**Language/Version**: Python 3.10+ (per pyproject.toml `requires-python`); tested with Python 3.13.3  
**Primary Dependencies**: mdBook 0.4.52+ (with admonish, alerts, pagetoc plugins), Click 8.1+, FastAPI, asyncio, PyMySQL, injector, NumPy  
**Storage**: N/A — documentation-only feature, no persistent data  
**Testing**: unittest-style tests in `tests/basic/` for basic modules; advance sample files need test verification (some require external DB)  
**Target Platform**: Static HTML via mdBook → GitHub Pages  
**Project Type**: CLI + documentation tutorial  
**Performance Goals**: mdBook build <5 minutes per constitution; individual chapter build <30 seconds  
**Constraints**: Chinese (Simplified) primary language; English technical terms in parentheses; 12-section chapter template must match basic tutorial; `database_sample.py` must not auto-connect on import  
**Scale/Scope**: 8 advance chapters + 1 review chapter; `docs/src/advance/` directory with all chapter markdown files; `SUMMARY.md` update with advance section

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Code Quality | **PASS** | Only docs creation + 1 sample refactor; all following existing conventions |
| II. Test-First Development | **PASS** | Basic tests complete; advance chapter code already exists (no new code to test except `database_sample.py` refactor) |
| III. UX Consistency | **PASS** | 12-section template mirrors basic tutorial; Chinese primary language maintained |
| IV. Performance | **PASS** | mdBook build targets per constitution (<5 min full, <30s per chapter) |
| V. SDD Harness | **PASS** | Full `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement` workflow followed for basic; advance follows same pattern |

**Documentation Quality Gates** (per Principle I):
- All advance chapters MUST have same 12-section structure as basic chapters
- Code examples must reference real `hello_python/advance/*_sample.py` files
- Each chapter MUST have ≥3 code examples, ≥3 knowledge checkpoint questions, ≥500 Chinese characters

## Project Structure

### Documentation (this feature)

```text
docs/specs/001-python-basic-tutorial/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output (for basic — already exists)
├── quickstart.md        # Phase 1 output (for basic — already exists)
├── contracts/           # Phase 1 output (chapter-contract.md — already exists)
└── tasks.md             # Phase 2 output — needs update for advance tasks
```

### Source Code (repository root)

```text
hello-python/
├── docs/
│   ├── book.toml                            # EXISTING — already configured with plugins
│   └── src/
│       ├── SUMMARY.md                       # EXISTING — needs advance section added
│       ├── getting-started.md               # EXISTING
│       ├── basic/                           # COMPLETE — 13 chapter files
│       │   ├── basic-overview.md
│       │   ├── expression.md
│       │   ├── datatype.md
│       │   ├── control-flow.md
│       │   ├── loops.md
│       │   ├── functions.md
│       │   ├── list-dict.md
│       │   ├── file-io.md
│       │   ├── exception.md
│       │   ├── modules-packages.md
│       │   ├── oop.md
│       │   ├── string-advanced.md
│       │   └── review-basic.md
│       └── advance/                         # NEW — advance chapter files
│           ├── advance-overview.md          # NEW: 进阶入门
│           ├── async.md                     # NEW: 异步编程
│           ├── fastapi-routes.md            # NEW: FastAPI 路由基础
│           ├── fastapi-server.md            # NEW: FastAPI 服务器管理
│           ├── dependency-injection.md      # NEW: 依赖注入
│           ├── database.md                  # NEW: 数据库操作
│           ├── json.md                      # NEW: JSON 数据处理
│           ├── numpy.md                     # NEW: NumPy 数值计算
│           └── review-advance.md            # NEW: 阶段复习：进阶部分
│
├── hello_python/
│   ├── basic/                               # COMPLETE — 11 sample files (all implemented)
│   └── advance/                             # EXISTING — 9 sample files (need 1 refactor)
│       ├── asyncs_sample.py                 # EXISTING — reference for async.md
│       ├── fastapi_sample.py                # EXISTING — reference for fastapi-routes.md
│       ├── fastapi_server_sample.py         # EXISTING — reference for fastapi-server.md
│       ├── injector_sample.py               # EXISTING — reference for dependency-injection.md
│       ├── database_sample.py               # EXISTING — NEEDS REFACTOR (hardcoded creds, auto-connect)
│       ├── database_sqlite_sample.py        # EXISTING — reference for database.md
│       ├── json_sample.py                   # EXISTING — reference for json.md
│       └── numpy_sample.py                  # EXISTING — reference for numpy.md
│
└── tests/
    └── basic/                               # COMPLETE — 11 test files
```

**Structure Decision**: Single project extension. Basic tutorial is already fully implemented (13 docs, 11 samples, 11 tests). This plan adds advance documentation only — 8 new mdBook chapters under `docs/src/advance/` plus a SUMMARY.md update. One existing sample file (`database_sample.py`) needs refactoring for safety.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Refactor `database_sample.py` + keep `database_sqlite_sample.py` | User chose Option B — keep both FastAPI files as separate chapters; same for DB files | Removing would lose MySQL connection reference that users may need |

## Constitution Check (Post-Design Re-Evaluation)

*Re-checked after Phase 1 design — all gates continue to pass.*

| Principle | Status | Verification Method |
|-----------|--------|---|
| I. Code Quality | **PASS** | `database_sample.py` refactor must pass `uv run ruff check`; no other code changes |
| II. Test-First | **PASS** | Only refactor to existing code; docs-only otherwise |
| III. UX Consistency | **PASS** | All advance chapters follow same 12-section template as basic |
| IV. Performance | **PASS** | `mdbook build docs` must pass within 5 minutes |
| V. SDD Harness | **PASS** | All phases followed: specify → plan → tasks → implement |
