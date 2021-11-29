import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton
from project.constant import constant
from project.exception.wrong_display_size_exception import WrongDisplaySizeException


class Viewer(metaclass=MetaSingleton):

    def __init__(self, width: int, height: int):
        pygame.init()
        self.__screen = self.__init_screen()
        self.__display = self.__init_display(width=width, height=height)
        self.__clock = pygame.time.Clock()

    @staticmethod
    def __init_screen():
        screen = pygame.display
        screen.set_caption("Hardest game IA")
        screen.set_icon(pygame.image.load('../static/artificial-intelligence.png'))
        return screen

    def __init_display(self, width: int, height: int):
        if width > 20 or height > 20:
            raise WrongDisplaySizeException(width, height)
        height_border_size, width_border_size = 1, 1
        my_display = self.__screen.set_mode(((width_border_size + width + width_border_size) * constant.DRAW_SCALE,
                                             (height_border_size + height + height_border_size) * constant.DRAW_SCALE))
        return my_display

    @staticmethod
    def create_rectangle(left_arg: int, top_arg: int) -> pygame.Rect:
        size = constant.SQUARE_SIZE * constant.DRAW_SCALE
        return pygame.Rect(left_arg * constant.DRAW_SCALE, top_arg * constant.DRAW_SCALE, size, size)

    def draw_image(self, picture_path: str, picture_size: int, co_x: int, co_y: int) -> pygame.Rect:
        image = pygame.image.load(picture_path)
        scaled_image = pygame.transform.scale(image, (picture_size, picture_size))

        return self.__display.blit(scaled_image, pygame.Rect(co_x * constant.DRAW_SCALE * constant.SQUARE_SIZE,
                                                             co_y * constant.DRAW_SCALE * constant.SQUARE_SIZE,
                                                             picture_size * constant.DRAW_SCALE,
                                                             picture_size * constant.DRAW_SCALE))

    def draw(self, color: (int, int, int), rect: pygame.Rect):
        pygame.draw.rect(self.__display, color, rect)

    def set_tick(self, time_to_stop: int):
        self.__clock.tick(time_to_stop)

    @property
    def display(self):
        return self.__display

    @property
    def screen(self):
        return self.__screen
