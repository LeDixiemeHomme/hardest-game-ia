from typing import List

import pytest

from project.custom_exception.wrong_display_size_exception import WrongDisplaySizeException
from project.model.board import Board, Position, SquareType, Obstacle, Direction, Movement, OutOfBoundBlockPositionException
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

    coordinates: [[int, int]] = [[0, 0], [0, 4], [0, 10], [4, 0], [10, 0], [10, 10]]
    positions_out: [Position] = []
    for coordinate in coordinates:
        positions_out.append(Position(co_x=coordinate[0], co_y=coordinate[1]))

    position_after_movement = [(up_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y - 1)),
                               (down_movement, Position(co_x=position_empty.co_x, co_y=position_empty.co_y + 1)),
                               (left_movement, Position(co_x=position_empty.co_x - 1, co_y=position_empty.co_y)),
                               (right_movement, Position(co_x=position_empty.co_x + 1, co_y=position_empty.co_y))]

    position_next_to_start: Position = Position(1, 2)
    obstacle_next_to_start: Obstacle = Obstacle(position=position_next_to_start, pattern=Pattern(
        list_of_movements=[up_movement, down_movement]))

    position_next_to_wall: Position = Position(1, 5)
    obstacle_next_to_wall: Obstacle = Obstacle(position=position_next_to_wall, pattern=Pattern(
        list_of_movements=[down_movement, down_movement]))

    board: Board = Board(height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle_next_to_start, obstacle_next_to_wall])

    board.instantiate_singleton_viewer()

    square_type_with_position = [
        (SquareType.START, position_start), (SquareType.GOAL, position_goal), (SquareType.EMPTY, position_empty)]

    @pytest.mark.parametrize("excepted_square_type, tested_position", square_type_with_position)
    def test_should_get_square_type_with_position_corresponding_square_type(self, excepted_square_type,
                                                                            tested_position):
        assert excepted_square_type.value == self.board.get_square_type_from_board_by_position(tested_position).value

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_square_type_with_position_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board.get_square_type_from_board_by_position(tested_position)

    def test_should_get_index_of_list_of_square_by_position_with_position_start_return_0(self):
        expected_index: int = 0
        assert expected_index == self.board._get_index_of_list_of_square_by_position(position=self.position_start)

    @pytest.mark.parametrize("tested_position", positions_out)
    def test_should_get_index_of_list_of_square_by_position_with_position_start_raise_exception(self, tested_position):
        with pytest.raises(OutOfBoundBlockPositionException):
            self.board._get_index_of_list_of_square_by_position(position=tested_position)
            
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

    def test_board_with_big_width_raise_wrong_display_size_exception(self):
        with pytest.raises(WrongDisplaySizeException):
            Board(width=21, height=10, position_start=Position(1, 1), position_goal=Position(2, 2),
                  list_of_obstacle=[])

    def test_board_with_big_height_raise_wrong_display_size_exception(self):
        with pytest.raises(WrongDisplaySizeException):
            Board(width=10, height=21, position_start=Position(1, 1), position_goal=Position(2, 2),
                  list_of_obstacle=[])
