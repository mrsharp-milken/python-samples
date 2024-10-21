import turtle
screen = turtle.Screen()
tina = turtle.Turtle()
tina.shape('turtle')
turtle.colormode(255)

points = screen.textinput("Input", "How many points on the star? (no evens)")
# make points an integer
points = int(points)















for i in range(0, points):
    tina.forward(40)
    tina.left(180-180/points)
    tina.forward(40)
    tina.right(180-180/points)
    tina.left(360/points)

turtle.done()
