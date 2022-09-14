from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.colormode(255)
s.listen()


def forwards():
    t.forward(30)


def backwards():
    t.backward(30)


def clockwise():
    t.right(45)


def counterclock():
    t.left(45)


def reset():
    s.resetscreen()


s.onkey(key='w', fun=forwards)
s.onkey(key='s', fun=backwards)
s.onkey(key='d', fun=clockwise)
s.onkey(key='a', fun=counterclock)
s.onkey(key='c', fun=reset)
s.exitonclick()
