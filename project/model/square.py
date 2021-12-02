from enum import Enum

from project.constant.constant import SQUARE_SIZE


class Position:
    def __init__(self, co_x: int, co_y: int):
        self._co_x: int = co_x
        self._co_y: int = co_y

    @property
    def co_x(self) -> int:
        return self._co_x

    @property
    def co_y(self) -> int:
        return self._co_y

    @co_x.setter
    def co_x(self, co_x: int):
        self._co_x = co_x

    @co_y.setter
    def co_y(self, co_y: int):
        self._co_y = co_y

    def __str__(self) -> str:
        string: str = "Position : { " + " co_x = " + str(self._co_x) + "; co_y = " + str(self._co_y) + " }"
        return string


class SquareType(Enum):
    START = 1
    GOAL = 2
    EMPTY = 3
    WALL = 4
    OBSTACLE = 5


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self._position: Position = position
        self._square_type = square_type

    def is_position_inside(self, position_to_test: Position) -> bool:
        return self._position.co_x <= position_to_test.co_x <= self._position.co_x + SQUARE_SIZE \
               and self._position.co_y <= position_to_test.co_y <= self._position.co_y + SQUARE_SIZE

    @property
    def position(self):
        return self._position

    @property
    def square_type(self):
        return self._square_type

    def __str__(self) -> str:
        string: str = "Square : { " + str(self._position) + "; " + str(self._square_type) + " }"
        return string


class OutOfBoundBlockPosition(Exception):
    def __init__(self, position: Position, square_type: SquareType, width: int, height: int):
        super().__init__(
            f'Position {str(position)} of the block {square_type} is out of bound. Width = {width},Height = {height}')
