import logging
import pygame

from project.constant import constant

logging.basicConfig(filename='./records.log', level=logging.DEBUG)

running = True
my_display = constant.VIEWER.display
screen = constant.VIEWER.screen

board = constant.MAIN_BOARD
logging.debug("Start drawing board ...")
board.draw_board()
for obst in board.list_of_obstacle:
    obst.draw_obstacle()

while running:
    screen.update()
    for event in pygame.event.get():
        logging.debug(str(event))
        if event.type == pygame.QUIT:
            running = False
