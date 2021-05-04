from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.create()


    def create(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def add_l_score(self):
        self.score_left += 1
        self.clear()
        self.write_score()

    def add_r_score(self):
        self.score_right += 1
        self.clear()
        self.write_score()
