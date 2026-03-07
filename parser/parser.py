from sly import Parser
from lexer.lexer import TKLexer


class TKParser(Parser):

    tokens = TKLexer.tokens

    precedence = (
        ('left','PLUS','MINUS'),
        ('left','TIMES','DIVIDE'),
    )

    # program
    @_('statements')
    def program(self, p):
        return ('program', p.statements)

    # multiple statements
    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    # assignment
    @_('ID EQUALS expr')
    def statement(self, p):
        return ('assign', p.ID, p.expr)

    # print
    @_('PRINT LPAREN expr RPAREN')
    def statement(self, p):
        return ('print', p.expr)

    # if
    @_('IF LPAREN expr RPAREN block')
    def statement(self, p):
        return ('if', p.expr, p.block)

    # while
    @_('WHILE LPAREN expr RPAREN block')
    def statement(self, p):
        return ('while', p.expr, p.block)

    # block
    @_('LBRACE statements RBRACE')
    def block(self, p):
        return ('block', p.statements)

    # expressions
    @_('expr GT expr')
    def expr(self, p):
        return ('gt', p.expr0, p.expr1)

    @_('expr LT expr')
    def expr(self, p):
        return ('lt', p.expr0, p.expr1)

    @_('expr EQEQ expr')
    def expr(self, p):
        return ('eq', p.expr0, p.expr1)

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

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)