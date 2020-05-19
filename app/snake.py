from __future__ import annotations
from typing import List, Collection
from app.node import Node
from app.utils import Direction, NODE_SIZE


class Snake:
    _speed: int = 3
    alive: bool = True

    def __init__(self, nodes: Collection[Node] = None, turns: Collection[Node] = None):
        self._nodes = list(nodes) if nodes else [Node(100, i, Direction.up) for i in range(100, 130, NODE_SIZE)]
        self._turns = list(turns) if turns else []

    @property
    def head(self) -> Node:
        return self._nodes[0]

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def nodes(self) -> Collection[Node]:
        return self._nodes

    @property
    def is_alive(self) -> bool:
        return self.alive

    def turn(self, direction: Direction):
        if (direction == Direction.left and self.head.direction == Direction.right or
                direction == Direction.right and self.head.direction == Direction.left or
                direction == Direction.up and self.head.direction == Direction.down or
                direction == Direction.down and self.head.direction == Direction.up):
            return
        self._turns.append(Node(self.head.x, self.head.y, direction))

    def move(self):
        for node in self.nodes:
            direction = node.direction.value
            if direction == 'UP':
                node.y -= self.speed
            elif direction == 'DOWN':
                node.y += self.speed
            elif direction == 'LEFT':
                node.x -= self.speed
            elif direction == 'RIGHT':
                node.x += self.speed

    def check_collision(self) -> bool:
        pass
