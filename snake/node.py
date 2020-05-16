from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, next: Optional[Node] = None):
        self._next = next

    @property
    def next(self) -> Node:
        return self._next

    @next.setter
    def next(self, value: Node) -> None:
        if isinstance(value, Node):
            self._next = value
