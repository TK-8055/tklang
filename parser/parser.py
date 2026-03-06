from sly import Parser
from lexer.lexer import TKLexer


class TKParser(Parser):

    tokens = TKLexer.tokens

    precedence = (
        ('left', 'PLUS'),
    )

    @_('ID EQUALS expr')
    def statement(self, p):
        return ('assign', p.ID, p.expr)

    @_('PRINT LPAREN expr RPAREN')
    def statement(self, p):
        return ('print', p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)