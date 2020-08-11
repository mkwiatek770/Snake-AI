from enum import Enum

FPS = 20
GRID_SIZE = 20
NODE_SIZE = 20
BIT_ERROR_RATE = 0.02


class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
