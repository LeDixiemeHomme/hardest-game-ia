import pygame

from project.custom_exception.wrong_display_size_exception import WrongDisplaySizeException
from project.metaSingleton.MetaSingleton import MetaSingleton
from project.constants import constants


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
        path_image: str = constants.ICON_PICTURE_PATH
        screen.set_icon(pygame.image.load(path_image))
        return screen

    def _init_display(self, width: int, height: int):
        if width > 20 or height > 20:
            raise WrongDisplaySizeException(width, height)
        height_border_size, width_border_size = 1, 1
        my_display = self._screen.set_mode(((width_border_size + width + width_border_size) * constants.DRAW_SCALE,
                                            (height_border_size + height + height_border_size) * constants.DRAW_SCALE))
        return my_display

    @staticmethod
    def create_rectangle(left_arg: int, top_arg: int) -> pygame.Rect:
        size = constants.SQUARE_SIZE * constants.DRAW_SCALE
        return pygame.Rect(left_arg * constants.DRAW_SCALE, top_arg * constants.DRAW_SCALE, size, size)

    @staticmethod
    def direction_from_key_down_value(key_down: pygame.KEYDOWN) -> Direction:
        direction: Direction = Direction.STAY
        if key_down == pygame.K_LEFT:
            direction = Direction.LEFT
        elif key_down == pygame.K_RIGHT:
            direction = Direction.RIGHT
        elif key_down == pygame.K_UP:
            direction = Direction.UP
        elif key_down == pygame.K_DOWN:
            direction = Direction.DOWN
        return direction

    def draw_image(self, picture_path: str, picture_size: int, co_x: int, co_y: int) -> pygame.Rect:
        image = pygame.image.load(picture_path)
        scaled_image = pygame.transform.scale(image, (picture_size, picture_size))

        return self._display.blit(scaled_image, pygame.Rect(co_x * constants.DRAW_SCALE * constants.SQUARE_SIZE,
                                                            co_y * constants.DRAW_SCALE * constants.SQUARE_SIZE,
                                                            picture_size * constants.DRAW_SCALE,
                                                            picture_size * constants.DRAW_SCALE))

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


VIEWER: Viewer = Viewer(constants.MAIN_BOARD_WIDTH, constants.MAIN_BOARD_HEIGHT)
