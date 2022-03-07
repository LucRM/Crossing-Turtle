from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-210, 260)
        self.hideturtle()
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)
        self.level += 1

    def game_over(self):
        self.home()
        self.write(f'Game Over', align='center', font=FONT)
