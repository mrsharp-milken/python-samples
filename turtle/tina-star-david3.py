import turtle
tina = turtle.Turtle()
tina.shape('turtle')
turtle.colormode(255)


for i in range(0, 2):
    for i in range(0, 3):
        tina.left(120)
        tina.forward(300)
    for angle in range(-120, 180, 180):
        tina.right(angle)
        tina.forward(100)

turtle.done()


