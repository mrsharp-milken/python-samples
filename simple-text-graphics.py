import tkinter
from tkinter import simpledialog

CANVAS_WIDTH = 500      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels


def draw(canvas):

    size = simpledialog.askstring("Font Size", "Enter a number for the font size:")
    size = int(size)

    center_x = CANVAS_WIDTH // 2

    canvas.create_text(center_x, 100, text="Hello World!", font=("Arial", size), fill="black")





# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('Python Graphics')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
