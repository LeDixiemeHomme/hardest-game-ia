from typing import List

from project.model.position import Position
from project.model.square_type import SquareType


class StateWithSurrounding:
    # a state is square types around a position and distance from goal and start of those positions
    def __init__(self, list_square_types: List['SquareType'], position_self: Position,
                 position_goal: Position, position_start: Position):
        distances_from_goal: List[int] = []
        distances_from_start: List[int] = []
        self._list_square_types = \
            [entry if entry != SquareType.START else SquareType.EMPTY for entry in list_square_types]

        for position_next in position_self.get_surrounding_positions():
            distances_from_start.append(
                position_next.number_of_square_between_positions(
                    tested_position_co_x=position_start.co_x, tested_position_co_y=position_start.co_y))
            distances_from_goal.append(
                position_next.number_of_square_between_positions(
                    tested_position_co_x=position_goal.co_x, tested_position_co_y=position_goal.co_y))
        self._distances_from_goal = distances_from_goal
        self._distances_from_start = distances_from_start

    @property
    def list_square_types(self):
        return self._list_square_types

    @property
    def distances_from_goal(self):
        return self._distances_from_goal

    @property
    def distances_from_start(self):
        return self._distances_from_start

    def __eq__(self, tested):
        if isinstance(tested, StateWithSurrounding):
            return self._list_square_types == tested.list_square_types \
                   and self._distances_from_goal == tested.distances_from_goal
        return False

    def __hash__(self):
        concat: int = 0
        for square in self._list_square_types:
            concat += hash(square)
        for dist in self._distances_from_goal:
            concat += hash(dist)
        return hash(concat)


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self._position: Position = position
        self._square_type: SquareType = square_type

    @property
    def position(self):
        return self._position

    @property
    def square_type(self):
        return self._square_type

    def __str__(self) -> str:
        string: str = "Square : { " + str(self._position) + "; " + str(self._square_type) + " }"
        return string

    def __eq__(self, tested):
        if isinstance(tested, Square):
            return self._position == tested.position and self._square_type == tested.square_type
        return False

    def __hash__(self):
        return hash((self._position, self._square_type))
