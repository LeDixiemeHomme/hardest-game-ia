import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton
from project.model import constant
from project.model.Board import Board
from project.model.SquareType import SquareType


class Viewer(metaclass=MetaSingleton):

    def __init__(self):
        pygame.init()
        self.__screen = self.__init_screen()
        self.__display = self.__init_display()

    @staticmethod
    def __init_screen():
        screen = pygame.display
        screen.set_caption("Hardest game IA")
        screen.set_icon(pygame.image.load('../static/artificial-intelligence.png'))
        return screen

    def __init_display(self):
        my_display = self.__screen.set_mode((800, 800))
        return my_display

    def draw(self, color: (int, int, int), rect: pygame.Rect):
        pygame.draw.rect(self.__display, color, rect)

    @staticmethod
    def draw_board(board: Board):
        size = constant.SQUARE_SIZE * constant.DRAW_SCALE
        color = constant.COLOR
        for square in board.list_of_square:
            rect = pygame.Rect(square.position.co_x * constant.DRAW_SCALE, square.position.co_y * constant.DRAW_SCALE,
                               size, size)
            if square.square_type == SquareType.GOAL:
                Viewer().draw(color=color.get("GREEN"), rect=rect)
            elif square.square_type == SquareType.START:
                Viewer().draw(color=color.get("RED"), rect=rect)
            elif square.square_type == SquareType.EMPTY:
                Viewer().draw(color=color.get("WHITE"), rect=rect)
            else:
                Viewer().draw(color=color.get("BLACK"), rect=rect)

    @property
    def display(self):
        return self.__display

    @property
    def screen(self):
        return self.__screen


