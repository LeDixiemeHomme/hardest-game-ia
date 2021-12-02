class Reward:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        string: str = "Reward :" + " value = " + str(self._value) + " }"
        return string
