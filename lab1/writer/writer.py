

class Writer:

    def __init__(self, renderer):
        self.__renderer = renderer

    def write(self, text):
        self.__renderer.render(text)