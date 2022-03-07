from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(1.0, 2.0)
        self.color(choice(COLORS))
        self.setheading(180)
        self.goto(300, randint(-250, 250))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_distance)

    def speed_up(self):
        self.move_distance

