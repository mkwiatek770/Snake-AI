from __future__ import annotations
from typing import Collection, Optional
from app.utils import Direction


class Node:
    def __init__(self, x: int, y: int, direction: Optional[Direction] = None) -> None:
        self.x = x
        self.y = y
        if direction:
            self.direction = direction
        self._turns = []

    @property
    def turns(self) -> Collection[Node]:
        return self._turns

    @property
    def next_turn(self) -> Node:
        return self._turns[0]

    def has_turns(self) -> bool:
        return len(self._turns) != 0

    def add_turn(self, turn: Node) -> None:
        self._turns.append(turn)

    def turn(self) -> None:
        self.direction = self._turns.pop(0).direction
