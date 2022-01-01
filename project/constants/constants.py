import os

from project.model.square_type import SquareType

# width == x and height == y
#
#  + -- -- -- -- -- -- > x
#  |
#  |
#  |
#  |
#  |
#  |
#  \/
#  y

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

MAIN_BOARD_WIDTH = 17

MAIN_BOARD_HEIGHT = 3

TEST_BOARD_WIDTH = 3

TEST_BOARD_HEIGHT = 3

SQUARE_BOARD_WIDTH = 10

SQUARE_BOARD_HEIGHT = 10

BASE_PATH: str = os.path.abspath("..") + '/'

START_PICTURE_PATH: str = BASE_PATH + "static/start.png"

GOAL_PICTURE_PATH: str = BASE_PATH + "static/goal.png"

AGENT_PICTURE_PATH: str = BASE_PATH + "static/knight.png"

OBSTACLE_PICTURE_PATH: str = BASE_PATH + "static/spike.png"

ICON_PICTURE_PATH: str = BASE_PATH + "static/artificial_intelligence.png"

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

REWARD_APPROACHING: float = 5

REWARD_WITH_TYPE: {SquareType: int} = {
    SquareType.EMPTY: -10,
    SquareType.START: -20,
    SquareType.WALL: -50,
    SquareType.OBSTACLE: - 100,
    SquareType.GOAL: 1000
}

