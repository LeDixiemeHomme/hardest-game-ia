from project.model.position import Position
from project.model.square_type import SquareType


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
