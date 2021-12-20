import pytest

from project.model.direction import Direction
from project.model.movement import Movement
from project.model.position import Position, OutOfBoundBlockPositionException


class TestPosition:
    width: int = 5
    height: int = 5
    up_movement: Movement = Movement(direction=Direction.UP)
    down_movement: Movement = Movement(direction=Direction.DOWN)
    left_movement: Movement = Movement(direction=Direction.LEFT)
    right_movement: Movement = Movement(direction=Direction.RIGHT)

    position_empty: Position = Position(2, 2)

    coordinates: [[int, int]] = [[0, 0], [0, 4], [0, 10], [4, 0], [10, 0], [10, 10]]
    positions_out: [Position] = []
    for coordinate in coordinates:
        positions_out.append(Position(co_x=coordinate[0], co_y=coordinate[1]))

    position_after_movement = [(up_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y - 1)),
                               (down_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y + 1)),
                               (left_movement, Position(co_x=position_empty.co_x - 1, co_y=position_empty.co_y)),
                               (right_movement, Position(co_x=position_empty.co_x + 1, co_y=position_empty.co_y))]

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_position_after_movement_with_position_out_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            tested_position.check_boundaries(width=self.width, height=self.height)

    @pytest.mark.parametrize("movement, position_expected", position_after_movement)
    def test_should_get_position_after_movement(self, movement, position_expected):
        result_position: Position = self.position_empty.apply_movement(movement=movement)
        assert position_expected == result_position

    def test_should_is_position_inside_board_boundaries_with_position_start_return_true(self):
        assert self.position_empty._is_position_inside_board_boundaries(
            width=self.width, height=self.height)

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_square_type_with_position_corresponding_square_type(self, tested_position):
        assert not tested_position._is_position_inside_board_boundaries(
            width=self.width, height=self.height)
