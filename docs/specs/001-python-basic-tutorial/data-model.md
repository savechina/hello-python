# Data Model: Hello Python Basic Tutorial

## Entities

### Chapter

**Purpose**: A self-contained tutorial unit covering one Python concept.

| Field | Type | Validation |
|---|---|---|
| slug | string | Kebab-case, matches filename without `.md` |
| title_zh | string | Chinese title, max 80 chars |
| title_en | string | English technical term reference, max 40 chars |
| difficulty | enum | `beginner`, `easy`, `medium` |
| estimated_minutes | int | Range: 5-60 |
| order | int | 1-based sequential |
| sample_file | string | Corresponding `*_sample.py` in `hello_python/basic/` |
| has_exercises | bool | Must be `true` for all non-overview/review chapters |
| has_quiz | bool | Must be `true` for all non-overview/review chapters |

**Relationships**:
- Chapter → Sample File (1:1, via `sample_file`)
- Chapter → Test File (1:1, `tests/basic/test_<sample>_py`)
- Chapter → Next/Previous Chapter (1:1, via ordering)

### Learning Path

**Purpose**: Ordered sequence of chapters showing recommended progression.

| Field | Type | Validation |
|---|---|---|
| name_zh | string | "基础部分" |
| name_en | string | "Basic" |
| chapters | list[Chapter] | Ordered by `order` field |
| total_minutes | int | Computed: sum of chapter times |
| total_chapters | int | Computed: length of chapters list |

### Code Example

**Purpose**: Runnable Python code snippet embedded in a chapter.

| Field | Type | Validation |
|---|---|---|
| name | string | Unique within chapter, describes purpose |
| language | string | Always `python` |
| source | string | Content of code block |
| expected_output | string | Expected stdout when executed |
| is_inline | bool | True if shown inline, false if linked to `*_sample.py` |

### Exercise

**Purpose**: Practice problem for hands-on learning.

| Field | Type | Validation |
|---|---|---|
| number | int | 1-based within chapter |
| problem_zh | string | Problem description in Chinese |
| difficulty | enum | `easy`, `medium` |
| answer_hidden | bool | Default `true` — hidden behind collapsible mdBook element |
| answer_code | string | Solution code (hidden until revealed) |
| explanation_zh | string | Explanation of solution |

### Quiz Question

**Purpose**: Knowledge checkpoint to validate learning outcomes.

| Field | Type | Validation |
|---|---|---|
| number | int | 1-based within chapter |
| question_zh | string | Question text |
| options | list[string] | 4 multiple-choice options (A/B/C/D) |
| correct_option | string | One of `A`, `B`, `C`, `D` |
| explanation_zh | string | Why the answer is correct |

### Glossary Term

**Purpose**: Key Python term with bilingual definition.

| Field | Type | Validation |
|---|---|---|
| term_en | string | English technical term |
| term_zh | string | Chinese translation |
| definition_zh | string | Explanation in Chinese |
| example | string | Short code usage example |
