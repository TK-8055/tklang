# TKLang Full Syntax Guide

## 1. Variables
```tk
x = 10
name = "tk"
print(x)
print(name)
```

## 2. Numbers
```tk
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```
- Number literals are integers (`\d+`).
- Division returns float.

## 3. Strings
```tk
msg = "hello tk"
print(msg)
```
- Strings use double quotes.

## 4. Booleans
```tk
flag = true
done = false
print(flag)
```

## 5. Comparison Operators
- `>`
- `<`
- `==`
- `>=`
- `<=`
- `!=`

```tk
x = 10
y = 5
if (x > y) {
    print("x greater")
}
```

## 6. Logical Operators
- `and`
- `or`
- `not`

```tk
if (x > 5 and y < 10) {
    print("valid")
}
```

## 7. If / Else
```tk
if (x > y) {
    print("x bigger")
} else {
    print("y bigger")
}
```

## 8. While Loop
```tk
i = 0
while (i < 3) {
    print(i)
    i = i + 1
}
```

## 9. For Loop
Supported headers:
- `for n in nums { ... }`
- `for (n in nums) { ... }`

```tk
nums = [1, 2, 3]
for n in nums {
    print(n)
}
```
- Loop variable is scoped to the loop (restored/removed after loop).

## 10. Break / Continue
```tk
while (true) {
    break
}

for n in [1, 2, 3] {
    continue
}
```

## 11. Lists
```tk
nums = [1, 2, 3]
print(nums)
print(nums[0])
```

## 12. Dictionaries
```tk
user = {
    "name": "tk",
    "age": 22
}
print(user["name"])
```
- Dictionary keys in literals are string keys only.

## 13. Indexing
Works with:
- list
- dictionary
- string

```tk
print([10, 20, 30][1])
print("tk"[0])
```

## 14. Functions
Standard syntax:
```tk
function add(a, b) {
    return a + b
}
print(add(5, 3))
```

Short syntax:
```tk
add!(a, b) {
    return a + b
}
print(add(4, 5))
```

## 15. Return
```tk
function square(x) {
    return x * x
}
```

## 16. Input
```tk
name = input()
print(name)
```

## 17. Built-ins (Auto Loaded)
No import needed. Available at startup:
- `append(list, value)`
- `range(n)`
- `keys(dict)`
- `values(dict)`
- `pop(list)`
- `sort(list)`
- `sum(list)`
- `min(list)`
- `max(list)`
- `type(value)`
- `str(value)`
- `int(value)`

```tk
nums = [1, 2]
append(nums, 3)
print(nums)

for i in range(3) {
    print(i)
}
```

## 18. Length
```tk
print(len([1, 2, 3]))
print(len("tk"))
print(len({"a": 1}))
```

## 19. File Loading
```tk
data = load("tests/sample.csv")
print(len(data))
```
- Returns CSV rows as list of rows.
- Path must stay inside current working directory.

## 20. Comments
```tk
# this is a comment
x = 5
y = 3
print(x + y)
```

## 21. Expression Usage
Expressions are valid in:
- assignments
- conditions
- print
- function arguments
- standalone call statements

```tk
print(add(5, 3) + 10)
append([1], 2)
```

## 22. Blocks
Empty block is valid:
```tk
if (true) {
}
```

## 23. Error Types
Internal error classes:
- `TKLexerError`
- `TKParserError`
- `TKRuntimeError`

CLI error output format:
- Lexer: `TK Lexer Error: ...`
- Parser: `TK Parser Error: ...`
- Runtime: `TK Error: ...`

Examples:
- `TK Error: division by zero`
- `TK Error: return statement outside function`
- `TK Error: break statement outside loop`
- `TK Error: continue statement outside loop`

## 24. Run Program
```bash
tk program.tk
```
Or:
```bash
python -m cli.tk program.tk
```

## 25. Current Limits
- No unary minus literal form like `-5` (use `0 - 5`).
- `print` takes exactly one expression.
- `input` is only `input()` with no arguments.
