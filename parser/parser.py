from sly import Parser
from lexer.lexer import TKLexer
from runtime.errors import TKParserError


class TKParser(Parser):

    tokens = TKLexer.tokens

    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQEQ', 'NEQ'),
        ('left', 'GT', 'LT', 'GTE', 'LTE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UNOT'),
    )

    @_('statements')
    def program(self, p):
        return ('program', p.statements)

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('ID EQUALS expr')
    def statement(self, p):
        return ('assign', p.ID, p.expr)

    @_('PRINT LPAREN expr RPAREN')
    def statement(self, p):
        return ('print', p.expr)

    @_('IF LPAREN expr RPAREN block')
    def statement(self, p):
        return ('if', p.expr, p.block)

    @_('IF LPAREN expr RPAREN block ELSE block')
    def statement(self, p):
        return ('ifelse', p.expr, p.block0, p.block1)

    @_('WHILE LPAREN expr RPAREN block')
    def statement(self, p):
        return ('while', p.expr, p.block)

    @_('FOR for_header block')
    def statement(self, p):
        return ('for', p.for_header[0], p.for_header[1], p.block)

    @_('ID IN expr')
    def for_header(self, p):
        return (p.ID, p.expr)

    @_('LPAREN ID IN expr RPAREN')
    def for_header(self, p):
        return (p.ID, p.expr)

    @_('FUNCTION ID LPAREN params RPAREN block')
    def statement(self, p):
        return ('function', p.ID, p.params, p.block)

    @_('ID BANG LPAREN params RPAREN block')
    def statement(self, p):
        return ('function', p.ID, p.params, p.block)

    @_('RETURN expr')
    def statement(self, p):
        return ('return', p.expr)

    @_('BREAK')
    def statement(self, p):
        return ('break',)

    @_('CONTINUE')
    def statement(self, p):
        return ('continue',)

    @_('call')
    def statement(self, p):
        return ('exprstmt', p.call)

    @_('LBRACE statements RBRACE')
    def block(self, p):
        return ('block', p.statements)

    @_('LBRACE RBRACE')
    def block(self, p):
        return ('block', [])

    @_('ID LPAREN args RPAREN')
    def call(self, p):
        return ('call', p.ID, p.args)

    @_('INPUT LPAREN RPAREN')
    def expr(self, p):
        return ('input',)

    @_('expr OR expr')
    def expr(self, p):
        return ('or', p.expr0, p.expr1)

    @_('expr AND expr')
    def expr(self, p):
        return ('and', p.expr0, p.expr1)

    @_('NOT expr %prec UNOT')
    def expr(self, p):
        return ('not', p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('expr GT expr')
    def expr(self, p):
        return ('gt', p.expr0, p.expr1)

    @_('expr LT expr')
    def expr(self, p):
        return ('lt', p.expr0, p.expr1)

    @_('expr EQEQ expr')
    def expr(self, p):
        return ('eq', p.expr0, p.expr1)

    @_('expr NEQ expr')
    def expr(self, p):
        return ('neq', p.expr0, p.expr1)

    @_('expr GTE expr')
    def expr(self, p):
        return ('gte', p.expr0, p.expr1)

    @_('expr LTE expr')
    def expr(self, p):
        return ('lte', p.expr0, p.expr1)

    @_('expr LBRACKET expr RBRACKET')
    def expr(self, p):
        return ('index', p.expr0, p.expr1)

    @_('LEN LPAREN expr RPAREN')
    def expr(self, p):
        return ('len', p.expr)

    @_('LOAD LPAREN expr RPAREN')
    def expr(self, p):
        return ('load', p.expr)

    @_('LBRACKET elements RBRACKET')
    def expr(self, p):
        return ('list', p.elements)

    @_('LBRACE dict_elements RBRACE')
    def expr(self, p):
        return ('dict', p.dict_elements)

    @_('call')
    def expr(self, p):
        return p.call

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)

    @_('TRUE')
    def expr(self, p):
        return ('bool', True)

    @_('FALSE')
    def expr(self, p):
        return ('bool', False)

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)

    @_('elements COMMA expr')
    def elements(self, p):
        return p.elements + [p.expr]

    @_('expr')
    def elements(self, p):
        return [p.expr]

    @_('')
    def elements(self, p):
        return []

    @_('dict_elements COMMA dict_pair')
    def dict_elements(self, p):
        return p.dict_elements + [p.dict_pair]

    @_('dict_pair')
    def dict_elements(self, p):
        return [p.dict_pair]

    @_('')
    def dict_elements(self, p):
        return []

    @_('STRING COLON expr')
    def dict_pair(self, p):
        return (p.STRING.strip('"'), p.expr)

    @_('params COMMA ID')
    def params(self, p):
        return p.params + [p.ID]

    @_('ID')
    def params(self, p):
        return [p.ID]

    @_('')
    def params(self, p):
        return []

    @_('args COMMA expr')
    def args(self, p):
        return p.args + [p.expr]

    @_('expr')
    def args(self, p):
        return [p.expr]

    @_('')
    def args(self, p):
        return []

    def error(self, token):
        if token is None:
            raise TKParserError("TK Parser Error: unexpected end of input")
        raise TKParserError(
            f"TK Parser Error: unexpected token '{token.value}' at line {token.lineno}"
        )
