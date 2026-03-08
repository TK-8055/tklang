import sys
from lexer.lexer import TKLexer
from parser.parser import TKParser
from interpreter.interpreter import TKInterpreter


def run(file):

    with open(file) as f:
        code=f.read()

    lexer=TKLexer()
    parser=TKParser()
    interpreter=TKInterpreter()

    tree=parser.parse(lexer.tokenize(code))

    if tree is None:
        # Guard: do not execute when parsing fails.
        print("TK Error: parsing failed")
        return

    interpreter.execute(tree)


if __name__=="__main__":

    if len(sys.argv)<2:
        print("Usage: tk <file.tk>")
        sys.exit(1)

    run(sys.argv[1])
