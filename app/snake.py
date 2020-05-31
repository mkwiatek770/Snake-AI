from __future__ import annotations
import copy
from typing import Collection, Tuple
from app.node import Node
from app.utils import Direction, NODE_SIZE, Speed


class Snake:
    _speed: int = Speed.normal.value
    alive: bool = True

    def __init__(self, w_size: Tuple[int, int], nodes: Collection[Node] = None, turns: Collection[Node] = None):
        self._nodes = list(nodes) if nodes else [Node(100, i, Direction.up) for i in range(100, 130, NODE_SIZE)]
        self._window_size = w_size

    @property
    def head(self) -> Node:
        return self._nodes[0]

    @property
    def tail(self) -> Node:
        return self._nodes[-1]

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def nodes(self) -> Collection[Node]:
        return self._nodes

    @property
    def is_alive(self) -> bool:
        return self.alive

    def turn_head(self, direction: Direction):
        if direction == self.head.direction:
            return

        current_direction = self.head.direction.value
        if (direction.value == 'LEFT' and current_direction == 'RIGHT' or
                direction.value == 'RIGHT' and current_direction == 'LEFT' or
                direction.value == 'UP' and current_direction == 'DOWN' or
                direction.value == 'DOWN' and current_direction == 'UP'):
            return

        self.head.direction = direction
        turn = Node(self.head.x, self.head.y, direction)
        for node in self.nodes[1:]:
            node.add_turn(turn)

    def move(self):
        for node in self.nodes:
            if node.has_turns():
                next_turn = node.next_turn

                if node.x == next_turn.x and node.y == next_turn.y:
                    node.turn()
            direction = node.direction.value
            if direction == 'UP':
                node.y -= self.speed
            elif direction == 'DOWN':
                node.y += self.speed
            elif direction == 'LEFT':
                node.x -= self.speed
            elif direction == 'RIGHT':
                node.x += self.speed

        if self.check_collision():
            self.alive = False

    def eat(self) -> None:
        new_node = copy.deepcopy(self.tail)
        direction = self.tail.direction.value
        if direction == 'UP':
            new_node.y += self.speed
        elif direction == 'DOWN':
            new_node.y -= self.speed
        elif direction == 'LEFT':
            new_node.x += self.speed
        elif direction == 'RIGHT':
            new_node.x -= self.speed
        self._nodes.append(new_node)

    def check_collision(self) -> bool:
        x, y = self.head.x, self.head.y
        if x <= 0 or x >= self._window_size[0] - NODE_SIZE or y <= 0 or y >= self._window_size[1] - NODE_SIZE:
            return True
        for node in self.nodes[1:]:
            if x == node.x and y == node.y:
                return True
        return False

    def check_food_collision(self, food_x: int, food_y: int) -> bool:
        return abs(self.head.x - food_x) <= NODE_SIZE and abs(self.head.y - food_y) <= NODE_SIZE
