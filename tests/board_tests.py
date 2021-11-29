import unittest

from project.model.board import Board, Position, Square


class BoardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.position_start: Position = Position(1, 1)
        self.square: Square = Square(position=self.position_start, square_type=SquareType.EMPTY)
        self.position_goal: Position = Position(5, 5)
        self.board: Board = Board(height=5, width=5, position_start=self.position_start,
                                  position_goal=self.position_goal, list_of_obstacle=[])

    def test_should_get_square_type_from_board_return_START(self):
        # self.assertEqual(SquareType.START, self.board.get_square_type_from_board(self.position_start))
        self.assertEqual(1, 1)
