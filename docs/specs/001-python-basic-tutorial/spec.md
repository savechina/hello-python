# Feature Specification: Hello Python Basic Tutorial

**Feature Branch**: `001-python-basic-tutorial`  
**Created**: 2026-04-26  
**Status**: Draft  
**Input**: User description: 参考 ../hello-rust/docs/src 样例教程，创建 hello python basic 教程

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Browse Basic Tutorial Overview (Priority: P1)

As a Python learner, I want to see a structured overview of all basic Python topics so that I can understand the learning path and choose where to start.

**Why this priority**: This is the entry point for all learners — without it, users cannot navigate the tutorial content.

**Independent Test**: Can be fully tested by opening the basic overview page in the mdBook and verifying that all chapter links are present, correctly ordered, and clickable.

**Acceptance Scenarios**:

1. **Given** a user opens the Hello Python docs, **When** they navigate to the Basic section, **Then** they see a structured overview with all chapters listed, difficulty ratings, and estimated time
2. **Given** a user is on the overview page, **When** they click any chapter link, **Then** they are taken to the corresponding chapter page

---

### User Story 2 - Read Individual Chapter Content (Priority: P1)

As a Python learner, I want to read a well-structured chapter that explains a specific Python concept with runnable code examples so that I can understand and practice the concept.

**Why this priority**: This is the core value of the tutorial — each chapter must be independently useful and complete.

**Independent Test**: Any single chapter can be read and understood independently, with working code examples that match the `hello_python/basic/` source files.

**Acceptance Scenarios**:

1. **Given** a user opens a chapter (e.g., "变量与表达式"), **When** they read through it, **Then** they see an opening story, learning objectives, code examples with explanations, common errors, exercises, and a summary
2. **Given** a user reads a code example in a chapter, **When** they copy and run it, **Then** it produces the expected output matching what the chapter describes
3. **Given** a user finishes a chapter, **When** they check the "next step" links, **Then** they can navigate to the next chapter or related chapters

---

### User Story 3 - Practice with Exercises and Quizzes (Priority: P2)

As a Python learner, I want to test my understanding after each chapter with exercises and quiz questions so that I can verify my learning progress.

**Why this priority**: Reinforces learning and provides self-assessment, but the tutorial is still valuable without it as an MVP.

**Independent Test**: Each chapter's exercises and quizzes can be completed independently, with answers hidden behind collapsible sections.

**Acceptance Scenarios**:

1. **Given** a user finishes reading a chapter, **When** they reach the exercise section, **Then** they see practice problems with hidden answers they can reveal
2. **Given** a user attempts a quiz question, **When** they reveal the answer, **Then** they see the correct answer with an explanation

---

### User Story 4 - Navigate the Full Basic Learning Path (Priority: P3)

As a Python learner, I want to see a visual learning path diagram and checklist so that I can track my progress through all basic topics.

**Why this priority**: Nice-to-have for motivation and progress tracking, but not essential for the core tutorial experience.

**Independent Test**: The learning path diagram and checklist are displayed on the overview page with clickable links to each chapter.

**Acceptance Scenarios**:

1. **Given** a user opens the basic overview, **When** they scroll to the learning path section, **Then** they see a visual flow diagram showing the recommended chapter order
2. **Given** a user completes a chapter, **When** they return to the overview, **Then** they can see which chapters they've completed via a checklist

### Edge Cases

- What happens when a user clicks a link to a chapter that hasn't been written yet? (Should show a "Coming Soon" placeholder)
- How does the docs build handle missing or broken mdBook links?
- What if the code examples in docs diverge from the actual `hello_python/basic/` source files?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a basic tutorial overview page that lists all basic Python topics with chapter titles, descriptions, difficulty levels, and estimated reading time
- **FR-002**: System MUST provide individual chapter pages for each basic Python topic, each containing: opening story/hook, learning objectives, code examples with explanations, common errors and fixes, hands-on exercises, chapter summary, and glossary terms
- **FR-003**: Users MUST be able to navigate between chapters via previous/next links and a sidebar table of contents
- **FR-004**: System MUST include runnable code examples in each chapter that match the corresponding `hello_python/basic/*_sample.py` source files — new sample files will be created for each chapter topic
- **FR-005**: System MUST provide a learning path diagram showing the recommended order of chapters
- **FR-006**: System MUST provide practice exercises with hidden answers (collapsible sections) for each chapter
- **FR-007**: System MUST include a glossary of key Python terms (English + Chinese) at the end of each chapter
- **FR-008**: System MUST update the mdBook SUMMARY.md to include the new basic tutorial chapter structure
- **FR-009**: System MUST provide a "review basic" summary chapter that consolidates key concepts and a knowledge checklist

### Key Entities

- **Chapter**: A self-contained tutorial unit covering one Python concept (e.g., variables, data types, functions). Has a title, difficulty level, estimated time, code examples, exercises, and glossary.
- **Learning Path**: An ordered sequence of chapters showing the recommended progression from beginner to competent.
- **Code Example**: A runnable Python code snippet embedded in a chapter, linked to the corresponding `*_sample.py` file in `hello_python/basic/`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A Python beginner can understand and run their first Python program within 15 minutes of starting the tutorial
- **SC-002**: All code examples in the documentation execute without errors when copied and run with Python 3.13
- **SC-003**: The mdBook builds successfully with zero broken links across all basic tutorial pages
- **SC-004**: Each chapter includes at least 3 runnable code examples, 2 practice exercises, and a glossary of 5+ terms; the basic tutorial covers 10+ chapters matching the hello-rust basic section scope
- **SC-005**: A learner can complete the entire basic tutorial (all chapters) within 8 hours of total reading time

## Clarifications

### Session 2026-04-26

- Q: Should new `*_sample.py` files be created in `hello_python/basic/` to support additional tutorial chapters, or should docs only cover the 2 existing files? → A: Create new sample files to match tutorial chapters
- Q: 002-python-basic-tutorial is a duplicate empty template — merge or delete? → A: Deleted `002-python-basic-tutorial/` entirely; 001 retained as sole active spec
- Q: Feature scope — does "update advance tutorial" mean create mdBook docs for advance topics, update existing sample code, create a new spec, both? → A: Create mdBook docs for advance topics only (sample code already exists)
- Q: How to handle `database_sample.py` which hardcodes credentials and auto-connects on import? → A: Refactor into safe self-contained sample using `if __name__` block, add connection error handling
- Q: Two FastAPI files (`fastapi_sample.py` vs `fastapi_server_sample.py`) with unclear boundary — how to handle in docs? → A: Keep both as separate chapters: basic FastAPI routes vs advanced server management
- Q: Should advance docs use the same 12-section structure as basic tutorial, or a different format? → A: Mirror the same 12-section structure for consistent UX across basic and advance tutorials
- Q: How many advance chapters — all 9 sample files, merge some, or subset? → A: 8 chapters total — merge `database_sample.py` + `database_sqlite_sample.py` into one combined DB chapter
- Q: Docs pre-pages — should `about-hello.md`, `introduction.md`, and `getting-started.md` be created/updated referencing hello-rust structure? → A: Yes — create `about-hello.md`, `introduction.md`, update `getting-started.md` with Python/uv/mdBook content, and add all three to SUMMARY.md

## Advance Tutorial Scope (Extension)

This feature now also covers the advance tutorial documentation alongside the basic tutorial.

### User Story 5 - Read Advance Tutorial Chapters (Priority: P2)

As a Python learner who has completed the basic tutorial, I want to read well-structured advance chapters covering async, FastAPI, dependency injection, databases, JSON, and NumPy so that I can deepen my Python skills.

**Independent Test**: Each advance chapter can be read independently with runnable code examples matching the `hello_python/advance/*_sample.py` source files.

**Acceptance Scenarios**:
1. **Given** a user opens an advance chapter (e.g., "异步编程"), **When** they read through it, **Then** they see the same 12-section structure as basic chapters, with working code samples from `hello_python/advance/`
2. **Given** a user copies an advance code example, **When** they run it, **Then** it executes without errors (or requires only pre-configured external resources that the chapter documents)

### Advance Chapter List (8 chapters)

| # | Chapter Title | Source File | Difficulty |
|---|---------------|-------------|------------|
| 1 | 异步编程 (Async) | `asyncs_sample.py` | ⭐⭐⭐ |
| 2 | FastAPI 路由基础 (FastAPI Routes) | `fastapi_sample.py` | ⭐⭐⭐ |
| 3 | FastAPI 服务器管理 (FastAPI Server) | `fastapi_server_sample.py` | ⭐⭐⭐ |
| 4 | 依赖注入 (Dependency Injection) | `injector_sample.py` | ⭐⭐⭐ |
| 5 | 数据库操作 (Database) | `database_sample.py` + `database_sqlite_sample.py` | ⭐⭐⭐ |
| 6 | JSON 数据处理 (JSON Processing) | `json_sample.py` | ⭐⭐ |
| 7 | NumPY 数值计算 (NumPy) | `numpy_sample.py` | ⭐⭐⭐ |
| 8 | 阶段复习：进阶部分 (Review Advance) | N/A | — |

## Assumptions

- The target audience is Chinese-speaking learners with basic programming concepts knowledge (variables, loops, functions) but no Python experience
- The tutorial format should mirror the hello-rust docs structure (opening story → objectives → examples → errors → exercises → summary → glossary)
- mdBook is the documentation build tool (already configured in the project)
- Each tutorial chapter will have a corresponding `*_sample.py` file in `hello_python/basic/` — new sample files will be created as needed to match the chapter list
- The basic tutorial covers: Python basics (variables, expressions, data types, functions, control flow, collections, modules) — topics that map to Rust's basic section but adapted for Python's paradigms
- Chinese language is the primary documentation language (matching hello-rust docs)
