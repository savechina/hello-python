# Tasks: Hello Python Basic Tutorial

**Input**: Design documents from `/docs/specs/001-python-basic-tutorial/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/chapter-contract.md, quickstart.md

**Tests**: YES — each `*_sample.py` requires a corresponding `test_*_sample.py` in `tests/basic/` per plan.md and constitution Principle II.

**Organization**: Tasks organized by user story (from spec.md) to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

Repository root: `/Users/weirenyan/CodeRepo/funspace/hello-python/`

- **Documentation**: `docs/src/basic/<chapter>.md`, `docs/src/SUMMARY.md`, `docs/book.toml`
- **Sample code**: `hello_python/basic/<topic>_sample.py`
- **Tests**: `tests/basic/test_<topic>_sample.py`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Configure mdBook plugins, create directory structure, prepare chapter skeleton

- [X] T001 Create `docs/src/basic/` directory for tutorial chapters
- [X] T002 Copy mdBook assets from hello-rust: `mdbook-admonish.css`, `pagetoc.css`, `pagetoc.js` into `docs/src/assets/` and `docs/theme/`
- [X] T003 Update `docs/book.toml` with admonish, alerts, pagetoc plugin configuration per research.md
- [X] T004 [P] Create `docs/src/basic/basic-overview.md` skeleton (structure only, no content yet)
- [X] T005 [P] Create `docs/src/basic/review-basic.md` skeleton (structure only, no content yet)
- [X] T006 Verify mdBook build passes: `mdbook build docs` — must succeed with zero errors/warnings

**Checkpoint**: mdBook infrastructure ready, all plugins configured, build passing

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish chapter templates, sample file templates, and test templates that ALL user stories depend on

- [X] T007 [P] Create existing sample test baseline
- [X] T008 Update existing `hello_python/basic/datatype_sample.py` to conform to contract
- [X] T009 Update existing `hello_python/basic/expression_sample.py` to conform to contract
- [X] T010 Run `uv run ruff check hello_python/basic/` and fix all lint issues on existing files
- [X] T011 Run `uv run ruff format hello_python/basic/` and `tests/basic/` for consistent code style
- [X] T012 Create `hello_python/basic/control_flow_sample.py` skeleton
- [X] T013 [P] Create chapter template function
- [X] T014 Create `tests/basic/test_control_flow_sample.py` skeleton

**Checkpoint**: Foundation ready — existing tests pass, lint clean, templates established, all new sample files have skeleton structure

---

## Phase 3: User Story 1 — Browse Basic Tutorial Overview + Read Core Chapters (P1) 🎯 MVP

**Goal**: Users can navigate to the Basic section, see the overview with all chapters listed, and read the first few core chapters (variables/expressions, datatypes, control flow) with runnable code examples.

**Independent Test**: Open mdBook docs → navigate to Basic Overview → verify all 12 chapters listed with links → click expression/datatype/control-flow chapters → verify each chapter has all 12 sections → copy code examples → run them with `python -m hello_python.basic.<topic>_sample` → verify expected output.

### Tests for User Story 1

- [X] T015 [P] [US1] Create `tests/basic/test_control_flow_sample.py` — implement actual tests for `if/elif/else` functions with output assertions
- [X] T016 [P] [US1] Enhance `tests/basic/test_datatype_sample.py` — add assertions verifying `string_sample()` output contains expected strings
- [X] T017 [P] [US1] Enhance `tests/basic/test_expression_sample.py` — add assertions verifying `number_calc()` output contains expected calculations

### Implementation for User Story 1 — Sample Code

- [X] T018 [US1] Implement `hello_python/basic/control_flow_sample.py` — `if/else`, `if/elif/else`, ternary operator, `match` statements with 3+ examples
- [X] T019 [US1] Run `python -m hello_python.basic.control_flow_sample` — must execute without errors

### Implementation for User Story 1 — Documentation

- [X] T020 [US1] Write `docs/src/basic/basic-overview.md` — full content: learning path overview, chapter list with descriptions, difficulty ratings, estimated time
- [X] T021 [US1] Write `docs/src/basic/expression.md` — full content: 变量与表达式, all 12 sections, code from `expression_sample.py`, exercises, quiz
- [X] T022 [US1] Write `docs/src/basic/datatype.md` — full content: 基础数据类型, all 12 sections, code from `datatype_sample.py`, exercises, quiz
- [X] T023 [US1] Write `docs/src/basic/control-flow.md` — full content: 流程控制, all 12 sections, code from `control_flow_sample.py`, exercises, quiz
- [X] T024 [US1] Update `docs/src/SUMMARY.md` — add `# 基础部分 (Basic)` section with all chapter links (nested hierarchy per research.md)

### Verify User Story 1

- [X] T025 [US1] Run `mdbook build docs` — must pass with zero broken links for expression, datatype, control-flow, basic-overview, review-basic
- [X] T026 [US1] Run `uv run pytest tests/basic/test_control_flow_sample.py -s -v` — must pass
- [X] T027 [US1] Serve docs locally with `mdbook serve docs`, verify basic-overview renders with clickable links to all 12 chapters

**Checkpoint**: US1 complete — Basic Overview exists, 3 core chapters fully written, all tests pass, mdBook builds cleanly

---

## Phase 4: User Story 2 — Read Remaining Core Chapters (P2)

**Goal**: Users can read the next set of foundational chapters: loops, functions, list/dict, and file I/O. Each chapter is independently testable with runnable code examples.

**Independent Test**: Navigate to loops, functions, list-dict, file-io chapters → verify each has all 12 sections → copy and run code examples → verify output matches description → complete exercises.

### Tests for User Story 2

- [X] T028 [P] [US2] Create `tests/basic/test_loops_sample.py` — test all loop functions with output assertions
- [X] T029 [P] [US2] Create `tests/basic/test_functions_sample.py` — test function definitions, scope, lambda with output assertions
- [X] T030 [P] [US2] Create `tests/basic/test_list_dict_sample.py` — test list comprehension, dict operations with output assertions
- [X] T031 [P] [US2] Create `tests/basic/test_file_io_sample.py` — test file read/write, context manager, temp file handling

### Implementation for User Story 2 — Sample Code

- [X] T032 [P] [US2] Implement `hello_python/basic/loops_sample.py` — `for`, `while`, `range()`, `enumerate()`, `zip()`, list comprehension basics — 3+ examples
- [X] T033 [P] [US2] Implement `hello_python/basic/functions_sample.py` — `def`, parameters, `*args`/`**kwargs`, `lambda`, scope rules — 3+ examples
- [X] T034 [P] [US2] Implement `hello_python/basic/list_dict_sample.py` — dict methods, dict comprehension, set, tuple unpacking — 3+ examples
- [X] T035 [P] [US2] Implement `hello_python/basic/file_io_sample.py` — `open()` modes, context manager (`with`), reading/writing, `pathlib` — 3+ examples
- [X] T036 [US2] Run all 4 new sample files individually — must execute without errors
- [X] T037 [US2] Run `uv run pytest tests/basic/test_loops_sample.py tests/basic/test_functions_sample.py tests/basic/test_list_dict_sample.py tests/basic/test_file_io_sample.py -s -v` — all must pass
- [X] T038 [US2] Run `uv run ruff check hello_python/basic/loops_sample.py hello_python/basic/functions_sample.py hello_python/basic/list_dict_sample.py hello_python/basic/file_io_sample.py` — must pass

### Implementation for User Story 2 — Documentation

- [X] T039 [P] [US2] Write `docs/src/basic/loops.md` — full content: 循环结构, all 12 sections
- [X] T040 [P] [US2] Write `docs/src/basic/functions.md` — full content: 函数基础, all 12 sections
- [X] T041 [P] [US2] Write `docs/src/basic/list-dict.md` — full content: 列表与字典, all 12 sections
- [X] T042 [P] [US2] Write `docs/src/basic/file-io.md` — full content: 文件操作, all 12 sections

**Checkpoint**: US2 complete — 4 additional chapters written, all sample code + tests passing, lint clean

---

## Phase 5: User Story 3 — Read Advanced Basic Chapters + Full Learning Path (P3)

**Goal**: Complete remaining chapters (exception handling, modules, OOP, string advanced), add review chapter, finalize full basic learning path diagram and checklist.

**Independent Test**: Navigate to all remaining chapters → verify 12-section structure → copy and run code → complete review chapter exercises → verify full learning path diagram on overview page.

### Tests for User Story 3

- [X] T043 [P] [US3] Create `tests/basic/test_exception_sample.py` — test try/except/finally, custom exceptions with assertions
- [X] T044 [P] [US3] Create `tests/basic/test_modules_packages_sample.py` — test import patterns, module loading with assertions
- [X] T045 [P] [US3] Create `tests/basic/test_oop_sample.py` — test class definition, inheritance, `__init__` with assertions
- [X] T046 [P] [US3] Create `tests/basic/test_string_advanced_sample.py` — test regex, string templates, f-string advanced patterns with assertions

### Implementation for User Story 3 — Sample Code

- [X] T047 [P] [US3] Implement `hello_python/basic/exception_sample.py` — `try/except/finally`, multiple except clauses, `raise`, custom exceptions — 3+ examples
- [X] T048 [P] [US3] Implement `hello_python/basic/modules_packages_sample.py` — `import`, `from...import`, `__name__`, package structure, `__all__` — 3+ examples
- [X] T049 [P] [US3] Implement `hello_python/basic/oop_sample.py` — class definition, `__init__`, `self`, inheritance, method overriding — 3+ examples
- [X] T050 [P] [US3] Implement `hello_python/basic/string_advanced_sample.py` — `re` module basics, string `.split()/.join()`, f-string advanced formatting, templates — 3+ examples
- [X] T051 [US3] Run all 4 new sample files individually — must execute without errors
- [X] T052 [US3] Run `uv run pytest tests/basic/test_exception_sample.py tests/basic/test_modules_packages_sample.py tests/basic/test_oop_sample.py tests/basic/test_string_advanced_sample.py -s -v` — all must pass
- [X] T053 [US3] Run `uv run ruff check hello_python/basic/exception_sample.py hello_python/basic/modules_packages_sample.py hello_python/basic/oop_sample.py hello_python/basic/string_advanced_sample.py` — must pass

### Implementation for User Story 3 — Documentation

- [X] T054 [P] [US3] Write `docs/src/basic/exception.md` — full content: 异常处理, all 12 sections
- [X] T055 [P] [US3] Write `docs/src/basic/modules-packages.md` — full content: 模块与包, all 12 sections
- [X] T056 [P] [US3] Write `docs/src/basic/oop.md` — full content: 面向对象编程, all 12 sections
- [X] T057 [P] [US3] Write `docs/src/basic/string-advanced.md` — full content: 字符串高级处理, all 12 sections
- [X] T058 [US3] Write `docs/src/basic/review-basic.md` — full content: 阶段复习：基础部分, consolidated key concepts, knowledge checklist
- [X] T059 [US3] Update `docs/src/basic/basic-overview.md` — add visual learning path diagram and chapter completion checklist
- [X] T060 [US3] Verify `docs/src/SUMMARY.md` has all 13 chapter links present and correctly nested (basic-overview + 11 topics + review-basic)

**Checkpoint**: US3 complete — ALL 12 chapters + overview fully written, all tests pass, lint clean

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: End-to-end verification, lint, build, and documentation quality gates

- [X] T061 Run `mdbook build docs` — must pass with ZERO errors and ZERO warnings
- [X] T062 Run `mdbook serve docs --open` — manually verify all links are clickable, no 404 errors
- [X] T063 Run `uv run pytest tests/basic/ -s -v` — ALL tests must pass (existing + new)
- [X] T064 Run `uv run ruff check hello_python/basic/` — ALL files must pass
- [X] T065 Run `uv run ruff format hello_python/basic/` — confirm consistent formatting across all files
- [X] T066 Verify each chapter meets constitution quality gates: ≥3 code examples, ≥2 exercises, ≥3 quiz questions, ≥5 glossary terms, ≥500 Chinese characters
- [X] T067 Verify `docs/book.toml` language setting consistent (en vs zh consideration — match hello-rust pattern)

---

## Phase 7: Advance Tutorial — Setup & Foundation

**Purpose**: Create advance docs directory, refactor `database_sample.py` for safety, ensure all advance samples execute

- [X] T068 Create `docs/src/advance/` directory for advance tutorial chapters
- [X] T069 Read `hello_python/advance/database_sample.py` — refactor to wrap DB connection in `if __name__` block with try/except
- [X] T070 Run all 8 advance sample files individually — verify each executes without fatal errors
- [X] T071 Create `docs/src/advance/advance-overview.md` skeleton: `# 进阶入门 (Advance Overview)` + brief intro

**Checkpoint**: Advance infrastructure ready, `database_sample.py` import-safe, all samples verified

---

## Phase 8: User Story 5 — Read Advance Tutorial Chapters (P2) 🎯

**Goal**: Users can navigate to the Advance section in mdBook and read 7 topic chapters + 1 review chapter about async, FastAPI, DI, DB, JSON, and NumPy.

**Independent Test**: Each chapter has all 12 sections, links to correct `hello_python/advance/*_sample.py` code, and mdBook includes them in SUMMARY.md.

### Implementation for User Story 5 — Sample Code Refactor

- [X] T072 [US5] Refactor `hello_python/advance/database_sample.py` — wrap pymysql connection in `if __name__` block, add try/except for connection failure, use placeholder credentials safely

### Implementation for User Story 5 — Documentation

- [X] T073 [P] [US5] Write `docs/src/advance/advance-overview.md` — full content: advance topics overview, chapter table with descriptions and difficulty
- [X] T074 [P] [US5] Write `docs/src/advance/async.md` — full content: 异步编程, all 12 sections, code from `asyncs_sample.py`
- [X] T075 [P] [US5] Write `docs/src/advance/fastapi-routes.md` — full content: FastAPI 路由基础, all 12 sections, code from `fastapi_sample.py`
- [X] T076 [P] [US5] Write `docs/src/advance/fastapi-server.md` — full content: FastAPI 服务器管理, all 12 sections, code from `fastapi_server_sample.py`
- [X] T077 [P] [US5] Write `docs/src/advance/dependency-injection.md` — full content: 依赖注入, all 12 sections, code from `injector_sample.py`
- [X] T078 [P] [US5] Write `docs/src/advance/database.md` — full content: 数据库操作, all 12 sections, code from `database_sample.py` + `database_sqlite_sample.py` (combined)
- [X] T079 [P] [US5] Write `docs/src/advance/json.md` — full content: JSON 数据处理, all 12 sections, code from `json_sample.py`
- [X] T080 [P] [US5] Write `docs/src/advance/numpy.md` — full content: NumPy 数值计算, all 12 sections, code from `numpy_sample.py`
- [X] T081 [US5] Write `docs/src/advance/review-advance.md` — full content: 阶段复习：进阶部分, consolidated concepts, knowledge checklist
- [X] T082 [US5] Update `docs/src/SUMMARY.md` — add `# 进阶部分 (Advance)` section nested after basic section

**Checkpoint**: US5 complete — ALL 8 advance chapters written, SUMMARY.md updated, database_sample.py refactored

---

## Phase 9: Advance Polish & Cross-Cutting Concerns

**Purpose**: End-to-end verification for advance docs

- [X] T083 Run `mdbook build docs` — must pass with ZERO errors
- [X] T084 Run `mdbook serve docs --open` — verify advance links clickable
- [X] T085 Run ruff check on advance samples — `database_sample.py` passes lint
- [X] T086 Verify each advance chapter constitution quality gates
- [X] T087 Verify `docs/src/SUMMARY.md` has both sections with all links

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|-----------|--------|
| Phase 1: Setup | None | Phase 2 |
| Phase 2: Foundational | Phase 1 | Phase 3, 4, 5 |
| Phase 3: US1 (P1) | Phase 2 | Phase 6 |
| Phase 4: US2 (P2) | Phase 2 | Phase 6 |
| Phase 5: US3 (P3) | Phase 2 | Phase 6 |
| Phase 6: Basic Polish | Phase 3, 4, 5 | Phase 7 |
| Phase 7: Advance Setup | Phase 6 | Phase 8 |
| Phase 8: US5 (Advance) | Phase 7 | Phase 9 |
| Phase 9: Advance Polish | Phase 8 | — |

### User Story Dependencies

- **US1 (P1)**: Depends only on Foundational (Phase 2). Delivers: Overview + 3 core chapters.
- **US2 (P2)**: Depends only on Foundational (Phase 2). Delivers: 4 more chapters.
- **US3 (P3)**: Depends only on Foundational (Phase 2). Delivers: 4 more chapters + review.
- **US5 (P2)**: Depends on Phase 7 (Advance Setup — database_sample.py refactor). Delivers: 8 advance chapters + SUMMARY.md update.

### Within Each User Story

1. Tests MUST be written before sample code (TDD per constitution Principle II)
2. Sample code MUST be implemented before documentation (docs reference real code)
3. Each chapter document MUST match its `*_sample.py` content
4. Lint check MUST pass before moving to next phase

### Parallel Opportunities

**Phase 4 (US2)**: 
- T028, T029, T030, T031 (tests) can run in parallel — 4 different test files
- T032, T033, T034, T035 (sample code) can run in parallel — 4 different sample files
- T039, T040, T041, T042 (documentation) can run in parallel — 4 different chapter files

**Phase 5 (US3)**:
- T043, T044, T045, T046 (tests) can run in parallel — 4 different test files
- T047, T048, T049, T050 (sample code) can run in parallel — 4 different sample files
- T054, T055, T056, T057 (documentation) can run in parallel — 4 different chapter files

**Phase 8 (US5 — Advance Docs)**:
- T073, T074, T075, T076, T077, T078, T079, T080 (documentation) can ALL run in parallel — 8 different chapter files, no dependencies

---

## Parallel Example: User Story 5 (Advance Docs — Phase 8)

```bash
# Launch ALL 8 advance chapter docs in parallel (independent files):
Task: "Write advance-overview.md"
Task: "Write async.md (异步编程) with all 12 sections"
Task: "Write fastapi-routes.md (FastAPI 路由) with all 12 sections"
Task: "Write fastapi-server.md (FastAPI Server) with all 12 sections"
Task: "Write dependency-injection.md (依赖注入) with all 12 sections"
Task: "Write database.md (数据库) with all 12 sections"
Task: "Write json.md (JSON处理) with all 12 sections"
Task: "Write numpy.md (NumPy) with all 12 sections"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only — Basic Tutorial)

1. Complete Phase 1: Setup — mdBook infrastructure ready
2. Complete Phase 2: Foundational — templates, existing tests pass, lint clean
3. Complete Phase 3: US1 — Overview + expression/datatype/control-flow chapters
4. **STOP and VALIDATE**: `mdbook build docs` passes, `mdbook serve docs` renders basic overview, 3 chapters readable, tests pass
5. Demo: Learner can navigate to Basic section and read first 3 chapters

### Incremental Delivery (Basic → Advance)

1. Phase 1+2 → Foundation ready
2. Phase 3 (US1) → 3 chapters + overview → TEST → Demo (MVP Basic!)
3. Phase 4 (US2) → 4 more chapters → TEST → Demo
4. Phase 5 (US3) → 4 more chapters + review → TEST → Demo (Feature Complete: Basic)
5. Phase 6 (Basic Polish) → Final lint/build for basic
6. Phase 7 (Advance Setup) → database_sample.py refactor, advance dir created
7. Phase 8 (US5) → 8 advance chapters → TEST → Demo (Feature Complete: Advance)
8. Phase 9 (Advance Polish) → Final lint/build for advance + basic

### Parallel Team Strategy

With multiple developers:
1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: Phase 3 (US1) — core chapters
   - Developer B: Phase 4 (US2) — loops/functions/list-dict/file-io
   - Developer C: Phase 5 (US3) — exception/modules/oop/string-review
3. All three stories complete independently, merge and run Phase 6 polish together
4. Phase 7: database_sample.py refactor (sequential) + advance-overview.md skeleton
5. Phase 8: ALL 8 advance chapter docs can be parallelized across 8 developers
6. Phase 9: Team runs final polish together

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each chapter MUST have all 12 sections per chapter contract (`contracts/chapter-contract.md`)
- Each `*_sample.py` MUST have `if __name__ == "__main__"` block per contract
- Advance chapters reference EXISTING `hello_python/advance/*_sample.py` files (no new code needed except database_sample.py refactor)
- `database_sample.py` refactor MUST not break backward compatibility — wrap in `if __name__` block with safe error handling
- Run `uv run ruff check` and `uv run ruff format` after each sample file change
- Advance chapters use the SAME 12-section template as basic chapters for consistent UX

**Total task count**: 87
**Phase 1 (Setup)**: 6 tasks — ✅ COMPLETE
**Phase 2 (Foundational)**: 8 tasks — ✅ COMPLETE
**Phase 3 (US1 — P1)**: 13 tasks — ✅ COMPLETE
**Phase 4 (US2 — P2)**: 15 tasks — ✅ COMPLETE
**Phase 5 (US3 — P3)**: 18 tasks — ✅ COMPLETE
**Phase 6 (Basic Polish)**: 7 tasks — ✅ COMPLETE
**Phase 7 (Advance Setup)**: 4 tasks — TODO
**Phase 8 (US5 — Advance Docs)**: 11 tasks — TODO
**Phase 9 (Advance Polish)**: 5 tasks — TODO

**Parallel opportunities identified**:
- Phase 8 (Advance Docs): 8 parallelizable tasks (all 8 chapter docs are independent files)

**Remaining work for advance tutorial**: 20 tasks (Phase 7 + Phase 8 + Phase 9)
