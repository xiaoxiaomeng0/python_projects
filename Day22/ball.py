from turtle import Turtle

START_ANGLE = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.add_x = 10
        self.add_y = 10
        self.move_speed = 0.5

    def create(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.add_x
        new_y = self.ycor() + self.add_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.add_y *= -1

    def bounce_x(self):
        self.add_x *= -1
        self.move_speed *= 0.6

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.5


