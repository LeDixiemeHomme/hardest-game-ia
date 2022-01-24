import os

from project.model.square_type import SquareType

#  + -- -- -- -- -- -- > width
#  |
#  |
#  |
#  |
#  |
#  |
#  \/
#  height

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

BOARD_LEVEL_1_WIDTH = 7

BOARD_LEVEL_1_HEIGHT = 3

BOARD_LEVEL_2_WIDTH = 7

BOARD_LEVEL_2_HEIGHT = 3

BOARD_LEVEL_3_WIDTH = 9

BOARD_LEVEL_3_HEIGHT = 3

SQUARE_BOARD_WIDTH = 10

SQUARE_BOARD_HEIGHT = 10

NUMBER_ON_INFO_TO_DISPLAY: int = 12

BASE_PATH: str = os.path.abspath("..") + '/'

START_PICTURE_PATH: str = BASE_PATH + "static/start.png"

GOAL_PICTURE_PATH: str = BASE_PATH + "static/goal.png"

AGENT_PICTURE_PATH: str = BASE_PATH + "static/knight.png"

OBSTACLE_PICTURE_PATH: str = BASE_PATH + "static/python.xcf"

ICON_PICTURE_PATH: str = BASE_PATH + "static/artificial_intelligence.png"

STORAGE_DIR_NAME: str = "generated_q_tables"

PICTURE_SIZE: int = SQUARE_SIZE * DRAW_SCALE

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

TICK: int = 60
# TICK: int = 30
# TICK: int = 6
