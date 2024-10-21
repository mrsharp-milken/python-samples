import turtle

turtle.hideturtle()
turtle.color('red')

turtle.up()
turtle.goto(-300,-100)
turtle.down()

turtle.begin_fill()

for i in range(4):
    turtle.fd(200)
    turtle.right(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    
turtle.end_fill()