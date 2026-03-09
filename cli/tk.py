import sys
from lexer.lexer import TKLexer
from parser.parser import TKParser
from interpreter.interpreter import TKInterpreter
from runtime.errors import BreakLoop, ContinueLoop, TKError, ReturnValue
from runtime.io import safe_open


def run(file):
    lexer = TKLexer()
    parser = TKParser()
    interpreter = TKInterpreter()

    try:
        with safe_open(file, encoding="utf-8") as f:
            code = f.read()
        tree = parser.parse(lexer.tokenize(code))
        interpreter.execute(tree)
        return 0
    except FileNotFoundError:
        print(f"TK Error: file not found: {file}", file=sys.stderr)
        return 1
    except ReturnValue:
        print("TK Error: return statement outside function", file=sys.stderr)
        return 1
    except BreakLoop:
        print("TK Error: break statement outside loop", file=sys.stderr)
        return 1
    except ContinueLoop:
        print("TK Error: continue statement outside loop", file=sys.stderr)
        return 1
    except TKError as e:
        print(str(e), file=sys.stderr)
        return 1


if __name__=="__main__":

    if len(sys.argv)<2:
        print("Usage: tk <file.tk>")
        sys.exit(1)

    sys.exit(run(sys.argv[1]))
