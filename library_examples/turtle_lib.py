from random import random
from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("DarkViolet")
tim.resizemode("user")
tim.shapesize(1, 1, 1)

screen = Screen()
screen.setup(height=0.5, width=0.32)

for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    tim.right(angle)
    tim.fd(steps)

screen.exitonclick()
