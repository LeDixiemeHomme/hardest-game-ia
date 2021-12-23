from typing import List
from collections import namedtuple

import pytest

from project.model.agent import Agent
from project.model.board import Board, Position
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle


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

    obstacle: Obstacle = Obstacle(position=position_obstacle)

    board: Board = Board(height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle])

    board.instantiate_singleton_viewer()

    def test_should_is_position_on_goal_square_with_agent_on_position_goal_return_true(self):
        agent: Agent = Agent(board=self.board, position=self.position_goal)
        assert agent.is_position_on_goal_square()

    def test_should_is_position_on_goal_square_with_agent_on_position_goal_return_false(self):
        agent: Agent = Agent(board=self.board, position=self.position_start)
        assert not agent.is_position_on_goal_square()

    def test_should_is_position_on_obstacle_square_with_agent_on_position_obstacle_return_true(self):
        agent: Agent = Agent(board=self.board, position=self.position_obstacle)
        assert agent.is_position_on_obstacle_square()

    def test_should_is_position_on_obstacle_square_with_agent_on_position_obstacle_return_false(self):
        agent: Agent = Agent(board=self.board, position=self.position_start)
        assert not agent.is_position_on_obstacle_square()

    @pytest.mark.parametrize("movements", movements)
    def test_should_move_agent_if_possible_updates_agent_position(self, movements):
        agent: Agent = Agent(board=self.board, position=self.centered_position)
        agent.move_agent_if_possible(requested_movement=movements)
        assert agent.position == self.centered_position.apply_movement(movement=movements)

    @pytest.mark.parametrize("movements_to_times_five, wall_positions", movements_to_times_five_wall_positions)
    def test_should_move_agent_if_possible_stop_on_wall(self, movements_to_times_five, wall_positions):
        agent: Agent = Agent(board=self.board, position=self.centered_position)
        for _ in range(5):
            agent.move_agent_if_possible(requested_movement=movements_to_times_five)
        print(agent.position, wall_positions)
        assert agent.position == wall_positions
