import turtle

screen = turtle.Screen()
tina = turtle.Turtle()
tina.shape('turtle')
turtle.colormode(255) # changes color mode to RGB

tina.forward(100)
tina.left(45)
tina.color(40, 250, 250)
tina.forward(100)
tina.circle(50)

tina.penup()
tina.forward(100)
tina.pendown()

tina.forward(100)

turtle.done()