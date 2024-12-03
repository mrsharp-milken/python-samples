import turtle
import random

turtle.colormode(255)  # Allows using RGB values from 0 to 255
tina = turtle.Turtle()
tina.width(3)
tina.speed(0)

diameter = 150

while diameter > 20:
    # Get random colors
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)

    tina.color(r, g, b)
    tina.circle(diameter)
    
    diameter -= 20 # make diameter 20 smaller each time


turtle.done()