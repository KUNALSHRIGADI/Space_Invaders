from turtle import *
from spaceship import Spaceship
from beam import Beam
import time
from message import Message

screen = Screen()
screen.listen()
screen.tracer(0)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.addshape("arcade-game.gif")
screen.addshape("alien0.gif")
screen.addshape("alien1.gif")
screen.addshape("explosion.gif")
screen.bgpic("bg-stars.gif")
screen.setup(width=1300, height=700)
screen.colormode(255)

spaceship = Spaceship((0, -300))
beam = Beam()
message = Message()

game_is_on = True
all_aliens = []


def move_spaceship(x_val, y_val):
    if -650 < x_val < 650:
        spaceship.goto(x_val, -300)


spaceship.ondrag(move_spaceship)


x = -570
y = 300
sec = 0.1
number_of_alien = 30
reach = 550
start_point = -570
time_on = time.time() + sec
for i in range(number_of_alien):
    new_alien = Turtle()
    new_alien.shape("alien0.gif")
    new_alien.penup()
    new_alien.goto(x, y)
    all_aliens.append(new_alien)
    x += 100
    if x > reach:
        y -= 40
        x = start_point

while game_is_on:
    time.sleep(0.03)
    beam.forward(15)
    if beam.ycor() >= 350:
        space_posx = spaceship.xcor()
        space_posy = spaceship.ycor()
        incre_posy = space_posy + 20
        beam.goto(space_posx, incre_posy)
        beam.showturtle()
        beam.beam = True
    screen.update()

    if time_on <= time.time():
        for alien in all_aliens:
            alien.goto(alien.xcor(), alien.ycor() - 30)
            if alien.ycor() < -280:
                game_is_on = False
                message.game_over()
        time_on = time.time() + sec
    for alien in all_aliens:
        if beam.distance(alien) < 40 and beam.beam:
            alien.shape("explosion.gif")
            alien.hideturtle()
            all_aliens.remove(alien)
            beam.hideturtle()
            beam.beam = False

            if len(all_aliens) == 0:
                game_is_on = False
                message.you_won()


screen.exitonclick()