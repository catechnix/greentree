"""
Write a program that creates a Canvas and a Button. When the user presses the Button, it should draw a circle on the canvas.
"""

from swampy.Gui import *

g = Gui()
g.title('Canvas')

canvas=g.ca(width=500, height=500)
canvas.config(bg='blue')

def draw_circle():
    global canvas
    canvas.circle([0,0], 100, fill='red')

g.bu(text='Press me', command=draw_circle)

g.mainloop() 
