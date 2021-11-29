from project.display.viewer import Viewer
from project.model.board import Board, Position
from project.model.movement import Movement, Direction
from project.model.obstacle import Pattern, Obstacle

# width == x and height == y

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

PICTURE_PATH: str = "../static/obstacle.png"
PICTURE_SIZE: int = SQUARE_SIZE * DRAW_SCALE

CROSS_PATTERN: Pattern = Pattern(list_of_movements=
                                 [Movement(direction=Direction.RIGHT, length=1, speed=3),
                                  Movement(direction=Direction.LEFT, length=1, speed=3),
                                  Movement(direction=Direction.UP, length=1, speed=3),
                                  Movement(direction=Direction.DOWN, length=1, speed=3),
                                  Movement(direction=Direction.LEFT, length=1, speed=3),
                                  Movement(direction=Direction.RIGHT, length=1, speed=3),
                                  Movement(direction=Direction.DOWN, length=1, speed=3),
                                  Movement(direction=Direction.UP, length=1, speed=3)])

UP_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP, length=1, speed=3)])

OBSTACLE_UP_PATTERN: Obstacle = Obstacle(
                              initial_position=Position(2, 2),
                              pattern=UP_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

MAIN_BOARD: Board = Board(width=6, height=3, position_start=Position(6, 1), position_goal=Position(1, 3),
                          list_of_obstacle=[OBSTACLE_UP_PATTERN])

# TEST_BOARD = Board = Board(width=4, height=4, position_start=Position(1, 1), position_goal=Position(2, 2),
#                           list_of_obstacle=[OBSTACLE_UP_PATTERN])

VIEWER: Viewer = Viewer(MAIN_BOARD.width, MAIN_BOARD.height)
