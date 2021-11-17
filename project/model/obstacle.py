from project.display.Viewerben import Viewerben
from project.model import Pattern
from project.model import Square


class Obstacle:
    def __init__(self, position_square: Square, pattern: Pattern, picture: (str, float)):
        self.__picture = picture
        self.__position_square = position_square
        self.__pattern = pattern
        self.__viewer = Viewerben()

    def draw_obstacle(self):
        self.__viewer.draw_image(image_path_size=self.__picture, position_image=self.__position_square.position)

    @property
    def current_position(self):
        return self.__position_square

    @property
    def pattern(self):
        return self.__pattern

    @property
    def picture(self):
        return self.__picture
