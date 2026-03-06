from sly import Parser
from lexer.lexer import TKLexer


class TKParser(Parser):

    tokens = TKLexer.tokens

    precedence = (
        ('left','PLUS','MINUS'),
        ('left','TIMES','DIVIDE'),
    )

    @_('ID EQUALS expr')
    def statement(self,p):
        return ('assign',p.ID,p.expr)

    @_('PRINT LPAREN expr RPAREN')
    def statement(self,p):
        return ('print',p.expr)

    @_('expr PLUS expr')
    def expr(self,p):
        return ('add',p.expr0,p.expr1)

    @_('expr MINUS expr')
    def expr(self,p):
        return ('sub',p.expr0,p.expr1)

    @_('expr TIMES expr')
    def expr(self,p):
        return ('mul',p.expr0,p.expr1)

    @_('expr DIVIDE expr')
    def expr(self,p):
        return ('div',p.expr0,p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self,p):
        return p.expr

    @_('NUMBER')
    def expr(self,p):
        return ('number',p.NUMBER)

    @_('STRING')
    def expr(self,p):
        return ('string',p.STRING)

    @_('ID')
    def expr(self,p):
        return ('var',p.ID)