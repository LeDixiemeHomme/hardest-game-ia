import pygame

from project.constants import constants
from project.logger.logger import Logger
from project.display.viewer import VIEWER


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

UP_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP)])

OBSTACLE_CROSS_PATTERN1: Obstacle = Obstacle(position=Position(5, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN2: Obstacle = Obstacle(position=Position(7, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN3: Obstacle = Obstacle(position=Position(9, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN4: Obstacle = Obstacle(position=Position(11, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN5: Obstacle = Obstacle(position=Position(13, 1), pattern=CROSS_PATTERN)

MAIN_BOARD: Board = Board(width=constants.MAIN_BOARD_WIDTH, height=constants.MAIN_BOARD_HEIGHT, position_start=Position(2, 2),
                          position_goal=Position(16, 2), list_of_obstacle=[
        OBSTACLE_CROSS_PATTERN1,
        OBSTACLE_CROSS_PATTERN2,
        OBSTACLE_CROSS_PATTERN3,
        OBSTACLE_CROSS_PATTERN4,
        OBSTACLE_CROSS_PATTERN5
    ])


if __name__ == '__main__':

    running = True
    my_display = VIEWER.display
    screen = VIEWER.screen
    board = MAIN_BOARD

    stdout_logger.debug("Start drawing board ...")
    board.draw_board()

    while running:
        screen.update()
        for event in pygame.event.get():
            # stdout_logger.debug(str(event))
            if event.type == pygame.QUIT:
                running = False

        board.move_obstacles()
