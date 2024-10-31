import turtle

# turtle.hideturtle()
turtle.color('red')

turtle.up()
turtle.goto(-100,-100)
turtle.down()

turtle.begin_fill()

for i in range(2):
    turtle.circle(100, 180)
    turtle.forward(100)

    
turtle.end_fill()