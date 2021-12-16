import pytest

from project.model.agent import Agent
from project.model.board import Board, Position
from project.model.obstacle import Obstacle


class TestAgent:
    board_height: int = 5
    board_width: int = 5

    position_start: Position = Position(1, 1)
    position_goal: Position = Position(5, 5)
    position_obstacle: Position = Position(2, 2)

    obstacle: Obstacle = Obstacle(position=position_obstacle)

    board: Board = Board(height=board_height, width=board_width,
                         position_start=position_start, position_goal=position_goal,
                         list_of_obstacle=[obstacle])

    board.instantiate_singleton_viewer()

    agent: Agent = Agent(board=board)

    def test_should_is_position_on_goal_square_with_agent_on_position_goal_return_true(self):
        self.agent.position = self.position_goal
        assert self.agent.is_position_on_goal_square()

    def test_should_is_position_on_obstacle_square_with_agent_on_position_obstacle(self):
        self.agent.position = self.position_obstacle
        assert self.agent.is_position_on_obstacle_square()
