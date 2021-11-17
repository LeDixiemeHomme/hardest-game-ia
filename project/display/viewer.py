import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton
from project.constant import constant
from project.exception.wrong_display_size_exception import WrongDisplaySizeException


class Viewer(metaclass=MetaSingleton):

    def __init__(self, width: int, height: int):
        pygame.init()
        self.__screen = self.__init_screen()
        self.__display = self.__init_display(width=width, height=height)

    @staticmethod
    def __init_screen():
        screen = pygame.display
        screen.set_caption("Hardest game IA")
        screen.set_icon(pygame.image.load('../static/artificial-intelligence.png'))
        return screen

    def __init_display(self, width: int, height: int):
        if width > 20 or height > 20:
            raise WrongDisplaySizeException(width, height)
        my_display = self.__screen.set_mode(((height + 2) * constant.DRAW_SCALE,
                                             (width + 2) * constant.DRAW_SCALE))
        return my_display

    @staticmethod
    def create_rectangle(left_arg: int, top_arg: int, width_arg: int, height_arg: int) -> pygame.Rect:
        return pygame.Rect(left_arg, top_arg, width_arg, height_arg)

    def draw_image(self, image_path_size: (str, int), co_x: int, co_y: int) -> pygame.Rect:
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
