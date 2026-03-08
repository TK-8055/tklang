from sly import Parser
from lexer.lexer import TKLexer


class TKParser(Parser):

    tokens = TKLexer.tokens

    precedence = (
        ('left','EQEQ'),
        ('left','GT','LT'),
        ('left','PLUS','MINUS'),
        ('left','TIMES','DIVIDE'),
    )

    @_('statements')
    def program(self,p):
        # Root node: execute these statements in order.
        return ('program',p.statements)

    @_('statements statement')
    def statements(self,p):
        return p.statements+[p.statement]

    @_('statement')
    def statements(self,p):
        return [p.statement]

    @_('ID EQUALS expr')
    def statement(self,p):
        # Variable assignment: name = evaluated expression.
        return ('assign',p.ID,p.expr)

    @_('PRINT LPAREN expr RPAREN')
    def statement(self,p):
        return ('print',p.expr)

    @_('IF LPAREN expr RPAREN block')
    def statement(self,p):
        return ('if',p.expr,p.block)

    @_('WHILE LPAREN expr RPAREN block')
    def statement(self,p):
        return ('while',p.expr,p.block)

    @_('FOR for_header block')
    def statement(self,p):
        # Normalized for-loop AST for both header syntaxes.
        return ('for',p.for_header[0],p.for_header[1],p.block)

    @_('ID IN expr')
    def for_header(self,p):
        return (p.ID,p.expr)

    @_('LPAREN ID IN expr RPAREN')
    def for_header(self,p):
        return (p.ID,p.expr)

    @_('FUNCTION ID LPAREN params RPAREN block')
    def statement(self,p):
        # Function declaration stores name, parameter names, and body block.
        return ('function',p.ID,p.params,p.block)

    @_('ID LPAREN args RPAREN')
    def statement(self,p):
        # Function call with positional arguments.
        return ('call',p.ID,p.args)

    @_('params COMMA ID')
    def params(self,p):
        return p.params+[p.ID]

    @_('ID')
    def params(self,p):
        return [p.ID]

    @_('')
    def params(self,p):
        return []

    @_('args COMMA expr')
    def args(self,p):
        return p.args+[p.expr]

    @_('expr')
    def args(self,p):
        return [p.expr]

    @_('')
    def args(self,p):
        return []

    @_('LBRACE statements RBRACE')
    def block(self,p):
        # Block wraps a list of statements for if/while/for/function bodies.
        return ('block',p.statements)

    @_('LBRACE RBRACE')
    def block(self,p):
        # Empty block support: {}.
        return ('block',[])

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

    @_('expr GT expr')
    def expr(self,p):
        return ('gt',p.expr0,p.expr1)

    @_('expr LT expr')
    def expr(self,p):
        return ('lt',p.expr0,p.expr1)

    @_('expr EQEQ expr')
    def expr(self,p):
        return ('eq',p.expr0,p.expr1)

    @_('LEN LPAREN expr RPAREN')
    def expr(self,p):
        # len(expr) node; interpreter applies Python len() on runtime value.
        return ('len',p.expr)

    @_('LOAD LPAREN expr RPAREN')
    def expr(self,p):
        # load(expr) node; expr must evaluate to a filename string.
        return ('load',p.expr)

    @_('LBRACKET elements RBRACKET')
    def expr(self,p):
        # List literal: [a, b, c].
        return ('list',p.elements)

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

    @_('elements COMMA expr')
    def elements(self,p):
        return p.elements+[p.expr]

    @_('expr')
    def elements(self,p):
        return [p.expr]

    @_('')
    def elements(self,p):
        return []
