from typing import List

from project.model.movement import Movement


class Pattern:

    def __init__(self, list_of_movements: List[Movement]):
        self.__list_of_movements = list_of_movements

    @property
    def list_of_movements(self):
        return self.__list_of_movements
