import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
my_turtle = Turtle()
my_turtle.shape("turtle")

# for i in range(0, 4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

colors = ["gray", "brown", "tan", "tomato", "orange", "yellow", "limegreen", "violet", "yellow4", "plum"]
directions = [0, 90, 180, 270]


def draw_dash(space, dash_length, total_length):
    for i in range(total_length):
        for j in range(total_length):
            my_turtle.pendown()
            my_turtle.forward(dash_length)
            my_turtle.penup()
            my_turtle.forward(space)

        my_turtle.penup()
        my_turtle.backward((space + dash_length) * total_length)

        my_turtle.right(90)
        my_turtle.forward(space)
        my_turtle.left(90)
        my_turtle.pendown()


def draw_shape(length):
    # TODO decide the number of times that the turtle will turn
    #
    # TODO pass in the length of shape

    for i in range(3, 10):
        j = i
        while j > 0:
            my_turtle.forward(length)
            my_turtle.right(360 / i)
            j -= 1


def rand_pick_from_list(r_list):
    # TODO random pick a direction/color

    index = random.randint(0, len(r_list) - 1)
    return r_list[index]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk(times):
    for i in range(times):
        my_turtle.pensize(20)
        rand_color = random_color()
        rand_direct = rand_pick_from_list(directions)
        my_turtle.pencolor(rand_color)
        my_turtle.right(rand_direct)
        my_turtle.forward(100)


def draw_circle(space):
    my_turtle.speed(10)
    for i in range(1, int(360 / space)):
        my_turtle.pencolor(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(space*i)


# my_turtle.penup()
# draw_dash(5, 5, 20)
# draw_shape(100)
# random_walk(20)
draw_circle(10)

# print(my_turtle.speed())

screen = Screen()
screen.exitonclick()
