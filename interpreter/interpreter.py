import csv


class TKInterpreter:

    def __init__(self):
        self.variables={}
        self.functions={}

    def error(self,msg):
        raise Exception(f"TK Error: {msg}")

    def evaluate(self,node):

        if node[0]=='number':
            # Number literals are already converted by the lexer.
            return node[1]

        elif node[0]=='string':
            # Parser stores token text with quotes; remove them for runtime.
            return node[1].strip('"')

        elif node[0]=='var':
            # Variable read from current scope.
            if node[1] not in self.variables:
                self.error(f"unknown variable {node[1]}")
            return self.variables[node[1]]

        elif node[0]=='list':
            # Evaluate each element expression to build runtime list.
            return [self.evaluate(x) for x in node[1]]

        elif node[0]=='add':
            return self.evaluate(node[1]) + self.evaluate(node[2])

        elif node[0]=='sub':
            return self.evaluate(node[1]) - self.evaluate(node[2])

        elif node[0]=='mul':
            return self.evaluate(node[1]) * self.evaluate(node[2])

        elif node[0]=='div':
            b=self.evaluate(node[2])
            if b==0:
                self.error("division by zero")
            return self.evaluate(node[1]) / b

        elif node[0]=='gt':
            return self.evaluate(node[1]) > self.evaluate(node[2])

        elif node[0]=='lt':
            return self.evaluate(node[1]) < self.evaluate(node[2])

        elif node[0]=='eq':
            return self.evaluate(node[1]) == self.evaluate(node[2])

        elif node[0]=='len':
            # len() works for list and string values.
            return len(self.evaluate(node[1]))

        elif node[0]=='load':

            filename=self.evaluate(node[1])

            if not isinstance(filename,str):
                self.error("load() expects filename string")

            data=[]

            try:
                with open(filename) as f:
                    reader=csv.reader(f)
                    for r in reader:
                        data.append(r)
            except FileNotFoundError:
                self.error(f"file not found: {filename}")

            return data

        else:
            self.error(f"unknown node type {node[0]}")

    def execute(self,tree):

        if tree[0]=='program':
            # Program executes top-level statements sequentially.
            for s in tree[1]:
                self.execute(s)

        elif tree[0]=='assign':
            # Assignment stores evaluated value in current variable scope.
            self.variables[tree[1]]=self.evaluate(tree[2])

        elif tree[0]=='print':
            print(self.evaluate(tree[1]))

        elif tree[0]=='block':
            for s in tree[1]:
                self.execute(s)

        elif tree[0]=='if':
            if self.evaluate(tree[1]):
                self.execute(tree[2])

        elif tree[0]=='while':
            while self.evaluate(tree[1]):
                self.execute(tree[2])

        elif tree[0]=='for':

            var=tree[1]
            iterable=self.evaluate(tree[2])

            for v in iterable:
                # Rebind loop variable for each item, then run body block.
                self.variables[var]=v
                self.execute(tree[3])

        elif tree[0]=='function':

            name=tree[1]
            params=tree[2]
            block=tree[3]

            # Store function definition for later calls.
            self.functions[name]=(params,block)

        elif tree[0]=='call':

            name=tree[1]
            args=tree[2]

            if name not in self.functions:
                self.error(f"unknown function {name}")

            params,block=self.functions[name]

            if len(params)!=len(args):
                self.error("argument mismatch")

            old=self.variables.copy()

            try:

                for p,a in zip(params,args):
                    # Bind argument values to function parameter names.
                    self.variables[p]=self.evaluate(a)

                self.execute(block)

            finally:
                # Always restore caller scope, even if function body fails.
                self.variables=old

        else:
            self.error(f"unknown statement {tree[0]}")
