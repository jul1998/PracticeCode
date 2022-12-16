import turtle
import time
from turtle import *
import random



screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
# set the background color
screen.bgcolor("black")

directions = [0, 90,180,270]

position = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg in range(3):
            self.snake = turtle.Turtle("square")
            self.snake.color("white")
            self.snake.penup()
            self.snake.goto(position[seg])
            self.segments.append(self.snake)


    def move_up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
            self.head.forward(10)


    def move_down(self):
        if self.head.heading() != 90:
            self.head.seth(270)
            self.head.forward(10)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
            self.head.forward(10)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
            self.head.forward(10)


    def move_all_snakes(self):
        for seg_number in range(len(self.segments)-1, 0, -1):
            x= self.segments[seg_number-1].xcor()
            y = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(x,y)
        self.head.forward(10)



class Food:

    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("yellow")
        self.food.goto(random.randint(-280, 280),random.randint(-280, 280))
        self.food.shapesize(0.5)


    def reset_position(self):
        self.food.goto(random.randint(-280, 280),random.randint(-280, 280))

class Score:
    def __init__(self):
        self.scoreboard = Turtle("turtle")
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.score = 0
        self.scoreboard.goto(0, 270)
        self.scoreboard.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def add_score(self):
        self.scoreboard.clear()
        print(self.score)
        self.score += 1
        self.scoreboard.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def write_score(self):
        self.scoreboard.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))


snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_left, "Left")

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    snake.move_all_snakes()
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        break

    if snake.head.distance(food.food) < 10:
        scoreboard.add_score()
        food.reset_position()
        snake.create_snake()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 3:
            print("hit")
            game_on = False


screen.mainloop()