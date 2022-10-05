from turtle import *


class Beam(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.shapesize(0.3, 1)
        self.color("yellow")
        self.setheading(90)
        self.pencolor(255, 0, 0)
        self.beam = True
