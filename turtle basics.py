import turtle


turtle.circle(10)


turtle.width(3)
turtle.color('red')
turtle.penup()
turtle.goto(150,-150)
turtle.pendown()

turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)



turtle.penup()
turtle.goto(10,-10)
turtle.pendown()

for i in range(4):
    turtle.left(90)
    turtle.forward(300)


turtle.exitonclick()