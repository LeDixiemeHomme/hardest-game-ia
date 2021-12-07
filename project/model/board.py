import pygame
from typing import List

from project.custom_exception.out_of_bound_block_position_exception import OutOfBoundBlockPositionException

from project.constants import constants
from project.logger.logger import Logger
from project.display.viewer import VIEWER

from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="board_log")
stdout_logger = logger.stdout_log


class Board:
    def __init__(self, width: int, height: int, position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        stdout_logger.debug("init board")
        self._position_start = position_start
        self._position_goal = position_goal
        self._list_of_obstacle: List[Obstacle] = list_of_obstacle
        self._width = width
        self._height = height
        self._init_start()
        self._init_goal()
        self._init_list_of_obstacle()
        self._list_of_square: List[Square] = self._init_list_of_square()

    def _init_start(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_start):
            raise OutOfBoundBlockPositionException(position=self._position_start, square_type=SquareType.START,
                                                   width=self._width, height=self._height)
        return SquareType.START

    def _init_goal(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_goal):
            raise OutOfBoundBlockPositionException(position=self._position_goal, square_type=SquareType.GOAL,
                                                   width=self._width, height=self._height)
        return SquareType.GOAL

    def _init_list_of_square(self) -> List[Square]:
        list_of_square = []
        # dans range 1, size + 1 pour que position(0, 9) -> position(1, 10)
        for x in range(1, self._width + 1):
            for y in range(1, self._height + 1):
                list_of_square.append(Square(position=Position(x, y), square_type=SquareType.EMPTY))

        list_of_square[self.get_index_of_list_of_square_by_position(self._position_start)] = \
            Square(position=self._position_start, square_type=SquareType.START)

        list_of_square[self.get_index_of_list_of_square_by_position(self._position_goal)] = \
            Square(position=self._position_goal, square_type=SquareType.GOAL)

        for obstacle in self._list_of_obstacle:
            obstacle_position = obstacle.position
            list_of_square[self.get_index_of_list_of_square_by_position(position=obstacle_position)] = \
                Square(position=obstacle_position, square_type=SquareType.OBSTACLE)

        return list_of_square

    def _init_list_of_obstacle(self) -> List[Obstacle]:
        for obstacle in self._list_of_obstacle:
            if not self.is_position_inside_board_boundaries(obstacle.position):
                raise OutOfBoundBlockPositionException(position=obstacle.position, square_type=SquareType.OBSTACLE,
                                                       width=self._width, height=self._height)
        return self._list_of_obstacle

    def move_obstacles(self):
        VIEWER.set_tick(time_to_stop=6)
        for obstacle in self._list_of_obstacle:

            current_position: Position = obstacle.position
            current_position_type: SquareType = obstacle.temp_type
            current_movement: Movement = obstacle.pattern.list_of_movements[
                obstacle.pattern_state % len(obstacle.pattern.list_of_movements)]

            try:
                next_position: Position = self.get_position_after_movement(current_position=current_position,
                                                                           current_movement=current_movement)
                next_square_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
            except OutOfBoundBlockPositionException:
                next_position: Position = current_position
                next_square_type = current_position_type

            # draw the obstacle on the next block
            next_square: Square = Square(position=next_position, square_type=next_square_type)
            obstacle.move(next_square=next_square)

            # update the list of square to set the new type at the current_position and the next_position
            self.update_list_of_square(position=current_position, square_type=current_position_type)
            self.update_list_of_square(position=next_square.position, square_type=SquareType.OBSTACLE)

    def draw_board(self):
        for square in self._list_of_square:
            rect: pygame.Rect = VIEWER.create_rectangle(
                left_arg=square.position.co_x, top_arg=square.position.co_y)
            VIEWER.draw(color=constants.COLOR_WITH_TYPE.get(square.square_type), rect=rect)

    def get_square_type_from_board_by_position(self, position: Position) -> SquareType:
        if not self.is_position_inside_board_boundaries(position_to_test=position):
            raise OutOfBoundBlockPositionException(position=position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)
        return self._list_of_square[
            self.get_index_of_list_of_square_by_position(position)].square_type

    def get_index_of_list_of_square_by_position(self, position: Position) -> int:
        if not self.is_position_inside_board_boundaries(position_to_test=position):
            raise OutOfBoundBlockPositionException(position=position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)
        return self._height * position.co_x - (self._height - position.co_y) - 1

    def get_position_after_movement(self, current_position: Position, current_movement: Movement) -> Position:
        if not self.is_position_inside_board_boundaries(position_to_test=current_position):
            raise OutOfBoundBlockPositionException(position=current_position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)

        position_after_movement: Position = Position(co_x=current_position.co_x, co_y=current_position.co_y)

        direction = current_movement.direction
        length = current_movement.length

        if direction == Direction.UP:
            position_after_movement.co_y -= length
        elif direction == Direction.DOWN:
            position_after_movement.co_y += length
        elif direction == Direction.LEFT:
            position_after_movement.co_x -= length
        elif direction == Direction.RIGHT:
            position_after_movement.co_x += length

        return position_after_movement

    def is_position_inside_board_boundaries(self, position_to_test: Position) -> bool:
        return 0 < position_to_test.co_x <= self._width and 0 < position_to_test.co_y <= self._height

    @property
    def list_of_square(self):
        return self._list_of_square

    def update_list_of_square(self, position: Position, square_type: SquareType):
        self._list_of_square[self.get_index_of_list_of_square_by_position(position=position)] = \
            Square(position=position, square_type=square_type)

    @property
    def list_of_obstacle(self):
        return self._list_of_obstacle

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def position_start(self):
        return self._position_start

    @property
    def position_goal(self):
        return self._position_goal

    def __str__(self) -> str:
        string: str = "Board : { height = " + str(self._height) + "; width = " + str(
            self._width) + "; position_start = " + str(self._position_start) + "; width = " + str(
            self._position_goal) + " }"
        return string
