from project.constants import constants
from project.logger.logger import Logger
from project.model.board import Board, Position
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.position import OutOfBoundBlockPositionException
from project.model.square import Square
from project.model.square_list import SquareList
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="agent_log")
stdout_logger = logger.stdout_log


class Agent:
    picture_path: str = constants.AGENT_PICTURE_PATH
    picture_size: int = constants.PICTURE_SIZE

    def __init__(self, board: Board,
                 qtable: {} = None,
                 picture_path: str = picture_path,
                 picture_size: int = picture_size,
                 learning_rate: float = 1,
                 discount_factor: float = 0.5):
        self._board: Board = board
        self._square: Square = Square(board.position_start, square_type=SquareType.START)
        self._picture_path: str = picture_path
        self._picture_size: int = picture_size
        self._learning_rate: float = learning_rate
        self._discount_factor: float = discount_factor
        if qtable is None:
            self._qtable = self._fill_qtable(square_list=board.square_list)
        else:
            self._qtable = qtable
        self._score = 0

    def _fill_qtable(self, square_list: SquareList) -> {}:
        qtable = {}
        for square in square_list.list_of_square:
            tuple_position = (square.position.co_x, square.position.co_y)
            qtable[tuple_position] = {}
            for direction in Direction.__members__.values():
                qtable[tuple_position][direction] = 0.0
        return qtable

    def update(self, square: Square, action: Direction, reward: int):
        tuple_position = (square.position.co_x, square.position.co_y)

        # Q(s, a) <- Q(s, a) + learning_rate *
        #                     [reward + discount_factor * max(Q(state)) - Q(s, a)]

        max_q: int = max(self._qtable[tuple_position].values())
        self._qtable[tuple_position][action] += self._learning_rate * (
                reward + self._discount_factor * max_q - self._qtable[tuple_position][action])
        self._score += reward

    def best_action(self) -> Direction:
        best_direction: Direction = Direction.STAY
        tuple_position = (self._square.position.co_x, self._square.position.co_y)
        for direction in self._qtable[tuple_position]:
            if self._qtable[tuple_position][direction] > self._qtable[tuple_position][best_direction]:
                best_direction = direction
        return best_direction

    def is_position_on_goal_square(self):
        return self._square.position == self._board.position_goal

    def is_position_on_obstacle_square(self):
        for obstacle in self._board.list_of_obstacle:
            if obstacle.position == self._square.position:
                return True
        return False

    def draw_image_on_current_position(self):
        self.board.viewer.viewer_draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                                            co_x=self._square.position.co_x, co_y=self._square.position.co_y)

    def draw_square_type_on_position(self, position_to_draw: Position):
        self.board.viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(self._square.square_type),
                                      rect=self.board.viewer.create_rectangle(
                                          left_arg=position_to_draw.co_x, top_arg=position_to_draw.co_y))

    def move_agent_if_possible(self, requested_movement: Movement):
        try:
            next_position: Position = self._square.position.apply_movement(movement=requested_movement)
            next_square_type: SquareType = \
                self._board.square_list.get_square_type_from_board_by_position(position=next_position)
        except OutOfBoundBlockPositionException:
            next_position: Position = self._square.position
            next_square_type: SquareType = self._square.square_type
        self._move(square_to_move_on=Square(position=next_position, square_type=next_square_type))

    def _move(self, square_to_move_on: Square):
        self.draw_square_type_on_position(position_to_draw=self._square.position)
        self._square = square_to_move_on
        self.draw_image_on_current_position()

    def _update_then_move(self, square_to_move_on: Square, action: Direction, reward: int):
        self.update(square=self._square, action=action, reward=reward)
        self._move(square_to_move_on=square_to_move_on)

    def move_agent_with_qtable_update(self, requested_movement: Movement) -> int:
        try:
            next_position: Position = self._square.position.apply_movement(movement=requested_movement)
            next_square_type: SquareType = \
                self._board.square_list.get_square_type_from_board_by_position(position=next_position)
            reward = constants.REWARD_WITH_TYPE.get(next_square_type)
        except OutOfBoundBlockPositionException:
            next_position: Position = self._square.position
            next_square_type: SquareType = self._square.square_type
            reward = constants.REWARD_WITH_TYPE.get(SquareType.WALL)
        self._update_then_move(square_to_move_on=Square(position=next_position, square_type=next_square_type),
                               action=requested_movement.direction, reward=reward)
        return reward

    @property
    def board(self):
        return self._board

    @property
    def learning_rate(self):
        return self._learning_rate

    @property
    def discount_factor(self):
        return self._discount_factor

    @property
    def score(self):
        return self._score

    @property
    def qtable(self):
        return self._qtable
