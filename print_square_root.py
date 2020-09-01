import math

def square_root (a,x):
    while True:
       # print (x)
        y = (x+a/x)/2
        if y == x:
            break
        x=y
    return x

fourth_c=square_root(1,1)-math.sqrt(1)

for i in range(1,10):
    print (str(i)+" "+str(square_root(i,1))+" "+str(math.sqrt(i))+" "+str(fourth_c)+"\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              