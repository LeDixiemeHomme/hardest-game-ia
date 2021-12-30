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

    @staticmethod
    def create_dict_index_with_square_type(starting_point: int, number_of_square: int,
                                           length_of_surrounding: int, square_type: SquareType) -> {int: SquareType}:
        result_dict: {int: SquareType} = {}
        for i in range(starting_point, number_of_square + starting_point):
            result_dict[i % length_of_surrounding] = square_type
        return result_dict

    def _part_state(self, iterator: int, i: int, nb_surrounding_position: int) -> [StateWithSurrounding]:
        list_of_possible_state: List[StateWithSurrounding] = []
        for y in range(iterator):
            dict_ind_squ_type = \
                self.create_dict_index_with_square_type(starting_point=y, number_of_square=i,
                                                        length_of_surrounding=nb_surrounding_position,
                                                        square_type=SquareType.OBSTACLE)
            list_of_possible_state.append(
                self._create_state(index_in_surrounding_with_square_type=dict_ind_squ_type))
            dict_temp = copy(dict_ind_squ_type)
            if y - 1 >= 0:
                dict_temp[y - 1] = SquareType.GOAL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
            dict_temp = copy(dict_ind_squ_type)
            if y + i < nb_surrounding_position:
                dict_temp[y + i] = SquareType.GOAL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
            dict_temp = copy(dict_ind_squ_type)
            if y - 1 >= 0:
                dict_temp[y - 1] = SquareType.WALL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
            dict_temp = copy(dict_ind_squ_type)
            if y + i < nb_surrounding_position:
                dict_temp[y + i] = SquareType.WALL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
        return list_of_possible_state

    def all_possible_state(self) -> [StateWithSurrounding]:
        # ça retourne une liste qui va etre iteré pour avoir les key de la qtable
        list_of_possible_state: List[StateWithSurrounding] = []
        nb_surrounding_position: int = len(self.position.get_surrounding_positions())
        for i in range(nb_surrounding_position+1):
            # elif i == 3:
            if i == 0:
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type={}))
            if i == 1:
                for y in range(nb_surrounding_position):
                    dict_ind_squ_type = \
                        self.create_dict_index_with_square_type(starting_point=y, number_of_square=i,
                                                                length_of_surrounding=nb_surrounding_position,
                                                                square_type=SquareType.GOAL)
                    list_of_possible_state.append(
                        self._create_state(index_in_surrounding_with_square_type=dict_ind_squ_type))

                for y in range(nb_surrounding_position):
                    dict_ind_squ_type = \
                        self.create_dict_index_with_square_type(starting_point=y, number_of_square=i,
                                                                length_of_surrounding=nb_surrounding_position,
                                                                square_type=SquareType.WALL)
                    list_of_possible_state.append(
                        self._create_state(index_in_surrounding_with_square_type=dict_ind_squ_type))

                ind_squ_type = self._part_state(iterator=nb_surrounding_position, i=i,
                                                nb_surrounding_position=nb_surrounding_position)
                for state in ind_squ_type:
                    list_of_possible_state.append(state)

            elif i == 2:
                ind_squ_type = self._part_state(iterator=4, i=i, nb_surrounding_position=nb_surrounding_position)
                for state in ind_squ_type:
                    list_of_possible_state.append(state)
            elif i == 3:
                ind_squ_type = self._part_state(iterator=3, i=i, nb_surrounding_position=nb_surrounding_position)
                for state in ind_squ_type:
                    list_of_possible_state.append(state)
            elif i == 4:
                ind_squ_type = self._part_state(iterator=2, i=i, nb_surrounding_position=nb_surrounding_position)
                for state in ind_squ_type:
                    list_of_possible_state.append(state)
            elif i == 5:
                ind_squ_type = self._part_state(iterator=1, i=i, nb_surrounding_position=nb_surrounding_position)
                for state in ind_squ_type:
                    list_of_possible_state.append(state)
        return list_of_possible_state

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
