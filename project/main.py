import logging
import pygame

from project.display.Viewer import Viewer
from project.model import constant
from project.model.Board import Board
from project.model.Direction import Direction
from project.model.Movement import Movement
from project.model.Pattern import Pattern
from project.model.Obstacle import Obstacle
from project.model.Position import Position
from project.model.Square import Square
from project.model.SquareType import SquareType

logging.basicConfig(filename='records.log', level=logging.DEBUG)

running = True
my_display = Viewer().display
screen = Viewer().screen


color: {str: (int, int, int)} = {"RED": (255, 0, 0),
                                 "GREEN": (0, 255, 0),
                                 "BLUE": (0, 0, 255),
                                 "WHITE": (255, 255, 255),
                                 "BLACK": (0, 0, 0)}

cross_pattern = Pattern([Movement(direction=Direction.RIGHT, length=1), Movement(direction=Direction.LEFT, length=1),
                         Movement(direction=Direction.UP, length=1), Movement(direction=Direction.DOWN, length=1),
                         Movement(direction=Direction.LEFT, length=1), Movement(direction=Direction.RIGHT, length=1),
                         Movement(direction=Direction.DOWN, length=1), Movement(direction=Direction.UP, length=1)])

board = Board(width=5, height=5, position_start=Position(0.0, 1.0), position_goal=Position(3.0, 4.0),
              list_of_enemy=[Obstacle(current_position=Position(2.0, 2.0), pattern=cross_pattern)])

for k in board.list_of_square:
    print(k.square_type, k.position.co_x, k.position.co_y)

square = Square(Position(5.0, 5.0), SquareType.EMPTY)

print("test                        ", square.is_position_inside(Position(1.0, 3.0)))
print("test                        ", square.is_position_inside(Position(1.0, 5.5)))
print("test                        ", square.is_position_inside(Position(5.5, 6.0)))
print("test                        ", square.is_position_inside(Position(1.0, 6.0)))
print("test                        ", square.is_position_inside(Position(6.0, 6.0)))
print("test                        ", square.is_position_inside(Position(5.0, 5.0)))
print("test                        ", square.is_position_inside(Position(5.4, 5.1)))

while running:
    screen.update()
    for event in pygame.event.get():
        logging.debug(event)
        if event.type == pygame.QUIT:
            running = False

    for square in board.list_of_square:
        size = constant.SQUARE_SIZE * 100
        rect = pygame.Rect(square.position.co_x * size,
                           square.position.co_y * size,
                           size, size)
        if square.square_type == SquareType.GOAL:
            Viewer().draw(color=color.get("GREEN"), rect=rect)
        elif square.square_type == SquareType.START:
            Viewer().draw(color=color.get("RED"), rect=rect)
        elif square.square_type == SquareType.EMPTY:
            Viewer().draw(color=color.get("WHITE"), rect=rect)
        else:
            Viewer().draw(color=color.get("BLACK"), rect=rect)
