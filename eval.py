import math

y=None
while True:
    
    x = input("input a number for evaluating a square function\n")
    if str(x) != "done": 
        y=int(x)
        print (eval("math.sqrt(y)"))
    else:
        if y==None:
            break
        else:
            print(eval("math.sqrt(y)"))
            break
        