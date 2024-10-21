# import tkinter
# import turtle
# 
# diameter = 50
# 
# root = turtle.Screen()._root
# 
# button = tkinter.Button(root, text="Click Me", command=on_button_click)
# button.pack()
# button.place(x=300, y=100)
# 
# butt2 = tkinter.Button(root, text="Other", command=on_button_click)
# butt2.pack(side="left")
# 
# slider = tkinter.Scale(root, label="Percent", orient="horizontal", command=slide) # from_=20, to=50
# slider.pack(side="left")
# 
# tina = turtle.Turtle()
# tina.color('blue')
# tina.shape('turtle')
# 
# turtle.done()
# 
# def on_button_click():
#     print("Button clicked!", diameter, type(diameter))
#     tina.circle(int(diameter))
#     
# def slide(value):
#     global diameter
#     diameter = value
#     

def foo():
    return bar

bar = 10  # bar is defined after foo, causing an error

print(foo())  # Error: bar is not defined