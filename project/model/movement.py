from project.model.direction import Direction


class Movement:
    def __init__(self, direction: Direction, length: int, speed: int):
        self.__direction = direction
        self.__length = length
        self.__speed = speed

    @property
    def direction(self):
        return self.__direction

    @property
    def length(self):
        return self.__length

    @property
    def speed(self):
        return self.__speed

    @length.setter
    def length(self, length: int):
        self.__length = length

    def __str__(self) -> str:
        string: str = "Movement : { " + " direction = " + str(self.__direction) + "; length = " + str(
            self.__length) + "; speed = " + str(self.__speed) + " }"
        return string
