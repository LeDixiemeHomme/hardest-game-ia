from project.model.direction import Direction
from project.model.square import StateWithSurrounding
from project.model.square_list import SquareList


class QTable:
    def __init__(self, square_list: SquareList = None):
        if square_list is None:
            self._table: {StateWithSurrounding: {Direction: float}} = {}

    def add_state_to_table(self, state_to_add: StateWithSurrounding) -> {StateWithSurrounding: {Direction: float}}:
        self._table[state_to_add]: {Direction: float} = {}
        for direction in Direction.__members__.values():
            self._table[state_to_add][direction] = 0.0
        self._table = self._table

    def give_best_direction(self, state: StateWithSurrounding) -> Direction:
        best_direction: Direction = Direction.STAY
        for possible_direction in self._table[state]:
            if not best_direction or self._table[state][possible_direction] > \
                    self._table[state][best_direction]:
                best_direction = possible_direction
        return best_direction

    # Q(s, a) <- Q(s, a) + learning_rate * [reward + discount_factor * max(Q(state)) - Q(s, a)]_square
    def add_q_rate_to_table(self, state_with_surrounding: StateWithSurrounding, action: Direction,
                            earned_reward: float, discount_factor: float, learning_rate: float):

        max_q: int = max(self._table[state_with_surrounding].values())
        previous_q_rate: float = self._table[state_with_surrounding][action]
        calculated_q_rate: float = self._calculate_q_rate(
            earned_reward=earned_reward, previous_q_rate=previous_q_rate,
            max_q=max_q, learning_rate=learning_rate, discount_factor=discount_factor)
        self._table[state_with_surrounding][action] += calculated_q_rate

    @staticmethod
    def _calculate_q_rate(earned_reward: float, previous_q_rate: float, max_q: float,
                          learning_rate: float, discount_factor: float) -> float:
        return learning_rate * (earned_reward + discount_factor * max_q - previous_q_rate)

    @property
    def table(self):
        return self._table
