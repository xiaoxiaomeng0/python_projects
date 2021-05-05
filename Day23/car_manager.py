#TODO random generate the cars from the right side of the screen to the left.
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.create()
        self.car_const_move()

    def create(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-230, 230))
            self.all_cars.append(car)

    def car_const_move(self):
        for each_car in self.all_cars:
            each_car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT





