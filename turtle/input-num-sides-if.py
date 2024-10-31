import turtle

tina = turtle.Turtle()
screen = turtle.Screen() # need this for input to work!
tina.pensize(10)


sides = screen.textinput("Number of sides", "How many sides will the shape have?")
# make it an integer
sides = int(sides)

while sides <= 2:
    print("Not enough sides!")
    sides = screen.textinput("Not enough sides", "Try again")
    # make it an integer
    sides = int(sides)
    
for i in range(sides):
    tina.forward(100)
    tina.right(360 / sides)

turtle.done()