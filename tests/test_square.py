from typing import List

import pytest

from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType


class TestSquare:
    square_1: Square = Square(position=Position(co_x=3, co_y=3), square_type=SquareType.START)
    square_2: Square = Square(position=Position(co_x=3, co_y=3), square_type=SquareType.EMPTY)

    result_1: [{'Square': ['Square']}] = \
        [{square_1: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.START),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.EMPTY)]},
         {square_1: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.START),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.OBSTACLE)]},
         {square_1: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.START),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.GOAL),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.OBSTACLE)]},
         {square_1: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.START),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.OBSTACLE)]}
         ]

    result_2: [{'Square': ['Square']}] = \
        [{square_2: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.EMPTY)]},
         {square_2: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.GOAL),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.EMPTY)]},
         {square_2: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.EMPTY),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.GOAL),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.OBSTACLE)]},
         {square_2: [Square(position=Position(co_x=3, co_y=3), square_type=SquareType.GOAL),
                     Square(position=Position(co_x=3, co_y=2), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=3, co_y=4), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=2, co_y=3), square_type=SquareType.OBSTACLE),
                     Square(position=Position(co_x=4, co_y=3), square_type=SquareType.OBSTACLE)]}
         ]

    @pytest.mark.parametrize("result_1", result_1)
    def test_all_possible_state_1(self, result_1):
        assert result_1 in self.square_1.all_possible_state()

    @pytest.mark.parametrize("result_2", result_2)
    def test_all_possible_state_2(self, result_2):
        assert result_2 in self.square_2.all_possible_state()
