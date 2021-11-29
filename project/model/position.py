class Position:
    def __init__(self, co_x: int, co_y: int):
        self.__co_x: int = co_x
        self.__co_y: int = co_y

    @property
    def co_x(self) -> int:
        return self.__co_x

    @property
    def co_y(self) -> int:
        return self.__co_y

    @co_x.setter
    def co_x(self, co_x: int):
        self.__co_x = co_x

    @co_y.setter
    def co_y(self, co_y: int):
        self.__co_y = co_y

    def __str__(self) -> str:
        string: str = "Position : { " + " co_x = " + str(self.__co_x) + "; co_y = " + str(self.__co_y) + " }"
        return string
