from typing import List

import pytest

from project.model.board import Board, Position, Obstacle
from project.model.movement import Movement, Direction
from project.model.position import Pattern, OutOfBoundBlockPositionException
from project.model.square_type import SquareType


class TestSquareList:
    board_height: int = 5
    board_width: int = 5
    up_movement: Movement = Movement(direction=Direction.UP)
    down_movement: Movement = Movement(direction=Direction.DOWN)
    left_movement: Movement = Movement(direction=Direction.LEFT)
    right_movement: Movement = Movement(direction=Direction.RIGHT)

    position_start: Position = Position(1, 1)
    position_empty: Position = Position(2, 2)
    position_goal: Position = Position(5, 5)

    coordinates: [[int, int]] = [[0, 0], [0, 4], [0, 10], [4, 0], [10, 0], [10, 10]]
    positions_out: [Position] = []
    for coordinate in coordinates:
        positions_out.append(Position(co_x=coordinate[0], co_y=coordinate[1]))

    position_next_to_start: Position = Position(1, 2)
    obstacle_next_to_start: Obstacle = Obstacle(position=position_next_to_start, pattern=Pattern(
        list_of_movements=[up_movement, down_movement]))

    position_next_to_wall: Position = Position(1, 5)
    obstacle_next_to_wall: Obstacle = Obstacle(position=position_next_to_wall, pattern=Pattern(
        list_of_movements=[down_movement, down_movement]))

    board: Board = Board(name="test_board", height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle_next_to_start, obstacle_next_to_wall])

    board.instantiate_singleton_viewer()

    square_type_with_position = [
        (SquareType.START, position_start), (SquareType.GOAL, position_goal), (SquareType.EMPTY, position_empty)]

    @pytest.mark.parametrize("excepted_square_type, tested_position", square_type_with_position)
    def test_should_get_square_type_with_position_corresponding_square_type(self, excepted_square_type,
                                                                            tested_position):
        assert excepted_square_type.value == self.board.square_list.get_square_type_from_board_by_position(
            tested_position).value

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_square_type_with_position_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.square_list.get_square_type_from_board_by_position(tested_position)

    def test_should_get_index_of_list_of_square_by_position_with_position_start_return_0(self):
        expected_index: int = 0
        assert expected_index == self.board.square_list.get_index_of_list_of_square_by_position(
            position=self.position_start)

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_index_of_list_of_square_by_position_with_position_start_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.square_list.get_index_of_list_of_square_by_position(position=tested_position)

    def test_should_move_obstacles_not_erase_start_position(self):
        expected_log: List[SquareType] = [SquareType.START, SquareType.OBSTACLE, SquareType.START]
        square_type_log: List[SquareType] = []
        for i in range(3):
            square_type_log.append(self.board.square_list.get_square_type_from_board_by_position(self.position_start))
            self.board.move_obstacles()
        assert expected_log == square_type_log
