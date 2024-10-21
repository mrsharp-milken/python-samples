import turtle
screen = turtle.Screen() # need this for input to work!
tina = turtle.Turtle()
tina.shape('turtle')

num = screen.textinput("Number of Circles", "How many circles to draw?")
# make it an integer
num = int(num)

tina.penup()
tina.goto(-250, 0)
tina.pendown()

# use num in the loop to repeat num times!
for i in range(num):
    tina.circle(50)
    tina.penup()
    tina.forward(120)
    tina.pendown()
    

turtle.done()


