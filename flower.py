try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *    

from polygon import *

world=TurtleWorld()
t=Turtle()
t.delay = 0.001

def pedal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,n,r,angle):
    for i in range (n):
        pedal(t,r,angle)
        lt(t,360/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)

move(t,-100)
flower(t,7,60,60)

move(t,120)
flower(t,10,60,60)

move(t,120)
flower(t,20,60,60)

die(t)
wait_for_user()