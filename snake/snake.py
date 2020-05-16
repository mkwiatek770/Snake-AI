
from __future__ import annotations
from typing import List, Collection
from snake.node import Node


class Snake:
    _speed: int = 3

    def __init__(self, nodes: Collection[Node] = None, turns: Collection[Node] = None):
        self._nodes = list(nodes) if nodes else []
        self._turns = list(turns) if turns else []

    @property
    def head(self) -> Node:
        return self._nodes[0]
    
    @property
    def speed(self) -> int:
        return self._speed
