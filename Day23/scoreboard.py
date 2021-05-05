#TODO create a scoreboard

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.create()


    def create(self):
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))

