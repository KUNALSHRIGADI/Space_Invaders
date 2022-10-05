from turtle import *


class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("arcade-game.gif")
        self.color("white")
        self.penup()
        self.goto(position)
