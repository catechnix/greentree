def print_hello():
    print ("This is a test!")

def do_n (n,print_n):
    if n<=0:
        return
    print_n()
    do_n(n-1,print_n)
    

do_n(3,print_hello)
