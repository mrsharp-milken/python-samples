import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(20)

screen = turtle.Screen() # need this for input to work!
num = screen.textinput("Number of Circles", "How many circles to draw?")
# make it an integer
num = int(num)

tina.penup()
tina.goto(250, 0)
tina.left(90)
tina.pendown()

# use num in the loop to repeat num times!
for i in range(num):
    print("here is is: ", i)
    tina.circle(50,180)
    tina.right(180)
    tina.penup()
    
    if i == 4:
        tina.forward(200)
        tina.left(90)
        tina.backward(500)
        tina.right(90)
        
    tina.pendown()

turtle.done()


