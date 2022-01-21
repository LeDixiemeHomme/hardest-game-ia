from copy import copy
from typing import List

from project.model.position import Position
from project.model.square_type import SquareType


class StateWithSurrounding:
    def __init__(self, center_square: 'Square', list_square: List['Square']):
        self._center_square = center_square
        self._list_square = list_square

    @property
    def center_square(self):
        return self._center_square

    @property
    def list_square(self):
        return self._list_square

    def __str__(self) -> str:
        string: str = "Square : { " + str(self._center_square) + " }"
        return string

    def __eq__(self, tested):
        if isinstance(tested, StateWithSurrounding):
            return self._center_square == tested.center_square and self._list_square == tested.list_square
        return False

    def __hash__(self):
        concat: int = hash(self._center_square)
        for square in self._list_square:
            concat += hash(square)
        return hash(concat)


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self._position: Position = position
        self._square_type: SquareType = square_type

    def _create_state(self, index_in_surrounding_with_square_type: {int: SquareType}) -> StateWithSurrounding:
        copy_self: Square = copy(self)
        if len(index_in_surrounding_with_square_type) > len(copy_self.position.get_surrounding_positions()):
            raise Exception
        for index_square_type in index_in_surrounding_with_square_type:
            if index_square_type > len(copy_self.position.get_surrounding_positions()):
                raise Exception

        state: StateWithSurrounding = StateWithSurrounding(center_square=copy_self, list_square=[])
        for i in range(len(copy_self.position.get_surrounding_positions())):
            contains: bool = False
            position: Position = copy_self.position.get_surrounding_positions()[i]
            square_type: SquareType = SquareType.EMPTY
            for index_square_type in index_in_surrounding_with_square_type:
                if i == index_square_type:
                    contains = True
            if contains:
                square_type = index_in_surrounding_with_square_type.get(i)
            square_to_add: Square = Square(position=position, square_type=square_type)
            state.list_square.append(square_to_add)
        if copy_self.square_type == SquareType.START:
            state.list_square[0] = copy_self
        return state

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
