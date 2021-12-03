import logging
import pygame

from project.model.board import MAIN_BOARD
from project.display.viewer import VIEWER

if __name__ == '__main__':
    logging.basicConfig(filename='./records.log', level=logging.DEBUG)

    running = True
    my_display = VIEWER.display
    screen = VIEWER.screen
    board = MAIN_BOARD

    logging.debug("Start drawing board ...")
    board.draw_board()

    while running:
        screen.update()
        for event in pygame.event.get():
            logging.debug(str(event))
            if event.type == pygame.QUIT:
                running = False

        board.move_obstacles()
