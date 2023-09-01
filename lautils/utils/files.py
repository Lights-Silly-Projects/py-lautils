import inspect

from .lpath import LPath

__all__: list[str] = [
    "get_caller_file",
]


def get_caller_file() -> LPath:
    """Obtain the caller's file as an LPath."""
    return LPath(inspect.stack()[2].filename)
