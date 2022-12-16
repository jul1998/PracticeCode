import turtle
import time
from turtle import Turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
# set the background color

STARTING_POSITION = (0,-280)
PLAYER_MOVE = 40
class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.color("black")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)
        self.player.shape("turtle")

    def move_up(self):
        y = self.player.ycor() + PLAYER_MOVE
        self.player.sety(y)

    def reset_position(self):
        self.player.goto(STARTING_POSITION)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars(Turtle):
    def __init__(self):
        super().__init__()

        self.cars_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 3) == 3:
            new_car = Turtle()
            new_car.color("red")
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.goto(280,random.randint(-280, 280))
            new_car.shapesize(stretch_wid=0.8, stretch_len=2, outline=None)
            self.cars_list.append(new_car)

    def move_car(self):
        for car in self.cars_list:
            car.forward(self.speed)

    def increment_speed(self):
        self.speed += 10


player = Player()
cars = Cars()


screen.listen()
screen.onkeypress(player.move_up, "Up")

while True:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    if player.player.ycor()> 280:
        cars.increment_speed()
        player.reset_position()



screen.mainloop()



