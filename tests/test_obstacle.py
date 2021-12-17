import pytest

from project.model.board import Obstacle, Position


class TestObstacle:
    obstacle_position: Position = Position(co_x=5, co_y=5)
    coordinates: [[int, int]] = [[0, 0], [10, 10], [0, 10], [10, 0], [4, 4],
                                 [4, 4], [5, 4], [4, 5], [5, 6], [6, 5], [6, 6]]
    positions: [Position] = []
    for coordinate in coordinates:
        positions.append(Position(co_x=coordinate[0], co_y=coordinate[1]))

    obstacle: Obstacle = Obstacle(position=obstacle_position)

    @pytest.mark.parametrize("tested_position", positions)
    def test_should_is_position_inside_with_position_return_false(self, tested_position):
        assert not self.obstacle.is_position_same(tested_position)

    def test_should_is_position_inside_with_position_0_return_true(self):
        assert self.obstacle.is_position_same(self.obstacle_position)
