# TKLang

TKLang is a small interpreted scripting language built for learning
language design and building DSLs.

It includes a full interpreter pipeline:
lexer -> parser -> AST -> interpreter -> runtime.

## Features

- Variables, numbers, strings, booleans
- Arithmetic: `+`, `-`, `*`, `/`
- Comparisons: `>`, `<`, `==`, `!=`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`
- Control flow: `if`, `if/else`, `while`, `for`, `break`, `continue`
- Collections: lists, dictionaries, indexing
- Functions: standard `function name(...) {}` and short `name!(...) {}`
- `return` with proper function return propagation
- Built-ins:
  - Core: `print(...)`, `len(...)`, `input()`, `load("file.csv")`
  - Auto-loaded stdlib: `append`, `range`, `keys`, `values`, `pop`, `sort`, `sum`, `min`, `max`, `type`, `str`, `int`
- Comments: `# ...`
- Typed error classes and CLI error handling
- File path safety for CLI source files and `load(...)` paths

## Full Syntax

See [SYNTAX.md](./SYNTAX.md) for complete grammar and examples.

## Quick Example

```tk
x = 10
y = 5
print(x + y)

nums = [1, 2, 3]
append(nums, 4)

for n in nums {
    print(n)
}

add!(a, b) {
    return a + b
}

print(add(7, 8))
```

Example output:

```text
15
1
2
3
4
```

## Installation

```bash
git clone https://github.com/<your-username>/tklang
cd tklang
pip install sly
```

## Run

```bash
python -m cli.tk examples/test.tk
```

If you set up a shell alias/entry point:

```bash
tk examples/test.tk
```

## Tests

Run full test suite:

```bash
python tests/run_tests.py
```

## Project Structure

```text
tklang/
|-- cli/
|   `-- tk.py
|-- lexer/
|   `-- lexer.py
|-- parser/
|   `-- parser.py
|-- interpreter/
|   `-- interpreter.py
|-- runtime/
|   |-- errors.py
|   `-- io.py
|-- tests/
|   `-- run_tests.py
|-- examples/
|   `-- test.tk
|-- SYNTAX.md
`-- README.md
```

## Architecture

```text
TKLang Program
      |
      v
    Lexer
      |
      v
    Parser
      |
      v
      AST
      |
      v
 Interpreter
      |
      v
   Runtime
```

## Goals

- Simple scripting language for practical local scripting
- Educational interpreter architecture
- Platform for future ML-oriented DSL features

## Version

Current version: `v1.0`

## Status

TKLang is stable for local scripting and educational language development.

## License

MIT
