from enum import Enum
from typing import List


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Movement:
    def __init__(self, direction: Direction, length: int, speed: int):
        self._direction = direction
        self._length = length
        self._speed = speed

    @property
    def direction(self):
        return self._direction

    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed

    @length.setter
    def length(self, length: int):
        self._length = length

    def __str__(self) -> str:
        string: str = "Movement : { " + str(self._direction) + "; length = " + str(
            self._length) + "; speed = " + str(self._speed) + " }"
        return string


class Pattern:
    def __init__(self, list_of_movements: List[Movement]):
        self._list_of_movements = list_of_movements

    @property
    def list_of_movements(self):
        return self._list_of_movements
