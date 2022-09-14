from turtle import Turtle, Screen
import random

colors = ["Blue", "Green", "yellow", "red", "orange", "purple"]

is_race_on = False
s = Screen()
s.colormode(255)
s.setup(width=500, height=400)
bet = s.textinput("Make your bet", "Choose a turtle: enter a color")
all_turtle = []

coordinate = [-230, -100]

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(coordinate)
    all_turtle.append(t)
    coordinate[1] += 30

if bet:
    is_race_on = True

while is_race_on:
    for x in all_turtle:
        if x.xcor() > 230:
            is_race_on = False
            winning = x.pencolor()
            if winning == bet:
                print("You Won!")
            else:
                print(f"You lose! {winning} is winner!")
        distance = random.randint(0, 10)
        x.forward(distance)

s.exitonclick()
