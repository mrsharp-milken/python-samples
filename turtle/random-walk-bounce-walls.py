import turtle
import random

tina = turtle.Turtle()
tina.width(5)

for i in range(1000):
    tina.forward(50)
    
    num = random.randint(0, 1) # Randomly choose 0 or 1
    if num == 0:
        tina.right(90)
    else:
        tina.left(90)
        
    x, y = tina.position()
    
    if y > 350:
        tina.right(180)
    if y < -350:
        tina.right(180)
    if x > 400:
        tina.right(180)
    if x < -400:
        tina.right(180)
    

turtle.done()