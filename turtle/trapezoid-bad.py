import turtle

turtle.shapesize(2, 2)
turtle.pensize(3)

a = -250
b = 100
c = 200

turtle.penup()
turtle.goto(a, b)
turtle.pendown()

for i in range(2):
    turtle.forward(400)
    turtle.right(45)
    turtle.forward(c)
    turtle.right(135)

turtle.goto(a, a)
turtle.forward(b)

turtle.done()
