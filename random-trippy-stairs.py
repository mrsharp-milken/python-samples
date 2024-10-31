import turtle
import random # must import random!

tina = turtle.Turtle()
tina.width(5)
tina.up()
tina.goto(-300, 300)
tina.down()

for i in range(30):
    distance = random.randint(20, 50) # Choose a random number between 20-50
    tina.forward(distance)

    tina.right(90)
    
    tina.forward(distance)
    
    tina.left(90)

turtle.done()
