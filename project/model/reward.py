class Reward:

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self) -> str:
        string: str = "Reward :" + " value = " + str(self.__value) + " }"
        return string
