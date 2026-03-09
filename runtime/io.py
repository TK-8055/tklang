import os
from runtime.errors import TKRuntimeError


def validate_path_in_cwd(path):
    base = os.path.abspath(os.getcwd())
    full = os.path.abspath(path)

    try:
        if os.path.commonpath([base, full]) != base:
            raise TKRuntimeError("TK Error: invalid file path")
    except ValueError:
        raise TKRuntimeError("TK Error: invalid file path")

    return full


def safe_open(path, mode="r", encoding=None):
    full = validate_path_in_cwd(path)
    return open(full, mode, encoding=encoding)
