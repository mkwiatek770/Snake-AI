from enum import Enum

NODE_SIZE = 10


class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    left = 'LEFT'
    right = 'RIGHT'


class Speed(Enum):
    debug = 1
    slow = 2
    normal = 3
    fast = 4
