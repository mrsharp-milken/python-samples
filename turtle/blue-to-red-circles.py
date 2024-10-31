import turtle

tina = turtle.Turtle()
tina.up()
tina.goto(-300, 0)
tina.down()
tina.speed(1)
tina.pensize(5)

for i in range(50):
    
    x, y = tina.position()  # Get current position
    
    print("x: ", x)
    
    if x > 0:              # If x-coordinate is greater than 50
        tina.color("red")
        tina.right(20)
    else:
        tina.color("blue")
        
    tina.forward(20)
    
turtle.done()