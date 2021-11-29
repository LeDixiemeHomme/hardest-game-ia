from project.constant import constant
from project.model.pattern import Pattern
from project.model.movement import Direction
from project.model.square import Position


class Obstacle:
    def __init__(self, initial_position: Position, pattern: Pattern, picture_path: str, picture_size: int):
        self.__picture_path = picture_path
        self.__picture_size = picture_size
        self.__initial_position = initial_position
        self.__pattern: Pattern = pattern
        self.__pattern_state = 0

    def draw_obstacle(self):
        constant.VIEWER.draw_image(picture_path=self.__picture_path,
                                   picture_size=self.__picture_size,
                                   co_x=self.__initial_position.co_x,
                                   co_y=self.__initial_position.co_y)

    # def move_up(self):
    #     constant.VIEWER.set_tick(3)
    #     movement: Movement = self.__pattern.list_of_movements[
    #         self.__pattern_state % len(self.__pattern.list_of_movements)]
    #     print(self.__temp_square_state.square_type)
    #
    #     if self.__temp_square_state.square_type == SquareType.GOAL:
    #         constant.VIEWER.draw(color=constant.COLOR.get("GREEN"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #     elif self.__temp_square_state.square_type == SquareType.START:
    #         constant.VIEWER.draw(color=constant.COLOR.get("RED"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #     else:
    #         constant.VIEWER.draw(color=constant.COLOR.get("WHITE"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #
    #     # constant.VIEWER.draw_image(image_path_size=self.__picture_path,
    #     #                            co_x=self.__position.position.co_x,
    #     #                            co_y=self.__position.position.co_y - movement.length)
    #
    #     self.__temp_square_state = Square(self.__position.position, SquareType.START)
    #
    #     self.__position.position.co_y -= movement.length
    #
    #     self.__pattern_state += 1



    # def move(self):
    #     constant.VIEWER.set_tick(3)
    #     movement: Movement = self.__pattern.list_of_movements[
    #         self.__pattern_state % len(self.__pattern.list_of_movements)]
    #
    #     if self.__temp_square_state.square_type == SquareType.GOAL:
    #         constant.VIEWER.draw(color=constant.COLOR.get("GREEN"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #     elif self.__temp_square_state.square_type == SquareType.START:
    #         constant.VIEWER.draw(color=constant.COLOR.get("RED"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #     else:
    #         constant.VIEWER.draw(color=constant.COLOR.get("BLUE"),
    #                              rect=constant.VIEWER.create_rectangle(
    #                                  left_arg=self.__temp_square_state.position.co_x,
    #                                  top_arg=self.__temp_square_state.position.co_y))
    #     #
        # if movement.direction == Direction.UP:
        #     constant.VIEWER.draw_image(image_path_size=self.__picture_path,
        #                                co_x=self.__position.position.co_x,
        #                                co_y=self.__position.position.co_y - movement.length)
        #     self.__temp_square_state = Square()
        #     self.__position.position.co_y -= movement.length
        # elif movement.direction == Direction.DOWN:
        #     constant.VIEWER.draw_image(image_path_size=self.__picture_path,
        #                                co_x=self.__position.position.co_x,
        #                                co_y=self.__position.position.co_y + movement.length)
        #     self.__position.position.co_y += movement.length
        # elif movement.direction == Direction.RIGHT:
        #     constant.VIEWER.draw_image(image_path_size=self.__picture_path,
        #                                co_x=self.__position.position.co_x + movement.length,
        #                                co_y=self.__position.position.co_y)
        #     self.__position.position.co_x += movement.length
        # elif movement.direction == Direction.LEFT:
        #     constant.VIEWER.draw_image(image_path_size=self.__picture_path,
        #                                co_x=self.__position.position.co_x - movement.length,
        #                                co_y=self.__position.position.co_y)
        #     self.__position.position.co_x -= movement.length

        # self.__pattern_state += 1

        # faire en sorte que la case du pattern suivant soit placer et que la case de l'obstacle soit mit de la
        # couleur de l'ancien block

        # draw de l'image sur le mouvement
        ##
        # effacement de l'ancienne image

    @property
    def initial_position(self):
        return self.__initial_position

    @initial_position.setter
    def initial_position(self, position: int):
        self.__initial_position = position

    @property
    def pattern(self):
        return self.__pattern

    # @property
    # def previous_square_state(self):
    #     return self.__temp_square_state

    @property
    def picture_path(self):
        return self.__picture_path

    @property
    def picture_size(self):
        return self.__picture_size

    def __str__(self) -> str:
        string: str = "Obstacle : { " + " position = " + str(self.__initial_position) + \
                      "; pattern = " + str(self.__pattern) + "; picture = " + str(self.__picture_path) + " }"
        return string

