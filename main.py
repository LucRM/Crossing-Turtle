import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = [CarManager()]
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, 'Up')
count = 0
game_is_on = True
while game_is_on:
    car_speed = (MOVE_INCREMENT*0.01)
    time.sleep(car_speed)
    screen.update()
    for car in cars:
        '#Detect if Level is Passed'
        if player.ycor() > 280:
            player.reset_game()
            MOVE_INCREMENT *= 0.8
            scoreboard.level_up()
        '#Detect Collision with Car'
        if player.distance(car) < 20:
            player.reset_game()
            scoreboard.game_over()
            game_is_on = False
        '#Delete Cars'
        if car.xcor() < -340:
            car.hideturtle()
            cars.pop(cars.index(car))
        print(len(cars))
        car.move()
    if count % 6 == 0:
        cars.append(CarManager())


    count += 1

screen.exitonclick()