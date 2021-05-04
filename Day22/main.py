from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    paddle_left.move_forward()
    paddle_right.move_forward()
    ball.move()

    # Detect ball collision with the top and bottom wall.
    if ball.ycor() > 282 or ball.ycor() < -282:
        ball.bounce_y()

    # Detect the paddle not over the wall
    if paddle_left.ycor() > 260 or paddle_left.ycor() < -240:
        paddle_left.move_backward()

    if paddle_right.ycor() > 260 or paddle_right.ycor() < -240:
        paddle_right.move_backward()

    # Detect the ball collision with the paddle
    if ball.distance(paddle_left) < 50 and ball.xcor() < -320 or ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() > 390:
        scoreboard.add_l_score()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.add_r_score()
        ball.reset_position()







screen.exitonclick()
