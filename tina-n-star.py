import turtle
tina = turtle.Turtle()
tina.shape('turtle')
turtle.colormode(255)

points = 6

# for i in range(0, points):
#     tina.forward(100)
#     tina.left(180-180/points)
# 
# tina.forward(100)

for i in range(0, points):
    tina.forward(40)
    tina.left(180-180/points)
    tina.forward(40)
    tina.right(180-180/points)
    tina.left(360/points)

tina.forward(100)
turtle.done()
