from project.model.position import Position
from project.model.square_type import SquareType


class OutOfBondBlockPosition(Exception):

    def __init__(self, position: Position, square_type: SquareType):
        super().__init__("Position %s of the block %s is out of bond" %
                         (position, square_type))
