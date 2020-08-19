from __future__ import annotations

import copy
import random
from typing import List

import numpy as np

from app.v2.constants import GRID_SIZE, Direction, Node
from app.v2.utils import angle_with_apple
from app.v2.neural_net import NeuralNet


class Snake:
    def __init__(self, weights: list = None, biases: list = None) -> None:
        self.alive = True
        self._nodes = [Node(GRID_SIZE // 2 - offset, GRID_SIZE // 2, Direction.RIGHT) for offset in range(1, 4)]
        self.points = 0

        self.vision = []

        self.weights = weights if weights else [random.randint(0, 1) for _ in range(6)]
        self.biases = biases if biases else []
        self.neural_net = NeuralNet(weights, biases)
        # 24 input neurons
        # 8 angles (0, 45, 90, 135, 180, 225, 270, 315)
        # 3 distance measurements for current angle (to_food, to_wall, to_its_body) normalized to values [0, 1]
        # order is in following way [angle 0 to_food, angle 0 to_wall, ang 0 to_its_body, ang 45 to_food, ....]
        # angle 0 means straight (from head perspective)
        self.fitness = 0
        self._food = Node(GRID_SIZE // 2 + 2, GRID_SIZE // 2)
        self.age = 1
        self.hunger_level = 0

    @property
    def head(self) -> Node:
        return self._nodes[0]

    @property
    def tail(self) -> Node:
        return self._nodes[-1]

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    @property
    def is_alive(self) -> bool:
        return self.alive

    @property
    def food(self) -> Node:
        return self._food

    def play(self) -> None:
        score = 1
        while self.is_alive:
            next_direction = self.next_direction()
            if next_direction != self.head.direction:
                self.turn_head(next_direction)
            score += self.move()
        # fitness to będzie suma punktów + jak długo wąż został przy życiu (oczywiscie punkty są wazniejsze)
        self.fitness = round(20*score + self.age, 3)

    def next_direction(self) -> Direction:
        # main brain logic will be here
        # check if it's safe to go right, left, forward
        # calculate angle with apple
        # maybe also directions from head to apple, to itself, to wall

        # update vision parameter
        self.scan()
        decision = np.argmax(self.neural_net.feed_forward(self.vision))
        # możliwe, że zamiast tego decision to będzie tylko {1 2 3} gdzie 1 oznacza turn_right, 2 turn_left a 3 forward
        if decision == 1:
            return Direction.RIGHT
        elif decision == 2:
            return Direction.LEFT
        elif decision == 3:
            return Direction.UP
        elif decision == 4:
            return Direction.DOWN

        return random.choice([Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.LEFT])

    def scan(self) -> None:
        pass

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
        move_score = 0.01
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

        if self.check_food_collision():
            move_score += 1
            self._food = self._new_food()
        else:
            self.hunger_level -= 1
            if self.hunger_level == 0:
                self.alive = False
        self.age += 1
        # calculate move score
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
