import math

def check_fermat(a,b,c,n):
          
    if ((int(a))**int(n) + (int(b))**int(n) ==(int(c))**int(n)):
        print (int(a)^int(n))
        print ("Holy smokes, Fermat was wrong")
    else:
        print (int(a)^int(n))
        print ("No, that doesn't work")

a=input("please input number for a\n")

b=input("please input number for b\n")

c=input("please input number for c\n")

n=input("please input number for n which must be greater than 2\n")

if int(n) <= 2:
    n=input("please input number for n which must be greater than 2\n")
       

check_fermat(a,b,c,n) 