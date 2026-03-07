import sys
from lexer.lexer import TKLexer
from parser.parser import TKParser
from interpreter.interpreter import TKInterpreter


def run(file):

    with open(file) as f:
        code = f.read()

    lexer = TKLexer()
    parser = TKParser()
    interpreter = TKInterpreter()

    tree = parser.parse(lexer.tokenize(code))

    if tree is not None:
        interpreter.execute(tree)


if __name__ == "__main__":
    run(sys.argv[1])