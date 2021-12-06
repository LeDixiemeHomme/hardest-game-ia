import pygame

from project.constants import constants_model
from project.logger.logger import Logger
from project.display.viewer import VIEWER

logger: Logger = Logger(name=__name__, log_file_name="main_log")
stdout_logger = logger.stdout_log

if __name__ == '__main__':

    running = True
    my_display = VIEWER.display
    screen = VIEWER.screen
    board = constants_model.MAIN_BOARD

    stdout_logger.debug("Start drawing board ...")
    board.draw_board()

    while running:
        screen.update()
        for event in pygame.event.get():
            # stdout_logger.debug(str(event))
            if event.type == pygame.QUIT:
                running = False

        board.move_obstacles()
