from sly import Lexer


class TKLexer(Lexer):

    tokens = {
        'PRINT','STRING','NUMBER','ID',
        'LPAREN','RPAREN',
        'LBRACE','RBRACE',
        'EQUALS','EQEQ',
        'PLUS','MINUS','TIMES','DIVIDE',
        'GT','LT',
        'IF' , 'WHILE'
    }

    ignore = " \t"

    PRINT = r'print'
    IF = r'if'
    WHILE= r'while'

    STRING = r'"[^"]*"'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'

    EQEQ = r'=='
    EQUALS = r'='

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'

    GT = r'>'
    LT = r'<'


    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print("Illegal character:", t.value[0])
        self.index += 1