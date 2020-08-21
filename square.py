#!/usr/bin/python3.7

from swampy.TurtleWorld import *
world = TurtleWorld()
t=Turtle()
#print(t)

def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)
    wait_for_user()

#square(t)

def polygon(t,n,length):
    for i in range(n):
        fd(t,100)
        lt(t,360/n)
    wait_for_user()

polygon(t,10, 200)