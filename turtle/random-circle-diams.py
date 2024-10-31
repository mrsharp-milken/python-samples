import turtle
import random # must import random!

tina = turtle.Turtle()
tina.width(5)

for i in range(10):
    diameter = random.randint(20, 100) # Choose a random number
    tina.circle(diameter)

turtle.done()

