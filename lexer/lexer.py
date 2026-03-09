from sly import Lexer
from runtime.errors import TKLexerError


class TKLexer(Lexer):

    tokens = {
        'PRINT','STRING','NUMBER','ID',
        'LPAREN','RPAREN','COMMA',
        'LBRACE','RBRACE','LBRACKET','RBRACKET',
        'EQUALS','EQEQ','NEQ',
        'PLUS','MINUS','TIMES','DIVIDE',
        'GT','LT','GTE','LTE',
        'IF','ELSE','WHILE','FOR','IN','FUNCTION',
        'LEN','LOAD',
        'INPUT',
        'AND','OR','NOT',
        'RETURN',
        'BREAK','CONTINUE',
        'TRUE','FALSE',
        'COLON',
        'BANG'
    }

    ignore = " \t"
    ignore_comment = r'\#.*'

    keywords = {
        "print":"PRINT",
        "if":"IF",
        "else":"ELSE",
        "while":"WHILE",
        "for":"FOR",
        "in":"IN",
        "function":"FUNCTION",
        "len":"LEN",
        "load":"LOAD",
        "input":"INPUT",
        "and":"AND",
        "or":"OR",
        "not":"NOT",
        "return":"RETURN",
        "break":"BREAK",
        "continue":"CONTINUE",
        "true":"TRUE",
        "false":"FALSE"
    }

    STRING = r'"([^"\\]|\\.)*"'

    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    COLON = r':'

    LBRACE = r'\{'
    RBRACE = r'\}'

    LBRACKET = r'\['
    RBRACKET = r'\]'

    EQEQ = r'=='
    NEQ = r'!='
    EQUALS = r'='
    BANG = r'!'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'

    GTE = r'>='
    LTE = r'<='
    GT = r'>'
    LT = r'<'

    @_(r'\d+')
    def NUMBER(self,t):
        t.value=int(t.value)
        return t

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self,t):
        # Convert identifier to keyword token when it matches reserved words.
        t.type=self.keywords.get(t.value,"ID")
        return t

    @_(r'\n+')
    def newline(self,t):
        self.lineno+=len(t.value)

    def error(self,t):
        # Stop immediately so parser does not run on invalid token stream.
        raise TKLexerError(f"TK Lexer Error: illegal character '{t.value[0]}'")
