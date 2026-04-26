# hello_python.cli

**Purpose:** Click-based CLI tool. Entry: `hello` command. Dynamically loads subcommands from `commands/` directory.

## STRUCTURE
```
cli/
├── __init__.py            # CLI entry: @click.group(), main(), built-in commands
└── commands/
    ├── __init__.py        # Dynamic command loader: get_commands()
    ├── agent.py           # `hello agent` — FastAPI agent service management
    └── fastapi.py         # `hello fastapi` — Generic FastAPI service management
```

## WHERE TO LOOK
| Need | File |
|------|------|
| Add built-in command | `__init__.py` (add `@cli.command()`) |
| Add complex command group | `commands/*.py` (new file) |
| CLI entry point | `main()` in `__init__.py` |
| Command auto-discovery | `get_commands()` in `commands/__init__.py` |

## CONVENTIONS
- Built-in commands defined directly in `__init__.py` with `@cli.command()`
- Complex commands live in `commands/` directory as separate modules
- Dynamic loader: `get_commands()` scans `commands/*.py`, imports, extracts variable matching filename
- **CRITICAL**: Command filename MUST match the variable name (e.g., `fastapi.py` → `fastapi = cli.Command()`)
- Entry point registered in pyproject.toml: `hello = hello_python.cli:main`

## ANTI-PATTERNS
- Dynamic loader is fragile — relies on `filename[:-3] == variable_name` convention. Rename either and command breaks.
- Typo in log message: "dynmaically load and regester command"
- No `--version` flag configured

## COMMANDS
```bash
hello greet "Name"    # Greet a user
hello user "Name"     # User NAME
hello agent [cmd]     # Agent service management
hello fastapi [cmd]   # FastAPI service management
```
