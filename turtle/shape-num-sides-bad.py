import turtle

turtle.shapesize(2, 2)
turtle.pensize(3)

turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()

num = 3
for i in range(num):
    turtle.forward(100)
    turtle.right(360 / num)

turtle.penup()
turtle.goto(200, 300)
turtle.pendown()

num += 1
for i in range(num):
    turtle.forward(100)
    turtle.right(360 / num)
    
turtle.penup()
turtle.goto(200, -100)
turtle.pendown()

num += 2
for i in range(num):
    turtle.forward(80)
    turtle.right(360 / num)

turtle.done()

