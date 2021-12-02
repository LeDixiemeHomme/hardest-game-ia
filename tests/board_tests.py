import unittest
from typing import List

from project.constant.constant import PICTURE_PATH, PICTURE_SIZE
from project.model.board import Board, Position, SquareType, Obstacle
from project.model.pattern import Pattern, Movement, Direction


class BoardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.position_start: Position = Position(3, 3)
        self.position_empty: Position = Position(2, 2)
        self.position_obstacle: Position = Position(3, 4)
        self.position_goal: Position = Position(5, 5)
        self.pattern: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP, length=1, speed=3),
                                                           Movement(direction=Direction.UP, length=1, speed=3),
                                                           Movement(direction=Direction.UP, length=1, speed=3)])
        self.obstacle: Obstacle = Obstacle(position=self.position_obstacle, pattern=self.pattern,
                                           picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)
        self.board: Board = Board(height=5, width=5, position_start=self.position_start,
                                  position_goal=self.position_goal, list_of_obstacle=[self.obstacle])

    def test_should_get_square_type_from_board_return_START(self):
        self.assertEqual(SquareType.START, self.board.get_square_type_from_board_by_position(self.position_start))

    def test_should_get_square_type_from_board_return_GOAL(self):
        self.assertEqual(SquareType.GOAL, self.board.get_square_type_from_board_by_position(self.position_goal))

    def test_should_get_square_type_from_board_return_EMPTY(self):
        self.assertEqual(SquareType.EMPTY, self.board.get_square_type_from_board_by_position(self.position_empty))

    def test_should_move_obstacles_not_erase_start_position(self):
        expected_log: List[SquareType] = [SquareType.START, SquareType.OBSTACLE, SquareType.START]
        square_type_log: List[SquareType] = []
        for i in range(3):
            square_type_log.append(self.board.get_square_type_from_board_by_position(self.position_start))
            self.board.move_obstacles()
        self.assertEqual(first=expected_log, second=square_type_log)
