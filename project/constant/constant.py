from project.display.viewer import Viewer
from project.model.board import Board
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.pattern import Pattern
from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType

VIEWER: Viewer = Viewer()

SQUARE_SIZE: float = 0.50

DRAW_SCALE: int = 100

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

OBSTACLE_PICTURE: (str, float) = ("../static/slime.png", SQUARE_SIZE * DRAW_SCALE)

CROSS_PATTERN: Pattern = Pattern(
    [Movement(direction=Direction.RIGHT, length=1), Movement(direction=Direction.LEFT, length=1),
     Movement(direction=Direction.UP, length=1), Movement(direction=Direction.DOWN, length=1),
     Movement(direction=Direction.LEFT, length=1), Movement(direction=Direction.RIGHT, length=1),
     Movement(direction=Direction.DOWN, length=1), Movement(direction=Direction.UP, length=1)])

MAIN_BOARD: Board = Board(width=15, height=15, position_start=Position(1.0, 1.0), position_goal=Position(3.0, 1.0),
                          list_of_obstacle=[Obstacle(
                              position_square=Square(position=Position(2.0, 1.0), square_type=SquareType.OBSTACLE),
                              pattern=CROSS_PATTERN, picture=OBSTACLE_PICTURE)])
