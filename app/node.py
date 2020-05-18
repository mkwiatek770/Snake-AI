from __future__ import annotations
from typing import Optional
from app.utils import Direction


class Node:
    def __init__(self, x: int, y: int, direction: Direction, next: Optional[Node] = None):
        self.x = x
        self.y = x
        self.direction = direction
        self._next = next

    @property
    def next(self) -> Node:
        return self._next

    @next.setter
    def next(self, value: Node) -> None:
        if isinstance(value, Node):
            self._next = value
