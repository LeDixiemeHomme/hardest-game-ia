from typing import List

import pytest

from project.model.agent import Agent
from project.model.board import Board, Position
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.square import Square
from project.model.square_type import SquareType


class TestAgent:
    board_height: int = 5
    board_width: int = 5
    up_movement: Movement = Movement(direction=Direction.UP)
    down_movement: Movement = Movement(direction=Direction.DOWN)
    left_movement: Movement = Movement(direction=Direction.LEFT)
    right_movement: Movement = Movement(direction=Direction.RIGHT)
    movements: List[Movement] = [up_movement, down_movement, right_movement, left_movement]

    movements_to_times_five_wall_positions: (Movement, Position) = [
        (up_movement, Position(co_x=3, co_y=1)),
        (down_movement, Position(co_x=3, co_y=5)),
        (left_movement, Position(co_x=1, co_y=3)),
        (right_movement, Position(co_x=5, co_y=3))
    ]

    position_start: Position = Position(1, 1)
    position_goal: Position = Position(5, 5)
    centered_position: Position = Position(co_x=3, co_y=3)
    position_obstacle: Position = Position(1, 5)

    positions_with_is_closer_from_goal: [Position, bool] = [[centered_position, True],
                                                            [Position(co_x=0, co_y=0), False],
                                                            [Position(co_x=-1, co_y=-1), False],
                                                            [position_goal, True],
                                                            [position_start, False],
                                                            ]

    obstacle: Obstacle = Obstacle(position=position_obstacle)

    board: Board = Board(height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle])

    board.instantiate_singleton_viewer()

    def test_should_is_position_on_goal_square_with_agent_on_position_goal_return_true(self):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.position_goal, square_type=SquareType.GOAL))
        assert agent.is_position_on_goal_square()

    def test_should_is_position_on_goal_square_with_agent_on_position_goal_return_false(self):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.position_start, square_type=SquareType.START))
        assert not agent.is_position_on_goal_square()

    def test_should_is_position_on_obstacle_square_with_agent_on_position_obstacle_return_true(self):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.position_obstacle, square_type=SquareType.OBSTACLE))
        assert agent.is_position_on_obstacle_square()

    def test_should_is_position_on_obstacle_square_with_agent_on_position_obstacle_return_false(self):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.position_start, square_type=SquareType.START))
        assert not agent.is_position_on_obstacle_square()

    @pytest.mark.parametrize("movements", movements)
    def test_should_move_agent_if_possible_updates_agent_position(self, movements):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.centered_position, square_type=SquareType.EMPTY))
        agent.move_agent_if_possible(requested_movement=movements, should_qtable_be_updated=False)
        assert agent._square.position == self.centered_position.apply_movement(movement=movements)

    @pytest.mark.parametrize("movements_to_times_five, wall_positions", movements_to_times_five_wall_positions)
    def test_should_move_agent_if_possible_stop_on_wall(self, movements_to_times_five, wall_positions):
        agent: Agent = Agent(board=self.board)
        agent._move(square_to_move_on=Square(position=self.centered_position, square_type=SquareType.EMPTY))
        for _ in range(5):
            agent.move_agent_if_possible(requested_movement=movements_to_times_five, should_qtable_be_updated=False)
        assert agent._square.position == wall_positions

    @pytest.mark.parametrize("positions, is_closer", positions_with_is_closer_from_goal)
    def test_is_next_position_closer_from_goal_than_self_position(self, positions, is_closer):
        agent: Agent = Agent(board=self.board)
        assert agent.is_next_position_closer_from_goal_than_self_position(next_position=positions) is is_closer
