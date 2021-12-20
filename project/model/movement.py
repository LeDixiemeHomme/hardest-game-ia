from project.model.direction import Direction


class Movement:
    def __init__(self, direction: Direction, length: int = 1, speed: int = 5):
        self._direction: Direction = direction
        self._length: int = length
        self._speed: int = speed

    @property
    def direction(self):
        return self._direction

    @property
    def length(self):
        return self._length

    @property
    def speed(self):
        return self._speed

    def __str__(self) -> str:
        string: str = "Movement : { " + str(self._direction) + "; length = " + str(
            self._length) + "; speed = " + str(self._speed) + " }"
        return string
