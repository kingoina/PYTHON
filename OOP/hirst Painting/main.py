from  turtle import Turtle,Screen
import random

timmy = Turtle()
canvas = Screen()

color_list = [(246, 242, 235), (248, 242, 245), (240, 246, 242), (239, 242, 247), (198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23)]

canvas.title("Hirts Painting")
canvas.bgcolor("black")
timmy.speed("fastest")
timmy.hideturtle()
canvas.colormode(255)



circle_radius = int(input("What radius do you wish to have ?(5-30)"))
separation_length = int(input("What distance do you wish to have between the circles ?(25-500)"))


def starting_point():
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(350)
    timmy.setheading(0)
    timmy.pendown()


def spot():
    choice = random.choice(color_list)
    timmy.color(choice, choice)
    timmy.begin_fill()
    timmy.circle(circle_radius)
    timmy.end_fill()

def forward():
    timmy.penup()
    timmy.forward(separation_length)
    timmy.pendown()

def line():
    for _ in range(10):
        spot()
        forward()

def new_row():
    timmy.penup()
    timmy.left(90)
    timmy.forward(separation_length + 5)
    timmy.left(90)
    timmy.forward(separation_length * 10)
    timmy.right(180)
    timmy.penup()

starting_point()
for _ in range(10):
    line()
    new_row()
canvas.exitonclick()