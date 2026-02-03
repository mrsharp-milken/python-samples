import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.up()
tina.goto(-200,-100)
tina.down()

tina.width(5)
tina.color("purple")

tina.begin_fill()
tina.forward(400)
tina.left(120)
tina.forward(400)
tina.left(120)
tina.forward(400)
tina.end_fill()

tina.goto(0,-90)
tina.color("white")
tina.right(180)

tina.begin_fill()
tina.forward(180)
tina.left(120)
tina.forward(180)
tina.left(120)
tina.forward(180)
tina.end_fill()

tina.hideturtle()

turtle.done()
