#!/usr/bin/python3.7

from swampy.TurtleWorld import *
world = TurtleWorld()
t=Turtle()
print (t)

for i in range(4):
    fd(t,100)
    lt(t)

wait_for_user()
