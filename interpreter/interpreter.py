class TKInterpreter:

    def __init__(self):
        self.variables = {}

    def evaluate(self, node):

        if node is None:
            return None

        if node[0] == 'number':
            return node[1]

        elif node[0] == 'string':
            return node[1].strip('"')

        elif node[0] == 'var':
            return self.variables.get(node[1], 0)

        elif node[0] == 'add':
            return self.evaluate(node[1]) + self.evaluate(node[2])

        elif node[0] == 'sub':
            return self.evaluate(node[1]) - self.evaluate(node[2])

        elif node[0] == 'mul':
            return self.evaluate(node[1]) * self.evaluate(node[2])

        elif node[0] == 'div':
            return self.evaluate(node[1]) / self.evaluate(node[2])

        elif node[0] == 'gt':
            return self.evaluate(node[1]) > self.evaluate(node[2])

        elif node[0] == 'lt':
            return self.evaluate(node[1]) < self.evaluate(node[2])

        elif node[0] == 'eq':
            return self.evaluate(node[1]) == self.evaluate(node[2])

        else:
            raise Exception(f"Unknown node type: {node[0]}")

    def execute(self, tree):

        if tree is None:
            return

        if tree[0] == 'program':
            for stmt in tree[1]:
                self.execute(stmt)

        elif tree[0] == 'assign':
            name = tree[1]
            value = self.evaluate(tree[2])
            self.variables[name] = value

        elif tree[0] == 'print':
            print(self.evaluate(tree[1]))

        elif tree[0] == 'if':
            condition = self.evaluate(tree[1])
            if condition:
                self.execute(tree[2])

        elif tree[0] == 'block':
            for stmt in tree[1]:
                self.execute(stmt)

        elif tree[0] == 'while':
            while self.evaluate(tree[1]):
                self.execute(tree[2])

        else:
            raise Exception(f"Unknown statement: {tree[0]}")