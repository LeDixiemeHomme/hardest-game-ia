import pygame
from typing import List

from project.constant import constant
from project.model.obstacle import Obstacle
from project.model.square import Square, SquareType, Position
from project.exception.out_of_bond_block_position import OutOfBoundBlockPosition


class Board:
    def __init__(self, width: int, height: int, position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self.__position_start = position_start
        self.__position_goal = position_goal
        self.__list_of_obstacle: List[Obstacle] = list_of_obstacle
        self.__width = width
        self.__height = height
        self.init_start()
        self.init_goal()
        self.init_list_of_obstacle()
        self.__list_of_square: List[Square] = self.init_list_of_square()

    @property
    def list_of_square(self):
        return self.__list_of_square

    def update_list_of_square(self, position: Position, square_type: SquareType):
        self.__list_of_square[self.position_to_list_of_square_index(position=position)] = Square(position=position,
                                                                                                 square_type=square_type)

    @property
    def list_of_obstacle(self):
        return self.__list_of_obstacle

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def position_start(self):
        return self.__position_start

    @property
    def position_goal(self):
        return self.__position_goal

    def init_list_of_square(self) -> List[Square]:
        list_of_square = []
        # dans range 1, + 1 pour que position(0, 9) -> position(1, 10)
        for x in range(1, self.__width + 1):
            for y in range(1, self.__height + 1):
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
        color = constant.COLOR
        for square in self.__list_of_square:
            rect: pygame.Rect = constant.VIEWER \
                .create_rectangle(left_arg=square.position.co_x,
                                  top_arg=square.position.co_y)
            if square.square_type == SquareType.GOAL:
                constant.VIEWER.draw(color=color.get("GREEN"), rect=rect)
            elif square.square_type == SquareType.START:
                constant.VIEWER.draw(color=color.get("RED"), rect=rect)
            elif square.square_type == SquareType.EMPTY:
                constant.VIEWER.draw(color=color.get("WHITE"), rect=rect)
            else:
                constant.VIEWER.draw(color=color.get("BLUE"), rect=rect)

    def init_start(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self.__position_start):
            raise OutOfBoundBlockPosition(position=self.__position_start, square_type=SquareType.START,
                                          width=self.__width, height=self.__height)
        return SquareType.START

    def init_goal(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self.__position_goal):
            raise OutOfBoundBlockPosition(position=self.__position_goal, square_type=SquareType.GOAL,
                                          width=self.__width, height=self.__height)
        return SquareType.GOAL

    def init_list_of_obstacle(self) -> List[Obstacle]:
        for obstacle in self.__list_of_obstacle:
            if not self.is_position_inside_board_boundaries(obstacle.initial_position):
                raise OutOfBoundBlockPosition(position=obstacle.initial_position, square_type=SquareType.OBSTACLE,
                                              width=self.__width, height=self.__height)
        return self.__list_of_obstacle

    def get_square_type_from_board(self, position: Position) -> SquareType:
        return self.__list_of_square[
            self.position_to_list_of_square_index(position)].square_type

    def position_to_list_of_square_index(self, position: Position) -> int:
        return self.__height * position.co_x - (self.__height - position.co_y) - 1

    def is_position_inside_board_boundaries(self, position_to_test: Position) -> bool:
        return 0 < position_to_test.co_x <= self.__width and 0 < position_to_test.co_y <= self.__height

    # def list_of_obstacle_position(self): -> List[List[int]]:

    def __str__(self) -> str:
        string: str = "Board : { height = " + str(self.__height) + "; width = " + str(
            self.__width) + "; position_start = " + str(self.__position_start) + "; width = " + str(
            self.__position_goal) + "; list_of_obstacle = " + str(*self.__list_of_obstacle) + " }"
        return string
