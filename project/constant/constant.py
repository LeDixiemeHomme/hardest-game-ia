from project.display.viewer import Viewer
from project.model.board import Board
from project.model.direction import Direction
from project.model.movement import Movement
from project.model.obstacle import Obstacle
from project.model.pattern import Pattern
from project.model.position import Position
from project.model.square import Square
from project.model.square_type import SquareType

# width == x and height == y

SQUARE_SIZE: int = 1

DRAW_SCALE: int = 40

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

OBSTACLE_PICTURE: (str, int) = ("../static/obstacle.png", SQUARE_SIZE * DRAW_SCALE)

CROSS_PATTERN: Pattern = Pattern(
    [Movement(direction=Direction.RIGHT, length=1), Movement(direction=Direction.LEFT, length=1),
     Movement(direction=Direction.UP, length=1), Movement(direction=Direction.DOWN, length=1),
     Movement(direction=Direction.LEFT, length=1), Movement(direction=Direction.RIGHT, length=1),
     Movement(direction=Direction.DOWN, length=1), Movement(direction=Direction.UP, length=1)])

MAIN_BOARD: Board = Board(width=20, height=20, position_start=Position(1, 1), position_goal=Position(20, 20),
                          list_of_obstacle=[Obstacle(
                              position_square=Square(position=Position(2, 2), square_type=SquareType.OBSTACLE),
                              pattern=CROSS_PATTERN, picture=OBSTACLE_PICTURE)])

VIEWER: Viewer = Viewer(MAIN_BOARD.width, MAIN_BOARD.height)
