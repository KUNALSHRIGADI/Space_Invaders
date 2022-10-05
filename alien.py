from turtle import *


class Alien(Turtle):

    def __init__(self):
        super().__init__()
        self.x = -650
        self.y = 350
        self.all_aliens = []

    def create_alien(self):
        new_alien = Turtle()
        new_alien.penup()
        new_alien.goto(self.x, self.y)
        self.all_aliens.append(new_alien)

    def aliens(self, number_of_alien, reach, start_point):
        """ value 0f x take the value of, if the x value of turtle is greater than the certain point it
         will shift to the other line and sec_value of x takes the value of where the turtle should start"""
        for i in range(number_of_alien):
            self.x += 100
            if self.x > reach:
                self.y -= 40
                self.x = start_point

    def spawn_alien(self):
        self.aliens(50, 500, -620)
