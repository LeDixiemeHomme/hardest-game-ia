from typing import List

from project.custom_exception.none_instantiate_singleton_viewer_exception import NoneInstantiateSingletonViewerException

from project.constants import constants
from project.custom_exception.wrong_display_size_exception import WrongDisplaySizeException
from project.logger.logger import Logger
from project.display.viewer import Viewer

from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.position import Position, OutOfBoundBlockPositionException
from project.model.square import Square
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="board_log")
stdout_logger = logger.stdout_log


class Board:
    def __init__(self, width: int, height: int,
                 position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self._viewer = None
        self._list_of_square: List[Square] = self._init_list_of_square(
            width=width, height=height, position_start=position_start,
            position_goal=position_goal, list_of_obstacle=list_of_obstacle)

    def instantiate_singleton_viewer(self):
        stdout_logger.debug("Instantiate board singleton viewer ...")
        self._viewer: Viewer = Viewer(width=self._width, height=self._height)

    @staticmethod
    def _check_board_size(width: int, height: int):
        if width > 20 or height > 20:
            raise WrongDisplaySizeException(width, height)

    @staticmethod
    def _check_init_position(width: int, height: int, position_start: Position,
                             position_goal: Position, list_of_obstacle: List[Obstacle]):
        position_start.check_boundaries(width=width, height=height)
        position_goal.check_boundaries(width=width, height=height)
        for obstacle in list_of_obstacle:
            obstacle.position.check_boundaries(width=width, height=height)

    def _generate_list_of_square(self, width: int, height: int) -> List[Square]:
        self._check_board_size(width=width, height=height)
        list_of_square: List[Square] = []
        # dans range 1, size + 1 pour que position soit pas de (0 to 9) mais de (1 to 10)
        for x in range(1, width + 1):
            for y in range(1, height + 1):
                list_of_square.append(Square(position=Position(co_x=x, co_y=y), square_type=SquareType.EMPTY))
        return list_of_square

    def _fill_list_of_square_with_init_square(self, width: int, height: int, list_of_obstacle: List[Obstacle],
                                              position_start: Position, position_goal: Position) -> List[Square]:
        filled_list_of_square: List[Square] = self._generate_list_of_square(width=width, height=height)
        filled_list_of_square[self._get_index_of_list_of_square_by_position(position_start)] = \
            Square(position=position_start, square_type=SquareType.START)

        filled_list_of_square[self._get_index_of_list_of_square_by_position(position_goal)] = \
            Square(position=position_goal, square_type=SquareType.GOAL)

        for obstacle in list_of_obstacle:
            obstacle_position = obstacle.position
            filled_list_of_square[self._get_index_of_list_of_square_by_position(position=obstacle_position)] = \
                Square(position=obstacle_position, square_type=SquareType.OBSTACLE)
        return filled_list_of_square

    def _init_list_of_square(self, width: int, height: int,
                             position_start: Position, position_goal: Position,
                             list_of_obstacle: List[Obstacle]) -> List[Square]:
        self._check_board_size(width=width, height=height)
        self._width = width
        self._height = height

        self._check_init_position(width=width, height=height, position_start=position_start,
                                  position_goal=position_goal, list_of_obstacle=list_of_obstacle)
        self._position_start = position_start
        self._position_goal = position_goal
        self._list_of_obstacle: List[Obstacle] = list_of_obstacle

        list_of_square: List[Square] = self._fill_list_of_square_with_init_square(
            width=width, height=height, list_of_obstacle=list_of_obstacle,
            position_start=position_start, position_goal=position_goal)
        return list_of_square

    def _get_index_of_list_of_square_by_position(self, position: Position) -> int:
        position.check_boundaries(width=self._width, height=self._height)
        return self._height * position.co_x - (self._height - position.co_y) - 1

    def get_square_type_from_board_by_position(self, position: Position) -> SquareType:
        return self._list_of_square[
            self._get_index_of_list_of_square_by_position(position)].square_type

    def move_obstacles(self):
        self.viewer.set_tick(time_to_stop=6)
        for obstacle in self._list_of_obstacle:
            self.update_list_of_square(position=obstacle.position, square_type=obstacle.square_type)
            movement_to_apply: Movement = obstacle.get_movement_to_do()
            try:
                position_after_movement: Position = \
                    obstacle.position.apply_movement(movement=movement_to_apply)
                next_square_type: SquareType = self.get_square_type_from_board_by_position(
                    position=position_after_movement)
            except OutOfBoundBlockPositionException:
                position_after_movement = obstacle.position
                next_square_type = obstacle.square_type
            self.update_list_of_square(position=position_after_movement, square_type=SquareType.OBSTACLE)

            obstacle.move_obstacle_if_possible(square_to_move_on=Square(
                position=position_after_movement, square_type=next_square_type), viewer=self.viewer)

    def draw_board(self):
        for square in self._list_of_square:
            rect = self.viewer.create_rectangle(
                left_arg=square.position.co_x, top_arg=square.position.co_y)
            self.viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(square.square_type), rect=rect)

    @property
    def list_of_square(self):
        return self._list_of_square

    def update_list_of_square(self, position: Position, square_type: SquareType):
        self._list_of_square[self._get_index_of_list_of_square_by_position(position=position)] = \
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

    @property
    def viewer(self):
        if self._viewer is None:
            raise NoneInstantiateSingletonViewerException(method_name=self.instantiate_singleton_viewer.__name__)
        return self._viewer

    def __str__(self) -> str:
        string: str = "Board : { height = " + str(self._height) + "; width = " + str(
            self._width) + "; position_start = " + str(self._position_start) + "; width = " + str(
            self._position_goal) + " }"
        return string
