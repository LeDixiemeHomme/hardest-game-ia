import pygame
from typing import List

from project.constant.constant import PICTURE_PATH, PICTURE_SIZE, COLOR, \
    MAIN_BOARD_WIDTH, MAIN_BOARD_HEIGHT
from project.display.viewer import VIEWER
from project.model.pattern import Pattern, Movement, Direction
from project.model.square import Square, SquareType, Position, OutOfBoundBlockPosition

COLOR_WITH_TYPE: {SquareType: COLOR} = {
    SquareType.EMPTY: COLOR.get("WHITE"),
    SquareType.START: COLOR.get("RED"),
    SquareType.GOAL: COLOR.get("GREEN"),
    SquareType.OBSTACLE: COLOR.get("WHITE"),
    SquareType.WALL: COLOR.get("BLACK")
}


class Obstacle:
    def __init__(self, position: Position, pattern: Pattern, picture_path: str, picture_size: int):
        self._picture_path = picture_path
        self._picture_size = picture_size
        self._position = position
        self._pattern: Pattern = pattern
        self._pattern_state = 0
        self._temp_type = SquareType.EMPTY

    def draw_obstacle(self):
        VIEWER.draw_image(picture_path=self._picture_path,
                          picture_size=self._picture_size,
                          co_x=self._position.co_x,
                          co_y=self._position.co_y)

    def move(self, next_square: Square):
        # draw obstacle picture on the next_position
        VIEWER.draw_image(picture_path=self.picture_path, picture_size=self.picture_size,
                          co_x=next_square.position.co_x, co_y=next_square.position.co_y)
        # draw color type on the current position
        VIEWER.draw(color=COLOR_WITH_TYPE.get(self._temp_type),
                    rect=VIEWER.create_rectangle(left_arg=self._position.co_x, top_arg=self._position.co_y))
        
        # update obstacle position and temp_type
        self.position = next_square.position
        self.temp_type = next_square.square_type
        
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
        string: str = "Obstacle : { " + str(self._position) + \
                      "; " + str(self._pattern) + "; picture = " + str(self._picture_path) + " }"
        return string


class Board:
    def __init__(self, width: int, height: int, position_start: Position, position_goal: Position,
                 list_of_obstacle: List[Obstacle]):
        self._position_start = position_start
        self._position_goal = position_goal
        self._list_of_obstacle: List[Obstacle] = list_of_obstacle
        self._width = width
        self._height = height
        self.init_start()
        self.init_goal()
        self.init_list_of_obstacle()
        self._list_of_square: List[Square] = self.init_list_of_square()

    @property
    def list_of_square(self):
        return self._list_of_square

    def update_list_of_square(self, position: Position, square_type: SquareType):
        self._list_of_square[self.position_to_list_of_square_index(position=position)] = \
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

    def init_list_of_square(self) -> List[Square]:
        list_of_square = []
        # dans range 1, size + 1 pour que position(0, 9) -> position(1, 10)
        for x in range(1, self._width + 1):
            for y in range(1, self._height + 1):
                list_of_square.append(Square(position=Position(x, y), square_type=SquareType.EMPTY))

        list_of_square[self.position_to_list_of_square_index(self._position_start)] = \
            Square(position=self._position_start, square_type=SquareType.START)

        list_of_square[self.position_to_list_of_square_index(self._position_goal)] = \
            Square(position=self._position_goal, square_type=SquareType.GOAL)

        for obstacle in self._list_of_obstacle:
            obstacle_position = obstacle.position
            list_of_square[self.position_to_list_of_square_index(position=obstacle_position)] = \
                Square(position=obstacle_position, square_type=SquareType.OBSTACLE)

        return list_of_square

    def move_obstacles(self):
        VIEWER.set_tick(time_to_stop=6)
        for obstacle in self._list_of_obstacle:
            # todo find a way to give a tick by obstacle and how tick work

            # met le tick egal a la speed du mouvement
            # tick: int = obstacle.pattern.list_of_movements[
            #     obstacle.pattern_state % len(obstacle.pattern.list_of_movements)].speed
            # VIEWER.set_tick(time_to_stop=tick)

            # create position with the current obstacle's position
            current_position: Position = obstacle.position
            current_position_type: SquareType = obstacle.temp_type
            current_movement: Movement = obstacle.pattern.list_of_movements[
                obstacle.pattern_state % len(obstacle.pattern.list_of_movements)]

            next_square: Square = self.next_square(current_position=current_position,
                                                   current_position_type=current_position_type,
                                                   current_movement=current_movement)

            if next_square.square_type == SquareType.WALL:
                obstacle.increment_pattern_state()
                return

            # draw the obstacle on the next block
            obstacle.move(next_square=next_square)

            # update the list of square to set the self type at the next_position
            self.update_list_of_square(position=current_position, square_type=current_position_type)
            self.update_list_of_square(position=next_square.position, square_type=SquareType.OBSTACLE)

    def draw_board(self):
        for square in self._list_of_square:
            rect: pygame.Rect = VIEWER.create_rectangle(
                left_arg=square.position.co_x, top_arg=square.position.co_y)
            VIEWER.draw(color=COLOR_WITH_TYPE.get(square.square_type), rect=rect)

    def init_start(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_start):
            raise OutOfBoundBlockPosition(position=self._position_start, square_type=SquareType.START,
                                          width=self._width, height=self._height)
        return SquareType.START

    def init_goal(self) -> SquareType:
        if not self.is_position_inside_board_boundaries(self._position_goal):
            raise OutOfBoundBlockPosition(position=self._position_goal, square_type=SquareType.GOAL,
                                          width=self._width, height=self._height)
        return SquareType.GOAL

    def init_list_of_obstacle(self) -> List[Obstacle]:
        for obstacle in self._list_of_obstacle:
            if not self.is_position_inside_board_boundaries(obstacle.position):
                raise OutOfBoundBlockPosition(position=obstacle.position, square_type=SquareType.OBSTACLE,
                                              width=self._width, height=self._height)
        return self._list_of_obstacle

    def get_square_type_from_board_by_position(self, position: Position) -> SquareType:
        return self._list_of_square[
            self.position_to_list_of_square_index(position)].square_type

    def position_to_list_of_square_index(self, position: Position) -> int:
        return self._height * position.co_x - (self._height - position.co_y) - 1

    def is_position_inside_board_boundaries(self, position_to_test: Position) -> bool:
        return 0 < position_to_test.co_x <= self._width and 0 < position_to_test.co_y <= self._height

    def __str__(self) -> str:
        string: str = "Board : { height = " + str(self._height) + "; width = " + str(
            self._width) + "; position_start = " + str(self._position_start) + "; width = " + str(
            self._position_goal) + " }"
        return string

    def next_square(self, current_position: Position, current_position_type: SquareType,
                    current_movement: Movement) -> Square:

        if current_movement.direction == Direction.UP:
            next_position: Position = Position(co_x=current_position.co_x,
                                               co_y=current_position.co_y - current_movement.length)
            next_position_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
        elif current_movement.direction == Direction.DOWN:
            next_position: Position = Position(co_x=current_position.co_x,
                                               co_y=current_position.co_y + current_movement.length)
            next_position_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
        elif current_movement.direction == Direction.RIGHT:
            next_position: Position = Position(co_x=current_position.co_x + current_movement.length,
                                               co_y=current_position.co_y)
            next_position_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
        elif current_movement.direction == Direction.LEFT:
            next_position: Position = Position(co_x=current_position.co_x - current_movement.length,
                                               co_y=current_position.co_y)
            next_position_type: SquareType = self.get_square_type_from_board_by_position(position=next_position)
        else:
            next_position = current_position
            next_position_type = current_position_type

        return Square(position=next_position, square_type=next_position_type)


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

OBSTACLE_UP_PATTERN1: Obstacle = Obstacle(
    position=Position(5, 2),
    pattern=CROSS_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

OBSTACLE_UP_PATTERN2: Obstacle = Obstacle(
    position=Position(7, 3),
    pattern=CROSS_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

OBSTACLE_UP_PATTERN3: Obstacle = Obstacle(
    position=Position(9, 2),
    pattern=CROSS_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

OBSTACLE_UP_PATTERN4: Obstacle = Obstacle(
    position=Position(11, 2),
    pattern=CROSS_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

OBSTACLE_UP_PATTERN5: Obstacle = Obstacle(
    position=Position(13, 2),
    pattern=CROSS_PATTERN, picture_path=PICTURE_PATH, picture_size=PICTURE_SIZE)

MAIN_BOARD: Board = Board(width=MAIN_BOARD_WIDTH, height=MAIN_BOARD_HEIGHT, position_start=Position(2, 2),
                          position_goal=Position(14, 2),
                          list_of_obstacle=[
                              OBSTACLE_UP_PATTERN1,
                              OBSTACLE_UP_PATTERN2,
                              OBSTACLE_UP_PATTERN3,
                              OBSTACLE_UP_PATTERN4,
                              OBSTACLE_UP_PATTERN5
                          ])
