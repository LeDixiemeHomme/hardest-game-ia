import logging
import pygame

from project.display.Viewer import Viewer
from project.model import constant

logging.basicConfig(filename='./records.log', level=logging.DEBUG)

running = True
my_display = Viewer().display
screen = Viewer().screen

board = constant.MAIN_BOARD
logging.debug("Start drawing board ...")
board.draw_board()

while running:
    screen.update()
    for event in pygame.event.get():
        logging.debug(str(event))
        if event.type == pygame.QUIT:
            running = False
