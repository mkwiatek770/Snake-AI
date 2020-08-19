import math
import numpy as np
from app.v2.constants import Direction, Node, GRID_SIZE


def angle_with_apple(snake_position, apple_position):
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
    apple_direction_vector = np.array(apple_position) - np.array(snake_position[0])
    snake_direction_vector = np.array(snake_position[0]) - np.array(snake_position[1])

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
    return angle, snake_direction_vector, apple_direction_vector_normalized, snake_direction_vector_normalized


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
