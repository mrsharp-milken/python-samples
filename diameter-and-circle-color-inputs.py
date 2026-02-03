import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')
# Input variable step 1
screen = turtle.Screen()

# Input variable step 2
circle_color = screen.textinput("Circle color", "What color should the circle be?")

# Input variable step 2
diameter = screen.textinput("Diameter", "What should the diameter of the circle be?")
# Input variable step 2b (convert text to number)
diameter = int(diameter)

tina.penup()
tina.goto(-250, 0)
tina.pendown()

# Input variable step 3
tina.color(circle_color)

for i in range(4):
    tina.begin_fill()
    tina.circle(diameter)
    tina.end_fill()
    tina.penup()
    tina.forward(diameter * 2)
    tina.pendown()

turtle.done()

