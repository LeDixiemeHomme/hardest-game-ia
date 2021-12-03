import os

# width == x and height == y

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

FILE_PATH: str = os.path.dirname(os.path.realpath(__file__)).replace("project/constant", '')

OBSTACLE_PICTURE_PATH: str = FILE_PATH + "static/obstacle.png"

ICON_PICTURE_PATH: str = FILE_PATH + "static/artificial-intelligence.png"

PICTURE_SIZE: int = SQUARE_SIZE * DRAW_SCALE

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}
MAIN_BOARD_WIDTH = 17

MAIN_BOARD_HEIGHT = 3
