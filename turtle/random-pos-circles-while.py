import turtle
import random

tina = turtle.Turtle()
tina.width(3)

circles = 0

while circles < 10:
    # Get random colors
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    tina.up()
    tina.goto(x, y)
    tina.down()
    
    tina.circle(10)
    
    circles += 1


turtle.done()
