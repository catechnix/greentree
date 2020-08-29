import math 

def hypotenuse(a,b):
    x=a**2+b**2
    result=math.sqrt(x)
    
    return result

hypotenuse(4,5)

def is_between(x,y,z):
    if (x<=y<=z):
        return True
    else:
        return False