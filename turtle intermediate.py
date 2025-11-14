import turtle


my_pen=turtle.Turtle()

my_pen.speed(0)
my_pen.color('white')
my_pen.pensize(3)

turtle.bgcolor('black')
size=400

my_pen.penup()
my_pen.goto(-200,-200)
my_pen.pendown()

for i in range(1,100):
    my_pen.forward(size)
    my_pen.left(90)
    size-=4


from random import randint

turtle.speed(0)
turtle.bgcolor('black')
turtle.pensize(3)

colors=['magenta','cyan','yellow','white','orange','lightgreen']
num_circles=21
radius=13


for i in range(1,num_circles):
    turtle.color(colors[randint(0,len(colors)-1)])
    turtle.circle(i * radius)
    turtle.penup()
    turtle.goto(0,-i * radius)
    turtle.pendown()

for i in range(num_circles,0,-1):
    turtle.penup()
    turtle.goto(0,-i * radius)
    turtle.pendown()
    turtle.color(colors[randint(0,len(colors)-1)])
    turtle.circle(i * radius)

turtle.exitonclick()