from copy import copy
from typing import List

from project.model.movement import Movement, Direction


class Position:
    def __init__(self, co_x: int, co_y: int):
        self._co_x: int = co_x
        self._co_y: int = co_y

    def apply_movement(self, movement: Movement):
        applied: Position = copy(self)
        direction: Direction = movement.direction
        length: int = movement.length
        if direction == Direction.UP:
            applied._co_y -= length
        elif direction == Direction.DOWN:
            applied._co_y += length
        elif direction == Direction.LEFT:
            applied._co_x -= length
        elif direction == Direction.RIGHT:
            applied._co_x += length

        return applied

    def get_surrounding_positions(self):
        positions: List[Position] = []
        #             *
        #          *  *  *
        #       *  *  ¤  *  *
        #          *  *  *
        #             *
        for direction in Direction.__members__.values():
            position_plus_one: Position = self.apply_movement(Movement(direction=direction))
            positions.append(position_plus_one)
            if direction != direction.STAY:
                position_plus_two: Position = position_plus_one.apply_movement(Movement(direction=direction))
                positions.append(position_plus_two)
        positions.append(Position(co_x=self._co_x - 1, co_y=self._co_y))
        positions.append(Position(co_x=self._co_x + 1, co_y=self._co_y))
        positions.append(Position(co_x=self._co_x, co_y=self._co_y - 1))
        positions.append(Position(co_x=self._co_x, co_y=self._co_y + 1))
        return positions

    def number_of_square_between_self_and_tested_position(self, tested_position_co_x: int,
                                                          tested_position_co_y: int) -> int:
        tested_position: Position = Position(co_x=tested_position_co_x, co_y=tested_position_co_y)
        return abs(tested_position.co_x - self._co_x) + abs(tested_position.co_y - self._co_y)

    def check_boundaries(self, width: int, height: int):
        if not self._is_position_inside_board_boundaries(width=width, height=height):
            raise OutOfBoundBlockPositionException(position=self,
                                                   width=width, height=height)

    def _is_position_inside_board_boundaries(self, width: int, height: int) -> bool:
        return 0 < self.co_x <= width and 0 < self.co_y <= height

    @property
    def co_x(self) -> int:
        return self._co_x

    @property
    def co_y(self) -> int:
        return self._co_y

    def to_tuple(self) -> (int, int):
        return self._co_x, self._co_y

    def __str__(self) -> str:
        string: str = "Position : { " + " co_x = " + str(self._co_x) + "; co_y = " + str(self._co_y) + " }"
        return string

    def __eq__(self, tested):
        if isinstance(tested, Position):
            return self._co_x == tested.co_x and self._co_y == tested.co_y
        return False


class OutOfBoundBlockPositionException(Exception):
    def __init__(self, position: Position, width: int, height: int):
        super().__init__(
            f'Position {str(position)} is out of bound. Width = {width},Height = {height}')


class Pattern:
    def __init__(self, list_of_movements: List[Movement] = List):
        self._list_of_movements: List[Movement] = list_of_movements

    @property
    def list_of_movements(self):
        return self._list_of_movements
