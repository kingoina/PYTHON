from turtle import Turtle, Screen
import random

timmy = Turtle()
canvas = Screen()

# Allow RGB values from 0–255
canvas.colormode(255)

timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)


for angle in range(160):
    random_color()
    timmy.circle(100)
    timmy.left(30)

canvas.exitonclick()
