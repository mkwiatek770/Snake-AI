from __future__ import annotations
from typing import Optional
from app.utils import Direction


class Node:

    size = 10

    def __init__(self, x: int, y: int, direction: Direction, next_node: Optional[Node] = None):
        self.x = x
        self.y = y
        self.direction = direction
        self._next_node = next_node

    @property
    def next_node(self) -> Node:
        return self._next_node

    @next_node.setter
    def next_node(self, value: Node) -> None:
        if isinstance(value, Node):
            self._next_node = value
