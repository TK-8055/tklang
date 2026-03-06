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

**TK Lang** is a minimal Domain-Specific Language (DSL) built to simplify machine learning workflows and data analysis.
It removes repetitive Python setup code and gives you a clean, human-readable syntax.

## Why It Stands Out

- Fast to read, fast to write
- Simple syntax for beginners and rapid prototyping
- Interpreter architecture that is easy to extend
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

## Vision: ML in Plain Language

Future syntax target:

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
| Addition (`+`) | Done |
| Print statements | Done |
| Lexer -> Parser -> AST -> Interpreter pipeline | Done |

## Architecture

```text
.tk source file
    -> Lexer (tokenizes input)
    -> Parser (builds AST)
    -> Interpreter (executes AST)
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
|
+-- cli/
|   +-- tk.py
+-- lexer/
|   +-- lexer.py
+-- parser/
|   +-- parser.py
+-- interpreter/
|   +-- interpreter.py
+-- runtime/
+-- examples/
|   +-- test.tk
+-- README.md
```

## Getting Started

### Requirements

- Python 3.11+
- `sly`

Install dependency:

```bash
pip install sly
```

(Optional) activate virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Run a `.tk` file:

```bash
python cli/tk.py examples/test.tk
```

## Roadmap

Planned additions:

- Subtraction, multiplication, division
- Conditional statements (`if`)
- Loops
- Functions
- Data loading helpers
- EDA commands
- ML automation helpers
- NLP utilities
- Forecasting tools

## Development Status

TK Lang is currently **experimental** and focused on learning language design while building a simplified ML interface.

## Contributing

Contributions are welcome and appreciated.

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
6. Open a Pull Request with:
   - What changed
   - Why it was needed
   - How to test it

### Contribution Ideas

- Add new language operators
- Improve parser error messages
- Add test coverage
- Add ML/EDA built-in commands
- Improve docs and tutorials

## License

MIT License
