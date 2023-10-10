#!/usr/bin/python3
""" my class module """


class MyClass:
    """ Myclass """

    score = 0
    def __init__(self, name, number =  4):
        self.__name = name
        self.__number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.__number, self.score)
