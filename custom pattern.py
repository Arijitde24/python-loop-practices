import turtle
from random import randint

turtle.speed(0)
turtle.bgcolor('black')
turtle.pensize(3)

colors=['magenta','cyan','yellow','white','orange','lightgreen']
squares=60
size=300
x=0
y=0

for i in range(squares,1,-1):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(colors[randint(0,len(colors)-1)])
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    x+=2
    y-=2
    size-=10
turtle.exitonclick()