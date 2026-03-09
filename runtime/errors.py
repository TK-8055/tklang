class TKError(Exception):
    pass


class TKLexerError(TKError):
    pass


class TKParserError(TKError):
    pass


class TKRuntimeError(TKError):
    pass


class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value


class BreakLoop(Exception):
    pass


class ContinueLoop(Exception):
    pass
