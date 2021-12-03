import pygame

from project.metaSingleton.MetaSingleton import MetaSingleton
from project.constant.constant import DRAW_SCALE, SQUARE_SIZE, MAIN_BOARD_WIDTH, MAIN_BOARD_HEIGHT, ICON_PICTURE_PATH


class WrongDisplaySizeException(Exception):
    def __init__(self, width: int, height: int):
        super().__init__("%d x %d aren't valid display size" % (width, height))


class Viewer(metaclass=MetaSingleton):
    def __init__(self, width: int, height: int):
        pygame.init()
        self._screen = self._init_screen()
        self._display = self._init_display(width=width, height=height)
        self._clock = pygame.time.Clock()

    @staticmethod
    def _init_screen():
        screen = pygame.display
        screen.set_caption("Hardest game IA")
        path_image: str = ICON_PICTURE_PATH
        screen.set_icon(pygame.image.load(path_image))
        return screen

    def _init_display(self, width: int, height: int):
        if width > 20 or height > 20:
            raise WrongDisplaySizeException(width, height)
        height_border_size, width_border_size = 1, 1
        my_display = self._screen.set_mode(((width_border_size + width + width_border_size) * DRAW_SCALE,
                                            (height_border_size + height + height_border_size) * DRAW_SCALE))
        return my_display

    @staticmethod
    def create_rectangle(left_arg: int, top_arg: int) -> pygame.Rect:
        size = SQUARE_SIZE * DRAW_SCALE
        return pygame.Rect(left_arg * DRAW_SCALE, top_arg * DRAW_SCALE, size, size)

    def draw_image(self, picture_path: str, picture_size: int, co_x: int, co_y: int) -> pygame.Rect:
        image = pygame.image.load(picture_path)
        scaled_image = pygame.transform.scale(image, (picture_size, picture_size))

        return self._display.blit(scaled_image, pygame.Rect(co_x * DRAW_SCALE * SQUARE_SIZE,
                                                            co_y * DRAW_SCALE * SQUARE_SIZE,
                                                            picture_size * DRAW_SCALE,
                                                            picture_size * DRAW_SCALE))

    def draw(self, color: (int, int, int), rect: pygame.Rect):
        pygame.draw.rect(self._display, color, rect)

    def set_tick(self, time_to_stop: int):
        self._clock.tick(time_to_stop)

    @property
    def display(self):
        return self._display

    @property
    def screen(self):
        return self._screen


VIEWER: Viewer = Viewer(MAIN_BOARD_WIDTH, MAIN_BOARD_HEIGHT)
