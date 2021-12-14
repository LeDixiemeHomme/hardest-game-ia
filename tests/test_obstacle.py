import unittest
import pytest

from project.model.board import Obstacle, Position
from project.model.pattern import Pattern


class TestObstacle:
    obstacle: Obstacle = Obstacle(position=Position(5, 5), pattern=Pattern())
    coordinates: [[float, float]] = [[5, 5], [0, 0], [10, 10], [0, 10], [10, 0], [4, 4]]
    positions: [Position] = []
    for position in coordinates:
        positions.append(Position(co_x=position[0], co_y=position[1]))

    @pytest.mark.parametrize("tested_position", [positions[1], positions[2], positions[3],
                                                 positions[4], positions[5]])
    def test_should_is_position_inside_with_position_return_false(self, tested_position):
        assert not self.obstacle.is_position_inside(tested_position)

    def test_should_is_position_inside_with_position_0_return_true(self):
        assert self.obstacle.is_position_inside(self.positions[0])


if __name__ == '__main__':
    unittest.main()
