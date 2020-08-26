from swampy.TurtleWorld import *

world=TurtleWorld()
t=Turtle()

def draw(t, length, n): 
    if n == 0: 
        return 
    angle = 50 
    fd(t, length*n) 
    lt(t, angle) 
    draw(t, length, n-1) 
    rt(t, 2*angle) 
    draw(t, length, n-1) 
    lt(t, angle) 
    bk(t, length*n)

draw(t, 25, 4)