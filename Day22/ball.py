from turtle import Turtle

START_ANGLE = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
        self.add_x = 10
        self.add_y = 10

    def create(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        # self.setheading(START_ANGLE)

    def move(self):
        new_x = self.xcor() + self.add_x
        new_y = self.ycor() + self.add_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.add_y *= -1