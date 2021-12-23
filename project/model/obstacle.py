from copy import copy

from project.constants import constants
from project.display.viewer import Viewer

from project.model.position import Pattern, Movement, OutOfBoundBlockPositionException
from project.model.square import Square, Position, SquareType
from project.model.square_list import SquareList


class Obstacle:
    picture_path: str = constants.OBSTACLE_PICTURE_PATH
    picture_size: int = constants.PICTURE_SIZE

    def __init__(self, position: Position,
                 pattern: Pattern = Pattern(list_of_movements=[]),
                 picture_path: str = picture_path,
                 picture_size: int = picture_size,
                 pattern_state: int = 0):
        self._picture_path: str = picture_path
        self._picture_size: int = picture_size
        self._position: Position = position
        self._pattern: Pattern = pattern
        self._pattern_state: int = pattern_state
        self._square_type: SquareType = SquareType.EMPTY

    def draw_image_on_current_position(self, viewer: Viewer):
        viewer.viewer_draw_image(picture_path=self._picture_path, picture_size=self._picture_size,
                                 co_x=self._position.co_x, co_y=self._position.co_y)

    def draw_square_type_on_position(self, position_to_draw: Position, viewer: Viewer):
        viewer.viewer_draw(color=constants.COLOR_WITH_TYPE.get(self._square_type),
                           rect=viewer.create_rectangle(
                               left_arg=position_to_draw.co_x, top_arg=position_to_draw.co_y))

    def is_position_same(self, position_to_test: Position) -> bool:
        return self._position == position_to_test

    def move_obstacle_if_possible(self, square_list: SquareList, viewer: Viewer) -> SquareList:
        copy_square_list: SquareList = copy(square_list)
        movement_to_apply: Movement = self.get_movement_to_do()
        try:
            position_after_movement: Position = \
                self.position.apply_movement(movement=movement_to_apply)
            next_square_type: SquareType = copy_square_list.get_square_type_from_board_by_position(
                position=position_after_movement)
        except OutOfBoundBlockPositionException:
            position_after_movement = self.position
            next_square_type = self.square_type

        copy_square_list.put_square_in_list_of_square(Square(position=self.position,
                                                             square_type=self.square_type))
        copy_square_list.put_square_in_list_of_square(Square(position=position_after_movement,
                                                             square_type=SquareType.OBSTACLE))

        self.move(square_to_move_on=Square(
            position=position_after_movement, square_type=next_square_type), viewer=viewer)

        return copy_square_list

    def move(self, square_to_move_on: Square, viewer: Viewer):
        self.draw_square_type_on_position(position_to_draw=self._position, viewer=viewer)
        self._position = square_to_move_on.position
        self.draw_image_on_current_position(viewer=viewer)
        self._square_type = square_to_move_on.square_type

        self.increment_pattern_state()

    def get_movement_to_do(self) -> Movement:
        return self._pattern.list_of_movements[
            self._pattern_state % len(self._pattern.list_of_movements)]

    @property
    def position(self):
        return self._position

    @property
    def square_type(self):
        return self._square_type

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
