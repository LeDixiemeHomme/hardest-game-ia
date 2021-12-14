class NoneInstantiateSingletonViewerException(Exception):
    def __init__(self, method_name: str):
        super().__init__(
            f'None value for Viewer. You need to use the method {method_name} '
            f'before using the viewer in the main function. This method instantiate the singleton Viewer.')
