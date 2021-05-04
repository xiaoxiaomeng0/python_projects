from turtle import Screen
from paddle import Paddle
from ball import Ball

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    paddle_left.move_forward()
    paddle_right.move_forward()
    ball.move()

    # Detect ball collision with the top and bottom wall.
    if ball.ycor() > 282 or ball.ycor() < -282:
        ball.bounce()

    # Detect the paddle not over the wall
    if paddle_left.ycor() > 260 or paddle_left.ycor() < -260:
        paddle_left.move_backward()

    if paddle_right.ycor() > 260 or paddle_right.ycor() < -260:
        paddle_right.move_backward()



screen.exitonclick()
