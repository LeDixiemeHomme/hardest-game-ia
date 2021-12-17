from project.constants import constants
from project.logger.logger import Logger
from project.model.board import Board, Position, Square, SquareType, \
    Movement, OutOfBoundBlockPositionException

logger: Logger = Logger(name=__name__, log_file_name="agent_log")
stdout_logger = logger.stdout_log


class Agent:
    picture_path: str = constants.AGENT_PICTURE_PATH
    picture_size: str = constants.PICTURE_SIZE

    def __init__(self, board: Board,
                 picture_path: str = picture_path,
                 picture_size: int = picture_size,
                 learning_rate: float = 1,
                 discount_factor: float = 0.5):
        self._board = board
        self._position = board.position_start
        self._picture_path = picture_path
        self._picture_size = picture_size
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self.__qtable = {}
        self._square_type = SquareType.START

    def is_position_on_goal_square(self):
        return self._position == self._board.position_goal

    def is_position_on_obstacle_square(self):
        for obstacle in self._board.list_of_obstacle:
            if obstacle.is_position_same(position_to_test=self._position):
                return True
        return False

    def draw_image_on_current_position(self):
        self.board.viewer.viewer_draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                                            co_x=self._position.co_x, co_y=self._position.co_y)

    def draw_square_type_on_position(self, position_to_draw: Position):
        self.board.viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(self._square_type),
                                      rect=self.board.viewer.create_rectangle(
                                          left_arg=position_to_draw.co_x, top_arg=position_to_draw.co_y))

    def move_agent_if_possible(self, requested_movement: Movement):
        try:
            next_position: Position = self._position.apply_movement(movement=requested_movement)
            next_square_type: SquareType = self._board.get_square_type_from_board_by_position(position=next_position)
        except OutOfBoundBlockPositionException:
            next_position: Position = self._position
            next_square_type: SquareType = self._square_type
        self.move(square_to_move_on=Square(position=next_position, square_type=next_square_type))

    def move(self, square_to_move_on: Square):
        self.draw_square_type_on_position(position_to_draw=self._position)
        self._position = square_to_move_on.position
        self.draw_image_on_current_position()
        self._square_type = square_to_move_on.square_type

    @property
    def position(self):
        return self._position

    @property
    def board(self):
        return self._board

    @position.setter
    def position(self, position: Position):
        self._position = position

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def discount_factor(self):
        return self._discount_factor
