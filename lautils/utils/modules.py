import inspect
from typing import TypeVar


__all__: list[str] = [
    "get_caller_module",
    "get_all_functions"
]

def get_caller_module() -> str:
    """Obtain the caller's module name as a string."""
    return inspect.stack()[2].filename


def get_all_functions(module: object) -> list[tuple[str, TypeVar("_T")]]:
    """Get a tuple containing all the names and functions of a given module object."""
    return inspect.getmembers(module, inspect.isfunction)
