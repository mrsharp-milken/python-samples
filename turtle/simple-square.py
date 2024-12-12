import turtle

turtle.shapesize(2, 2)
turtle.pensize(3)

for i in range(4):
    turtle.forward(200)
    turtle.right(90)

turtle.left(45)
turtle.forward(100)
turtle.write("Hello", move=False, font=('Arial', 30, 'normal'))

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.circle(50)


turtle.done()