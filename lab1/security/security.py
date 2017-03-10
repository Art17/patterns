

class PasswordSecurity:
    def __init__(self, password):
        self.__password = password

    def check(self):
        p = input('Enter password: ')
        return self.__password == p


class NoSecurity:
    def __init__(self):
        pass

    def check(self):
        return True
