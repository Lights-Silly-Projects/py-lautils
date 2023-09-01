import inspect

__all__: list[str] = [
    "get_caller_filename"
]


def get_caller_filename() -> str:
    """Obtain the caller's filename."""
    return inspect.stack()[2].filename
