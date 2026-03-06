class TKInterpreter:

    def __init__(self):
        self.variables = {}

    def evaluate(self,node):

        if node[0]=='number':
            return node[1]

        if node[0]=='string':
            return node[1].strip('"')

        if node[0]=='var':
            return self.variables.get(node[1],0)

        if node[0]=='add':
            return self.evaluate(node[1]) + self.evaluate(node[2])

        if node[0]=='sub':
            return self.evaluate(node[1]) - self.evaluate(node[2])

        if node[0]=='mul':
            return self.evaluate(node[1]) * self.evaluate(node[2])

        if node[0]=='div':
            return self.evaluate(node[1]) / self.evaluate(node[2])

    def execute(self,tree):

        if tree[0]=='assign':
            name = tree[1]
            value = self.evaluate(tree[2])
            self.variables[name] = value

        elif tree[0]=='print':
            print(self.evaluate(tree[1]))