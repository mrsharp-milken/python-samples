import turtle
# turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape("turtle")

tina.width(5)
tina.color("deep sky blue")

for i in range(8):
    tina.forward(200)
    tina.circle(20)
    tina.backward(200)
    tina.left(360/8)

turtle.done()
