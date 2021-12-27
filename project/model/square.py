from copy import copy
from typing import List

from project.model.position import Position
from project.model.square_type import SquareType


class StateWithSurrounding:
    def __init__(self, center_square: 'Square', index_square_type: {int: SquareType}):
        self._square = center_square
        self._list_square = None


class Square:
    def __init__(self, position: Position, square_type: SquareType):
        self._position: Position = position
        self._square_type: SquareType = square_type

    def create_dict_index_with_square_type(self, starting_point: int, number_of_square: int,
                                           length_of_surrounding: int, square_type: SquareType) -> {int: SquareType}:
        result_dict: {int: SquareType} = {}
        for i in range(starting_point, number_of_square + starting_point):
            result_dict[i % length_of_surrounding] = square_type
        # if number_of_square == length_of_surrounding:
        #     for i in range(starting_point, number_of_square + starting_point):
        #         result_dict[i] = square_type

        # print("------------------------------------------------------")
        # for key, value in result_dict.items():
        #     print(key, value)
        # print("------------------------------------------------------")
        return result_dict

    def part_state(self, iterator: int, i: int, nb_surrounding_position: int) -> List[{'Square': ['Square']}]:
        list_of_possible_state: List[{Square: [Square]}] = []
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
            if y + i < nb_surrounding_position:
                dict_temp[y + i] = SquareType.WALL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
            dict_temp = copy(dict_ind_squ_type)
            if y - 1 >= 0:
                dict_temp[y - 1] = SquareType.WALL
                list_of_possible_state.append(
                    self._create_state(index_in_surrounding_with_square_type=dict_temp))
            return list_of_possible_state

    def all_possible_state(self) -> [{'Square': ['Square']}]:
        # ça retourne une liste qui va etre iteré pour avoir les key de la qtable
        list_of_possible_state: List[{Square: [Square]}] = []
        nb_surrounding_position: int = len(self.position.get_surrounding_positions())
        for i in range(nb_surrounding_position+1):
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

                for y in range(nb_surrounding_position):
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
                    if y + i < nb_surrounding_position:
                        dict_temp[y + i] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
                    dict_temp = copy(dict_ind_squ_type)
                    if y - 1 >= 0:
                        dict_temp[y - 1] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))

            elif i == 2:
                for y in range(4):
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
                    if y + i < nb_surrounding_position:
                        dict_temp[y + i] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
                    dict_temp = copy(dict_ind_squ_type)
                    if y - 1 >= 0:
                        dict_temp[y - 1] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
            elif i == 3:
                for y in range(3):
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
                    if y + i < nb_surrounding_position:
                        dict_temp[y + i] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
                    dict_temp = copy(dict_ind_squ_type)
                    if y - 1 >= 0:
                        dict_temp[y - 1] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
            elif i == 4:
                for y in range(2):
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
                    if y + i < nb_surrounding_position:
                        dict_temp[y + i] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
                    dict_temp = copy(dict_ind_squ_type)
                    if y - 1 >= 0:
                        dict_temp[y - 1] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
            elif i == 5:
                for y in range(1):
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
                    if y + i < nb_surrounding_position:
                        dict_temp[y + i] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))
                    dict_temp = copy(dict_ind_squ_type)
                    if y - 1 >= 0:
                        dict_temp[y - 1] = SquareType.WALL
                        list_of_possible_state.append(
                            self._create_state(index_in_surrounding_with_square_type=dict_temp))





            # else:
            #     dict_ind_squ_type = \
            #         self.create_dict_index_with_square_type(starting_point=x, number_of_square=i,
            #                                                 length_of_surrounding=nb_surrounding_position,
            #                                                 square_type=SquareType.OBSTACLE)
            #     list_of_possible_state.append(
            #         self._create_state(dict_index_in_surrounding_with_square_type=dict_ind_squ_type))




            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type={i: SquareType.GOAL}))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {i: SquareType.GOAL,
            #                         ((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {i: SquareType.GOAL,
            #                         ((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {i: SquareType.GOAL,
            #                         ((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 3) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {i: SquareType.GOAL,
            #                         ((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 3) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 4) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 3) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 3) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 4) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
            # list_of_possible_state.append(
            #     self._create_state(dict_index_in_surrounding_with_square_type=
            #                        {((i + 1) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 2) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 3) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 4) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         ((i + 5) % nb_surrounding_position): SquareType.OBSTACLE,
            #                         }))
        return list_of_possible_state

    def temp_create_state(self, dict_index_square_type: {int: SquareType}) -> StateWithSurrounding:
        state: StateWithSurrounding = StateWithSurrounding(center_square=self, index_square_type=dict_index_square_type)

        return state

    def _create_state(self, index_in_surrounding_with_square_type: {int: SquareType}) -> {'Square': ['Square']}:
        copy_self: Square = copy(self)
        if len(index_in_surrounding_with_square_type) > len(copy_self.position.get_surrounding_positions()):
            raise Exception
        for index_square_type in index_in_surrounding_with_square_type:
            if index_square_type > len(copy_self.position.get_surrounding_positions()):
                raise Exception

        state: {Square: [Square]} = {copy_self: []}
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
            state[copy_self].append(square_to_add)
        if copy_self.square_type == SquareType.START:
            state[copy_self][0] = copy_self
        # for squ, sques in state.items():
        #     print("------------------> ", squ)
        #     for elem in sques:
        #         print(elem)
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
