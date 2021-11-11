from project.model.Pattern import Pattern
from project.model.Position import Position


class Obstacle:
    def __init__(self, current_position: Position, pattern: Pattern):
        self.__current_position = current_position
        self.__pattern = pattern

    @property
    def current_position(self):
        return self.__current_position

    @property
    def pattern(self):
        return self.__pattern
