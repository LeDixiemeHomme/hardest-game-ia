import os
import errno
import pickle
from random import *

from project.logger.logger import Logger
from project.metaSingleton.MetaSingleton import MetaSingleton

from project.constants import game_constants
from project.model.movement import Direction
from project.model.square import StateWithSurrounding
from project.model.square_list import SquareList

logger: Logger = Logger(name=__name__, log_file_name="q_table_logger")
stdout_logger = logger.stdout_log


class QTable:
    def __init__(self, square_list: SquareList = None):
        self._exploration: float = game_constants.EXPLORATION_RATE
        if square_list is None:
            self._table: {StateWithSurrounding: {Direction: float}} = {}
        else:
            stdout_logger.debug("implem smth with square_list")

    def add_state_to_table(self, state_to_add: StateWithSurrounding) -> {StateWithSurrounding: {Direction: float}}:
        self._table[state_to_add]: {Direction: float} = {}
        for direction in Direction.__members__.values():
            self._table[state_to_add][direction] = game_constants.DEFAULT_REWARD_VALUE * random()
        self._table = self._table

    def give_best_direction(self, state_to_search: StateWithSurrounding) -> Direction:
        best_direction = None
        # test that introduce random action choice -> exploration
        if random() < self._exploration:
            # reduce chance of random
            self._exploration *= game_constants.DIMINUTION_RATE
            return choice(list(Direction.__members__.values()))
        else:
            # for every action for this state, return action with the highest reward
            for possible_direction in self._table[state_to_search]:
                if not best_direction or self._table[state_to_search][possible_direction] > \
                        self._table[state_to_search][best_direction]:
                    best_direction = possible_direction
            return best_direction

    # Q(s, a) <- Q(s, a) + learning_rate * [reward + discount_factor * max(Q(state)) - Q(s, a)]_square
    def add_q_rate_to_table(self, state_with_surrounding: StateWithSurrounding, action: Direction,
                            earned_reward: float, discount_factor: float, learning_rate: float):
        max_q: int = max(self._table[state_with_surrounding].values())
        previous_q_rate: float = self._table[state_with_surrounding][action]
        calculated_q_rate: float = learning_rate * (earned_reward + discount_factor * max_q - previous_q_rate)
        self._table[state_with_surrounding][action] += calculated_q_rate

    @property
    def table(self):
        return self._table

    @property
    def exploration(self):
        return self._exploration

    def __str__(self) -> str:
        string: str = "QTable : { " + " table = " + str(self._table) + " }"
        return string


class Pickle(metaclass=MetaSingleton):
    def __init__(self):
        self._pickle = pickle

    def save(self, filename: str, qtable: QTable):
        stdout_logger.info("Saving qtable data at file " + filename)
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, 'wb') as file:
            self._pickle.dump(qtable, file)

    def load(self, filename) -> QTable:
        stdout_logger.info("Loading qtable data from file " + filename)
        try:
            with open(filename, 'rb') as file:
                qtable: QTable = self._pickle.load(file)
        except FileNotFoundError as e:
            stdout_logger.debug("No .dat found or provided for filename " + filename +
                                ", using empty qtable.")
            qtable = QTable()
        return qtable
