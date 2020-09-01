def power_num(a,b):
    if a%b == 0 and a/b%b == 0:
        return True
    else:
        return False

print (power_num(9,3))