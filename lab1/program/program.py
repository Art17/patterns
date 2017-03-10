

class Program:
    def __init__(self, security, data):
        self.__security = security
        self.__data = data

    def set_security(self, security):
        if self.__security.check():
            self.__security = security

    def set_data(self, data):
        if self.__security.check():
            self.__data = data

    def get_data(self):
        if self.__security.check():
            return self.__data
        else:
            return "Access denied"
