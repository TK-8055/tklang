import csv
from runtime.errors import (
    BreakLoop,
    ContinueLoop,
    ReturnValue,
    TKRuntimeError,
)
from runtime.io import safe_open


class TKInterpreter:

    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.load_stdlib()

    def load_stdlib(self):
        self.functions["append"] = (["list", "value"], ("builtin", "append"))
        self.functions["range"] = (["n"], ("builtin", "range"))
        self.functions["keys"] = (["dict"], ("builtin", "keys"))
        self.functions["values"] = (["dict"], ("builtin", "values"))
        self.functions["pop"] = (["list"], ("builtin", "pop"))
        self.functions["sort"] = (["list"], ("builtin", "sort"))
        self.functions["sum"] = (["list"], ("builtin", "sum"))
        self.functions["min"] = (["list"], ("builtin", "min"))
        self.functions["max"] = (["list"], ("builtin", "max"))
        self.functions["type"] = (["value"], ("builtin", "type"))
        self.functions["str"] = (["value"], ("builtin", "str"))
        self.functions["int"] = (["value"], ("builtin", "int"))

    def error(self, msg):
        raise TKRuntimeError(f"TK Error: {msg}")

    def evaluate(self, node):

        if node[0] == 'number':
            return node[1]

        if node[0] == 'string':
            return node[1].strip('"')

        if node[0] == 'bool':
            return node[1]

        if node[0] == 'var':
            if node[1] not in self.variables:
                self.error(f"unknown variable {node[1]}")
            return self.variables[node[1]]

        if node[0] == 'list':
            return [self.evaluate(x) for x in node[1]]

        if node[0] == 'dict':
            result = {}
            for key, value_expr in node[1]:
                result[key] = self.evaluate(value_expr)
            return result

        if node[0] == 'index':
            obj = self.evaluate(node[1])
            idx = self.evaluate(node[2])
            try:
                return obj[idx]
            except (TypeError, KeyError, IndexError):
                self.error(f"invalid index access: {idx}")

        if node[0] == 'add':
            return self.evaluate(node[1]) + self.evaluate(node[2])

        if node[0] == 'sub':
            return self.evaluate(node[1]) - self.evaluate(node[2])

        if node[0] == 'mul':
            return self.evaluate(node[1]) * self.evaluate(node[2])

        if node[0] == 'div':
            b = self.evaluate(node[2])
            if b == 0:
                self.error("division by zero")
            result = self.evaluate(node[1]) / b
            if result != result:  # NaN check
                self.error("invalid numeric operation")
            return result

        if node[0] == 'gt':
            return self.evaluate(node[1]) > self.evaluate(node[2])

        if node[0] == 'lt':
            return self.evaluate(node[1]) < self.evaluate(node[2])

        if node[0] == 'eq':
            return self.evaluate(node[1]) == self.evaluate(node[2])

        if node[0] == 'neq':
            return self.evaluate(node[1]) != self.evaluate(node[2])

        if node[0] == 'gte':
            return self.evaluate(node[1]) >= self.evaluate(node[2])

        if node[0] == 'lte':
            return self.evaluate(node[1]) <= self.evaluate(node[2])

        if node[0] == 'and':
            left = self.evaluate(node[1])
            return left and self.evaluate(node[2])

        if node[0] == 'or':
            left = self.evaluate(node[1])
            return left or self.evaluate(node[2])

        if node[0] == 'not':
            return not self.evaluate(node[1])

        if node[0] == 'len':
            try:
                return len(self.evaluate(node[1]))
            except TypeError:
                self.error("len() expects list, dict, or string")

        if node[0] == 'load':
            filename = self.evaluate(node[1])
            if not isinstance(filename, str):
                self.error("load() expects filename string")

            data = []
            try:
                with safe_open(filename, encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
            except FileNotFoundError:
                self.error(f"file not found: {filename}")
            return data

        if node[0] == 'input':
            return input()

        if node[0] == 'call':
            return self.call_function(node[1], node[2])

        self.error(f"unknown node type {node[0]}")

    def call_function(self, name, args):
        if name not in self.functions:
            self.error(f"unknown function {name}")

        params, block = self.functions[name]
        if len(params) != len(args):
            self.error("argument mismatch")

        if block[0] == "builtin":
            return self.run_builtin(block[1], args)

        old_variables = self.variables.copy()
        result = None

        try:
            for param, arg_expr in zip(params, args):
                self.variables[param] = self.evaluate(arg_expr)
            self.execute(block)
        except ReturnValue as returned:
            result = returned.value
        finally:
            self.variables = old_variables

        return result

    def run_builtin(self, name, args):
        values = [self.evaluate(arg) for arg in args]

        if name == "append":
            if not isinstance(values[0], list):
                self.error("append() expects list as first argument")
            values[0].append(values[1])
            return None

        if name == "range":
            if not isinstance(values[0], int):
                self.error("range() expects integer")
            return list(range(values[0]))

        if name == "keys":
            if not isinstance(values[0], dict):
                self.error("keys() expects dictionary")
            return list(values[0].keys())

        if name == "values":
            if not isinstance(values[0], dict):
                self.error("values() expects dictionary")
            return list(values[0].values())

        if name == "pop":
            if not isinstance(values[0], list):
                self.error("pop() expects list")
            if not values[0]:
                self.error("pop() from empty list")
            return values[0].pop()

        if name == "sort":
            if not isinstance(values[0], list):
                self.error("sort() expects list")
            values[0].sort()
            return None

        if name == "sum":
            if not isinstance(values[0], list):
                self.error("sum() expects list")
            return sum(values[0])

        if name == "min":
            if not isinstance(values[0], list):
                self.error("min() expects list")
            return min(values[0])

        if name == "max":
            if not isinstance(values[0], list):
                self.error("max() expects list")
            return max(values[0])

        if name == "type":
            value = values[0]
            if isinstance(value, bool):
                return "bool"
            if isinstance(value, int):
                return "number"
            if isinstance(value, str):
                return "string"
            if isinstance(value, list):
                return "list"
            if isinstance(value, dict):
                return "dict"
            if value is None:
                return "null"
            return "unknown"

        if name == "str":
            return str(values[0])

        if name == "int":
            try:
                return int(values[0])
            except (TypeError, ValueError):
                self.error("int() conversion failed")

        self.error(f"unknown builtin {name}")

    def execute(self, tree):

        if tree[0] == 'program':
            for statement in tree[1]:
                self.execute(statement)
            return

        if tree[0] == 'assign':
            self.variables[tree[1]] = self.evaluate(tree[2])
            return

        if tree[0] == 'print':
            print(self.evaluate(tree[1]))
            return

        if tree[0] == 'block':
            for statement in tree[1]:
                self.execute(statement)
            return

        if tree[0] == 'if':
            if self.evaluate(tree[1]):
                self.execute(tree[2])
            return

        if tree[0] == 'ifelse':
            if self.evaluate(tree[1]):
                self.execute(tree[2])
            else:
                self.execute(tree[3])
            return

        if tree[0] == 'while':
            while self.evaluate(tree[1]):
                try:
                    self.execute(tree[2])
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
            return

        if tree[0] == 'for':
            var = tree[1]
            iterable = self.evaluate(tree[2])
            sentinel = object()
            old = self.variables.get(var, sentinel)

            try:
                for value in iterable:
                    self.variables[var] = value
                    try:
                        self.execute(tree[3])
                    except BreakLoop:
                        break
                    except ContinueLoop:
                        continue
            finally:
                if old is sentinel:
                    self.variables.pop(var, None)
                else:
                    self.variables[var] = old
            return

        if tree[0] == 'function':
            self.functions[tree[1]] = (tree[2], tree[3])
            return

        if tree[0] == 'return':
            raise ReturnValue(self.evaluate(tree[1]))

        if tree[0] == 'break':
            raise BreakLoop()

        if tree[0] == 'continue':
            raise ContinueLoop()

        if tree[0] == 'exprstmt':
            self.evaluate(tree[1])
            return

        self.error(f"unknown statement {tree[0]}")
