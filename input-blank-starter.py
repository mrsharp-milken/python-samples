import turtle
turtle.setup(startx=10, starty=10) # Make window appear on the left
tina = turtle.Turtle()
tina.shape('turtle')



tina.penup()
tina.goto(-250, 0)
tina.pendown()

for i in range(4):
    tina.circle(40)
    tina.penup()
    tina.forward(120)
    tina.pendown()

turtle.done()
