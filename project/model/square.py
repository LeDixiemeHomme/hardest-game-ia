from enum import Enum


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

    def __eq__(self, tested):
        if isinstance(tested, Position):
            return self._co_x == tested.co_x and self._co_y == tested.co_y
        return False


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

    @property
    def position(self):
        return self._position

    @property
    def square_type(self):
        return self._square_type

    def __str__(self) -> str:
        string: str = "Square : { " + str(self._position) + "; " + str(self._square_type) + " }"
        return string


class OutOfBoundBlockPositionException(Exception):
    def __init__(self, position: Position, square_type: SquareType, width: int, height: int):
        super().__init__(
            f'Position {str(position)} of the block {square_type} is out of bound. Width = {width},Height = {height}')
