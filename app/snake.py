from __future__ import annotations

import copy
import random
from typing import Collection, Tuple

from app.node import Node
from app.utils import Direction, NODE_SIZE, Speed


class Snake:
    _speed: int = Speed.slow.value
    alive: bool = True

    def __init__(self, w_size: Tuple[int, int], nodes: Collection[Node] = None):
        self._nodes = list(nodes) if nodes else [Node(100, i, Direction.up) for i in range(100, 130, NODE_SIZE)]
        self._window_size = w_size
        self.points = 0
        # 24 input neurons
        # 8 angles (0, 45, 90, 135, 180, 225, 270, 315)
        # 3 distance meassurements for current angle (to_food, to_wall, to_its_body) normalized to values [0, 1]
        # order is in following way [angle 0 to_food, angle 0 to_wall, ang 0 to_its_body, ang 45 to_food, ....]
        # angle 0 means straight (from head perspective)
        self.chromosome = [random.uniform(0, 1) for _ in range(24)]

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
        # move head
        new_x = self.head.x
        new_y = self.head.y
        direction = self.head.direction.value
        if direction == 'UP':
            new_y -= NODE_SIZE
        elif direction == 'DOWN':
            new_y += NODE_SIZE
        elif direction == 'LEFT':
            new_x -= NODE_SIZE
        elif direction == 'RIGHT':
            new_x += NODE_SIZE
        if self.check_collision(new_x, new_y):
            self.alive = False
            return
        self.head.x = new_x
        self.head.y = new_y
        # move tail
        for node in self.nodes[1:]:
            if node.has_turns():
                next_turn = node.next_turn
                if node.x == next_turn.x and node.y == next_turn.y:
                    node.turn()
            direction = node.direction.value
            if direction == 'UP':
                node.y -= NODE_SIZE
            elif direction == 'DOWN':
                node.y += NODE_SIZE
            elif direction == 'LEFT':
                node.x -= NODE_SIZE
            elif direction == 'RIGHT':
                node.x += NODE_SIZE

    def eat(self) -> None:
        new_node = copy.deepcopy(self.tail)
        direction = self.tail.direction.value
        if direction == 'UP':
            new_node.y += NODE_SIZE
        elif direction == 'DOWN':
            new_node.y -= NODE_SIZE
        elif direction == 'LEFT':
            new_node.x += NODE_SIZE
        elif direction == 'RIGHT':
            new_node.x -= NODE_SIZE
        self._nodes.append(new_node)

    def check_collision(self, x: int, y: int) -> bool:
        direction = self.head.direction.value

        if x == -NODE_SIZE and direction == 'LEFT':
            return True
        elif x == self._window_size[0] and direction == 'RIGHT':
            return True
        elif y == -NODE_SIZE and direction == 'UP':
            return True
        elif y == self._window_size[1] and direction == 'DOWN':
            return True
        for node in self.nodes[1:]:
            if x == node.x and y == node.y:
                return True
        return False

    def check_food_collision(self, food_x: int, food_y: int) -> bool:
        snake_x = self.head.x
        snake_y = self.head.y
        direction = self.head.direction.value

        if direction == 'UP':
            snake_y -= NODE_SIZE
        elif direction == 'DOWN':
            snake_y += NODE_SIZE
        elif direction == 'LEFT':
            snake_x -= NODE_SIZE
        elif direction == 'RIGHT':
            snake_x -= NODE_SIZE
        return snake_x == food_x and snake_y == food_y

    def fitness(self):
        #  Desired fitness will be something like:
        #  F = 20*points + 5*health
        return 20 * self.points
