import turtle
import random

tina = turtle.Turtle()
tina.width(5)

for i in range(30):
    tina.forward(20)
    
    num = random.randint(0, 1) # Randomly choose 0 or 1
    if num == 0:
        tina.right(90)
    else:
        tina.left(90)

turtle.done()