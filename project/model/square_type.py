from enum import Enum


class SquareType(Enum):
    START = 1
    GOAL = 2
    EMPTY = 3
    WALL = 4
    OBSTACLE = 5

    def __hash__(self):
        return hash(self.value)
