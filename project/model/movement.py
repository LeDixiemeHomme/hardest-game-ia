from project.model.Direction import Direction


class Movement:
    def __init__(self, direction: Direction, length: int):
        self.__direction = direction
        self.__length = length

    @property
    def direction(self):
        return self.__direction

    @property
    def length(self):
        return self.__length
