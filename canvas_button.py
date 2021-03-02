"""
Write a program that creates a Canvas and a Button. When the user presses the Button, it should draw a circle on the canvas
"""
 


from swampy.Gui import *

#g=Gui()
#g.title('Gui')
#g.mainloop()

#button=g.bu(text='Press me')



g = Gui()
g.title('Test')

def callback1():
    g.bu(text='Now press me.', command=callback2)

def callback2():
    g.la(text='Nice job.')

g.bu(text='Press me.', command=callback1)

g.mainloop()
