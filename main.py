import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()


def move_up():
    new_y = player.ycor() + 10
    player.goto(player.xcor(), new_y)


screen.listen()
screen.onkey(move_up, 'Up')

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.01)
    screen.update()


screen.exitonclick()
