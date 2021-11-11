from project.model import constant
from project.model.Position import Position
from project.model.SquareType import SquareType


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self.__position: Position = position
        self.__square_type = square_type

    def is_position_inside(self, position_to_test: Position) -> bool:
        test1 = self.__position.co_x <= position_to_test.co_x
        test2 = position_to_test.co_x <= self.__position.co_x + constant.SQUARE_SIZE * 0.01
        test3 = self.__position.co_y <= position_to_test.co_y
        test4 = position_to_test.co_y <= self.__position.co_y + constant.SQUARE_SIZE * 0.01
        print(test1, test2, test3, test4)
        return self.__position.co_x < position_to_test.co_x < self.__position.co_x + constant.SQUARE_SIZE * 0.01 \
               and self.__position.co_y < position_to_test.co_y < self.__position.co_y + constant.SQUARE_SIZE * 0.01

    @property
    def position(self):
        return self.__position

    @property
    def square_type(self):
        return self.__square_type

    def __repr__(self):
        return "Square : square_type = " + str(self.__square_type)
