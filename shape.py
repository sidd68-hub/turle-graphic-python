from turtle import Turtle,Screen
import random


timmy_the_turtle = Turtle()
colors = ["medium aquamarine", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side_n in range(3,11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)        