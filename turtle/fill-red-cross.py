import turtle

tina = turtle.Turtle()

tina.up()
tina.goto(50, -50)
tina.down()

tina.color('red')

tina.begin_fill()

# draw cross
for i in range(4):
    tina.forward(200)
    tina.circle(50, 180)
    tina.forward(200)
    tina.right(90)

tina.end_fill()

turtle.done()
