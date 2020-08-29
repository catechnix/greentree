def is_triangle():
    user_prompt()
    if (a>b+c) or (b>a+c) or (c>a+b):
        print ("No")
    else:
        print ("Yes")

def user_prompt():
    global a, b, c
    a=input("please input 1st stick length:\n")
    int(a)
    b=input("please input 2nd stick length:\n")
    int(b)
    c=input("please input 3rd stick length:\n")
    int(c)
    #print (a,b,c)
    return (a,b,c)

is_triangle()