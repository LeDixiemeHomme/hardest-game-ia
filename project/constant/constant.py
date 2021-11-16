from project.model.Board import Board
from project.model.Direction import Direction
from project.model.Movement import Movement
from project.model.Obstacle import Obstacle
from project.model.Pattern import Pattern
from project.model.Position import Position

SQUARE_SIZE: float = 0.10

DRAW_SCALE: int = 100

COLOR: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

CROSS_PATTERN: Pattern = Pattern(
    [Movement(direction=Direction.RIGHT, length=1), Movement(direction=Direction.LEFT, length=1),
     Movement(direction=Direction.UP, length=1), Movement(direction=Direction.DOWN, length=1),
     Movement(direction=Direction.LEFT, length=1), Movement(direction=Direction.RIGHT, length=1),
     Movement(direction=Direction.DOWN, length=1), Movement(direction=Direction.UP, length=1)])

MAIN_BOARD: Board = Board(width=50, height=50, position_start=Position(1.0, 1.0), position_goal=Position(45.0, 45.0),
                          list_of_enemy=[Obstacle(current_position=Position(2.0, 2.0), pattern=CROSS_PATTERN)])
