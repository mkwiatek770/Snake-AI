import math
from typing import List

import numpy as np
from app.v2.constants import Direction, Node, GRID_SIZE

_DIRECTION_TO_VALUE_MAP = {
    Direction.LEFT: 0,
    Direction.UP: 1,
    Direction.RIGHT: 2,
    Direction.DOWN: 3,
}


def angle_with_apple(snake_nodes: List[Node], apple: Node):
    """
    -1: 180 degrees
    -0.5 90 degrees right
    0: 0 degrees
    0.5: 90 degrees left
    1:
LEFT -> button_direction = 0
RIGHT -> button_direction = 1
DOWN ->button_direction = 2
UP -> button_direction = 3
    """
    apple_direction_vector = np.array([apple.x, apple.y]) - np.array([snake_nodes[0].x, snake_nodes[0].y])
    snake_direction_vector = np.array([snake_nodes[0].x, snake_nodes[0].y]) - np.array([snake_nodes[1].x, snake_nodes[1].y])

    norm_of_apple_direction_vector = np.linalg.norm(apple_direction_vector)
    norm_of_snake_direction_vector = np.linalg.norm(snake_direction_vector)
    if norm_of_apple_direction_vector == 0:
        norm_of_apple_direction_vector = 10
    if norm_of_snake_direction_vector == 0:
        norm_of_snake_direction_vector = 10

    apple_direction_vector_normalized = apple_direction_vector / norm_of_apple_direction_vector
    snake_direction_vector_normalized = snake_direction_vector / norm_of_snake_direction_vector
    angle = math.atan2(
        apple_direction_vector_normalized[1] * snake_direction_vector_normalized[0] - apple_direction_vector_normalized[
            0] * snake_direction_vector_normalized[1],
        apple_direction_vector_normalized[1] * snake_direction_vector_normalized[1] + apple_direction_vector_normalized[
            0] * snake_direction_vector_normalized[0]) / math.pi
    return angle


def is_direction_blocked(snake, direction: Direction) -> bool:
    next_x = snake.head.x
    next_y = snake.head.y
    if direction == Direction.RIGHT:
        next_x += 1
    elif direction == Direction.LEFT:
        next_x -= 1
    elif direction == Direction.UP:
        next_y -= 1
    elif direction == Direction.DOWN:
        next_y += 1

    # check collision with boundaries
    if next_x not in range(0, GRID_SIZE + 1) or next_y not in range(0, GRID_SIZE + 1):
        return True

    # check collision with itself
    # to moze nie zadzialac prawidlowo, porownuje przyszy stan z obecnymi node'ami w razie czego napisac funkcje
    # get_next_step i obliczac pozycje dla kazdego node'a
    for node in snake.nodes[1:-1]:
        if node.x == next_x and node.y == next_y:
            return True
    return False


def right_direction_from_snake_perspective(snake_direction: Direction) -> Direction:
    current_dir = _DIRECTION_TO_VALUE_MAP[snake_direction]
    right_dir_value = (current_dir + 1) % 4
    for direction, value in _DIRECTION_TO_VALUE_MAP.items():
        if value == right_dir_value:
            return direction


def left_direction_from_snake_perspective(snake_direction: Direction) -> Direction:
    current_dir = _DIRECTION_TO_VALUE_MAP[snake_direction]
    right_dir_value = (current_dir + 3) % 4
    for direction, value in _DIRECTION_TO_VALUE_MAP.items():
        if value == right_dir_value:
            return direction


def euclidean_distance(first_node: Node, second_node: Node) -> float:
    return math.sqrt(math.pow(second_node.x - first_node.x, 2) + math.pow(second_node.y - first_node.y, 2))


def manhattan_distance(first_node: Node, second_node: Node) -> int:
    return int(abs(second_node.x - first_node.x) + abs(second_node.y - first_node.y))


def sigmoid(z):
    """
    The sigmoid function, classic neural net activation function

    z is weighted sum of input from preactivation step
    """
    return 1 / (1 + np.exp(-z))


def normalize(data: List[float]) -> List[float]:
    """
    Normalize data using min-max scaler
    """
    normalized_data = []
    x_min, x_max = min(data), max(data)
    for x in data:
        normalized_value = (x - x_min) / (x_max - x_min)
        normalized_data.append(normalized_value)
    return normalized_data
