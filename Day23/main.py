import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "Up")
screen.listen()

# generate a lot of cars.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.car_const_move()

    # decide when is level up,
    # TODO change the speed
    if player.ycor() > 290:
        scoreboard.level_up()
        player.reset_position()
        car_manager.speed_up()

    # TODO decide when is game over
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break


screen.exitonclick()