class WrongDisplaySizeException(Exception):
    def __init__(self, width: int, height: int):
        super().__init__("%d x %d aren't valid display size" % (width, height))
