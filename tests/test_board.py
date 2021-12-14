import unittest
from typing import List

from project.custom_exception.out_of_bound_block_position_exception import OutOfBoundBlockPositionException
from project.model.agent import Agent
from project.model.board import Board, Position, SquareType, Obstacle
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.pattern import Pattern


class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        board_height: int = 5
        board_width: int = 5
        self.up_movement: Movement = Movement(direction=Direction.UP)
        self.down_movement: Movement = Movement(direction=Direction.DOWN)
        self.left_movement: Movement = Movement(direction=Direction.LEFT)
        self.right_movement: Movement = Movement(direction=Direction.RIGHT)

        self.position_start: Position = Position(1, 1)
        self.position_empty: Position = Position(2, 2)
        self.position_goal: Position = Position(5, 5)

        self.agent: Agent = Agent(position=self.position_start)

        self.position_out_under_under: Position = Position(0, 0)
        self.position_out_under_in: Position = Position(0, 4)
        self.position_out_under_over: Position = Position(0, 10)
        self.position_out_in_under: Position = Position(4, 0)
        self.position_out_over_under: Position = Position(10, 0)
        self.position_out_over_over: Position = Position(10, 10)

        self.position_next_to_start: Position = Position(1, 2)
        self.obstacle_next_to_start: Obstacle = Obstacle(position=self.position_next_to_start, pattern=Pattern(
            list_of_movements=[self.up_movement, self.down_movement]))

        self.position_next_to_wall: Position = Position(1, 5)
        self.obstacle_next_to_wall: Obstacle = Obstacle(position=self.position_next_to_wall, pattern=Pattern(
            list_of_movements=[self.down_movement, self.down_movement]))

        self.board: Board = Board(height=board_height, width=board_width,
                                  position_start=self.position_start, position_goal=self.position_goal,
                                  list_of_obstacle=[self.obstacle_next_to_start, self.obstacle_next_to_wall],
                                  agent=self.agent)
        self.board.instantiate_singleton_viewer()

    def test_should_get_square_type_with_position_start_from_board_return_START(self):
        self.assertEqual(SquareType.START, self.board.get_square_type_from_board_by_position(self.position_start))

    def test_should_get_square_type_with_position_goal_from_board_return_GOAL(self):
        self.assertEqual(SquareType.GOAL, self.board.get_square_type_from_board_by_position(self.position_goal))

    def test_should_get_square_type_with_position_empty_from_board_return_EMPTY(self):
        self.assertEqual(SquareType.EMPTY, self.board.get_square_type_from_board_by_position(self.position_empty))

    def test_should_get_square_type_with_position_out_under_under_from_board_return_EMPTY(self):
        self.assertRaises(OutOfBoundBlockPositionException,
                          self.board.get_square_type_from_board_by_position, self.position_out_under_under)

    def test_should_get_square_type_with_position_out_over_over_from_board_return_EMPTY(self):
        self.assertRaises(OutOfBoundBlockPositionException,
                          self.board.get_square_type_from_board_by_position, self.position_out_over_over)

    def test_should_get_square_type_with_position_out_under_in_from_board_return_EMPTY(self):
        self.assertRaises(OutOfBoundBlockPositionException,
                          self.board.get_square_type_from_board_by_position, self.position_out_under_in)

    def test_should_move_obstacles_not_erase_start_position(self):
        expected_log: List[SquareType] = [SquareType.START, SquareType.OBSTACLE, SquareType.START]
        square_type_log: List[SquareType] = []
        for i in range(3):
            square_type_log.append(self.board.get_square_type_from_board_by_position(self.position_start))
            self.board.move_obstacles()
        self.assertEqual(first=expected_log, second=square_type_log)

    def test_should_move_obstacles_not_move_inside_wall(self):
        expected_log: List[Position] = [self.position_next_to_wall, self.position_next_to_wall,
                                        self.position_next_to_wall, self.position_next_to_wall]
        position_log: List[Position] = []
        for i in range(4):
            position_log.append(self.board.list_of_obstacle[1].position)
            self.board.move_obstacles()
        self.assertEqual(first=expected_log, second=position_log)

    def test_should_is_position_inside_board_boundaries_with_position_out_under_under_return_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_under_under))

    def test_should_is_position_inside_board_boundaries_with_position_out_under_in_return_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_under_in))

    def test_should_is_position_inside_board_boundaries_with_position_out_under_over_return_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_under_over))

    def test_should_is_position_inside_board_boundaries_with_position_out_in_under_return_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_in_under))

    def test_should_is_position_inside_board_boundaries_return_with_position_out_over_under_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_over_under))

    def test_should_is_position_inside_board_boundaries_with_position_out_over_over_return_false(self):
        self.assertEqual(first=False, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_out_over_over))

    def test_should_is_position_inside_board_boundaries_with_position_start_return_true(self):
        self.assertEqual(first=True, second=self.board.is_position_inside_board_boundaries(
            position_to_test=self.position_start))

    def test_should_get_index_of_list_of_square_by_position_with_position_start_return_0(self):
        self.assertEqual(first=0, second=self.board.get_index_of_list_of_square_by_position(
            position=self.position_start))

    def test_should_get_index_of_list_of_square_by_position_with_position_start_raise_OutOfBoundBlockPosition(self):
        self.assertRaises(OutOfBoundBlockPositionException,
                          self.board.get_index_of_list_of_square_by_position, self.position_out_over_over)

    def test_should_get_position_after_movement_with_position_empty_and_up_movement_return_position_co_y_minus(self):
        movement: Movement = self.up_movement
        length: int = movement.length
        initial_position: Position = self.position_empty
        result_position: Position = self.board.get_position_after_movement(current_position=initial_position,
                                                                           current_movement=movement)
        position_expected: Position = Position(co_x=initial_position.co_x, co_y=initial_position.co_y - length)

        self.assertEqual(first=position_expected, second=result_position)

    def test_should_get_position_after_movement_with_position_empty_and_down_movement_return_position_co_y_plus(self):
        movement: Movement = self.down_movement
        length: int = movement.length
        initial_position: Position = self.position_empty
        result_position: Position = self.board.get_position_after_movement(current_position=initial_position,
                                                                           current_movement=movement)
        position_expected: Position = Position(co_x=initial_position.co_x, co_y=initial_position.co_y + length)

        self.assertEqual(first=position_expected, second=result_position)

    def test_should_get_position_after_movement_with_position_empty_and_left_movement_return_position_co_x_minus(self):
        movement: Movement = self.left_movement
        length: int = movement.length
        initial_position: Position = self.position_empty
        result_position: Position = self.board.get_position_after_movement(current_position=initial_position,
                                                                           current_movement=movement)
        position_expected: Position = Position(co_x=initial_position.co_x - length, co_y=initial_position.co_y)

        self.assertEqual(first=position_expected, second=result_position)

    def test_should_get_position_after_movement_with_position_empty_and_right_movement_return_position_co_y_plus(self):
        movement: Movement = self.right_movement
        length: int = movement.length
        initial_position: Position = self.position_empty
        result_position: Position = self.board.get_position_after_movement(current_position=initial_position,
                                                                           current_movement=movement)
        position_expected: Position = Position(co_x=initial_position.co_x + length, co_y=initial_position.co_y)

        self.assertEqual(first=position_expected, second=result_position)

    def test_should_get_position_after_movement_with_position_out_raise_OutOfBoundBlockPositionException(self):
        self.assertRaises(OutOfBoundBlockPositionException,
                          self.board.get_position_after_movement, self.position_out_over_over, self.right_movement)


if __name__ == '__main__':
    unittest.main()
