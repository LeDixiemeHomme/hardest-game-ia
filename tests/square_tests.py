import unittest

from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType


class SquareTests(unittest.TestCase):

    def setUp(self) -> None:
        self.square: Square = Square(Position(5.0, 5.0), SquareType.EMPTY)
        coordinates: [[float, float]] = [[5.01, 5.01], [0.0, 0.0], [10.0, 10.0], [0.0, 10.0], [10.0, 0.0], [4.9, 4.7]]
        self.positions: [Position] = []
        for position in coordinates:
            self.positions.append(Position(co_x=position[0], co_y=position[1]))

    def test_should_is_position_inside_with_position_0_return_true(self):
        self.assertTrue(self.square.is_position_inside(self.positions[0]))

    def test_should_is_position_inside_with_position_1_return_false(self):
        self.assertFalse(self.square.is_position_inside(self.positions[1]))

    def test_should_is_position_inside_with_position_2_return_false(self):
        self.assertFalse(self.square.is_position_inside(self.positions[2]))

    def test_should_is_position_inside_with_position_3_return_false(self):
        self.assertFalse(self.square.is_position_inside(self.positions[3]))

    def test_should_is_position_inside_with_position_4_return_false(self):
        self.assertFalse(self.square.is_position_inside(self.positions[4]))

    def test_should_is_position_inside_with_position_5_return_false(self):
        self.assertFalse(self.square.is_position_inside(self.positions[5]))


if __name__ == '__main__':
    unittest.main()
