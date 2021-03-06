from typing import List

from project.model.obstacle import Square, SquareType, Position
from project.model.position import OutOfBoundBlockPositionException


class SquareList:
    def __init__(self, width: int, height: int,
                 position_start: Position, position_goal: Position):
        self._width = width
        self._height = height
        self._list_of_square: List[Square] = self._generate_list_of_square()
        self._fill_list_of_square_with_init_square(position_start=position_start,
                                                   position_goal=position_goal)

    def _generate_list_of_square(self) -> List[Square]:
        # dans range 1, size + 1 pour que position soit pas de (0 to 9) mais de (1 to 10)
        list_of_square: List[Square] = []
        for x in range(1, self._width + 1):
            for y in range(1, self._height + 1):
                list_of_square.append(Square(position=Position(co_x=x, co_y=y), square_type=SquareType.EMPTY))
        return list_of_square

    def _fill_list_of_square_with_init_square(self, position_start: Position, position_goal: Position):
        self.put_square_in_list_of_square(square_to_put=Square(
            position=position_start, square_type=SquareType.START))
        self.put_square_in_list_of_square(square_to_put=Square(
            position=position_goal, square_type=SquareType.GOAL))

    def get_index_of_list_of_square_by_position(self, position: Position) -> int:
        position.check_boundaries(width=self._width, height=self._height)
        return self._height * position.co_x - (self._height - position.co_y) - 1

    def get_square_type_from_board_by_position(self, position: Position) -> SquareType:
        return self._list_of_square[
            self.get_index_of_list_of_square_by_position(position)].square_type

    def put_square_in_list_of_square(self, square_to_put: Square):
        self.list_of_square[
            self.get_index_of_list_of_square_by_position(
                position=square_to_put.position)] = square_to_put

    def get_surrounding_squares(self, position: Position) -> List[Square]:
        positions: List[Position] = position.get_surrounding_positions()
        squares: List[Square] = []
        for position in positions:
            try:
                square_type: SquareType = self.get_square_type_from_board_by_position(position=position)
            except OutOfBoundBlockPositionException:
                square_type: SquareType = SquareType.WALL
            squares.append(Square(position=position, square_type=square_type))
        return squares

    def get_surrounding_square_types(self, position: Position) -> List[SquareType]:
        square_types: List[SquareType] = []
        for square in self.get_surrounding_squares(position=position):
            square_types.append(square.square_type)
        return square_types

    @property
    def list_of_square(self):
        return self._list_of_square

    @list_of_square.setter
    def list_of_square(self, value: List[Square]):
        self._list_of_square = value
