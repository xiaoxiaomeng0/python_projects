from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.x_cor = x
        self.y_cor = y
        self.create()


    def create(self):
        self.penup()
        self.setpos(self.x_cor, self.y_cor)
        self.setheading(UP)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_forward(self):
        self.forward(20)

    def up(self):
        self.setheading(UP)

    def down(self):
        self.setheading(DOWN)

    def move_backward(self):
        self.backward(20)




