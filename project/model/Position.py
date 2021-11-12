class Position:
    def __init__(self, co_x: float, co_y: float):
        self.__co_x: float = co_x
        self.__co_y: float = co_y

    @property
    def co_x(self) -> float:
        return self.__co_x

    @property
    def co_y(self) -> float:
        return self.__co_y

    def __str__(self) -> str:
        string: str = "Position :" + " co_x = " + str(self.__co_x) + " co_y = " + str(self.__co_y)
        return string
