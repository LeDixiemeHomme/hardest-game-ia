from typing import List
import pygame

from project.display.Viewer import Viewer
from project.model import constant
from project.model.Position import Position
from project.model.Obstacle import Obstacle
from project.model.Square import Square
from project.model.SquareType import SquareType


class Board:

    def __init__(self, height: int, width: int,
                 position_start: Position, position_goal: Position, list_of_enemy: List[Obstacle]):
        self.__height = height
        self.__width = width
        self.__position_start = Position(co_x=position_start.co_x * constant.SQUARE_SIZE,
                                         co_y=position_start.co_y * constant.SQUARE_SIZE)
        self.__position_goal = Position(co_x=position_goal.co_x * constant.SQUARE_SIZE,
                                        co_y=position_goal.co_y * constant.SQUARE_SIZE)
        self.__list_of_square: List[Square] = self.init_list_of_square()
        self.__list_of_enemy = list_of_enemy

    @property
    def list_of_square(self):
        return self.__list_of_square

    @property
    def list_of_enemy(self):
        return self.__list_of_enemy

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def position_start(self):
        return self.__position_start

    @property
    def position_goal(self):
        return self.__position_goal

    def init_list_of_square(self) -> List[Square]:
        list_of_square = []
        for i in range(self.__height):
            for y in range(self.__width):
                # on prend ici non pas i mais i fois la taille d'un square pour avoir la proportion
                square_size_time_i = i * constant.SQUARE_SIZE
                square_size_time_y = y * constant.SQUARE_SIZE
                # test si il faut mettre le bloc de type start
                if square_size_time_i == self.__position_start.co_x \
                        and square_size_time_y == self.__position_start.co_y:
                    # ajoute dans le tableau un square
                    list_of_square.append(
                        Square(position=Position(square_size_time_i, square_size_time_y),
                               square_type=self.init_start()))
                # test si il faut mettre le bloc de type start
                elif square_size_time_i == self.__position_goal.co_x \
                        and square_size_time_y == self.__position_goal.co_y:
                    list_of_square.append(
                        Square(position=Position(square_size_time_i, square_size_time_y), square_type=self.init_goal()))
                else:
                    list_of_square.append(
                        Square(position=Position(square_size_time_i, square_size_time_y), square_type=SquareType.EMPTY))

        return list_of_square

    def draw_board(self):
        size = constant.SQUARE_SIZE * constant.DRAW_SCALE
        color = constant.COLOR
        for square in self.__list_of_square:
            rect: pygame.Rect = Viewer().create_rectangle(left_arg=(square.position.co_x * constant.DRAW_SCALE),
                                                          top_arg=(square.position.co_y * constant.DRAW_SCALE),
                                                          width_arg=size,
                                                          height_arg=size)
            if square.square_type == SquareType.GOAL:
                Viewer().draw(color=color.get("GREEN"), rect=rect)
            elif square.square_type == SquareType.START:
                Viewer().draw(color=color.get("RED"), rect=rect)
            elif square.square_type == SquareType.EMPTY:
                Viewer().draw(color=color.get("WHITE"), rect=rect)
            else:
                Viewer().draw(color=color.get("BLACK"), rect=rect)

    def init_start(self) -> SquareType:
        if self.__position_start.co_y < self.__height and self.__position_start.co_x < self.__width:
            return SquareType.START
            # todo throw error if not

    def init_goal(self) -> SquareType:
        if self.__position_goal.co_x < self.__width and self.__position_goal.co_y < self.__height:
            # todo throw error if not
            return SquareType.GOAL
