import pygame

from project.constants import constants
from project.logger.logger import Logger
from project.model.agent import Agent

from project.model.board import Board
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.pattern import Pattern
from project.model.position import Position

logger: Logger = Logger(name=__name__, log_file_name="main_log")
stdout_logger = logger.stdout_log

CROSS_PATTERN: Pattern = Pattern(list_of_movements=
                                 [Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.UP),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.UP)])

UP_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP),
                                                 Movement(direction=Direction.UP),
                                                 Movement(direction=Direction.UP),
                                                 Movement(direction=Direction.DOWN),
                                                 Movement(direction=Direction.DOWN),
                                                 Movement(direction=Direction.DOWN)])

OBSTACLE_UP_PATTERN: Obstacle = Obstacle(position=Position(co_x=3, co_y=3), pattern=UP_PATTERN)

OBSTACLE_CROSS_PATTERN1: Obstacle = Obstacle(position=Position(5, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN2: Obstacle = Obstacle(position=Position(7, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN3: Obstacle = Obstacle(position=Position(9, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN4: Obstacle = Obstacle(position=Position(11, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN5: Obstacle = Obstacle(position=Position(15, 2), pattern=CROSS_PATTERN)

MAIN_START_POSITION: Position = Position(2, 2)

MAIN_GOAL_POSITION: Position = Position(16, 2)

TEST_START_POSITION: Position = Position(1, 2)

TEST_GOAL_POSITION: Position = Position(3, 2)

if __name__ == '__main__':
    running = True
    lose = win = False

    MAIN_BOARD: Board = Board(width=constants.MAIN_BOARD_WIDTH, height=constants.MAIN_BOARD_HEIGHT,
                              position_start=MAIN_START_POSITION, position_goal=MAIN_GOAL_POSITION,
                              list_of_obstacle=[
                                  OBSTACLE_CROSS_PATTERN1,
                                  OBSTACLE_CROSS_PATTERN2, OBSTACLE_CROSS_PATTERN3,
                                  OBSTACLE_CROSS_PATTERN4, OBSTACLE_CROSS_PATTERN5
                              ])

    TEST_BOARD: Board = Board(width=constants.TEST_BOARD_WIDTH, height=constants.TEST_BOARD_HEIGHT,
                              position_start=TEST_START_POSITION, position_goal=TEST_GOAL_POSITION,
                              list_of_obstacle=[])

    board: Board = MAIN_BOARD
    # board: Board = TEST_BOARD

    board.instantiate_singleton_viewer()

    agent: Agent = Agent(board=board, position=board.position_start)

    stdout_logger.debug("Start drawing board ...")
    agent.board.draw_board()

    while running and not win and not lose:
        agent.board.viewer.screen.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                movement_next: Movement = Movement(
                    direction=board.viewer.direction_from_key_down_value(key_down=event.key))
                agent.move_agent_if_possible(requested_movement=movement_next)

        agent.board.move_obstacles()
        agent.draw_image_on_current_position()

        if agent.is_position_on_goal_square():
            win = True
        if agent.is_position_on_obstacle_square():
            lose = True

    if win:
        stdout_logger.debug("You win")
    if lose:
        stdout_logger.debug("You lose")
