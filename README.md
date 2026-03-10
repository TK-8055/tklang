# TK Lang

<p align="center">
  <strong>A tiny language for big ML ideas.</strong><br/>
  Write less boilerplate. Run more experiments.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Status-Experimental-orange" alt="Experimental" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" />
  <img src="https://img.shields.io/badge/Built%20with-SLY-blue" alt="Built with SLY" />
</p>

## What Is TK Lang?

**TK Lang** is a minimal interpreted domain-specific language (DSL) designed to simplify machine learning workflows and data analysis.
It removes repetitive Python setup code and provides a clean, human-readable syntax.

TK Lang is an experimental DSL project developed with AI-assisted tooling.

## Why It Stands Out

- Fast to read and fast to write
- Simple syntax for beginners and rapid prototyping
- A simple interpreter architecture that is easy to extend
- Designed for future ML-first commands

## Quick Example

```tk
x = 10
y = 20
print(x + y)
print("TK Lang")
```

Output:

```text
30
TK Lang
```

## Example Program

```tk
nums = [1,2,3]

for n in nums {
    print(n)
}

function add(a,b) {
    print(a+b)
}

add(5,7)
```

Output:

```text
1
2
3
12
```

## Vision: ML in Plain Language

Future target syntax:

```tk
data = load("sales.csv")
model = linear_regression(data)
forecast(model, 30)
plot(model)
```

TK Lang will use Python's ML ecosystem under the hood while keeping a compact DSL interface.

## Current Features

| Feature | Status |
|---|---|
| Variables | Done |
| Numbers | Done |
| Strings | Done |
| Arithmetic (`+`, `-`, `*`, `/`) | Done |
| Comparisons (`>`, `<`, `==`) | Done |
| Print statements | Done |
| `if` statements | Done |
| `while` loops | Done |
| Functions | Done |
| Function parameters and arguments | Done |
| Lists | Done |
| `for` loops | Done |
| `len()` | Done |
| `load()` file loading | Done |
| Error messages | Done |
| Lexer -> Parser -> AST -> Interpreter pipeline | Done |

## Architecture

```text
.tk source file
    -> Lexer
    -> Parser
    -> AST
    -> Interpreter
    -> Program output
```

### Component Snapshot

- **Lexer**: Converts source text into tokens (`PRINT`, `ID`, `NUMBER`, `STRING`, etc.)
- **Parser**: Converts tokens into structured AST nodes
- **Interpreter**: Evaluates expressions and executes statements

Example AST:

```text
x = 10
('assign', 'x', ('number', 10))
```

## Project Structure

```text
tklang/
│
├── cli/
│   └── tk.py
├── lexer/
│   └── lexer.py
├── parser/
│   └── parser.py
├── interpreter/
│   └── interpreter.py
├── runtime/
├── tests/
│   └── run_tests.py
├── examples/
│   └── test.tk
├── README.md
└── LICENSE
```

## Quick Install

```bash
git clone https://github.com/TK-8055/tklang
cd tklang
pip install sly
python cli/tk.py examples/test.tk
```

## Getting Started

### Requirements

- Python 3.11+
- `sly`

Install dependency:

```bash
pip install sly
```

Optional: activate a virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Run a `.tk` file:

```bash
python cli/tk.py examples/test.tk
```

## Roadmap

Planned additions:

- DataFrame-like data operations
- Built-in EDA commands
- Automatic ML pipelines
- Time-series forecasting helpers
- NLP utilities
- Visualization commands
- Plugin system

## Tests

TK Lang includes automated regression tests to verify language features.

Run all tests:

```bash
python tests/run_tests.py
```

Current test coverage:

- Arithmetic
- Comparisons
- Variables
- Lists
- Loops
- Functions
- File loading
- Error handling

Example result:

```text
Summary: 14/14 tests passed
```

## Version

Current version: v0.1

## Development Status

TK Lang is currently **experimental**, actively evolving, and developed with AI-assisted tools.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes with clear commits.
4. Add or update examples/tests where relevant.
5. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a Pull Request and include:
   - What changed
   - Why it was needed
   - How to test it

### Contribution Ideas

- Add new language operators
- Improve parser error messages
- Add test coverage
- Add ML/EDA built-in commands
- Improve docs and tutorials

## 💡 Ideas & Discussions

[![Share Ideas](https://img.shields.io/badge/💡-Share%20Ideas-yellow)](https://github.com/<your-username>/tklang/discussions)

Have an idea for new syntax or features? Join the discussion!

## License

MIT License
