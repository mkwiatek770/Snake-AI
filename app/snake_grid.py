import random
from typing import List

from app.utils import Direction
from app.constants import GRID_SIZE, PLAYS_PER_SNAKE

START_DIRECTION = Direction.right
START_SNAKE_COORDS = (GRID_SIZE // 2, GRID_SIZE // 2)
START_FOOD_COORDS = (GRID_SIZE // 2 + 3, GRID_SIZE // 2 + 3)


class SnakeGrid:
    def __init__(self, chromosome: List[float] = None):
        self.fitness = 0
        self.chromosome = list(chromosome) if chromosome else [round(random.uniform(0, 1), 2) for _ in range(24)]

    def play(self) -> None:
        total_score = 0
        for _ in range(PLAYS_PER_SNAKE):
            total_score += self._perform_simulation()
        self.fitness = round(total_score / PLAYS_PER_SNAKE, 2)

    def _perform_simulation(self) -> float:
        # initial data
        self.head = START_SNAKE_COORDS
        self.food = START_FOOD_COORDS
        self.turns = []
        self.direction = START_DIRECTION
        self.is_alive = True
        self.grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
        self.grid[self.head[0]][self.head[1]] = 1
        self.grid[self.head[0]][self.head[1] - 1] = 1
        self.grid[self.head[0]][self.head[1] - 2] = 1

        score = 0
        while self.is_alive:
            self.move()
            score += self.check_collision_wall()
            score += self.check_collision_itself()
            score += self.check_collision_food()
            next_dir = self.next_direction()
            if next_dir != self.direction:
                self.turn()
            self.is_alive = False
            self._display_grid()
        return score

    def move(self):
        pass

    def check_collision_wall(self):
        return 1

    def check_collision_itself(self):
        return 1

    def check_collision_food(self):
        return 1

    def next_direction(self) -> Direction:
        return Direction.up

    def turn(self):
        pass

    def _display_grid(self):
        print('-'*(GRID_SIZE + 1))
        for i in range(GRID_SIZE):
            row = ''
            for j in range(GRID_SIZE):
                if self.food == (i, j):
                    row += 'F'
                elif self.head == (i, j):
                    row += 'Q'
                else:
                    element = self.grid[i][j]
                    row += ' ' if element == 0 else 'X'
            print(f'|{row}|')
        print('-'*(GRID_SIZE + 1))

