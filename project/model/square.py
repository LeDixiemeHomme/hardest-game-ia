from project.constant import constant
from project.model.position import Position
from project.model.SquareType import SquareType


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self.__position: Position = position
        self.__square_type = square_type

    def is_position_inside(self, position_to_test: Position) -> bool:
        return self.__position.co_x <= position_to_test.co_x <= self.__position.co_x + constant.SQUARE_SIZE \
               and self.__position.co_y <= position_to_test.co_y <= self.__position.co_y + constant.SQUARE_SIZE

    @property
    def position(self):
        return self.__position

    @property
    def square_type(self):
        return self.__square_type

    def __str__(self) -> str:
        string: str = "Square :" + " position = " + str(self.__position) + " square_type = " + str(self.__square_type)
        return string
