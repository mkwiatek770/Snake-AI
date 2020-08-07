from __future__ import annotations
from typing import List

from app.utils import Direction
from app.constants import GRID_SIZE

Grid = List[List[str]]


def perform_simulation(snake: Snake) -> float:
    raise NotImplementedError

def _init_grid(snake: Snake) -> Grid:
    # Empty grid
    grid = [[' ']*GRID_SIZE for _ in range(GRID_SIZE)]
    # snake
    # Problem jaki się pojawił - snake to tej pory przyjmował piksele a ja bym chcial podac tylko index X,Y gridu
    # Może stworzyc nową klasę do tego, a ta która już jest będzie służyć do wizualizacji ?