from typing import List

from project.custom_exception.none_instantiate_singleton_viewer_exception import NoneInstantiateSingletonViewerException
from project.custom_exception.wrong_display_size_exception import WrongDisplaySizeException
from project.constants import constants
from project.logger.logger import Logger
from project.display.viewer import Viewer

from project.model.obstacle import Obstacle, Position
from project.model.square import Square
from project.model.square_list import SquareList
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="board_log")
stdout_logger = logger.stdout_log


class Board:
    def __init__(self, width: int, height: int,
                 position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self._viewer = None
        self._square_list: SquareList = self._init_square_list(
            width=width, height=height, list_of_obstacle=list_of_obstacle,
            position_start=position_start, position_goal=position_goal)

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

    def _init_square_list(self, width: int, height: int, list_of_obstacle: List[Obstacle],
                          position_start: Position, position_goal: Position) -> SquareList:
        self._check_board_size(width=width, height=height)
        self._width = width
        self._height = height

        self._check_init_position(width=width, height=height, position_start=position_start,
                                  position_goal=position_goal, list_of_obstacle=list_of_obstacle)
        self._position_start = position_start
        self._position_goal = position_goal
        self._list_of_obstacle: List[Obstacle] = list_of_obstacle

        square_list: SquareList = SquareList(width=width, height=height,
                                             position_start=position_start, position_goal=position_goal)

        for obstacle in list_of_obstacle:
            obstacle_position = obstacle.position
            square_list.put_square_in_list_of_square(square_to_put=Square(
                position=obstacle_position, square_type=SquareType.OBSTACLE))
        return square_list

    def move_obstacles(self):
        self.viewer.set_tick(time_to_stop=6)
        for obstacle in self._list_of_obstacle:
            new_square_list: SquareList = obstacle.move_obstacle_if_possible(square_list=self._square_list,
                                                                             viewer=self.viewer)
            self._square_list = new_square_list

    def draw_board(self):
        for square in self._square_list.list_of_square:
            rect = self.viewer.create_rectangle(
                left_arg=square.position.co_x, top_arg=square.position.co_y)
            self.viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(square.square_type), rect=rect)

    @property
    def square_list(self):
        return self._square_list

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
