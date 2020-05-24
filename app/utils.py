from enum import Enum

NODE_SIZE = 10


class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    left = 'LEFT'
    right = 'RIGHT'


class Speed(Enum):
    debug = int(NODE_SIZE * 0.1)
    slow = int(NODE_SIZE * 0.2)
    normal = int(NODE_SIZE * 0.5)
    fast = int(NODE_SIZE * 1)
