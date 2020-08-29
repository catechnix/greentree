from swampy.TurtleWorld import *

world=TurtleWorld()
t=Turtle()

def koch_curve(t, length):
    angle=60
    fd(t, length/3)
    lt(t,angle)
    fd(t,length/3)
    rt(t,angle*2)
    fd(t,length/3)
    lt(t,angle)
    fd(t,length/3)

for i in range(3):  
    koch_curve(t,50)

die(t)
wait_for_user()
