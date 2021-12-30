from typing import List

from project.constants import constants
from project.logger.logger import Logger
from project.model.board import Board, Position
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.position import OutOfBoundBlockPositionException
from project.model.square import Square, StateWithSurrounding
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
            self._qtable = self._fill_qtable()
        else:
            self._qtable = qtable
        self._score = 0

    def _fill_qtable(self) -> {}:
        qtable = {}
        for square in self._board.square_list.list_of_square:
            for state in square.all_possible_state():
                qtable[state] = {}
                for direction in Direction.__members__.values():
                    qtable[state][direction] = 0.0
        return qtable

    def _update_qtable(self, state_with_surrounding: StateWithSurrounding, action: Direction, reward: float):
        # Q(s, a) <- Q(s, a) + learning_rate * [reward + discount_factor * max(Q(state)) - Q(s, a)]_square

        if state_with_surrounding not in self._qtable:
            print(state_with_surrounding)
        max_q: int = max(self._qtable[state_with_surrounding].values())
        self._qtable[state_with_surrounding][action] += self._learning_rate * (
                reward + self._discount_factor * max_q - self._qtable[state_with_surrounding][action])

    def best_action(self) -> Direction:
        best_direction = None
        self_state: StateWithSurrounding = StateWithSurrounding(center_square=self._square,
                                                                list_square=self.get_surrounding_squares())

        if self_state not in self._qtable:
            self._qtable[self_state] = {}
            for direction in Direction.__members__.values():
                self._qtable[self_state][direction] = 0.0

        for possible_direction in self._qtable[self_state]:
            if not best_direction or self._qtable[self_state][possible_direction] > \
                    self._qtable[self_state][best_direction]:
                best_direction = possible_direction

        return best_direction

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
            reward = constants.REWARD_WITH_TYPE.get(next_square_type)
        except OutOfBoundBlockPositionException:
            next_position: Position = self._square.position
            next_square_type: SquareType = self._square.square_type
            reward = constants.REWARD_WITH_TYPE.get(SquareType.WALL)

        is_approaching: bool = self.is_next_position_closer_from_goal_than_self_position(
            next_position=next_position)
        reward_approaching: float = constants.REWARD_APPROACHING

        aware_of_goal_position_reward: float = reward + reward_approaching \
            if is_approaching else reward - reward_approaching

        if should_qtable_be_updated:
            self._update_qtable(state_with_surrounding=
                                StateWithSurrounding(center_square=self._square,
                                                     list_square=self.get_surrounding_squares()),
                                action=requested_movement.direction,
                                reward=aware_of_goal_position_reward)

        self._move(square_to_move_on=Square(position=next_position, square_type=next_square_type))
        self._score += aware_of_goal_position_reward

    def _move(self, square_to_move_on: Square):
        self.draw_square_type_on_position(position_to_draw=self._square.position)
        self._square = square_to_move_on
        self.draw_image_on_current_position()

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
