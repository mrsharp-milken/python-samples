import turtle
screen = turtle.Screen() # need this for input to work!
tina = turtle.Turtle()
tina.shape('turtle')

length = screen.textinput("Square Size", "How big should the square be?")
# make it an integer
length = int(length)

for i in range(0, 4):
    # use length when moving forwards
    tina.forward(length)
    tina.left(90)

turtle.done()

