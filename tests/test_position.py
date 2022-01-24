import pytest

from project.model.movement import Movement, Direction
from project.model.position import Position, OutOfBoundBlockPositionException


class TestPosition:
    width: int = 5
    height: int = 5
    up_movement: Movement = Movement(direction=Direction.UP)
    down_movement: Movement = Movement(direction=Direction.DOWN)
    left_movement: Movement = Movement(direction=Direction.LEFT)
    right_movement: Movement = Movement(direction=Direction.RIGHT)

    position_in: Position = Position(2, 2)
    position_out: Position = Position(2, 10)

    coordinates: [[int, int]] = [[0, 0], [0, 4], [0, 10], [4, 0], [10, 0], [10, 10]]
    positions_out: [Position] = []
    for coordinate in coordinates:
        positions_out.append(Position(co_x=coordinate[0], co_y=coordinate[1]))

    position_with_is_inside: [Position, bool] = [[position_in, True], [position_out, False]]

    position_after_movement = [(up_movement, Position(co_x=position_in.co_x, co_y=position_in.co_y - 1)),
                               (down_movement, Position(co_x=position_in.co_x, co_y=position_in.co_y + 1)),
                               (left_movement, Position(co_x=position_in.co_x - 1, co_y=position_in.co_y)),
                               (right_movement, Position(co_x=position_in.co_x + 1, co_y=position_in.co_y))]

    position_3_3: Position = Position(co_x=3, co_y=3)
    position_3_4: Position = Position(co_x=3, co_y=4)
    position_4_4: Position = Position(co_x=4, co_y=4)
    position_10_10: Position = Position(co_x=10, co_y=10)

    two_positions_with_number_of_squares_between: [Position, int] = [[position_3_3, 0],
                                                                     [position_3_4, 1],
                                                                     [position_4_4, 2],
                                                                     [position_10_10, 14]]

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_position_after_movement_with_position_out_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            tested_position.check_boundaries(width=self.width, height=self.height)

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_square_type_with_position_corresponding_square_type(self, tested_position):
        assert not tested_position._is_position_inside_board_boundaries(
            width=self.width, height=self.height)

    @pytest.mark.parametrize("movement, position_expected", position_after_movement)
    def test_should_get_position_after_movement(self, movement, position_expected):
        result_position: Position = self.position_in.apply_movement(movement=movement)
        assert position_expected == result_position

    @pytest.mark.parametrize("position, is_inside", position_with_is_inside)
    def test_should_is_position_inside_board_boundaries_with_position_works(self, position, is_inside):
        assert position._is_position_inside_board_boundaries(width=self.width, height=self.height) is is_inside

    @pytest.mark.parametrize("position, number", two_positions_with_number_of_squares_between)
    def test_should_number_of_square_between_self_and_tested_position_works(self, position, number):
        number_to_test: int = self.position_3_3.number_of_square_between_positions(
            tested_position_co_x=position.co_x,
            tested_position_co_y=position.co_y)
        assert number_to_test == number

    def test_should_number_of_square_between_self_and_tested_position_works_reciprocally(self):
        distance_one = self.position_3_3.number_of_square_between_positions(
            tested_position_co_x=self.position_10_10.co_x,
            tested_position_co_y=self.position_10_10.co_y)
        distance_two = self.position_10_10.number_of_square_between_positions(
            tested_position_co_x=self.position_3_3.co_x,
            tested_position_co_y=self.position_3_3.co_y)
        assert distance_one == distance_two
