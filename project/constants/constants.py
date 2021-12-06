import os

from project.model.square_type import SquareType

# width == x and height == y

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

COLOR_WITH_TYPE: {SquareType: COLOR} = {
    SquareType.EMPTY: COLOR.get("WHITE"),
    SquareType.START: COLOR.get("RED"),
    SquareType.GOAL: COLOR.get("GREEN"),
    SquareType.OBSTACLE: COLOR.get("WHITE"),
    SquareType.WALL: COLOR.get("BLACK")
}

MAIN_BOARD_WIDTH = 17

MAIN_BOARD_HEIGHT = 3

BASE_PATH: str = os.path.abspath("..") + '/'

OBSTACLE_PICTURE_PATH: str = BASE_PATH + "static/obstacle.png"

ICON_PICTURE_PATH: str = BASE_PATH + "static/artificial-intelligence.png"

PICTURE_SIZE: int = SQUARE_SIZE * DRAW_SCALE
