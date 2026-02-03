import turtle
tina = turtle.Turtle()

tina.speed(0)

# outer circle
tina.fillcolor('black')
tina.begin_fill()
tina.circle(100)
tina.end_fill()

# white half
tina.fillcolor('white')
tina.begin_fill()
tina.circle(100, 180)
tina.circle(50, 180)
tina.circle(-50, 180)
tina.end_fill()

# small black dot
tina.penup()
tina.goto(0, 50)
tina.pendown()
tina.fillcolor('white')
tina.begin_fill()
tina.circle(15)
tina.end_fill()

# small white dot
tina.penup()
tina.goto(0, 150)
tina.pendown()
tina.fillcolor('black')
tina.begin_fill()
tina.circle(15)
tina.end_fill()

tina.hideturtle()
turtle.done()