def parse_number(raw_number:str):
    #precisa polir ainda
    polished_number = raw_number
    return polished_number

class Contact:
    def __init__(self, name:str, number:str):
        self.__name = name
        self.__number = parse_number(number)

    def getTime(self):
        return 10

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number
