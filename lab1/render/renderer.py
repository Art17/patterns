

class SimpleRenderer:
    def __init__(self):
        pass

    def render(self, text):
        print(text)


class AsteriskRenderer:

    data = [
        "     *\n"
        "    * *\n"
        "   *   *\n"
        "  *******\n"
        " *       *\n"
        "*         *\n",

        "    ***    \n"
        "   *   *   \n"
        "   *   *   \n"
        "    ***    \n"
    ]

    def __init__(self):
        pass

    def render(self, text):
        for c in text:
            if c == 'a':
                print(self.data[0])
            elif c == 'o':
                print(self.data[1])
