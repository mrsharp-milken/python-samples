import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

circle_color = "lime"

diameter = 50

tina.penup()
tina.goto(-250, 0)
tina.pendown()

tina.color(circle_color)

for i in range(4):
    tina.begin_fill()
    tina.circle(diameter)
    tina.end_fill()
    tina.penup()
    tina.forward(diameter * 2)
    tina.pendown()

turtle.done()


