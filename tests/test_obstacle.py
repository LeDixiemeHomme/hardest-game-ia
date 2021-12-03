import unittest

from project.model.board import Obstacle, Position, SquareType
from project.model.pattern import Pattern, Movement


class TestObstacle(unittest.TestCase):

    def setUp(self) -> None:
        self.obstacle: Obstacle = Obstacle(position=Position(5, 5), pattern=Pattern())
        coordinates: [[float, float]] = [[5, 5], [0, 0], [10, 10], [0, 10], [10, 0], [4, 4]]
        self.positions: [Position] = []
        for position in coordinates:
            self.positions.append(Position(co_x=position[0], co_y=position[1]))

    def test_should_is_position_inside_with_position_0_return_true(self):
        self.assertTrue(self.obstacle.is_position_inside(self.positions[0]))

    def test_should_is_position_inside_with_position_1_return_false(self):
        self.assertFalse(self.obstacle.is_position_inside(self.positions[1]))

    def test_should_is_position_inside_with_position_2_return_false(self):
        self.assertFalse(self.obstacle.is_position_inside(self.positions[2]))

    def test_should_is_position_inside_with_position_3_return_false(self):
        self.assertFalse(self.obstacle.is_position_inside(self.positions[3]))

    def test_should_is_position_inside_with_position_4_return_false(self):
        self.assertFalse(self.obstacle.is_position_inside(self.positions[4]))

    def test_should_is_position_inside_with_position_5_return_false(self):
        self.assertFalse(self.obstacle.is_position_inside(self.positions[5]))


if __name__ == '__main__':
    unittest.main()
