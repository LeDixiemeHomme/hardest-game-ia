class Position:
    def __init__(self, co_x: int, co_y: int):
        self._co_x: int = co_x
        self._co_y: int = co_y

    @property
    def co_x(self) -> int:
        return self._co_x

    @property
    def co_y(self) -> int:
        return self._co_y

    @co_x.setter
    def co_x(self, co_x: int):
        self._co_x = co_x

    @co_y.setter
    def co_y(self, co_y: int):
        self._co_y = co_y

    def __str__(self) -> str:
        string: str = "Position : { " + " co_x = " + str(self._co_x) + "; co_y = " + str(self._co_y) + " }"
        return string

    def __eq__(self, tested):
        if isinstance(tested, Position):
            return self._co_x == tested.co_x and self._co_y == tested.co_y
        return False
