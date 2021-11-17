import pygame
from typing import List

from project.model.position import Position
from project.model.obstacle import Obstacle
from project.model.square import Square
from project.model.square_type import SquareType
from project.constant import constant
from project.exception.out_of_bond_block_position import OutOfBondBlockPosition


class Board:

    def __init__(self, height: int, width: int, position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self.__height = height
        self.__width = width
        self.__position_start = Position(co_x=position_start.co_x, co_y=position_start.co_y)
        self.__position_goal = Position(co_x=position_goal.co_x, co_y=position_goal.co_y)
        self.__list_of_square: List[Square] = self.init_list_of_square()
        self.__list_of_obstacle = list_of_obstacle
        self.init_start()
        self.init_goal()

    @property
    def list_of_square(self):
        return self.__list_of_square

    @property
    def list_of_obstacle(self):
        return self.__list_of_obstacle

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
        for x in range(1, self.__height + 1):
            for y in range(1, self.__width + 1):
                # test si il faut mettre le bloc de type start
                if x == self.__position_start.co_x \
                        and y == self.__position_start.co_y:
                    # ajoute dans le tableau un square
                    list_of_square.append(
                        Square(position=Position(x, y), square_type=SquareType.START))
                # test si il faut mettre le bloc de type start
                elif x == self.__position_goal.co_x \
                        and y == self.__position_goal.co_y:
                    list_of_square.append(
                        Square(position=Position(x, y), square_type=SquareType.GOAL))
                else:
                    list_of_square.append(
                        Square(position=Position(x, y), square_type=SquareType.EMPTY))

        return list_of_square

    def draw_board(self):
        size = constant.SQUARE_SIZE * constant.DRAW_SCALE
        color = constant.COLOR
        for square in self.__list_of_square:
            rect: pygame.Rect = constant.VIEWER \
                .create_rectangle(left_arg=(square.position.co_x * constant.DRAW_SCALE),
                                  top_arg=(square.position.co_y * constant.DRAW_SCALE),
                                  width_arg=size, height_arg=size)
            if square.square_type == SquareType.GOAL:
                constant.VIEWER.draw(color=color.get("GREEN"), rect=rect)
            elif square.square_type == SquareType.START:
                constant.VIEWER.draw(color=color.get("RED"), rect=rect)
            elif square.square_type == SquareType.EMPTY:
                constant.VIEWER.draw(color=color.get("WHITE"), rect=rect)
            else:
                constant.VIEWER.draw(color=color.get("BLUE"), rect=rect)

    def init_start(self) -> SquareType:
        if 0 >= self.__position_start.co_x > self.__width or 0 >= self.__position_start.co_y > self.__height \
                or self.__position_start.co_x <= 0 or self.__position_start.co_y <= 0:
            raise OutOfBondBlockPosition(position=self.__position_start, square_type=SquareType.START)
        return SquareType.START

    def init_goal(self) -> SquareType:
        if self.__position_goal.co_x > self.__width or 0 >= self.__position_goal.co_y > self.__height \
                or self.__position_goal.co_x <= 0 or self.__position_goal.co_y <= 0:
            raise OutOfBondBlockPosition(position=self.__position_goal, square_type=SquareType.GOAL)
        return SquareType.GOAL
