from copy import copy

from project.model.direction import Direction
from project.model.movement import Movement


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

    @co_x.setter
    def co_x(self, co_x: int):
        self._co_x = co_x

    @co_y.setter
    def co_y(self, co_y: int):
        self._co_y = co_y

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
