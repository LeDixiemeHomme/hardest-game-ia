from project.constant import constant
from project.model.pattern import Pattern
from project.model.square import Square


class Obstacle:
    def __init__(self, position_square: Square, pattern: Pattern, picture: (str, float)):
        self.__picture = picture
        self.__position_square = position_square
        self.__pattern = pattern

    def draw_obstacle(self):
        constant.VIEWER.draw_image(image_path_size=self.__picture,
                                   co_x=self.__position_square.position.co_x,
                                   co_y=self.__position_square.position.co_y)

    @property
    def current_position(self):
        return self.__position_square

    @property
    def pattern(self):
        return self.__pattern

    @property
    def picture(self):
        return self.__picture
