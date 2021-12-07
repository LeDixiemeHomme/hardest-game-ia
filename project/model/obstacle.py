from project.constants import constants
from project.display.viewer import VIEWER

from project.model.pattern import Pattern
from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType


class Obstacle:
    picture_path: str = constants.OBSTACLE_PICTURE_PATH
    picture_size: str = constants.PICTURE_SIZE

    def __init__(self, position: Position, pattern: Pattern,
                 picture_path: str = picture_path, picture_size: int = picture_size):
        self._picture_path = picture_path
        self._picture_size = picture_size
        self._position = position
        self._pattern: Pattern = pattern
        self._pattern_state = 0
        self._temp_type = SquareType.EMPTY

    def draw_obstacle(self):
        VIEWER.draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                          co_x=self._position.co_x, co_y=self._position.co_y)

    def is_position_inside(self, position_to_test: Position) -> bool:
        return self._position.co_x <= position_to_test.co_x <= self._position.co_x + constants.SQUARE_SIZE \
               and self._position.co_y <= position_to_test.co_y <= self._position.co_y + constants.SQUARE_SIZE

    def move(self, next_square: Square):
        # draw color type on the current position
        VIEWER.draw(color=constants.COLOR_WITH_TYPE.get(self._temp_type),
                    rect=VIEWER.create_rectangle(left_arg=self._position.co_x,
                                                 top_arg=self._position.co_y))

        # update obstacle position and temp_type
        self.position = next_square.position
        self.temp_type = next_square.square_type

        # draw obstacle picture on the next_position
        self.draw_obstacle()

        # increase pattern state when the move is done
        self.increment_pattern_state()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: int):
        self._position = position

    @property
    def temp_type(self):
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type: SquareType):
        self._temp_type = temp_type

    @property
    def pattern(self):
        return self._pattern

    @property
    def pattern_state(self):
        return self._pattern_state

    def increment_pattern_state(self):
        self._pattern_state += 1

    @property
    def picture_path(self):
        return self._picture_path

    @property
    def picture_size(self):
        return self._picture_size

    def __str__(self) -> str:
        string: str = "Obstacle : { " + str(self._position) + "; " + \
                      str(self._pattern) + "; picture = " + str(self._picture_path) + " }"
        return string
