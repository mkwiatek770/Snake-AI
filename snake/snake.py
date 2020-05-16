
from __future__ import annotations
from typing import List, Collection
from snake.node import Node
from snake.utils import Direction


class Snake:
    _speed: int = 3
    alive: bool = True

    def __init__(self, nodes: Collection[Node] = None, turns: Collection[Node] = None):
        self._nodes = list(nodes) if nodes else []
        self._turns = list(turns) if turns else []

    @property
    def head(self) -> Node:
        return self._nodes[0]
    
    @property
    def speed(self) -> int:
        return self._speed

    @property
    def is_alive(self) -> bool:
        return self.alive

    def turn(self, direction: Direction):
        if (direction == Direction.left and self.head.direction == Direction.right or 
            direction == Direction.right and self.head.direction == Direction.left or
            direction == Direction.up and self.head.direction == Direction.down or
            direction == Direction.down and self.head.direction == Direction.up):
            return
        self._turns.append((self.head.x, self.head.y, direction))

    def move(self):
        pass
