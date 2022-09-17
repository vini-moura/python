from turtle import Turtle, Screen
import random

# import colorgram
#w3schools.com/colors/colors_rgb.asp

# rgb = []
# colors = colorgram.extract("hisrtimage.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g,b)
#     rgb.append(new_color)
#  print(rgb)
color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 34), (199, 142, 34), (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130), (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), (51, 126, 121), (197, 124, 143), (166, 21, 31), (222, 93, 79), (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), (161, 26, 23), (19, 79, 92), (233, 167, 172), (175, 207, 187), (101, 127, 158), (165, 203, 210)]

t = Turtle()
s = Screen()
s.colormode(255)
t.speed('fast')
t.penup()
t.setposition(-255, -255)
t.pendown()

for i in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.penup(); t.forward(50); t.pendown()
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


s.exitonclick()
