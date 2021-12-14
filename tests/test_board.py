import unittest
from typing import List

import pytest

from project.custom_exception.out_of_bound_block_position_exception import OutOfBoundBlockPositionException
from project.model.agent import Agent
from project.model.board import Board, Position, SquareType, Obstacle
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.pattern import Pattern


class TestBoard:
    board_height: int = 5
    board_width: int = 5
    up_movement: Movement = Movement(direction=Direction.UP)
    down_movement: Movement = Movement(direction=Direction.DOWN)
    left_movement: Movement = Movement(direction=Direction.LEFT)
    right_movement: Movement = Movement(direction=Direction.RIGHT)

    position_start: Position = Position(1, 1)
    position_empty: Position = Position(2, 2)
    position_goal: Position = Position(5, 5)

    agent: Agent = Agent(position=position_start)

    position_out_under_under: Position = Position(0, 0)
    position_out_under_in: Position = Position(0, 4)
    position_out_under_over: Position = Position(0, 10)
    position_out_in_under: Position = Position(4, 0)
    position_out_over_under: Position = Position(10, 0)
    position_out_over_over: Position = Position(10, 10)
    position_next_to_start: Position = Position(1, 2)
    obstacle_next_to_start: Obstacle = Obstacle(position=position_next_to_start, pattern=Pattern(
        list_of_movements=[up_movement, down_movement]))

    position_next_to_wall: Position = Position(1, 5)
    obstacle_next_to_wall: Obstacle = Obstacle(position=position_next_to_wall, pattern=Pattern(
        list_of_movements=[down_movement, down_movement]))

    board: Board = Board(height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle_next_to_start, obstacle_next_to_wall],
                         agent=agent)
    board.instantiate_singleton_viewer()

    @pytest.mark.parametrize("excepted_square_type, tested_position", [(SquareType.START, position_start),
                                                                       (SquareType.GOAL, position_goal),
                                                                       (SquareType.EMPTY, position_empty)])
    def test_should_get_square_type_with_position_corresponding_square_type(self, excepted_square_type,
                                                                            tested_position):
        assert excepted_square_type.value == self.board.get_square_type_from_board_by_position(tested_position).value

    @pytest.mark.parametrize("tested_position", [position_out_under_under,
                                                 position_out_over_over,
                                                 position_out_under_in])
    def test_should_get_square_type_with_position_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.get_square_type_from_board_by_position(tested_position)

    @pytest.mark.parametrize("tested_position", [position_out_under_under, position_out_under_in,
                                                 position_out_under_over, position_out_in_under,
                                                 position_out_over_under, position_out_over_over])
    def test_should_get_square_type_with_position_corresponding_square_type(self, tested_position):
        assert not self.board.is_position_inside_board_boundaries(position_to_test=tested_position)

    def test_should_is_position_inside_board_boundaries_with_position_start_return_true(self):
        assert self.board.is_position_inside_board_boundaries(position_to_test=self.position_start)

    def test_should_get_index_of_list_of_square_by_position_with_position_start_return_0(self):
        expected_index: int = 0
        assert expected_index == self.board.get_index_of_list_of_square_by_position(position=self.position_start)

    def test_should_get_index_of_list_of_square_by_position_with_position_start_raise_exception(self):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.get_index_of_list_of_square_by_position(position=self.position_out_over_over)

    def test_should_get_position_after_movement_with_position_out_raise_exception(self):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.get_position_after_movement(current_position=self.position_out_over_over,
                                                   current_movement=self.right_movement)

    @pytest.mark.parametrize("movement, position_expected",
                             [(up_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y - 1)),
                              (down_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y + 1)),
                              (left_movement, Position(co_x=position_empty.co_x - 1, co_y=position_empty.co_y)),
                              (right_movement, Position(co_x=position_empty.co_x + 1, co_y=position_empty.co_y))])
    def test_should_get_position_after_movement(self, movement, position_expected):
        result_position: Position = self.board.get_position_after_movement(current_position=self.position_empty,
                                                                           current_movement=movement)
        assert position_expected == result_position

    def test_should_move_obstacles_not_erase_start_position(self):
        expected_log: List[SquareType] = [SquareType.START, SquareType.OBSTACLE, SquareType.START]
        square_type_log: List[SquareType] = []
        for i in range(3):
            square_type_log.append(self.board.get_square_type_from_board_by_position(self.position_start))
            self.board.move_obstacles()
        assert expected_log == square_type_log

    def test_should_move_obstacles_not_move_inside_wall(self):
        expected_log: List[Position] = [self.position_next_to_wall, self.position_next_to_wall,
                                        self.position_next_to_wall, self.position_next_to_wall]
        position_log: List[Position] = []
        for i in range(4):
            position_log.append(self.board.list_of_obstacle[1].position)
            self.board.move_obstacles()
        assert expected_log == position_log


if __name__ == '__main__':
    unittest.main()
