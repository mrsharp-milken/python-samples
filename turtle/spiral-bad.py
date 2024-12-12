import turtle

turtle.shapesize(2, 2)
turtle.pensize(3)

line = 0

turtle.write("Zoom", move=False)

while line < 600:
    turtle.forward(line)
    turtle.left(90)
    
    line += 100

turtle.write(line, move=False)

for step in range(10):
    if step % 2 == 0:
        turtle.penup()
    else:
        turtle.pendown()
    
    turtle.forward(50)

turtle.left(90)
turtle.circle(25)



turtle.done()
