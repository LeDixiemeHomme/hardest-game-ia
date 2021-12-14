from project.constants import constants
from project.display.viewer import Viewer

from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType


class Agent:
    picture_path: str = constants.AGENT_PICTURE_PATH
    picture_size: str = constants.PICTURE_SIZE

    def __init__(self, position: Position, picture_path: str = picture_path, picture_size: int = picture_size,
                 learning_rate: float = 1, discount_factor: float = 0.5):
        self._position = position
        self._picture_path = picture_path
        self._picture_size = picture_size
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self.__qtable = {}
        self._temp_type = SquareType.START

    def draw(self, viewer: Viewer):
        viewer.draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                          co_x=self._position.co_x, co_y=self._position.co_y)

    def move(self, next_square: Square, viewer: Viewer):
        # draw color type on the current position
        viewer.draw(color=constants.COLOR_WITH_TYPE.get(self._temp_type),
                    rect=viewer.create_rectangle(left_arg=self._position.co_x,
                                                 top_arg=self._position.co_y))

        # update obstacle position and temp_type
        self._position = next_square.position
        self._temp_type = next_square.square_type

        # draw obstacle picture on the next_position
        self.draw(viewer=viewer)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: Position):
        self._position = position

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def discount_factor(self):
        return self._discount_factor

    @property
    def temp_type(self):
        return self._temp_type
