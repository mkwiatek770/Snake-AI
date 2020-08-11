from __future__ import annotations

import copy
import random
from typing import Collection, List

from app.v2.node import Node
from app.v2.constants import GRID_SIZE, Direction


class Snake:
    def __init__(self, chromosome: List[float] = None, display_mode: bool = False) -> None:
        self.alive = True
        self._nodes = [Node(GRID_SIZE // 2 - offset, GRID_SIZE // 2, Direction.LEFT) for offset in range(1, 4)]
        self.points = 0
        self.display_mode = display_mode
        # 24 input neurons
        # 8 angles (0, 45, 90, 135, 180, 225, 270, 315)
        # 3 distance measurements for current angle (to_food, to_wall, to_its_body) normalized to values [0, 1]
        # order is in following way [angle 0 to_food, angle 0 to_wall, ang 0 to_its_body, ang 45 to_food, ....]
        # angle 0 means straight (from head perspective)
        self.chromosome = list(chromosome) if chromosome else [round(random.uniform(0, 1), 2) for _ in range(24)]
        self.fitness = 0
        self._food = Node(GRID_SIZE // 2 + 2, GRID_SIZE // 2 + 2)

    @property
    def head(self) -> Node:
        return self._nodes[0]

    @property
    def tail(self) -> Node:
        return self._nodes[-1]

    @property
    def nodes(self) -> Collection[Node]:
        return self._nodes

    @property
    def is_alive(self) -> bool:
        return self.alive

    @property
    def food(self) -> Node:
        return self._food

    def play(self) -> None:
        score = 0
        while self.is_alive:
            next_direction = self.next_direction()
            if next_direction != self.head.direction:
                self.turn_head(next_direction)
            score += self.move()
            if self.check_food_collision():
                score += 1
                self._food = self._new_food()
        self.fitness = score

    def next_direction(self) -> Direction:
        return Direction.RIGHT

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

    def move(self) -> float:
        # move head
        new_x = self.head.x
        new_y = self.head.y
        direction = self.head.direction.value
        if direction == 'UP':
            new_y -= 1
        elif direction == 'DOWN':
            new_y += 1
        elif direction == 'LEFT':
            new_x -= 1
        elif direction == 'RIGHT':
            new_x += 1
        if self.check_collision(new_x, new_y):
            self.alive = False
            return 0

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
                node.y -= 1
            elif direction == 'DOWN':
                node.y += 1
            elif direction == 'LEFT':
                node.x -= 1
            elif direction == 'RIGHT':
                node.x += 1

        # calculate move score
        move_score = ...
        return move_score

    def eat(self) -> None:
        new_node = copy.deepcopy(self.tail)
        direction = self.tail.direction.value
        if direction == 'UP':
            new_node.y += 1
        elif direction == 'DOWN':
            new_node.y -= 1
        elif direction == 'LEFT':
            new_node.x += 1
        elif direction == 'RIGHT':
            new_node.x -= 1
        self._nodes.append(new_node)

    def check_collision(self, x: int, y: int) -> bool:
        direction = self.head.direction.value

        if x == -1 and direction == 'LEFT':
            return True
        elif x == GRID_SIZE and direction == 'RIGHT':
            return True
        elif y == -1 and direction == 'UP':
            return True
        elif y == GRID_SIZE and direction == 'DOWN':
            return True
        for node in self.nodes[1:]:
            if x == node.x and y == node.y:
                return True
        return False

    def check_food_collision(self) -> bool:
        snake_x = self.head.x
        snake_y = self.head.y
        direction = self.head.direction.value

        if direction == 'UP':
            snake_y -= 1
        elif direction == 'DOWN':
            snake_y += 1
        elif direction == 'LEFT':
            snake_x -= 1
        elif direction == 'RIGHT':
            snake_x -= 1
        return snake_x == self.food.x and snake_y == self.food.y

    def _new_food(self) -> Node:
        new_x: int = 0
        new_y: int = 0
        snake_intersection: bool = True

        while snake_intersection:
            new_x = random.randint(0, GRID_SIZE)
            new_y = random.randint(0, GRID_SIZE)
            for node in self.nodes:
                if node.x == new_x and node.y == new_y:
                    break
            else:
                snake_intersection = False
        return Node(new_x, new_y)
