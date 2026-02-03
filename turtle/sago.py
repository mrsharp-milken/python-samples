import turtle
import random
screen = turtle.Screen()
tina = turtle.Turtle()
screen.setup(width=700, height=750)
tina.shape("turtle")
tina.speed(0)
screen.bgcolor("powder blue")

flavor = screen.textinput("Flavor", "what flavor should the sago be? Taro, mango, strawberry, coconut, matcha.")
jelly = screen.textinput("Jelly amount","Do you want jelly?")
jelly_flavor = screen.textinput("Jelly","what flavor jelly do you want? Coconut, mango, lychee, grass")
mango = screen.textinput("Mango", "do you want mango?")
strawberry = screen.textinput("Strawberry amount", "Do you want strawberries?")
raspberry = screen.textinput("Raspberry amount", "Do you want raspberries?")
mint = screen.textinput("Mint amount", "Do you want mint?")

if mango == "yes":
    mango_amount = 8
else:
    mango_amount = 0
    
if jelly == "yes":
    jelly_amount = 10
else:
    jelly_amount = 0
    
if strawberry == "yes":
    strawberry_amount = 4
else:
    strawberry_amount = 0
    
if mint == "yes":
    mint_amount = 1
else:
    mint_amount = 0
        
if raspberry == "yes":
    raspberry_amount = 5
else:
    raspberry_amount = 0

tina.color("steel blue")
tina.penup()
tina.right(90)
tina.forward(150)
tina.left(90)
tina.pendown()
tina.begin_fill()
tina.circle(150)
tina.end_fill()

if flavor == "taro":
    tina.color("medium purple")
elif flavor == "mango":
    tina.color("gold")
elif flavor == "strawberry":
    tina.color("pink")
elif flavor == "coconut":
    tina.color("old lace")
elif flavor == "matcha":
    tina.color("yellow green")

tina.penup()
tina.left(90)
tina.forward(20)
tina.right(90)
tina.pendown()
tina.begin_fill()
tina.circle(130)
tina.end_fill()

if flavor == "taro":
    tina.color("dark slate blue")
elif flavor == "mango":
    tina.color("dark orange")
elif flavor == "strawberry":
    tina.color("pale violet red")
elif flavor == "coconut":
    tina.color("moccasin")
elif flavor == "matcha":
    tina.color("olive drab")

tina.penup()
tina.left(90)
tina.forward(10)
tina.pendown()

for i in range (60):
    tina.penup()
    tina.goto(0,0)
    tina.forward(random.randint(10, 110))
    tina.right(random.randint(0, 360))
    tina.pendown()
    tina.begin_fill()
    tina.circle(8)
    tina.end_fill() 

for i in range (80):
    tina.penup()
    tina.goto(0,0)
    tina.forward(random.randint(10, 110))
    tina.right(random.randint(0, 360))
    tina.pendown()
    tina.begin_fill()
    tina.circle(5)
    tina.end_fill()
    
if jelly_flavor == "coconut":
    tina.color("alice blue")
elif jelly_flavor == "lychee":
    tina.color("misty rose")
elif jelly_flavor == "mango":
    tina.color("sandy brown")
elif jelly_flavor == "grass":
    tina.color("black")
    
for i in range (jelly_amount):
    tina.penup()
    tina.goto(0,0)
    tina.forward(random.randint(50, 80))
    tina.right(random.randint(0, 360))
    tina.pendown()
    tina.begin_fill()
    for i in range (2):
        tina.forward(40)
        tina.right(90)
        tina.forward(40)
        tina.right(90)
    tina.end_fill()
    
for i in range(mango_amount):
    tina.color("orange")
    tina.penup()
    tina.goto(0,0)
    tina.right(random.randint(0,360))
    tina.forward(random.randint(30,90))
    tina.right(random.randint(0,360))
    tina.pendown()
    tina.begin_fill()
    tina.forward(20)
    tina.right(60)
    tina.forward(40)
    tina.right(100)
    tina.forward(19)
    tina.right(50)
    tina.forward(65)
    tina.end_fill()
    
for i in range (strawberry_amount):
    tina.color("red")
    tina.penup()
    tina.pendown()
    tina.begin_fill()
    tina.forward(20)
    tina.circle(20,120)
    tina.forward(45)
    tina.circle(10,130)
    tina.forward(45)
    tina.circle(20,120)
    tina.end_fill()
    
    tina.color("light coral")
    tina.begin_fill()
    tina.right(10)
    tina.forward(15)
    tina.circle(10,120)
    tina.forward(25)
    tina.circle(7,130)
    tina.forward(25)
    tina.circle(10,120)
    tina.end_fill()
    
    tina.penup()
    tina.goto(0,0)
    tina.right(random.randint(0,360))
    tina.forward(random.randint(30,60))
    tina.pendown()

for i in range (raspberry_amount):
    for i in range(5):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()
    tina.penup()
    tina.right(180)
    tina.right(90)
    tina.forward(2)
    tina.left(90)
    tina.forward(15)
    tina.pendown()
    for i in range (4):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()     
    tina.penup()
    tina.right(180)
    tina.right(90)
    tina.forward(2)
    tina.left(180)
    tina.backward(15)
    tina.right(90)
    tina.forward(10)
    tina.pendown()
    for i in range (4):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()
    tina.penup()
    tina.right(180)
    tina.right(90)
    tina.forward(2)
    tina.left(180)
    tina.forward(0)
    tina.right(90)
    tina.forward(15)
    tina.pendown()
    for i in range (3):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()
    tina.penup()
    tina.right(180)
    tina.right(90)
    tina.forward(2)
    tina.left(180)
    tina.backward(15)
    tina.right(90)
    tina.forward(10)
    tina.pendown()
    for i in range (3):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()
    tina.penup()
    tina.right(180)
    tina.right(90)
    tina.forward(2)
    tina.left(180)
    tina.forward(0)
    tina.right(90)
    tina.forward(15)
    tina.pendown()
    for i in range (2):
        tina.begin_fill()
        tina.color("crimson")
        tina.circle(5)
        tina.end_fill()
        tina.penup()
        tina.forward(10)
        tina.pendown()
    tina.penup()
    tina.goto(0,0)
    tina.right(random.randint(0,360))
    tina.forward(random.randint(50,80))
    tina.pendown()

for i in range (mint_amount):
    tina.color("forest green")
    tina.penup()
    tina.goto(0,0)
    tina.pendown()
    tina.begin_fill()
    tina.circle(30,140)
    tina.left(40)
    tina.circle(30,140)
    tina.end_fill()

    tina.right(100)
    tina.begin_fill()
    tina.circle(30,140)
    tina.left(40)
    tina.circle(30,140)
    tina.end_fill()

    tina.right(80)
    tina.begin_fill()
    tina.circle(20,140)
    tina.left(40)
    tina.circle(20,140)
    tina.end_fill()
