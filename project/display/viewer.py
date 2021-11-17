import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton
from project.constant import constant


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

    def draw_image(self, image_path_size: (str, float), co_x: float, co_y: float) -> pygame.Rect:
        image = pygame.image.load(image_path_size[0])
        scaled_image = pygame.transform.scale(image, (image_path_size[1], image_path_size[1]))

        return self.__display.blit(scaled_image, pygame.Rect(co_x * constant.DRAW_SCALE * constant.SQUARE_SIZE,
                                                             co_y * constant.DRAW_SCALE * constant.SQUARE_SIZE,
                                                             image_path_size[1] * constant.DRAW_SCALE,
                                                             image_path_size[1] * constant.DRAW_SCALE))

    def draw(self, color: (int, int, int), rect: pygame.Rect):
        pygame.draw.rect(self.__display, color, rect)

    @property
    def display(self):
        return self.__display

    @property
    def screen(self):
        return self.__screen
