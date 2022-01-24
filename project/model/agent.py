from typing import List

from project.constants import constants, game_constants
from project.logger.logger import Logger
from project.model.board import Board, Position
from project.model.movement import Movement, Direction
from project.model.position import OutOfBoundBlockPositionException
from project.model.q_table import QTable
from project.model.square import Square, StateWithSurrounding
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="agent_log")
stdout_logger = logger.stdout_log


class Agent:
    picture_path: str = constants.AGENT_PICTURE_PATH
    picture_size: int = constants.PICTURE_SIZE

    def __init__(self, board: Board,
                 qtable: QTable = None,
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
        self._score = 0
        self._history: List[int] = []
        if qtable is None:
            self._qtable = QTable()
        else:
            self._qtable = qtable

    def best_action(self) -> Direction:
        self_state = self._give_state()
        if self_state not in self._qtable.table:
            self._qtable.add_state_to_table(state_to_add=self_state)
        return self._qtable.give_best_direction(state_to_search=self_state)

    def is_next_position_closer_from_goal_than_self_position(self, next_position: Position) -> bool:
        return self._board.distance_from_position_goal(position_to_test=self._square.position) \
               > self._board.distance_from_position_goal(position_to_test=next_position)

    def is_position_on_goal_square(self):
        return self._square.position == self._board.position_goal

    def is_position_on_obstacle_square(self):
        for obstacle in self._board.list_of_obstacle:
            if obstacle.position == self._square.position:
                return True
        return False

    def get_surrounding_squares(self) -> List[Square]:
        return self._board.square_list.get_surrounding_squares(self._square.position)

    def get_surrounding_square_types(self) -> List[SquareType]:
        return self._board.square_list.get_surrounding_square_types(self._square.position)

    def draw_image_on_current_position(self):
        self.board.viewer.viewer_draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                                            co_x=self._square.position.co_x, co_y=self._square.position.co_y)

    def draw_square_type_on_position(self, position_to_draw: Position):
        self.board.viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(self._square.square_type),
                                      rect=self.board.viewer.create_rectangle(
                                          left_arg=position_to_draw.co_x, top_arg=position_to_draw.co_y))

    def move_agent_if_possible(self, requested_movement: Movement, should_qtable_be_updated: bool):
        try:
            next_position: Position = self._square.position.apply_movement(movement=requested_movement)
            next_square_type: SquareType = \
                self._board.square_list.get_square_type_from_board_by_position(position=next_position)
            if next_square_type is SquareType.START:
                reward = game_constants.REWARD_WITH_TYPE.get(SquareType.EMPTY)
            else:
                reward = game_constants.REWARD_WITH_TYPE.get(next_square_type)
        except OutOfBoundBlockPositionException:
            next_position: Position = self._square.position
            next_square_type: SquareType = self._square.square_type
            reward = game_constants.REWARD_WITH_TYPE.get(SquareType.WALL)

        aware_of_goal_position_reward = reward
        if should_qtable_be_updated:
            self._qtable.add_q_rate_to_table(
                state_with_surrounding=self._give_state(),
                action=requested_movement.direction, earned_reward=aware_of_goal_position_reward,
                learning_rate=self._learning_rate, discount_factor=self._discount_factor)

        self._move(square_to_move_on=Square(position=next_position, square_type=next_square_type))
        self._score += aware_of_goal_position_reward

    def _give_state(self) -> StateWithSurrounding:
        return StateWithSurrounding(list_square_types=self.get_surrounding_square_types(),
                                    position_self=self.square.position,
                                    position_goal=self.board.position_goal,
                                    position_start=self._board.position_start)

    def _move(self, square_to_move_on: Square):
        self.draw_square_type_on_position(position_to_draw=self._square.position)
        self._square = square_to_move_on
        self.draw_image_on_current_position()

    def display_info_on_screen(self, txt: List[str], rectangle: (float, float), font_name: str = "arial",
                               font_size: int = 25):
        self._board.viewer.viewer_write_font(
            txt=txt, rectangle=rectangle, a_font=self.board.viewer.create_font(name=font_name, size=font_size))

    @property
    def board(self):
        return self._board

    @property
    def square(self):
        return self._square

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

    @property
    def history(self):
        return self._history

    def update_history(self):
        self._history.append(self._score)
