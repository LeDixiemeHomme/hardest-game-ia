import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton


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

    @staticmethod
    def create_rectangle(left_arg: float, top_arg: float, width_arg: float, height_arg: float) -> pygame.Rect:
        return pygame.Rect(left_arg, top_arg, width_arg, height_arg)

    def draw(self, color: (int, int, int), rect: pygame.Rect):
        pygame.draw.rect(self.__display, color, rect)

    @property
    def display(self):
        return self.__display

    @property
    def screen(self):
        return self.__screen
