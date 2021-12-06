import pygame
from typing import List
from project.logger.logger import Logger

from project.constant.constant import OBSTACLE_PICTURE_PATH, PICTURE_SIZE, COLOR, \
    MAIN_BOARD_WIDTH, MAIN_BOARD_HEIGHT, SQUARE_SIZE
from project.display.viewer import VIEWER
from project.model.pattern import Pattern, Movement, Direction
from project.model.square import Square, SquareType, Position, OutOfBoundBlockPositionException

COLOR_WITH_TYPE: {SquareType: COLOR} = {
    SquareType.EMPTY: COLOR.get("WHITE"),
    SquareType.START: COLOR.get("RED"),
    SquareType.GOAL: COLOR.get("GREEN"),
    SquareType.OBSTACLE: COLOR.get("WHITE"),
    SquareType.WALL: COLOR.get("BLACK")
}

logger: Logger = Logger(name=__name__, log_file_name="board_log")
stdout_logger = logger.stdout_log


class Obstacle:
    def __init__(self, position: Position, pattern: Pattern,
                 picture_path: str = OBSTACLE_PICTURE_PATH, picture_size: int = PICTURE_SIZE):
        self._picture_path = picture_path
        self._picture_size = picture_size
        self._position = position
        self._pattern: Pattern = pattern
        self._pattern_state = 0
        self._temp_type = SquareType.EMPTY

    def draw_obstacle(self):
        VIEWER.draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                          co_x=self._position.co_x, co_y=self._position.co_y)

    def is_position_inside(self, position_to_test: Position) -> bool:
        return self._position.co_x <= position_to_test.co_x <= self._position.co_x + SQUARE_SIZE \
               and self._position.co_y <= position_to_test.co_y <= self._position.co_y + SQUARE_SIZE

    def move(self, next_square: Square):
        # draw color type on the current position
        VIEWER.draw(color=COLOR_WITH_TYPE.get(self._temp_type),
                    rect=VIEWER.create_rectangle(left_arg=self._position.co_x, top_arg=self._position.co_y))

        # update obstacle position and temp_type
        self.position = next_square.position
        self.temp_type = next_square.square_type

        # draw obstacle picture on the next_position
        self.draw_obstacle()

        # increase pattern state when the move is done
        self.increment_pattern_state()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: int):
        self._position = position

    @property
    def temp_type(self):
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type: SquareType):
        self._temp_type = temp_type

    @property
    def pattern(self):
        return self._pattern

    @property
    def pattern_state(self):
        return self._pattern_state

    def increment_pattern_state(self):
        self._pattern_state += 1

    @property
    def picture_path(self):
        return self._picture_path

    @property
    def picture_size(self):
        return self._picture_size

    def __str__(self) -> str:
        string: str = "Obstacle : { " + str(self._position) + "; " + \
                      str(self._pattern) + "; picture = " + str(self._picture_path) + " }"
        return string


class Board:
    def __init__(self, width: int, height: int, position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self._position_start = position_start
        self._position_goal = position_goal
        self._list_of_obstacle: List[Obstacle] = list_of_obstacle
        self._width = width
        self._height = height
        self._init_start()
        self._init_goal()
        self._init_list_of_obstacle()
        self._list_of_square: List[Square] = self._init_list_of_square()

    def _init_start(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_start):
            raise OutOfBoundBlockPositionException(position=self._position_start, square_type=SquareType.START,
                                                   width=self._width, height=self._height)
        return SquareType.START

    def _init_goal(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_goal):
            raise OutOfBoundBlockPositionException(position=self._position_goal, square_type=SquareType.GOAL,
                                                   width=self._width, height=self._height)
        return SquareType.GOAL

    def _init_list_of_square(self) -> List[Square]:
        list_of_square = []
        # dans range 1, size + 1 pour que position(0, 9) -> position(1, 10)
        for x in range(1, self._width + 1):
            for y in range(1, self._height + 1):
                list_of_square.append(Square(position=Position(x, y), square_type=SquareType.EMPTY))

        list_of_square[self.get_index_of_list_of_square_by_position(self._position_start)] = \
            Square(position=self._position_start, square_type=SquareType.START)

        list_of_square[self.get_index_of_list_of_square_by_position(self._position_goal)] = \
            Square(position=self._position_goal, square_type=SquareType.GOAL)

        for obstacle in self._list_of_obstacle:
            obstacle_position = obstacle.position
            list_of_square[self.get_index_of_list_of_square_by_position(position=obstacle_position)] = \
                Square(position=obstacle_position, square_type=SquareType.OBSTACLE)

        return list_of_square

    def _init_list_of_obstacle(self) -> List[Obstacle]:
        for obstacle in self._list_of_obstacle:
            if not self.is_position_inside_board_boundaries(obstacle.position):
                raise OutOfBoundBlockPositionException(position=obstacle.position, square_type=SquareType.OBSTACLE,
                                                       width=self._width, height=self._height)
        return self._list_of_obstacle

    def move_obstacles(self):
        VIEWER.set_tick(time_to_stop=6)
        for obstacle in self._list_of_obstacle:

            current_position: Position = obstacle.position
            current_position_type: SquareType = obstacle.temp_type
            current_movement: Movement = obstacle.pattern.list_of_movements[
                obstacle.pattern_state % len(obstacle.pattern.list_of_movements)]

            try:
                next_position: Position = self.get_position_after_movement(current_position=current_position,
                                                                           current_movement=current_movement)
                next_square_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
            except OutOfBoundBlockPositionException:
                next_position: Position = current_position
                next_square_type = current_position_type

            # draw the obstacle on the next block
            next_square: Square = Square(position=next_position, square_type=next_square_type)
            obstacle.move(next_square=next_square)

            # update the list of square to set the new type at the current_position and the next_position
            self.update_list_of_square(position=current_position, square_type=current_position_type)
            self.update_list_of_square(position=next_square.position, square_type=SquareType.OBSTACLE)

    def draw_board(self):
        for square in self._list_of_square:
            rect: pygame.Rect = VIEWER.create_rectangle(
                left_arg=square.position.co_x, top_arg=square.position.co_y)
            VIEWER.draw(color=COLOR_WITH_TYPE.get(square.square_type), rect=rect)

    def get_square_type_from_board_by_position(self, position: Position) -> SquareType:
        if not self.is_position_inside_board_boundaries(position_to_test=position):
            raise OutOfBoundBlockPositionException(position=position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)
        return self._list_of_square[
            self.get_index_of_list_of_square_by_position(position)].square_type

    def get_index_of_list_of_square_by_position(self, position: Position) -> int:
        if not self.is_position_inside_board_boundaries(position_to_test=position):
            raise OutOfBoundBlockPositionException(position=position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)
        return self._height * position.co_x - (self._height - position.co_y) - 1

    def get_position_after_movement(self, current_position: Position, current_movement: Movement) -> Position:
        if not self.is_position_inside_board_boundaries(position_to_test=current_position):
            raise OutOfBoundBlockPositionException(position=current_position, square_type=SquareType.OBSTACLE,
                                                   width=self._width, height=self._height)

        position_after_movement: Position = Position(co_x=current_position.co_x, co_y=current_position.co_y)

        direction = current_movement.direction
        length = current_movement.length

        if direction == Direction.UP:
            position_after_movement.co_y -= length
        elif direction == Direction.DOWN:
            position_after_movement.co_y += length
        elif direction == Direction.LEFT:
            position_after_movement.co_x -= length
        elif direction == Direction.RIGHT:
            position_after_movement.co_x += length

        return position_after_movement

    def is_position_inside_board_boundaries(self, position_to_test: Position) -> bool:
        return 0 < position_to_test.co_x <= self._width and 0 < position_to_test.co_y <= self._height

    @property
    def list_of_square(self):
        return self._list_of_square

    def update_list_of_square(self, position: Position, square_type: SquareType):
        self._list_of_square[self.get_index_of_list_of_square_by_position(position=position)] = \
            Square(position=position, square_type=square_type)

    @property
    def list_of_obstacle(self):
        return self._list_of_obstacle

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def position_start(self):
        return self._position_start

    @property
    def position_goal(self):
        return self._position_goal

    def __str__(self) -> str:
        string: str = "Board : { height = " + str(self._height) + "; width = " + str(
            self._width) + "; position_start = " + str(self._position_start) + "; width = " + str(
            self._position_goal) + " }"
        return string


CROSS_PATTERN: Pattern = Pattern(list_of_movements=
                                 [Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.UP),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.UP)])

UP_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP)])

OBSTACLE_CROSS_PATTERN1: Obstacle = Obstacle(position=Position(5, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN2: Obstacle = Obstacle(position=Position(7, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN3: Obstacle = Obstacle(position=Position(9, 1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN4: Obstacle = Obstacle(position=Position(11, 3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN5: Obstacle = Obstacle(position=Position(13, 1), pattern=CROSS_PATTERN)

MAIN_BOARD: Board = Board(width=MAIN_BOARD_WIDTH, height=MAIN_BOARD_HEIGHT, position_start=Position(2, 2),
                          position_goal=Position(16, 2), list_of_obstacle=[
        OBSTACLE_CROSS_PATTERN1,
        OBSTACLE_CROSS_PATTERN2,
        OBSTACLE_CROSS_PATTERN3,
        OBSTACLE_CROSS_PATTERN4,
        OBSTACLE_CROSS_PATTERN5
    ])
