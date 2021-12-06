from project.model.direction import Direction


class Movement:
    def __init__(self, direction: Direction, length: int = 1, speed: int = 5):
        self._direction = direction
        self._length = length
        self._speed = speed

    @property
    def direction(self):
        return self._direction

    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed

    @length.setter
    def length(self, length: int):
        self._length = length

    def __str__(self) -> str:
        string: str = "Movement : { " + str(self._direction) + "; length = " + str(
            self._length) + "; speed = " + str(self._speed) + " }"
        return string
