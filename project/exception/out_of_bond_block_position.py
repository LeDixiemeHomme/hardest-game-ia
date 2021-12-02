from project.model.position import Position
from project.model.square_type import SquareType


class OutOfBoundBlockPosition(Exception):
    def __init__(self, position: Position, square_type: SquareType, width: int, height: int):
        super().__init__(
            f'Position {position} of the block {square_type} is out of bound. Width = {width},Height = {height}')