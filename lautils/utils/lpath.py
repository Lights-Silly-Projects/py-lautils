from __future__ import annotations

from os import path
from pathlib import Path
from typing import Any, Union

__all__: list[str] = [
    "LPath", "LPathLike"
]


class LPath(Path):
    """An extension built on top of the Path class."""
    _flavour = type(Path())._flavour  # type: ignore

    def format(self, *args: Any, **kwargs: Any) -> LPath:
        """Format an LPath like you would a regular string."""
        return LPath(self.to_str().format(*args, **kwargs))

    def to_str(self) -> str:
        """Helper to convert an LPath to a string without having to jump back and forth in the editor."""
        return str(self)

    def startswith(self, prefix: str | tuple[str, ...]) -> bool:
        """Checks whether the path starts with a given prefix or list of prefixes."""
        return self.to_str().startswith(prefix)

    def endswith(self, suffix: str | tuple[str, ...]) -> bool:
        """Checks whether the path ends with a given suffix or list of suffixes."""
        return self.to_str().endswith(suffix)

    def get_top(self) -> LPath:
        """Get the top directory of the LPath."""
        folder_path = self.resolve()

        if folder_path.is_dir():
            return folder_path

        return LPath(path.dirname(folder_path))


LPathLike = Union[str, Path, LPath]
"""A type that is something akin to an LPath and can trivially be passed to LPath."""
