# import turtle
# jonny = turtle.Turtle()

from turtle import Turtle, Screen
from prettytable import PrettyTable

john = Turtle()
john.shape("turtle")
john.color('coral')
john.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("pokemon", ['pikachu', 'charmander', 'bulbasaur'])
table.add_column("type", ['eletric', 'fire', 'grass'])

table.align = 'l'

print(table)