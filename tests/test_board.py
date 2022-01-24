from typing import List

import pytest

from project.custom_exception.wrong_display_size_exception import WrongDisplaySizeException
from project.model.board import Board, Position, Obstacle
from project.model.movement import Movement, Direction
from project.model.position import Pattern


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

    position_next_to_start: Position = Position(1, 2)
    obstacle_next_to_start: Obstacle = Obstacle(position=position_next_to_start, pattern=Pattern(
        list_of_movements=[up_movement, down_movement]))

    position_next_to_wall: Position = Position(1, 5)
    obstacle_next_to_wall: Obstacle = Obstacle(position=position_next_to_wall, pattern=Pattern(
        list_of_movements=[down_movement, down_movement]))

    board: Board = Board(name="test_board", height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle_next_to_start, obstacle_next_to_wall])

    position_with_distance_from_goal: [Position, int] = [[position_start, 8], [position_empty, 6]]

    board.instantiate_singleton_viewer()

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
            Board(name="test_board", width=21, height=10,
                  position_start=Position(1, 1), position_goal=Position(2, 2),
                  list_of_obstacle=[])

    def test_board_with_big_height_raise_wrong_display_size_exception(self):
        with pytest.raises(WrongDisplaySizeException):
            Board(name="test_board", width=10, height=21,
                  position_start=Position(1, 1), position_goal=Position(2, 2),
                  list_of_obstacle=[])

    @pytest.mark.parametrize("position, distance", position_with_distance_from_goal)
    def test_distance_from_position_goal(self, position, distance):
        assert self.board.distance_from_position_goal(position_to_test=position) == distance
